
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

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


# # ------------------------------------------------------------------------------------------------------------------------
# # Uppgift 3
# # ------------------------------------------------------------------------------------------------------------------------


def function_1():

    # befolkningen ska vara större än medelvärdet av befolkningen över alla  länder.
    pop_mean = df_cia_factbook['population'].mean()

    # arean ska vara mindre än medelarean över alla länder.
    area_mean = df_cia_factbook['area'].mean()

    # birth_rate (som är angivet i csv-filen som personer per 1000 invånare) ska ligga mellan 15 och 24. och life_exp_at_birth ska vara större än 70 år.

    # boolean mask för att bara visa det som är intressant
    mask = (df_cia_factbook['population'] > pop_mean) & (df_cia_factbook['area'] < area_mean) & (df_cia_factbook['birth_rate'].between(15, 24)) & (
                df_cia_factbook['life_exp_at_birth'] > 70)

    # spara maskeringen i egen variabel för att kunna användas
    masked_df_cia_factbook = df_cia_factbook[mask]

    # tabell med kolumnerna country, area, birth_rate, life_exp_at_birth
    print(masked_df_cia_factbook.loc[:, ["country", "area", "birth_rate", "life_exp_at_birth"]])

def function_2():
    # skapa ny kolumn för internet_user_density, som är kvoten mellan kolumnen population och kolumnen internet_users.
    df_cia_factbook['internet_user_density'] = df_cia_factbook['internet_users'] / df_cia_factbook['population'] * 100000
    # gånga med 100 000 för att få användare per 100k personer

    # sortera
    df_cia_factbook.sort_values(by=['internet_user_density'], ascending=False, inplace=True)

    # tabell som visar högst och lägst antal
    # 2, 11, 13 -> index för de intressanta kolumnerna
    print("Högst antal internet användare per 100k personer")
    print(df_cia_factbook.iloc[:5, [2, 11, 12]])
    print("Lägst antal internet användare per 100k personer")
    print(df_cia_factbook.iloc[-5:, [2, 11, 12]])

def function_3():
    # uppskattning om länderna i df_cia_factbook som har en positiv eller negativ befolkningsförändring

    # skapa ny kolumn för population_growth_rate = (birth_rate - death_rate + net_migration_rate).
    df_cia_factbook['population_growth_rate'] = df_cia_factbook['birth_rate'] -df_cia_factbook['death_rate'] + df_cia_factbook[
        'net_migration_rate']

    # Använder sedan population_growth_rate för att beräkna befolkningsförändringen dvs population_change
    df_cia_factbook['population_change'] = df_cia_factbook['population_growth_rate'] / 10

    # sorterar
    df_cia_factbook.sort_values(by=['population_change'], ascending=False, inplace=True)

    # de fem länder med mest negativ befolkningsförändring och de fem länder med högst
    # mest
    print("Högst befolkningsförändring")
    print(df_cia_factbook.iloc[:5, [2, 4, 5, 10,  13]])
    # minst
    print("minst befolkningsförändring")
    print(df_cia_factbook.iloc[-5:, [2, 4, 5, 10, 13]])


#     De tio länderna ska också presenteras i ett stapeldiagram där
# namnet på länderna finns på x-axeln och befolkningsförändringen finns på y-axeln.
#skriva ut resultaten
    plt.title("befolkningsförändringen")
    plt.xlabel("Land")
    plt.ylabel("population_change")
    plt.grid()
    plt.xticks(rotation=45, ha='right')

    plt.bar(x=df_cia_factbook.iloc[-5:,2], height=df_cia_factbook.iloc[-5:,13], width=0.5, bottom=None, align='center',label='KPI in barchart')
    plt.bar(x=df_cia_factbook.iloc[:5,2], height=df_cia_factbook.iloc[:5,13], width=0.5, bottom=None, align='center',label='KPI in barchart')

    plt.show()



def function_4():
    print("Hejdå!")

#meny med while loop för att menyvalen ska fortsätta visas efter varje alternativ
i=0
while(i<1):
    print("Meny:")
    print(f"1. Visa tabell med country, area, birth_rate och life_exp_at_birth")
    print(f"2. Visa internet user density")
    print(f"3. Visa befolkningsförändringen")
    print(f"4. Avsluta programmet")

    menuEntry = int(input("Välj menyalternativ (1–4):"))
    if menuEntry == 1:
        print(f"du har valt nr {menuEntry}, visa tabell")
        function_1()
    if menuEntry == 2:
        print(f"du har valt nr {menuEntry}, visa internet user density")
        function_2()
    if menuEntry == 3:
        print(f"du har valt nr {menuEntry}, visa positiv eller negativ befolkningsförändring")
        function_3()
    if menuEntry == 4:
        print(f"du har valt nr {menuEntry}")
        function_4()
        i=1


