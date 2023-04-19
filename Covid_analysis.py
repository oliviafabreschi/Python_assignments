# -*- coding: utf-8 -*-

import pandas as pd


# Skriv ditt namn och ditt S-ID här:
# @author: Olivia Fabreschi
# UserID:   S2209588


# Skriv källkoden till Uppgift 3a här nedan:


try:
    df_covid19 = pd.read_csv("WHO_COVID19_GLOBAL_DATA-2.csv", delimiter=';')
except FileNotFoundError:
    print("fil hittades inte")
try:
    df_population = pd.read_csv("POPULATION_DATA_WORLD-2.csv", delimiter=';', encoding='ISO-8859-1')
except FileNotFoundError:
    print("fil hittades inte")

# tar bort alla nan för att undvika krascher
pd.options.display.float_format = '{:.2f}'.format

df_population = df_population.dropna()

df_covid19.info()

# Skriv källkoden till Uppgift 3b här nedan:
# Select countries and calculate relevant data
countries = ["United States of America", "India", "Brazil", "Russian Federation","Sweden", "Norway"]
countrylist = []
smittadlist = []
totalcovid100list = []
totalDeaths100list = []


for country in countries:
    population = df_population.loc[df_population['Country'] == country, "Population_2020"].values
    countrylist.append(population)
    # countryPop = df_population["Population_2020"].loc[df_population['Country'] == country]
    # countryName = df_population["Country"].loc[df_population['Country'] == country]
    # countrylist.append(countryName.tolist())
    # countryPop = country.loc[1]
    covid = df_covid19.loc[df_covid19['Country'] == country, "Cumulative_cases"].values
    deaths = df_covid19.loc[df_covid19['Country'] == country, "Cumulative_deaths"].values
    totalCovid = covid[-1]
    totalDeaths = deaths[-1]
    # print(countrylist)
    # % av befolkningen smittad
    smittad = totalCovid/population * 100
    smittadlist.append(smittad)
    # smittad och avlidna per 100k invånare
    totalCovid100 = totalCovid/(population/100000)
    # print(totalCovid100)
    totalcovid100list.append(totalCovid100.tolist())
    totalDeaths100 = totalDeaths/(population/100000)
    # print(totalDeaths100)
    totalDeaths100list.append(totalDeaths100.tolist())


# converting to float to remove brackets
clean_smittadlist = [item[0] for item in smittadlist]
clean_totalcovid100list = [item[0] for item in totalcovid100list]
clean_totalcovid100list = [item[0] for item in totalcovid100list]


print("\nTOTALA ANTALET SMITTADE UNDER PERIODEN 2020-01-03 -- 2021-08-06 UTTRYCKT I "
"FÖRHÅLLANDE TILL FOLKMÄNGD OCH TOTALA ANTALET SMITTADE OCH AVLIDNA PER "
"100.000 INVÅNARE.")
print("=================================================================================================")
print("Land                    Smittad (% av bef.)        Smittad per 100k       Avlidna per 100k")
print("_________________________________________________________________________________________________")
for i in range (0,5):
    print(f"{countries[i]:<24}      {clean_smittadlist[i]:^10.1f}       { clean_totalcovid100list[i]:^20.0f}     { clean_totalcovid100list[i]:>15.0f} ")

# 2020-01-03 -- 2021-08-06



# 2020-01-03 -- 2021-08-06)



# Skriv källkoden till Uppgift 3c här nedan:

df_seno = df_covid19[df_covid19["Country"].isin(["Sweden", "Norway"])].loc[:,["Country", "Date_reported", "New_cases"]].groupby("Date_reported")
df_test = df_covid19[df_covid19["Country"].isin(["Sweden", "Norway"])].loc[:,["Country", "Date_reported", "New_cases"]]

populations_seno = df_population[df_population["Country"].isin(["Sweden", "Norway"])].groupby("Country")
pop_se = populations_seno.get_group("Sweden")["Population_2020"].values[0]
pop_no = populations_seno.get_group("Norway")["Population_2020"].values[0]

# print(df_test)

print("\n\nDATUM UNDER PERIODEN 2020-01-03 -- 2021-08-06 DÅ ANTALET SMITTADE PER 100,000"
      "\nINVÅNARE I NORGE VAR STRIKT HÖGRE ÄN I SVERIGE. DATUM DÅ ANTALET SMITTADE I"
      "\nNORGE VAR MINDRE ÄN 500 PERSONER ÄR UTELÄMNADE I TABELLEN.")
print("="*80)

print("{:<30}{:^40}".format("Datum", "Smittotal per 100,000 invånare"))
print("{:<40}{:<15}{:<15}".format("", "Norge", "Sverige"))
print("-"*80)

for key, item in df_seno:
    infected = item["New_cases"].values
    infected_no = ((infected[0] / pop_no) * 100000)
    infected_se = ((infected[1] / pop_se) * 100000)
    if(infected[0] >= 500 and infected_no > infected_se):
        print("{:<40}{:<15.1f}{:<15.1f}".format(key, infected_no, infected_se))



# same but using regex instead!!!!
dftest = df_covid19.loc[df_covid19["Country"].str.contains("Sweden|Norway", regex= True),["Country", "Date_reported", "New_cases"]]
dftest = dftest.reset_index()
dftest = dftest.loc[(df_covid19["New_cases"] >= 500)]
print("this is dftest")
# print(dftest)

# same but using masks instead!!!!
df = df_covid19.loc[df_covid19["Country"].isin(["Sweden", "Norway"]) & (df_covid19["New_cases"] >= 500), ["Country", "Date_reported", "New_cases"]]
populations_snn = df_population.loc[df_population["Country"].isin(["Sweden", "Norway"]), ["Country", "Population_2020"]].set_index("Country")
# pop_snn = populations_snn.loc["Sweden", "Population_2020"]
# pop_noo = populations_snn.loc["Norway", "Population_2020"]
smittotal_snn = df.pivot(index="Date_reported", columns="Country", values="New_cases") / populations_snn.loc[df["Country"].unique(), "Population_2020"].values * 100000
mask = smittotal_snn["Norway"] > smittotal_snn["Sweden"]

# print(smittotal_snn[mask])


# Define the list of countries
countries = ["United States of America", "India", "Brazil", "Russian Federation", "Sweden", "Norway"]

# Merge the population data with the COVID-19 data
df = pd.merge(df_covid19[df_covid19['Country'].isin(countries)],
              df_population[['Country', 'Population_2020']],
              on='Country')

# Calculate the relevant data for each country
df['Smittad (%)'] = df['Cumulative_cases'] / df['Population_2020'] * 100
df['Smittad per 100k'] = df['Cumulative_cases'] / df['Population_2020'] * 100000
df['Avlidna per 100k'] = df['Cumulative_deaths'] / df['Population_2020'] * 100000

# Print the results
print("\nTOTALA ANTALET SMITTADE UNDER PERIODEN 2020-01-03 -- 2021-08-06 UTTRYCKT I "
      "FÖRHÅLLANDE TILL FOLKMÄNGD OCH TOTALA ANTALET SMITTADE OCH AVLIDNA PER "
      "100.000 INVÅNARE.")
print("=================================================================================================")
print("Land                    Smittad (% av bef.)        Smittad per 100k       Avlidna per 100k")
print("_________________________________________________________________________________________________")
# for _, row in df.iterrows():
    # if row['Country'] in countries:
        # print(f"{row['Country']:<24}      {row['Smittad (%)']:^10.1f}       {row['Smittad per 100k']:^20.0f}     {row['Avlidna per 100k']:}>")


