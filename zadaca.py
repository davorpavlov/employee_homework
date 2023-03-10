# # kreiranje rječnika sa podacima o vozilima
# vozila = {
#     1: {"tip": "Kamion", "proizvođač": "Iveco", "registarska oznaka": "OS 001 ZZ", "godina prve registracije": 2015, "cijena": 45000.00},
#     2: {"tip": "Kamion", "proizvođač": "Iveco", "registarska oznaka": "OS 002 ZZ", "godina prve registracije": 2015, "cijena": 47000.00},
#     3: {"tip": "Tegljač", "proizvođač": "MAN", "registarska oznaka": "RI 001 ZZ", "godina prve registracije": 2018, "cijena": 78000.00},
#     4: {"tip": "Tegljač", "proizvođač": "MAN", "registarska oznaka": "RI 002 ZZ", "godina prve registracije": 2020, "cijena": 97000.00},
#     5: {"tip": "Kombi", "proizvođač": "Mercedes Benz", "registarska oznaka": "ST 001 ZZ", "godina prve registracije": 2013, "cijena": 12000.00},
#     6: {"tip": "Kombi", "proizvođač": "Volkswagen", "registarska oznaka": "ST 002 ZZ", "godina prve registracije": 2021, "cijena": 35000.00},
#     7: {"tip": "Dostavno vozilo", "proizvođač": "Volkswagen", "registarska oznaka": "ZG 001 ZZ", "godina prve registracije": 2010, "cijena": 9000.00},
#     8: {"tip": "Dostavno vozilo", "proizvođač": "Volkswagen", "registarska oznaka": "ZG 002 ZZ", "godina prve registracije": 2010, "cijena": 9300.00},
# }

# # ispisivanje podataka o vozilima u konzoli
# print("{:^4} {:<16} {:<18} {:<16} {:^4} {:>12}".format("ID", "Tip", "Proizvođač", "Registarska oznaka", "Godina", "Cijena (EUR)"))
# print("-" * 82)
# for id, vozilo in vozila.items():
#     tip = vozilo["tip"]
#     proizvođač = vozilo["proizvođač"]
#     reg_oznaka = vozilo["registarska oznaka"]
#     godina_reg = vozilo["godina prve registracije"]
#     cijena = vozilo["cijena"]
#     print("{:^4} {:<16} {:<18} {:<16} {:^4} {:>12,.2f}".format(id, tip, proizvođač, reg_oznaka,

# podaci o vozilima
import os

os.system('cls')
vehicles = [
    {"ID": 1, "Tip": "Kamion", "Proizvođač": "Iveco", "Registarska oznaka": "OS 001 ZZ", "Godina prve registracije": 2015, "Cijena u EUR": 45000},
    {"ID": 2, "Tip": "Kamion", "Proizvođač": "Iveco", "Registarska oznaka": "OS 002 ZZ", "Godina prve registracije": 2015, "Cijena u EUR": 47000},
    {"ID": 3, "Tip": "Tegljač", "Proizvođač": "MAN", "Registarska oznaka": "RI 001 ZZ", "Godina prve registracije": 2018, "Cijena u EUR": 78000},
    {"ID": 4, "Tip": "Tegljač", "Proizvođač": "MAN", "Registarska oznaka": "RI 002 ZZ", "Godina prve registracije": 2020, "Cijena u EUR": 97000},
    {"ID": 5, "Tip": "Kombi", "Proizvođač": "Mercedes Benz", "Registarska oznaka": "ST 001 ZZ", "Godina prve registracije": 2013, "Cijena u EUR": 12000},
    {"ID": 6, "Tip": "Kombi", "Proizvođač": "Volkswagen", "Registarska oznaka": "ST 002 ZZ", "Godina prve registracije": 2021, "Cijena u EUR": 35000.00},    
    {"ID": 7, "Tip": "Dostavno vozilo", "Proizvođač": "Volkswagen", "Registarska oznaka": "ZG 001 ZZ", "Godina prve registracije": 2010, "Cijena u EUR": 9000.00},    
    {"ID": 8, "Tip": "Dostavno vozilo", "Proizvođač": "Volkswagen", "Registarska oznaka": "ZG 002 ZZ", "Godina prve registracije": 2010, "Cijena u EUR": 9300.00}
]

print("ID  | Tip             | Proizvođač      | Registarska oznaka  | Godina prve registracije | Cijena u EUR")
print("-------------------------------------------------------------------------------------------------------")

for vehicle in vehicles:
    print(f"{vehicle['ID']:2}  | {vehicle['Tip']:15} | {vehicle['Proizvođač']:15} | {vehicle['Registarska oznaka']:19} | {vehicle['Godina prve registracije']:24} | {vehicle['Cijena u EUR']:10}")
