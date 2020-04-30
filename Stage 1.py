print('Your turn -- Choose Rock, Paper, or Scissors (type "r", "p", or "s"): ', end = '')
x = input().lower()
while x == 'r' or x == 'p' or x == 's':
    if x == 'r':
        print('Sorry but computer chose paper\n')
        print('Your turn -- Choose Rock, Paper, or Scissors (type "r", "p", or "s"): ', end = '')
        x = input().lower()
    elif x == 'p':
        print('Sorry but computer chose scissors\n')
        print('Your turn -- Choose Rock, Paper, or Scissors (type "r", "p", or "s"): ', end = '')
        x = input().lower()
    elif x == 's':
        print('Sorry but computer chose rock\n')
        print('Your turn -- Choose Rock, Paper, or Scissors (type "r", "p", or "s"): ', end = '')
        x = input().lower()
else:
    print('YOU ARE A LOSER!!!')
    exit()
