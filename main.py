
import csv

pokemons = []

# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.in/python/file-handling
with open('pokemon.csv', newline='') as csv_file:
    file_reader = csv.reader(csv_file, delimiter = ',', quotechar='|')

    for row in file_reader:
        pokemons.append(row[0])

# print(pokemons)

print("Pokemon list command:")

while True:
    print("1. Get pokemon by sequence number")
    print("2. Sort by A-Z")
    print("3. Sort by Z-A")
    print("4. Search by name")
    print("5. Search by length of name")
    print("6. Print 10 pokemns")
    print("7. Exit")
    
    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        number = input("Choose a sequential number:")
        print(pokemons[int(number)])
        pass
    elif choice == '2':
        pokemons.sort()
        print(pokemons)
        pass
    elif choice == '3':
        pokemons.sort(reverse = True)
        print(pokemons)
        pass
    elif choice == '4':
        name = input('Find:')
        newpokemons = []
        for x in pokemons:
            if x.startswith(name) == True:
                newpokemons.append(x)
        print(newpokemons)   
        pass
    elif choice == '5':
        length = input('Find:')
        newpoki = []
        for x in pokemons:
            if int(length) == len(x):
                newpoki.append(x)
        print(newpoki)
        pass
    elif choice == '6':
        pokipoki = len(pokemons)
        for x in pokipoki:
            if x < 10:
    
    elif choice == '7':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 6")

    print("==========================")