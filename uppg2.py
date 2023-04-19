
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
# # Uppgift 2
# # ------------------------------------------------------------------------------------------------------------------------


#skapa ny kolumn för density, som är kvoten mellan kolumnen population och kolumnen area.
df_cia_factbook['density'] = df_cia_factbook['population'] / df_cia_factbook['area']

#sorterar för att kunna hitta högsta och lägsta
df_cia_factbook.sort_values(by=['density'], ascending=False, inplace=True)

#Få användarinput
userInput = input('Skriv in antal länder (med + eller - efter) eller namnet på ett land: ')


#funktion olika beroende på vad för input


# loop för att forstätta
check= 0;
while check==0:
    if userInput[0].isalpha(): #bokstav ifall det är land som är skrivet
        userInput = userInput[0].upper() + userInput[1:] # se till att första bokstav är stor
        selectedInput = df_cia_factbook.loc[df_cia_factbook['country'] == userInput]
        nameFromInput = selectedInput.iloc[0, 2]
        densityFromInput = selectedInput.iloc[0, 12]
        print(f"the density of {nameFromInput} is {densityFromInput}")
        check=1;
    elif not userInput[0].isalpha(): #siffra ifall det är antal länder
        match = re.search(r'\d+', userInput) #regex för att hitta digit, för 1-10
        if match:
            userInputInt = int(match.group())
            if 1 <= userInputInt <= 10:
                if userInput[-1] == "+":  # kolla ifall det är max eller min
                    print(f"Showing top {userInputInt} numbers of countries with highest density")
                    # function för att hitta densiteten baserat på user input nr
                    df_top = df_cia_factbook.iloc[:userInputInt, [2,12]]
                    print(f"the top max is: \n {df_top}")
                    x = df_top.iloc[:, 0].values
                    y = df_top.iloc[:, 1].values
                    print(f"x is {x}")
                    print(f"y is {y}")



                else:
                    print(f"Showing bottom  {userInputInt} numbers of countries ")
                    # Lägsta länderna
                    df_bottom = df_cia_factbook.iloc[-userInputInt:, [2, 12]] # - tail = last of nrs
                    print(f"the lowest density is: \n {df_bottom}")
                    x = df_bottom.iloc[:, 0].values
                    y = df_bottom.iloc[:, 1].values


            else:
                print("not a number between 1-10")
            check = 2
        else:
            print("The input is not a valid integer.")


    else:
        print("not a valid input, try again")

if check == 2: #bara ifall man valt siffra
    #plottar de olika siffrorna
    plt.bar(x=x, height=y, width=0.5,  align='center', label='Density of countries')
    plt.title('Countries by Density')
    plt.ylabel('Density (people per square km')
    plt.xlabel("country")
    plt.xticks(rotation=45, ha='right')
    plt.legend()
    plt.show()


