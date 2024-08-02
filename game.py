import random

l = ['rock', 'paper', 'scissor']
# '''
# rock vs paper-> paper wins
# rock vs scissor-> rock wins
# paper vs scissor-> scissor wins
#
# '''

while True:
    Ccount = 0
    Ucount = 0
    uc = int(input('''
    Game Start....
    1.Yes
    2.No| Exit
    '''))
    if uc == 1:
        for a in range(1, 6):
            usrIn = int(input('''
            1 Rock
            2 Scissor
            3 Paper
            '''))
            if usrIn == 1:
                uchoice = 'rock'
            elif usrIn == 2:
                uchoice = 'scissor'
            elif usrIn == 3:
                uchoice = 'paper'
            Cchoice = random.choice(l)
            if Cchoice == uchoice:
                print('Computer value:-', Cchoice)
                print('User value:-', uchoice)
                print('Game Draw')
                Ucount = Ucount + 1
                Ccount = Ccount + 1
            elif ((uchoice == 'rock' and Cchoice == 'scissor')
                  or (uchoice == 'paper' and Cchoice == 'rock')
                  or (uchoice == 'scissor' and Cchoice == 'paper')):
                print('Computer value:-', Cchoice)
                print('User value:-', uchoice)
                print('you win')
                Ucount = Ucount + 1
            else:
                print('computer value:-', Cchoice)
                print('user value:-', uchoice)
                print('computer win')
                Ccount = Ccount + 1
        if Ucount == Ccount:
            print('Game Draw...')
            print('User Score', Ucount)
            print('Computer Score', Ccount)
        elif Ucount > Ccount:
            print('Barvo!!..You have won...')
            print('User Score', Ucount)
            print('Computer Score', Ccount)
        else:
            print('Computer has Won...')
            print('User Score', Ucount)
            print('Computer Score', Ccount)

        pass
    else:
        break
