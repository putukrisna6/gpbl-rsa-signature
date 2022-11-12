import PySimpleGUI as sg

NUMBER_OF_EVALUATION = 4

from algorithms.millerRabin import isPrime
from algorithms.eulerTotient import phi
from helper.calculations import power
from helper.calculations import relativelyPrime
from helper.calculations import modInverse
from helper.strings import textToAscii
from helper.strings import asciiToText

def getTwoPrimes(n):
    primeNumbers = []
    while(len(primeNumbers) < 2):
        if (isPrime(n, NUMBER_OF_EVALUATION)):
            primeNumbers.append(n)
        n += 1
    return primeNumbers[0], primeNumbers[1]

def getE(phiN):
    e = -1
    for i in range(2, phiN):
        if (relativelyPrime(i, phiN)):
            e = i
            break
    return e

def getD(e, phiN):
    return modInverse(e, phiN)

def getKeys(startPrime):
    p, q = getTwoPrimes(startPrime)
    n = p * q
    resultPhiN = phi(p, q)
    e = getE(resultPhiN)
    d = getD(e, resultPhiN)

    publicKey = {'e': e, 'n': n}
    privateKey = {'d': d, 'n': n}

    return publicKey, privateKey

def main():
    sg.theme('LightBlue 1')
    layout = [[sg.Text('Prime start: '), sg.Text(size=(1,1)), sg.Input(key='-primefrom-')],
            [sg.Text('Public Key: '), sg.Text(size=(50,1), key='-pubkey-')],
            [sg.Text('Private Key: '), sg.Text(size=(50,1), key='-prikey-')],
            [sg.Button('Generate Keys')],
            [sg.Text('Plain text: '), sg.Text(size=(1,1)), sg.Input(key='-plaintext-')],
            [sg.Text('Cipher text: '), sg.Text(size=(50,1), key='-chipertext-')],
            [sg.Button('Encrypt'), sg.Button('Close')]
            ]

    window = sg.Window('Digital Signature', layout, [50,20])

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Close':
            break
            
        if event == 'Generate Keys':
            try:
                startPrime = int(values['-primefrom-'])
                publicKey, privateKey = getKeys(startPrime)
            except:
                publicKey, privateKey = 'ERROR', 'ERROR'

            window['-pubkey-'].update(publicKey)
            window['-prikey-'].update(privateKey)

        if event == 'Encrypt':
            plainText = values['-plaintext-']

            # Encrypt
            asciiPlainText = textToAscii(plainText)
            asciiCipherText = []
            for i in asciiPlainText:
                asciiCipherText.append(power(i, privateKey['d'], privateKey['n']))

            f = open("ascii_cipher.txt", "w")
            f.write('Public Key: {' + str(publicKey['e']) + ', ' + str(publicKey['n']) + '}\n')
            f.write('ASCII Cipher: ')
            f.write(', '.join([str(elem) for i,elem in enumerate(asciiCipherText)]))
            f.close()

            try:
                cipherText = asciiToText(asciiCipherText) 
            except:
                cipherText = 'Could not convert to text, see ASCII output'
            window['-chipertext-'].update(cipherText)
    window.close()

    # Decrypt
    # asciiDecrypted = []
    # for i in asciiCipherText:
    #     asciiDecrypted.append(power(i, publicKey['e'], publicKey['n']))

    # print(asciiDecrypted)
    # print(asciiToText(asciiDecrypted))

if __name__ == "__main__":
    main()