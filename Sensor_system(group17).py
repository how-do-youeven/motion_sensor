from microbit import *
sleep(5000)#startup delay
b=Image('00990:'#image
'00990:'
'00990:'
'00000:'
'00990')
a=Image('00009:'
'00009:'
'00009:'
'00000:'
'00009')
c=Image('09900:'
'09900:'
'09900:'
'00000:'
'09900')
d=Image('99000:'
'99000:'
'99000:'
'00000:'
'99000')
e=Image('90000:'
'90000:'
'90000:'
'00000:'
'90000')
o=Image(
'00900:'
'09090:'
'90009:'
'09090:'
'00900')
n=Image(
'90009:'
'99009:'
'90909:'
'90099:'
'90009')
f=Image(
'99999:'
'90000:'
'99990:'
'90000:'
'90000')
space=Image(
'00000:'
'00000:'
'00000:'
'00000:'
'00000')

system_loop = True
while system_loop == True:
    if button_a.get_presses():
        system_on= True
        display.show([o,n],delay=1000)
        display.clear()
    if button_b.get_presses():
        system_on = False
        display.show([o,f,space,f],delay=1000)
        display.clear()
    while system_on is True:
        reading = pin0.read_digital()
        sleep(1000)
        if reading ==1:
            display.show([a, b, c, d, e], delay=100)
            sleep(10)
            display.clear()
        if button_b.get_presses():
            system_on = False