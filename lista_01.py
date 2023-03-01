djelatnici = [] # inicijaliziraj praznu listu

while True:
    ime = input("Unesite ime djelatnika (ili 'kraj' za kraj unosa): ")
    if ime.lower() == 'kraj':
        break # prekidaj petlju ako korisnik unese 'kraj'
    djelatnici.append(ime) # dodaj ime djelatnika u listu

print("Djelatnici su:", djelatnici) # ispisi sve djelatnike nakon unosa
