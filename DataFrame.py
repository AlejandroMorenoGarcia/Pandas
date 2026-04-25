import pandas as pd

class DataFrame:
    def __init__(self):
        self.df = pd.read_csv("StudentPerformanceFactors.csv")
        
    def getdf(self):
        return self.df