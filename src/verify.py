import PySimpleGUI as sg

from helper.calculations import power
from helper.strings import asciiToText

sg.theme('LightBlue 1')
layout = [
        [sg.Text('Signature: '), sg.Text(size=(1,1)), sg.Input(key='-signature-')],
        [sg.Text('Public Key (e): '), sg.Text(size=(1,1)), sg.Input(key='-e-')],
        [sg.Text('Public Key (n): '), sg.Text(size=(1,1)), sg.Input(key='-n-')],
        [sg.Text('Check result: '), sg.Text(size=(50,1), key='-checkresult-')],
        [sg.Button('Check signature'), sg.Button('Bye!')]]

window = sg.Window('Digital Signature', layout, [100,20])

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Bye!':
        break
        
    if event == 'Check signature':
        signature = values['-signature-']
        signatureSplit = signature.split(", ")
        e = int(values['-e-'])
        n = int(values['-n-'])

        # Decrypt
        asciiDecrypted = []
        for i in signatureSplit:
            asciiDecrypted.append(power(int(i), e, n))

        result = asciiToText(asciiDecrypted)
        window['-checkresult-'].update(result)

window.close()