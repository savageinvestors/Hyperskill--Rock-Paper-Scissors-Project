import random
user_name = input('Enter your Name: ')
print(f'Hello {user_name}')

option = input().split(',')
default_option = ['rock', 'paper', 'scissors']
if option == ['']:
    option = default_option
len_option = len(option)
scores = open('rating.txt')
score = 0
for line in scores:
    n, s = line.rstrip().split()
    if user_name == n:
        score = int(s)
len_opponent = (len_option - 1)//2
new_option = option[-len_opponent:]
new_option.extend(option)
win = {}
for i in range(len_option):
    win[new_option[i]] = new_option[(i+1):(i+1+len_opponent)]
print('Okay, let\'s start')

while True:
    user = input()
    if user in win.keys():
        computer = random.choice(list(win.keys()))
        if user == computer:
            print(f'There is a draw ({user})')
            score += 50
        elif computer in win[user]:
            print(f'Sorry, but computer chose {computer}')
        else:
            print(f'Well done. Computer chose {computer} and failed')
            score += 100
    elif user == '!exit':
        print('Bye!')
        break
    elif user == '!rating':
        print('Your rating:', score)
    else:
        print('Invalid input')
scores.close()
