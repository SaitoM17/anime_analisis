import pandas as pd
import extract 

anime_raw = extract.extraccion_anime()

df = pd.DataFrame(anime_raw)
print(df)