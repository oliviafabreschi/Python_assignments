import numpy as np
import matplotlib.pyplot as plt

# 1a
# Skapa np array  f(x)=x+x**y
NP_A = np.array([[i+(i**y) for y in range(8)] for i in range(10)])

# 1b - extrahera med slicing och skriv ut

# minska storleken
extracted = NP_A[2:7,1:6]
# varannan element
extractedtwo = extracted[::2,::2]
print("1b. extracted values:")
print(extractedtwo)
print("\n")

#1C omvandla till lista, skriv ut

lista = NP_A.tolist()
print("1c. omvandlad till lista:")
print(lista)
print("\n")
# skrv sedan ut alla element i listan som är större än 10 men mindre än 100.
print("1c. omvandlad till lista med element större än 10, mindre än 100:")
for list in lista:
    for e in list:
        if 10<e<100:
            print(e)
        else:
            pass

# 1d
# Skriv ut summan av maximum och minimum samt medelvärdet för
# - varje rad
# - och varje kolumn  i NP_A i uppgift a.

#räknar ut max,min och medel varje rad
max_varje_rad = np.max(NP_A, axis=1)
min_varje_rad = np.min(NP_A, axis=1)
med_varje_rad = np.average(NP_A,axis =1)
#räknar ut max,min och medel varje kolumn
max_varje_kolumn= np.max(NP_A, axis=0)
min_varje_kolumn = np.min(NP_A, axis=0)
med_varje_kolumn = np.average(NP_A,axis =0)

# summorna
summa_varje_rad = max_varje_rad + min_varje_rad
print("1d. summa av min och max för varje rad: " , summa_varje_rad)
summa_varje_kolumn = max_varje_kolumn + min_varje_kolumn
print("")
print("1d. summa min och max för varje kolumn: " , summa_varje_kolumn)
print("")
print(f"1d. medelvärdet för varje rad:")
for e in med_varje_rad:
    print(e)
print("")
print(f"1d. medelvärdet för varje kolumn:")
for e in med_varje_kolumn:
    print(e)


# 1E
# Skapa en kopia av NP_A i uppg a
#  tillämpa funktionen where() för att byta ut alla element i denna kopia
#  som är större än 100 mot talet -1.
# Skriv därefter ut innehållet på skärmen.
print("")
print("1e. NP_A kopia med utbytte siffror:")
NP_A_kopia = np.copy(NP_A)
NP_A_kopia = np.where(NP_A > 100,-1,NP_A)
print(NP_A_kopia)

# 1F
# Omvandla NP_A i uppgift a till en vektor
#  (endimensionell NumPy-array) och döp den till
#  NP_Arr och skriv ut resultatet på skärmen.
print("")
print("1f. NP_Arr vektor: ")
NP_Arr = np.ravel(NP_A)
print(NP_Arr)

# 1G
# rita en graf över
# 1+NP_Arr**3+1+3*NP_Arr**2 + 6*NP_Arr
# 1+ 1+3*NP_Arr**2 + 6*NP_Arr
# 1+NP_Arr**3+ 6*NP_Arr
# i samma diagram


a = 1+NP_Arr**3+1+3*NP_Arr**2 + 6*NP_Arr
b = 1+ 1+3*NP_Arr**2 + 6*NP_Arr
c = 1+NP_Arr**3+ 6*NP_Arr


#en figyr med flera sub plots
fig, ax = plt.subplots(figsize=(12, 6))

#scatterplot
ax.plot(a, label="a")
ax.plot(b, label="b")
ax.plot(c, label="c")

plt.show()