
import matplotlib.pyplot as plt
def initial_plot():
    plt.plot([1, 2, 3], [1, 4, 9])
    plt.show()

def plot_cosine_with_labels():
    import numpy as np
    x = np.linspace(0, 2 * np.pi, 100)
    y = np.cos(x)
    plt.plot(x, y)
    plt.title('Cosine Function')
    plt.xlabel('Angle [radians]')
    plt.ylabel('Cosine Value')
    plt.grid()
    plt.show()

def plot_cosine_and_sine_with_labels():
    import numpy as np
    x = np.linspace(0, 2 * np.pi, 100)
    y_cos = np.cos(x)
    y_sin = np.sin(x)
    plt.plot(x, y_cos, label='Cosine')
    plt.plot(x, y_sin, label='Sine')
    plt.title('Cosine and Sine Functions')
    plt.xlabel('Angle [radians]')
    plt.ylabel('Function Value')
    plt.legend()
    plt.grid()
    plt.show()

def plot_world_poplulation():
    import pandas as pd
    #data
    data = pd.DataFrame({
        'Country': ['China', 'India', 'United States', 'Indonesia', 'Pakistan'],
        'Population': [1444216107, 1393409038, 331893745, 273523621, 220892331]
    })
    plt.bar(data['Country'], data['Population'])
    plt.title('World Population by Country')
    plt.xlabel('Country')
    plt.ylabel('Population')
    plt.xticks(rotation=90)
    plt.show()
