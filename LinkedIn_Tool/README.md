# LinkedIn Tool

This project is a local Python CLI and desktop GUI for managing LinkedIn prospects manually.

It does not automate LinkedIn login or send connection requests. Instead, it helps you:

- store and organize people you want to contact
- import and export CSV or Excel files
- rank people by the topics you care about
- match prospects against pasted profile text
- draft a personalized connection note for manual review
- track outreach status locally

## Requirements

- Python 3.10 or newer

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Quick start

Create an empty store:

```bash
python linkedin_tool.py init
```

Open the GUI:

```bash
python linkedin_tool.py gui
```

Add one prospect:

```bash
python linkedin_tool.py add --name "Jane Doe" --title "AI Engineer" --company "Acme" --topics "python, ai, startups" --profile-url "https://linkedin.com/in/janedoe"
```

List saved prospects:

```bash
python linkedin_tool.py list
```

Rank prospects by interests:

```bash
python linkedin_tool.py suggest --interests "ai, startups, product" --limit 10
```

Match prospects from pasted profile text:

```bash
python linkedin_tool.py match-text --text "Senior product leader helping startups scale AI products and developer platforms" --limit 10
```

Draft a connection note:

```bash
python linkedin_tool.py draft --name "Jane Doe" --company "Acme" --topics "ai, startups" --interests "ai, startups" --your-name "Your Name"
```

Update outreach status:

```bash
python linkedin_tool.py mark --name "Jane Doe" --status "contacted"
```

Export to Excel:

```bash
python linkedin_tool.py export-xlsx prospects.xlsx
```

Import from Excel:

```bash
python linkedin_tool.py import-xlsx prospects.xlsx
```

## CSV import

The importer accepts columns such as:

- name
- title
- company
- topics
- profile_url
- status
- note

Example:

```csv
name,title,company,topics,profile_url,status,note
Jane Doe,AI Engineer,Acme,"ai,python",https://linkedin.com/in/janedoe,to_contact,Met at a conference
```

Run:

```bash
python linkedin_tool.py import-csv prospects.csv
```

The same columns also work for `import-xlsx`.

## Storage

Prospects are stored in `prospects.json` in the same folder as the script.