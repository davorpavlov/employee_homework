import os

os.system('cls')
employee = {
    #kljuc            vrijednost
    #key              value
    '11111111111' : 'Pero Peric',
    '22222222222' : 'Ana Anic',
    '33333333333' : 'Marko Maric'
}

dict = employee.keys()
print(dict)

for key in employee.keys():
    print(key)
    print(employee[key])
    

names = ['Pero', 'Ana', 'The Marko', 'Mirko', 'Slavko']

employees_copy = employee.copy()
employee['11111111111'] = 'Mirko Mirkic'
print(employee)
print(employees_copy)