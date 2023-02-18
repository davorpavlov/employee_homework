employees = [
['Goran', 'Gorić', 'Accountant', 1500, 'goran.goric@firma.com', '0911234567'],
['Darko', 'Darković', 'Developer', 2000, 'darko.darkovic@firma.com', '0919876543'],
['Mauro', 'Maurović', 'CEO', 3000, 'mauro.maurovic@firma.com', '095225883']
]

# Funkcija za ispisivanje podataka o djelatniku(koristimo index)
def employee_data(employee):
  print('First name and last name:', employee[0], employee[1])
  print('Work place:', employee[2])
  print('Salary:', employee[3])
  print('Email:', employee[4])
  print('Phone number:', employee[5])
  print()

# Ispisivanje podataka o svakom djelatniku
for employee in employees:
  employee_data(employee)