import random
rules = {'rock': {'win': 'scissors', 'lose': 'paper', 'draw': 'rock'}, 'paper': {'win': 'rock', 'lose': 'scissors', 'draw': 'paper'}, 'scissors': {'win': 'paper', 'lose': 'rock', 'draw': 'scissors'}}
option = random.choice(['rock', 'paper', 'scissors'])
x = input()
while x == 'rock' or x == 'paper' or x == 'scissors':
    if x == 'rock':
        y = option
        if y == 'rock':
            print('There is a draw (' + rules['rock']['draw'] + ').')
            break
        elif y == 'scissors':
            print('Well done. Computer chose ' + rules['rock']['win'] + ' and failed.')
            break
        elif y == 'paper':
            print('Sorry, but computer chose ' + rules['rock']['lose'] + '.')
            break
    if x == 'paper':
        y = option
        if y == 'paper':
            print('There is a draw (' + rules['paper']['draw'] + ').')
            break
        elif y == 'rock':
            print('Well done. Computer chose ' + rules['paper']['win'] + ' and failed.')
            break
        elif y == 'scissors':
            print('Sorry, but computer chose ' + rules['paper']['lose'] + '.')
            break
    if x == 'scissors':
        y = option
        if y == 'scissors':
            print('There is a draw (' + rules['scissors']['draw'] + ').')
            break
        elif y == 'paper':
            print('Well done. Computer chose ' + rules['scissors']['win'] + ' and failed.')
            break
        elif y == 'rock':
            print('Sorry, but computer chose ' + rules['scissors']['lose'] + '.')
            break
else:
    exit()
