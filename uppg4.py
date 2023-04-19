
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


# ------------------------------------------------------------------------------------------------------------------------
# Uppgift 4
# ------------------------------------------------------------------------------------------------------------------------
# program som analyserar den procentuella befolkningsutvecklingen
# mellan åren 1960 och 2021 för de länder som finns i DataFrame df_worldpubind


# skapa ny kolumn för population_growth_rate = ((antal_invånare_2021 – antal_invånare_1960) / antal_invånare_1960)*100
df_worldpubind['population_growth_rate'] = (df_worldpubind['2021'] - df_worldpubind['1960']) /df_worldpubind["1960"] * 100
# sortera för att kunna hitta högsta och lägsta
df_worldpubind.sort_values(by=['population_growth_rate'], ascending=False, inplace=True)
print("Minst utveckling")
print(df_worldpubind.iloc[-5:, [0, 66]])
print("Störst utveckling")
print(df_worldpubind.iloc[:5, [0, 66]])

#skriva ut resultaten
plt.title("Minst befolkningsförändringen")
plt.xlabel("Land")
plt.ylabel("population_change")
plt.grid()
plt.xticks(rotation=45, ha='right')
plt.bar(x=df_worldpubind.iloc[-5:,0], height=df_worldpubind.iloc[-5:, 66], width=0.5, bottom=None, align='center', label='befolkningsförändring barchart')
plt.show()

plt.title("Störst befolkningsförändringen")
plt.xlabel("Land")
plt.ylabel("population_change")
plt.grid()
plt.xticks(rotation=45, ha='right')
plt.bar(x=df_worldpubind.iloc[:5,0], height=df_worldpubind.iloc[:5,66], width=0.5, bottom=None, align='center',label='befolkningsförändring barchart')
plt.show()


# input för del 2
userInput = input('Skriv in land: ')

# population_change.
if userInput[0].isalpha():  #kollar efter första bokstav för att hitta ifall det är ett land
    userInput = userInput[0].upper() + userInput[1:]  # se till att första bokstav är stor
    selectedInput = df_worldpubind.loc[df_worldpubind['ï»¿Country Name'] == userInput]
    print(selectedInput)

#titta bara på åren/kolumnerna mellan 1960 och 2021
start_col = "1960"
end_col = "2021"

#gör en slice av varje rad mellan årtalen
slicedrow = selectedInput.loc[:, start_col:end_col]

# transpose för att ha åren för plotten
slicedrowTransposed = slicedrow.transpose().reset_index()
yearList = slicedrowTransposed.iloc[:,0].squeeze()

#räknar ut procentskillnaden, först gör tomma listor sen jämföra index mot index-1 för att räkna procentskillnaden
percent_increases = []
difference = []
for col, value in slicedrow.items():
    # hoppa över första kolumnen, finns inget att jämföra mot
    if col == slicedrow.columns[0]:
        continue
    # räkna ut procentskilldan mellan kolummnen och den innan
    prev_col = slicedrow.columns[slicedrow.columns.get_loc(col) - 1]
    prev_value = slicedrow[prev_col]
    current_increase = ((value - prev_value) / prev_value) * 100
    difference_increase = value + prev_value
    # lägga till för att få totala skillnaden
    percent_increases.append(current_increase)
    difference.append(difference_increase)


# lista för antal endast
differenceDF = pd.DataFrame(difference)
print(differenceDF)
# differencePrint = differenceDF.iloc[0].differencePrint.tolist()
# print(differencePrint)

#skapa plotten
fig, ax1 = plt.subplots()

#plotta första linjen
ax1.plot(percent_increases, color='red')
ax1.set_xlabel('År')
ax1.set_ylabel('Befolkningsförändringen', color='red')
ax1.tick_params(axis='y')
ax1.legend([userInput + " befolkningsförändring"], fontsize=8)


# gör y-axis för att kunna göra subplot
ax2 = ax1.twinx()

# plotta andra
ax2.plot(difference, color='blue')
ax2.set_ylabel('Folkmängd', color='blue')
ax2.tick_params(axis='y')
ax2.legend([userInput + " folkmängd"], loc="upper right", fontsize=8)

plt.grid()

plt.title('Befolkningsutveckling år per år')

# visar årtalen vart 10e år
tickLocation = np.arange(0, len(yearList), 10)
ax2.set_xticks(tickLocation)
ax2.set_xticklabels(yearList[tickLocation])

# visa
plt.show()


