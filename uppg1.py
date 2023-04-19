
import pandas as pd


# ------------------------------------------------------------------------------------------------------------------------
# Uppgift 1 - läsa in en csv-fil till en pandas dataframe
# ------------------------------------------------------------------------------------------------------------------------

try:
    df_cia_factbook = pd.read_csv("cia_factbook.csv", delimiter=';')
except FileNotFoundError:
    print("fil hittades inte")
try:
    df_worldpubind = pd.read_csv("worldpubind.csv", delimiter=';', encoding='ISO-8859-1')
except FileNotFoundError:
    print("fil hittades inte")
try:
    df_worldcities = pd.read_csv("worldcities.csv", delimiter=';', encoding='ISO-8859-1')
except FileNotFoundError:
    print("fil hittades inte")


# tar bort alla nan för att undvika krascher
pd.options.display.float_format = '{:.2f}'.format
df_cia_factbook = df_cia_factbook.dropna()
df_worldcities = df_worldcities.dropna()
df_worldpubind = df_worldpubind.dropna()



