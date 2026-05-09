from pathlib import Path
import pandas as pd

"""
Clase para generar el Dataframe principal de nuestro código.
    
"""
class DataFrame:
    def __init__(self):
        # Carpeta donde está este archivo .py
        base_path = Path(__file__).resolve().parent
        
        # Ruta al CSV
        csv_path = base_path / "../CSVs/StudentPerformanceFactors_realistic.csv"
        
        # Normaliza la ruta
        csv_path = csv_path.resolve()

        self.df = pd.read_csv(csv_path)
        
    def getdf(self):
        return self.df