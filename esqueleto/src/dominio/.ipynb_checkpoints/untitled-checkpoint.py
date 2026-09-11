from pathlib import Path
import pandas as pd

camino_abs = os.path.abspath("../../data/canciones.csv")
database = pd.read_csv(camino_abs)

print(database.head(5))
