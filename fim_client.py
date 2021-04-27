import os

inputw = 'dum'
commands = ['tp','help','setcontainer','health','effect','lol','lol','lol','lol','lol']
tpcoords = '0 0 0'
fileline = 'dum'
click = 'False'

print(' 000000      0           00       0')
print(' 0                       0 0     00')
print(' 000000      0           0  0   0 0')
print(' 0           0           0   000  0')
print(' 0           0           0        0')
print(' 0           0           0        0')
print(' 0           0           0        0')
print(' 0           0           0        0')
print('                          client               ')
print('Enter "help" for help.          ')
print(' ')

while True:
    inputw = input('fim client >')
    if inputw in commands:
        if inputw =='tp':
            f = open('username.txt')
            fileline = f.read()
            f.close()
            tpcoords = input('Enter coordinates you want to teleport to >')
            os.system('python send_packet.py  '+ fileline + tpcoords + ' 1 1 1 2 true 3 player')
        if inputw == 'help':
            print('List of commands:')
            print('tp - teleport to any coordinates. NOTE: is only visible for other players. ')
            print('setcontainer - puts an item in entered contained count in the game.')
            print('health - set your helth. NOTE: cannot bypass server-side checks.')
            print('effect - set custom effect.')
        if inputw =='setcontainer':
            itemid = input('Enter item id you want to set >')
            winid = input('Enter window id >')
            value = input('Enter item value >')
            os.system('python send_packet.py 0x33 '+winid +' '+itemid+' '+value)
        if inputw =='health':
            health = input('Enter how much health you want >')
            os.system('python send_packet.py 0x2A ' + health + ' 10000')
        if inputw =='effect':
            effect = input('Enter effect id [you can get it from here: https://minecraft.fandom.com/wiki/Effect] >')
            duration = input('Enter effect duration >')
            amplifier = input('Enter effect amplifier >')
            f = open('username.txt')
            fileline = f.read()
            f.close()
            os.system('python send_packet.py '+ fileline + ' 1 ' + effect + ' True ' + duration)
            
        
                  
        
    else:
        print('Unknown command. Type "help" for help.')

        
      
