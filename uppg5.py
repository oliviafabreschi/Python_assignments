
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

# ------------------------------------------------------------------------------------------------------------------------
# Uppgift 5
# ------------------------------------------------------------------------------------------------------------------------
# Skriv din kod här:

# hittar de 10 länder med flest antal städer (country with most count of city)
# hittar de city with the highest population per country av dessa 10
# make columns with country, N of cities in the country, name of city with HIGHGEST POP, number of POP

#räknar ut antal städer
cityCount = df_worldcities['country'].value_counts()

#Lägger till ny kolumn med country valuues
topTenCountries = cityCount.reset_index().iloc[:10]

#döper om kolumnerna så att det inte står index och country
topTenCountries.columns = ['country', 'city_count']

#skapar dictionary för att spara max values för varje namn
max_dict = {}

#Loopa över varje land i listan
for country_name in topTenCountries['country']:
    #kommpilera som regex pattern
    pattern = re.compile(country_name)
    #filtrera orginaldatan för att endast ha rader där landet i top 10 ingår
    name_df = df_worldcities[df_worldcities['country'].str.contains(pattern)]
    #hitta max i "value" för detta både index och popuulationantal
    max_value = name_df['population'].max()
    max_index = name_df['population'].idxmax()
    #hitta staden från max
    cityName = name_df.loc[max_index, 'city_ascii']
    #lägg till max till dictionary
    max_dict[country_name] = {'population': max_value, 'city_ascii': cityName}


#ny tabell med country, N of cities in the country, name of city with HIGHGEST POP, number of POP

#göra om dictionary till dataframe
df_cities_pop = pd.DataFrame(max_dict)


#transposera df för att få rätt riktning
df_cities_pop = df_cities_pop.transpose().reset_index(drop=True)
print(df_cities_pop)
df_cities_pop = df_cities_pop[['city_ascii', 'population']]
#lägga till dataframe för att få till i samma tabell horizontally (axis=1)
fullTable= pd.concat([topTenCountries, df_cities_pop], axis=1)

# döpa om för att få titlarna på svenska
fullTable = fullTable.rename(columns={'city_ascii': 'Största stad'})
fullTable = fullTable.rename(columns={'city_count': 'antal städer'})
fullTable = fullTable.rename(columns={'country': 'land'})
fullTable = fullTable.rename(columns={'population': 'antal inv. i största stad'})
print(fullTable)

#skriva ut resultaten
fig, axs = plt.subplots(2, 1)

# första subplot
axs[0].set_title("Länder med flest antal städer")
axs[0].set_xlabel("Land")
axs[0].set_ylabel("antal städer")
axs[0].grid()
axs[0].bar(x=fullTable.iloc[:,0], height=fullTable.iloc[:,1], width=0.5, bottom=None, align='center',label='Länder och städer')
plt.setp(axs[0].get_xticklabels(), rotation=90, ha='right')


# andra subpot
axs[1].set_title("Den största staden i respektive land")
axs[1].set_xlabel("Stad")
axs[1].set_ylabel("Antal invånare")
axs[1].grid()
axs[1].bar(x=fullTable.iloc[:,2], height=fullTable.iloc[:,3], width=0.5, bottom=None, align='center',label='Länder och städer')
plt.setp(axs[1].get_xticklabels(), rotation=90, ha='right')

# ändra spacing
plt.subplots_adjust(hspace=1.2, bottom =0.2)



# Display the figure
plt.show()