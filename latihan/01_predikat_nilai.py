nilai = float (input("Nilai_akhir(0-100):"))

if nilai >= 85:
    Predikat = "A"
elif nilai >= 70:
    Predikat = "B"
elif nilai >= 60:
    Predikat = "C"
elif nilai >= 50:
    Predikat = "D"
else:
    Predikat = "E"

print(f"Nilai {nilai:.2f}, memperoleh predikat {Predikat}.")