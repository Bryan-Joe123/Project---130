import pandas as pd
import csv

df = pd.read_csv("Stars.csv")

del df["Luminosity"]

df = df.rename({
                'Star_name': "Name"
            }, axis='columns')

df.to_csv('stars.csv') 