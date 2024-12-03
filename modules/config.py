from imports import *

from objects.config import Config

class Configs:
    def __init__(self):
        self.config = self.load()
        
        self.configs = Config(self.config)
    
    def load(self) -> dict:
        with open("data/config.yaml", "r") as file:
            config = yaml.safe_load(file)
        
        return config