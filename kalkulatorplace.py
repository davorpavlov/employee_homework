bruto_placa = float(input("Unesite bruto plaću: "))

mirovinski_doprinos = 0.2 * bruto_placa
porezna_osnovica = 530.9
osnovica_poreza = max(bruto_placa - mirovinski_doprinos - porezna_osnovica, 0)

porezna_stopa = 0.2
porez = porezna_stopa * osnovica_poreza

prirez_na_porez = float(input("Unesite prirez na porez: ")) / 100 * porez

neto_placa = bruto_placa - mirovinski_doprinos - porez - prirez_na_porez

print(f"Bruto plaća: {bruto_placa:.2f} €")
print(f"Mirovinski doprinos: {mirovinski_doprinos:.2f} €")
print(f"Porez na dohodak: {porez:.2f} €")
print(f"Prirez na porez: {prirez_na_porez:.2f} €")
print(f"Neto plaća: {neto_placa:.2f} €")

