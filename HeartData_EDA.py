import pandas as pd
import yaml
import matplotlib.pyplot as plt
import plotly.express as px

class HeartEDA:
    def __init__(self, config_file):
        # Load config file into memory
        with open(config_file, 'r') as file:
            self.configs = yaml.safe_load(file)
        # Load data and assign to self
        self.data = pd.read_csv(self.configs['heart_data'])

    def get_info(self):
        print(self.data.info())
        print(self.data.describe())

    def plot_dist(self, col):
        fig = px.histogram(self.data[col])
        fig.show()


if __name__ == "__main__":
    heart_eda = HeartEDA('config.yaml')  # Instantiate class and load data
    heart_eda.get_info()
    heart_eda.plot_dist()
