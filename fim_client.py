import os

inputw = 'dum'
commands = ['tp','lol','lol','lol','lol','lol','lol','lol','lol','lol']
tpcoords = '0 0 0'
fileline = 'dum'


print(' 000000      0           00       0')
print(' 0                       0 0     00')
print(' 000000      0           0  0   0 0')
print(' 0           0           0   000  0')
print(' 0           0           0        0')
print(' 0           0           0        0')
print(' 0           0           0        0')
print(' 0           0           0        0')
print('                          client               ')
print('             ')           
os.system('pause')
while True:
    inputw = input('fim client >')
    if inputw in commands:
        if inputw =='tp':
            f = open('username.txt')
            fileline = f.read()
            f.close()
            tpcoords = input('Enter coordinates you want to teleport to >')
            os.system('python send_packet.py  '+ fileline + tpcoords + ' 1 1 1 2 true 3 player')
        if  inputw =='help':
            print('List of commands:')
            print('tp - teleport to any coordinates.')
    else:
        print('Unknown command.')
