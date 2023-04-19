# Skapa klassen Dator som ska hålla reda på
# datortillverkare och viss annan information om datorn

import pickle5 as pickle

# Dator huvudklassen med getters och setters för att kunna ha tillgång
class Dator:
    def __init__(self):
        self.lista()

    def set_tillverkare(self):
        print("Ange tillverkare: ")
        self.__tillverkare = self.validstring()

    def get_tillverkare(self):
        return self.__tillverkare

    def set_processortyp(self):
        print("Ange processortyp: ")
        self.__processortyp = self.validstring()

    def get_processortyp(self):
        return self.__processortyp

    def set_modell(self):
        print("Ange modell: ")
        self.__modell = self.validstring()

    def get_modell(self):
        return self.__modell

    def set_ram(self):
        print("Ange ram (GB): ")
        self.__ram= self.validint()

    def get_ram(self):
        return self.__ram

    def set_inkopspris(self):
        print("Ange inköpspris: ")
        self.__inkopspris = self.validint()

    def get_inkopspris(self):
        return self.__inkopspris

    #lägger in input i lista för att spara allt i dictionary+lista över varje
    # dictionary inslag
    def lista(self):
        print("Ange antal datorer som ska skrivas in: ")
        datorantal = self.validint()
        self.__storLista = []
        for i in range(datorantal):
            datorDict = {}
            self.set_tillverkare()
            datorDict["tillverkare"] = self.get_tillverkare()
            self.set_modell()
            datorDict["modell"] = self.get_modell()
            self.set_processortyp()
            datorDict["processortyp"] = self.get_processortyp()
            self.set_ram()
            datorDict["RAM"] = self.get_ram()
            self.set_inkopspris()
            datorDict["inkopspris"] = self.get_inkopspris()
            self.__storLista.append(datorDict)
        return self.__storLista

    # skriver ut listan på  dictionary inslagen med formattering
    def visa_data(self):
        print("Tillverkare    Modell         Processortyp   Installerat RAM          Pris[kr]")
        print("===============================================================================")
        for datorDict in self.__storLista:
            print("{:<15} {:<14} {:<15} {:<25} {:<10}".format(datorDict["tillverkare"], datorDict["modell"],
            datorDict["processortyp"], str(datorDict["RAM"]) + " GB", str(datorDict["inkopspris"])))

    # kolla så att det är valid input
    def validstring(self):
        check = 0
        while check == 0:
            try:
                stringinput = input()
                if stringinput == "":
                    print("inte valid input, försök igen")
                elif (stringinput[0].isalpha()) and (len(stringinput) != 0):
                    stringinput = stringinput
                    check = 1
                else:
                    print("inte valid input, försök igen")
            except ValueError:
                print("Invalid input. Please enter a valid input.")
        return stringinput
        # ser till att input inte kraschar
    # kolla så att det är valid input
    def validint(self):
        check = 0
        while check == 0:
            try:
                intinput = input()
                if intinput == "":
                    print("Invalid input. Skriv in en siffra.")
                elif ((intinput[0].isnumeric()) and (intinput[0] != "0")):
                    intinput = int(intinput)
                    check = 1
                else:
                    print("inte rätt siffra, försök igen")
            except ValueError:
                print("Invalid input. Skriv in en siffra.")
        return intinput


d1 = Dator()
d1.visa_data()

# child class till Dator men med särskilda attribut som skrivs in vid initiering
class Laptop(Dator):
    def __init__(self, tillverkare="", modell="", processor="", ram="", inkopspris="", tumstorlek = ""):
        # super().__init__()
        self.__tillverkare = tillverkare
        self.__model = modell
        self.__processor = processor
        self.__ram=ram
        self.__inkopspris = inkopspris
        self.__tumstorlek= tumstorlek
        self.__datorDict = {}
        self.lista()

    # lägga till allt i lista för att skriva ut
    def lista(self):
        self.__datorDict["Tillverkare"] = self.__tillverkare
        self.__datorDict["Modell"] = self.__model
        self.__datorDict["Processortyp"] = self.__processor
        self.__datorDict["Installerad RAM"] = self.__ram
        self.__datorDict["Pris"] = self.__inkopspris
        self.__datorDict["Skärmstorlek"] = self.__tumstorlek
        return self.__datorDict

    def show(self):
        for key, value in self.__datorDict.items():
            if key == "Pris":
                print(f"{key}: {value}.0 Kr")
            elif key == "Installerad RAM":
                print(f"{key}: {value} GB")
            elif key == "Skärmstorlek":
                print(f"{key}: {value} tum")
            else:
                print(f"{key}: {value}")



