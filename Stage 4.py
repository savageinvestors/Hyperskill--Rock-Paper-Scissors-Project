import random
user_name = input('Enter your Name: ')
print(f'Hello {user_name}')

rating_file = open("rating.txt")
rating: int = 0
for line in rating_file
    name, score = line.split(" ")
    if name == user_name:
        rating = int(score)

rules = {'rock': {'win': 'scissors', 'lose': 'paper', 'draw': 'rock'}, 'paper': {'win': 'rock', 'lose': 'scissors', 'draw': 'paper'}, 'scissors': {'win': 'paper', 'lose': 'rock', 'draw': 'scissors'}}
option = ['rock', 'paper', 'scissors']
x = input()

while x != '!exit':
    for i in range(100):
        y = random.choice(option)
        if x == '!exit':
            print('Bye!')
            rating_file.close()
            exit()
        if x == '!rating':
            print('Your rating: ' + str(rating))
            x = input()
        if x not in option and x != '!exit' and x != '!rating':
            print('Invalid input')
            x = input()
        if x == 'rock':
            if y == 'rock':
                print('There is a draw (' + rules['rock']['draw'] +')')
                rating += 50
                x = input()
            elif y == 'scissors':
                print('Well done. Computer chose ' + rules['rock']['win'] + ' and failed')
                x = input()
                rating += 100
            elif y == 'paper':
                print('Sorry, but computer chose ' + rules['rock']['lose'])
                x = input()
        if x == 'paper':
            if y == 'paper':
                print('There is a draw (' + rules['paper']['draw'] +')')
                x = input()
                rating += 50
            elif y == 'rock':
                print('Well done. Computer chose ' + rules['paper']['win'] + ' and failed')
                x = input()
                rating += 100
            elif y == 'scissors':
                print('Sorry, but computer chose ' + rules['paper']['lose'])
                x = input()
        if x == 'scissors':
            if y == 'scissors':
                print('There is a draw (' + rules['scissors']['draw'] +')')
                x = input()
                rating += 50
            elif y == 'paper':
                print('Well done. Computer chose ' + rules['scissors']['win'] + ' and failed')
                x = input()
                rating += 100
            elif y == 'rock':
                print('Sorry, but computer chose ' + rules['scissors']['lose'])
                x = input()

