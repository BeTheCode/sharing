import os

usr = {'X':'','O':''}
lnsd = {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9'}

def print_board():
    os.system('clear')
    print(lnsd['1']+'|'+lnsd['2']+'|'+lnsd['3'])
    print('-----')
    print(lnsd['4']+'|'+lnsd['5']+'|'+lnsd['6'])
    print('-----')
    print(lnsd['7']+'|'+lnsd['8']+'|'+lnsd['9'])

def test_winner():
    if len(set(lnsd['1']+lnsd['2']+lnsd['3'])) == 1:
        print('Winner is %s') %(usr[lnsd['1']])
        return 1
    elif len(set(lnsd['4']+lnsd['5']+lnsd['6'])) == 1:
        print('Winner is %s') %(usr[lnsd['4']])
        return 1
    elif len(set(lnsd['7']+lnsd['8']+lnsd['9'])) == 1:
        print('Winner is %s') %(usr[lnsd['7']])
        return 1
    #Verticals
    elif len(set(lnsd['1']+lnsd['4']+lnsd['7'])) == 1:
        print('Winner is %s') %(usr[lnsd['1']])
        return 1
    elif len(set(lnsd['2']+lnsd['5']+lnsd['8'])) == 1:
        print('Winner is %s') %(usr[lnsd['2']])
        return 1
    elif len(set(lnsd['3']+lnsd['6']+lnsd['9'])) == 1:
        print('Winner is %s') %(usr[lnsd['3']])
        return 1
    #Diags
    elif len(set(lnsd['1']+lnsd['5']+lnsd['9'])) == 1:
        print('Winner is %s') %(usr[lnsd['1']])
        return 1
    elif len(set(lnsd['3']+lnsd['5']+lnsd['9'])) == 1:
        print('Winner is %s') %(usr[lnsd['3']])
        return 1
    #
    elif len(set(lnsd.values())) == 2:
        print('Game is cats')
        return 2
    else:
        return 0

def plays(player):
    x=0
    while x == 0:
        print('Player %s choose an unused square: ') %(usr[player])
        x = raw_input()
        if (lnsd[x] == "O") or (lnsd[x] == "X"):
            print('That square is alredy used \n\n')
            x=0
        else:
            lnsd[x] = player


game = 0
usr['X'] = str(raw_input('Player 1 name: '))
usr['O'] = str(raw_input('Player 2 name: '))
while True:
    print_board()
    plays('X')
    print_board()
    if test_winner() > 0:
        break
    plays('O')
    print_board()
    if test_winner() > 0:
        break