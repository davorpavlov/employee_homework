def jutarnja_rutina ():
    print("DIJe vnago")
    print("SAmo jako")
jutarnja_rutina()


def upoznavanje(ime):
    print(f"Pozdrav, {ime}")
upoznavanje("Davor")

def user_status(status):
    username = "Davor"
    print(f"{username} is {status}")
user_status("Neactive")

def double_number(number):
    result = number * 2
    print(f"rezultat je: {result}")
double_number(100)

def age_label(age):
    label = "User age: " + age
    return label
result = age_label("29")
print(result)

def add_greeting(user):
    greeting = "Greetings " + user
    return greeting
result = add_greeting("Davor")
print(result)

def add_ten(number):
    sum = 10 + number
    return sum
print(add_ten(30))

def display(first, last):
    print(first + " " + last)
display("Davor", "Pavlovic")

def create_email(name, year):
    return name + year + "live.com"
email = create_email("play", "1991")
print(email)

def get_final_price (price, tax):
    return price * tax
price = get_final_price(30, 1.6)
print(price)

def zbroj(a, b):
    return a + b
zbrajanje = zbroj(42, 32)
print(f"Zbrajanje: {zbrajanje}")

def check_score(attempt):
    high_score = 97
    print(attempt > high_score)
check_score(1)