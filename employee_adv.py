employees = [
['Goran', 'Gorić', 'Accountant', 1500, 'goran.goric@firma.com', '0911234567'],
['Darko', 'Darković', 'Developer', 2000, 'darko.darkovic@firma.com', '0919876543'],
['Mauro', 'Maurović', 'CEO', 3000, 'mauro.maurovic@firma.com', '095225883']
]

def employee_data(employee):
    match employee:
        case [ime, prezime, radno_mjesto, placa, email, telefon]:
            print(f"First name and last name: {ime} {prezime}")
            print(f"Work place: {radno_mjesto}")
            print(f"Salary: {placa}")
            print(f"Email: {email}")
            print(f"Phone number: {telefon}")
            print()

# Ispisivanje podataka o svakom djelatniku
for employee in employees:
  employee_data(employee)