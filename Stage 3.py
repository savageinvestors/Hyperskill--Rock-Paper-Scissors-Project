import random
rules = {'rock': {'win': 'scissors', 'lose': 'paper', 'draw': 'rock'}, 'paper': {'win': 'rock', 'lose': 'scissors', 'draw': 'paper'}, 'scissors': {'win': 'paper', 'lose': 'rock', 'draw': 'scissors'}}
option = ['rock', 'paper', 'scissors']
x = input()
while x != 'exit':
    for i in range(1000):
        y = random.choice(option)
        if x == 'exit':
            print('Bye!')
            exit()
        if x not in option and x != 'exit':
            print('Invalid input')
            x = input()
        if x == 'rock':
            if y == 'rock':
                print('There is a draw (' + rules['rock']['draw'] +')')
                x = input()
            elif y == 'scissors':
                print('Well done. Computer chose ' + rules['rock']['win'] + ' and failed')
                x = input()
            elif y == 'paper':
                print('Sorry, but computer chose ' + rules['rock']['lose'])
                x = input()
        if x == 'paper':
            if y == 'paper':
                print('There is a draw (' + rules['paper']['draw'] +')')
                x = input()
            elif y == 'rock':
                print('Well done. Computer chose ' + rules['paper']['win'] + ' and failed')
                x = input()
            elif y == 'scissors':
                print('Sorry, but computer chose ' + rules['paper']['lose'])
                x = input()
        if x == 'scissors':
            if y == 'scissors':
                print('There is a draw (' + rules['scissors']['draw'] +')')
                x = input()
            elif y == 'paper':
                print('Well done. Computer chose ' + rules['scissors']['win'] + ' and failed')
                x = input()
            elif y == 'rock':
                print('Sorry, but computer chose ' + rules['scissors']['lose'])
                x = input()
