words = []
number_of_words = int(input('Koliko rijeci zelite napisati? '))

for i in range(number_of_words):
    word = input(f'Upisite {i + 1}. rijeci: ')
    words.append(word)

words.append("Algebra")

print()
print(f'Ispis rijeci iz "words({len(words)})" s brojem znakova')
print()

for word in words:
    print(f"Rijec '{word}' ima {len(word)} slova.")