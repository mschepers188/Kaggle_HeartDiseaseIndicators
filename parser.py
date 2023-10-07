import pandas as pd
import yaml


class FileParser:
    """
    Contains all functions to load and parse the heard disease file.
    """
    def __init__(self, config_file):
        # Load config file into memory
        with open(config_file, 'r') as file:
            self.configs = yaml.safe_load(file)

    def load_dataframe(self):
        # Return dataframe containing data
        return pd.read_csv(self.configs['heart_data'])


if __name__ == "__main__":
    fileparser = FileParser('config.yaml')
    print(fileparser.load_dataframe())
