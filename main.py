import pandas as pd
import sqlite3

matches = pd.read_csv("data/matches.csv")

conn = sqlite3.connect("ipl.db")

matches.to_sql("matches", conn, if_exists="replace", index=False)

print("Database created")