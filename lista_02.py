prirez_na_porez = float(input("Unesite prirez na porez: ")) / 100

neto_placa = float(input("Unesite neto plaću: "))

osnovica_poreza = (neto_placa / (1 - prirez_na_porez) - 530.9) / 0.8

bruto_placa = osnovica_poreza + neto_placa / (1 - prirez_na_porez)

mirovinski_doprinos = 0.2 * bruto_placa

print(f"Bruto plaća: {bruto_placa:.2f} €")
print(f"Mirovinski doprinos: {mirovinski_doprinos:.2f} €")
