# GDP per Capita, Family, Life Expectancy, Freedom, Generosity, Trust Government Corruption

# 3a
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

try:
    df_world_happiness_2015 = pd.read_csv("2015.csv", delimiter=';')
except FileNotFoundError:
    print("fil hittades inte")
try:
    df_world_happiness_2016 = pd.read_csv("2016.csv", delimiter=';', encoding='ISO-8859-1')
except FileNotFoundError:
    print("fil hittades inte")

# printing the first five lines of the DataFrames
print(" 3a:")
print(df_world_happiness_2015[:5])
print(df_world_happiness_2016[:5])

# 3b:
print(" 3b:")
df_world_happiness_2015 = df_world_happiness_2015.rename(columns={"Happiness Score": "Happiness", "Trust (Government Corruption)": "Trust"})
df_world_happiness_2016 = df_world_happiness_2016.rename(columns={"Happiness Score": "Happiness", "Trust (Government Corruption)": "Trust"})

databyregion2015 = df_world_happiness_2015.groupby("Region")
means2015 = databyregion2015[["Freedom", "Happiness", "Trust"]].mean()
databyregion2016 = df_world_happiness_2016.groupby("Region")
means2016 = databyregion2016[["Freedom", "Happiness", "Trust"]].mean()

# räknar ut skillnad i % från 2015 till 2016
meansdiff = (means2016 - means2015) / means2015 * 100

print("========================================================================")
print("Average Freedom, Happiness, and Trust by region for the year 2015 ")
print("========================================================================")
print(means2015.round(decimals=3))
print("========================================================================")
print("\n")

print("========================================================================")
print("Average Freedom, Happiness, and Trust by region for the year 2016 ")
print("========================================================================")
print(means2016.round(decimals=3))
print("========================================================================")

print("\n")
print("========================================================================")
print("relative change displayed in % Freedom, Happiness, and Trust 2015-2016 ")
print("========================================================================")
print(meansdiff.round(decimals=3))
print("========================================================================")



#för att ha x axis och staplarna bredvic
regions = list(meansdiff.index)
x=np.arange(len(regions))
bar_width = 0.2
bar_offset = 0.05
# create bar plot
plt.bar(x, height=meansdiff["Freedom"], width=bar_width, label='Freedom', align='center')
plt.bar(x+bar_width+bar_offset, height=meansdiff["Happiness"], width=bar_width, label='Happiness', align='center')
plt.bar(x+2*bar_width+2*bar_offset, height=meansdiff["Trust"], width=bar_width, label='Trust', align='center')

plt.title('relative change in freedom, happiness and trust from 2015-2016')
plt.ylabel('relative change in %')
plt.xlabel("region ")
plt.xticks(x+bar_width+bar_offset, regions, rotation=90, ha='right')
plt.legend(loc='lower right')
plt.show()


#3C
# analyzing the top 10 happiest countries in the year 2015 and 2016
# 1.Create the new DataFrames named as df_2015 and df_2016
# which contains only columns ‘Country’, ‘Health (Life Expectancy)’, ’Happiness Rank’

df_2015 = df_world_happiness_2015[["Country", "Health (Life Expectancy)", "Happiness Rank"]]
df_2016 = df_world_happiness_2016[["Country", "Health (Life Expectancy)", "Happiness Rank"]]

# 2. rename the colummns
df_2015 = df_2015.rename(columns={"Health (Life Expectancy)": "Health_Expectancy_2015", "Happiness Rank": "Rank_2015"})
df_2016 = df_2016.rename(columns={"Health (Life Expectancy)": "Health_Expectancy_2016", "Happiness Rank": "Rank_2016"})

# 3. Sort the values for the both DataFrames
# by 'Health_Expectancy_<year>’, where <year> refer to 2015 and 2016. (2p)
df_2015 = df_2015.sort_values(by='Health_Expectancy_2015', ascending=False)
df_2016 = df_2016.sort_values(by='Health_Expectancy_2016', ascending=False)

# 4.Create the new DataFrames from df_2015 and df_2016 for the top 10 countries
# by Health_Expectancy and their corresponding Rank and print a table as shown in Table 4 and 5. (2p)
df_2015_top10 = df_2015[:10].reset_index(drop=True)
df_2016_top10 = df_2016[:10].reset_index(drop=True)
print("")
print("3c:")
print("========================================================================")
print("Top 10 high life expectancy countries for year 2015")
print("========================================================================")
print(df_2015_top10)
print("========================================================================")
print("")
print("========================================================================")
print("Top 10 high life expectancy countries for year 2016")
print("========================================================================")
print(df_2016_top10)
print("========================================================================")

# 5.Plot the scatter plot with x axis as Health Expectancy and y axis as Rank for the top 10 countries in 2015 and 2016.
# Combine the scatterplots using the subplot function. The figure must have
# the title, x and y axis label, legend and text annotation with the country name as shown in Figure 2. (3p)

countrylabels1 = df_2015_top10["Country"]
countrylabels2 = df_2016_top10["Country"]

#skapa plotten
y1= df_2015_top10["Rank_2015"]
y2= df_2016_top10["Rank_2016"]

#plotta första för 2015
x1 = df_2015_top10["Health_Expectancy_2015"]
x2 = df_2016_top10["Health_Expectancy_2016"]

#en figyr med 2 sub plots
fig, ax = plt.subplots(figsize=(12, 6))

#scatterplot and labels for 2015 data
ax.scatter(x1, y1, label="2015")
for i, txt in enumerate(countrylabels1):
    ax.annotate(txt, (x1[i], y1[i]))

#scatterplot and labels for 2016 data
ax.scatter(x2, y2, label="2016")
for i, txt in enumerate(countrylabels2):
    ax.annotate(txt, (x2[i], y2[i]))


plt.xlabel('health expectancy')
plt.ylabel('rank')
plt.title('Top 10 countries for 2015 and 2016 by health expectancy and their corresponding ranks')
plt.legend()

#visa plotten
plt.show()

# 6.Plot the bar plots for the countries (Hong kong, Singapore, Japan, South Korea, Italy)
countries = ["Hong Kong", "Singapore", "Japan", "South Korea", "Italy"]

df_2015_countries = df_2015[df_2015['Country'].isin(countries)]
df_2016_countries = df_2016[df_2016['Country'].isin(countries)]


y1= df_2015_countries["Health_Expectancy_2015"]
y2= df_2016_countries["Health_Expectancy_2016"]
x=np.arange(len(countries))
bar_width = 0.2
bar_offset = 0.05
# create bar plot
plt.bar(countries, height=y1, width=bar_width, label='Health_Expectancy_2015', align='center')
plt.bar(x+bar_width+bar_offset, height=y2, width=bar_width, label='Health_Expectancy_2016', align='center')

plt.title('Countries with high Health expectancy')
plt.xlabel('Countries')
plt.ylabel('Health expectancy')
plt.legend()

plt.show()


y1= df_2015_countries["Rank_2015"]
y2= df_2016_countries["Rank_2016"]
x=np.arange(len(countries))
bar_width = 0.2
bar_offset = 0.05
# create bar plot
plt.bar(countries, height=y1, width=bar_width, label='Rank_2015', align='center', color = "blue")
plt.bar(x+bar_width+bar_offset, height=y2, width=bar_width, label='Rank_2016', align='center', color = "green")

plt.title('Happiest country ranking')
plt.xlabel('Countries')
plt.ylabel('Rank')
plt.legend()

plt.show()