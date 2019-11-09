import serial
import PySimpleGUIQt as sg

red    = "ff0000"
green  = "00ff00"
blue   = "0000ff"
purple = "9e0083"
off    = "000000"

ser = serial.Serial('COM5', 9600)

def requestColor(color):
    rgbSelectValue = str(int(color, 16))
    print(rgbSelectValue)
    ser.write(("#" + rgbSelectValue).encode())    

# **************************************** Defines the GUI *****************************************************************************************************
#
layout = [

            [sg.Text('Select case illumination color...')],        
            [sg.Button('RED', button_color = ("white", "red"), key='red', size=(207,40)), sg.Button('GREEN', button_color = ("white", "green"), key='green', size=(207,40))],
            [sg.Button('BLUE', button_color = ("white", "blue"), key='blue', size=(207,40)), sg.Button('PURPLE', button_color = ("white", "purple"), key='purple', size=(207,40))],
            [sg.ColorChooserButton("", button_color=sg.TRANSPARENT_BUTTON, image_filename="rgb.png", image_subsample=2, size=(207, 40), border_width=0, key="rgbSelect"), sg.Button('LEDs off', size=(207,40), key='Off')],
            [sg.Button('Apply selected color', size=(207,40), key="apply"), sg.Button('Exit', size=(207,40), key='exit')],

          ]

window = sg.Window('RGB Color Selector - v:1.0 -', no_titlebar=False).Layout(layout)

# **************************************** Runs the GUI ********************************************************************************************************
#

while True:
    event, values = window.Read()
    
    if event is None or event == 'exit':
        requestColor(off)
        print("Exit!")
        break

    elif event  == 'red':
        requestColor(red)

    elif event  == 'green':
        requestColor(green)

    elif event  == 'blue':
        requestColor(blue)

    elif event  == 'purple':
        requestColor(purple)

    elif event  == 'Off':
        requestColor(off)

    elif event  == 'apply':
        requestColor((values["rgbSelect"])[1:])

window.Close()
ser.close()