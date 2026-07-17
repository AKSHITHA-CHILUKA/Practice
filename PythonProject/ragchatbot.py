import streamlit as st
import pdfplumber
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

OPENAI_API_KEY = ""

st.header("My first chatbot")

with st.sidebar:
    st.title("Your Documents")
    file = st.file_uploader("Please upload a PDF file and start the conversation", type = "pdf")

#extract content from the pdf and chunk it 
if file is not None:
    #extract text from it
    with pdfplumber.open(file) as pdf:
        text=""
        for page in pdf.pages:
            text+=page.extract_text() + "\n"
    #st.write(text)

    #split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators = ["\n\n","\n", ".", " ", ""],
        chunk_size = 1000, #1000 characters
        chunk_overlap = 200 # to add meaning 
    )
    chunks = text_splitter.split_text(text)
    #st.write(chunks)

    #generating embeddings
    embeddings = OpenAIEmbeddings(
        model = "text-embedding-3-small",
        openai_api_key = OPENAI_API_KEY
    )

    #store embeddings in vector db
    vector_store = FAISS.from_texts(chunks,embeddings)

    #get user question 
    user_question = st.text_input("Type your question here")

    #generate answer 
    #question -> embeddings -> similarity search -> results to LLM -> response (chain)
    
    def format_docs(docs):
        return "\n\n".join([doc.page_content for doc in docs])

    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={"k":4}
    )

    #what color is apple - 9823723529
    #red,green,yellow - 927921,29174918,9102748

    #define the llm and promtps
    llm = ChatOpenAI(
        model = "gpt-4o-mini",
        temperature = 0.3, #higher number means more random answer , 0.3 means gives answer in context 
        max_tokens = 1000, #how many tokens to generate in final response
        openai_api_key = OPENAI_API_KEY
    )

    #provide the prompts
    prompt = ChatPromptTemplate.from_messages([
        ("system",
        "You are a helpful assistant answering about questions in a pdf documnet.\n\n"
        "Guidelines:\n"
        "1.Provide complete, well-explained answers using the context below"
        "2.Include relevant details , numbers and explanations to give a thorough response.\n"
        "Context:\n{context}"),
        ("human","{question}")
    ])

    chain = (
        {"context" : retriever | format_docs , "question" : RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    if user_question:
        response = chain.invoke(user_question)
        st.write(response)
