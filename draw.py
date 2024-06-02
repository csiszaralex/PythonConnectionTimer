import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# # Adatok beolvasása CSV fájlból
df = pd.read_csv("data.csv", encoding="utf-8")

df = df.sort_values(by="Hossz")

# Oszlopok kijelölése
x_oszlop = "Hossz"
y_oszlop = "Idő"

# Adatok kinyerése
x_adatok = np.array(df[x_oszlop])
y_adatok = np.array(df[y_oszlop])

mask = x_adatok <= 700
x_adatok = x_adatok[mask]
y_adatok = y_adatok[mask]

# Grafikon rajzolása
plt.plot(x_adatok, y_adatok, marker='o', linestyle='-')

# Cimkék és cím beállítása
plt.xlabel("Karakterek száma (DB)")
plt.ylabel("Idő (Másodperc)")
plt.title("Idő függése a szöveg hosszától")

# Hálózat beállítása
plt.grid(True)

# Grafikon megjelenítése
# plt.savefig("grafikon.png")
plt.show()
