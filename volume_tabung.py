print("Program Menghitung Volume Tabung")
print("================================")

r = float(input("\nMasukan nilai jari-jari tabung : "))
t = float(input("Masukan nilai tinggi tabung : "))

phi = 3.14

V = phi*r*r*t

print("Volume Tabung adalah =   cm³", "%.2f" % V)