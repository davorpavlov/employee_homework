vehicles = [
    {"ID": 1, "Tip": "Kamion", "Proizvođač": "Iveco", "Registarska oznaka": "OS 001 ZZ", "Godina prve registracije": 2015, "Cijena u EUR": 45000},
    {"ID": 2, "Tip": "Kamion", "Proizvođač": "Iveco", "Registarska oznaka": "OS 002 ZZ", "Godina prve registracije": 2015, "Cijena u EUR": 47000},
    {"ID": 3, "Tip": "Tegljač", "Proizvođač": "MAN", "Registarska oznaka": "RI 001 ZZ", "Godina prve registracije": 2018, "Cijena u EUR": 78000},
    {"ID": 4, "Tip": "Tegljač", "Proizvođač": "MAN", "Registarska oznaka": "RI 002 ZZ", "Godina prve registracije": 2020, "Cijena u EUR": 97000},
    {"ID": 5, "Tip": "Kombi", "Proizvođač": "Mercedes Benz", "Registarska oznaka": "ST 001 ZZ", "Godina prve registracije": 2013, "Cijena u EUR": 12000}
]

print("ID Tip Proizvođač Registarska oznaka Godina prve registracije Cijena u EUR")
for vehicle in vehicles:
    print(f"{vehicle['ID']}  {vehicle['Tip']} {vehicle['Proizvođač']} {vehicle['Registarska oznaka']} {vehicle['Godina prve registracije']} {vehicle['Cijena u EUR']}")