l1 = Laptop('ASUS', 'ExpertBook', 'Core i5','16', '7990','15.6')
print("")
l1.show()



# uppgift c
#  sparar informationen om datorerna
#  i en fil med namnet dator.dat.

# Gör en class som i del 2A men som inte frågar om antal datorer innan
# man lägger in. Frågar efteråt ifall man vill lägga till flera eller inte
# för att sedan spara allt med pickle
class DatorTwo:
    def __init__(self):

        check = 0
        while check == 0:
            self.lista()
            check2 = 0
            while check2 == 0:
                svar = input("Vill du ange flera datorer? (ja/nej): ")
                if svar == ("nej" or "Nej" or "NEJ"):
                    check += 1
                    check2 = 1
                    self.save_data()
                elif svar == ("ja" or "JA" or "Ja"):
                    check = 0
                    check2 = 1
                else:
                    print("Inte giltigt input, försök igen")
                    check = 1
                    check2 = 0


    def save_data(self):
        pickle_out = open("dator.dat", "wb")
        pickle.dump(self.__datorDict, pickle_out)
        pickle_out.close()
        print("")
        print("Data är skriven i filen dator.dat.")

    def set_tillverkare(self):
        print("Ange datorns fabrikat: ")
        self.__tillverkare = self.validstring()

    def get_tillverkare(self):
        return self.__tillverkare

    def set_processortyp(self):
        print("Ange processortyp: ")
        self.__processortyp = self.validstring()

    def get_processortyp(self):
        return self.__processortyp

    def set_modell(self):
        print("Ange modell: ")
        self.__modell = self.validstring()

    def get_modell(self):
        return self.__modell

    def set_ram(self):
        print("Ange installerat RAM (GB): ")
        self.__ram= self.validint()

    def get_ram(self):
        return self.__ram

    def set_inkopspris(self):
        print("Ange pris(Kr): ")
        self.__inkopspris = self.validint()

    def get_inkopspris(self):
        return self.__inkopspris

    def lista(self):
        self.__datorDict = {}
        self.set_tillverkare()
        self.__datorDict["Tillverkare"] = self.get_tillverkare()
        self.set_modell()
        self.__datorDict["Modell"] = self.get_modell()
        self.set_processortyp()
        self.__datorDict["processortyp"] = self.get_processortyp()
        self.set_ram()
        self.__datorDict["Installerad RAM"] = self.get_ram()
        self.set_inkopspris()
        self.__datorDict["Pris"] = self.get_inkopspris()
        return self.__datorDict




    def validstring(self):
        check = 0
        while check == 0:
            try:
                stringinput = input()
                if stringinput == "":
                    print("inte valid input, försök igen")
                elif (stringinput[0].isalpha()) and (len(stringinput) != 0):
                    stringinput = stringinput
                    check = 1
                else:
                    print("inte valid input, försök igen")
            except ValueError:
                print("Invalid input. Please enter a valid input.")
        return stringinput
        # ser till att input inte kraschar

    def validint(self):
        check = 0
        while check == 0:
            try:
                intinput = input()
                if intinput == "":
                    print("Invalid input. Skriv in en siffra.")
                elif ((intinput[0].isnumeric()) and (intinput != "0")):
                    intinput = int(intinput)
                    check = 1
                else:
                    print("inte rätt siffra, försök igen")
            except ValueError:
                print("Invalid input. Skriv in en siffra.")
        return intinput
print("")
DatorTwo()

#uppgift D

# Laddar in informationen med pickle
def visa_data():
    pickle_in = open("dator.dat", "rb")
    dator_dict = pickle.load(pickle_in)
    print("")
    for key, value in dator_dict.items():
        if key == "Pris":
            print(f"{key}: {value}.0 Kr")
        elif key == "Installerad RAM":
            print(f"{key}: {value} GB")
        else:
            print(f"{key}: {value}")


visa_data()