import PySimpleGUI as sg
from random import randint
import string, random



qq="'"
QA="}{"
special=f'{qq} !"#$%&\'()*+,-./:;<=>?@[\\]^_`|{QA}~'

digits = "0123456789"
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

flag_map = {"?u":uppercase_letters, "?l":lowercase_letters, "?s":special}


helper = {'upper case letter':"UL", 'lowercase letter':'LL', 'digit':'DT'}
current_password = ""
minimum_length_flag = '--increment-min'
uppercase_letter = '[upper letter]'
lowercase_letter = '[lower letter]'
special_character= '[special char]'
digit_character =  '[ int  digit ]'
min_lengths = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
max_lengths = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
whitespace = ' \t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + whitespace

def make_sequence(string):

    sequences = []
    sequence = str(string).split(']')
    print(sequence)
    for x in sequence:
        if x.startswith("[u"):
            sequences.append(random.choice(ascii_uppercase))
        if x.startswith("[l"):
            sequences.append(random.choice(ascii_lowercase))
        if x.startswith("[s"):
            sequences.append(random.choice(punctuation))
        if x.startswith("[i"):
            sequences.append(random.choice(digits))

    x = "".join(sequences)
    return x

def make_examples(password, minimum_length):
    passwords_ = []
    for x in range(0,minimum_length+1):
        p = make_sequence(password)
        passwords_.append(p)
    return passwords_

def make_command(length,maximum, statusbar_sequence):
    sbs = statusbar_sequence.split("]")
    my_sequence = []
    for x in sbs:
        if x.startswith("[u"):
            my_sequence.append('?u')
        if x.startswith("[l"):
            my_sequence.append('?l')
        if x.startswith("[s"):
            my_sequence.append('?s')
        if x.startswith("[i"):
            my_sequence.append('?d')

        x = "".join(my_sequence)
    
    cmdstr = f"hashcat -a 3 -1 ?l?u?d?s  --increment-min={length} --increment-max={maximum} <hash> {x}"
    return cmdstr 


def main():
    global current_password
    sg.SetOptions(margins=(0,0), element_padding=(0,0))
    minimum_length = 0
    maximum_length = 8
    layout = [
    [sg.T("Hashcat Helpcat", font='ubuntu 24')],
    [sg.T("Set minimum length:"),sg.Combo(
        min_lengths, 
        default_value=minimum_length,
        enable_events=True,
        key='MINIMUM_LENGTH'), 
     sg.T("Set maximum length:") ,
     sg.Combo(
         max_lengths, 
         enable_events=True, 
         default_value=maximum_length, 
         key="MAXIMUM_LENGTH")
    ],
    [sg.B("Uppercase Letter", key="ULETTER"), sg.B('Lowercase Letter', key='LLETTER'), sg.B("Digit", key='DIGIT'), sg.Button("Special Character", key='SCHARACTER'),sg.B('Back Space', key="BACKSPACE"), sg.B("Clear", key="CLEAR")],
    [sg.StatusBar(current_password, text_color="green", background_color='black', font='ubuntu 8', key='CURRENT_PASSWORD_SET', size=(200, 1))],
    [sg.T("Examples:", font='boldUbuntu 12')],
    [sg.Multiline("", size=(100, 4), key='EXAMPLES',background_color='black',text_color='red', font='italicubuntu 10')],
    [sg.Input(f"", key="COMMAND", size=(200,1), text_color='green', background_color='black')],
    [sg.Exit()],
    ]
    w = sg.Window("hash helper", layout)
    first_time = True

    while True:
        event_key, values = w.read()
        w.refresh()
        if event_key==sg.WINDOW_CLOSED or event_key=='Exit':
            w.close()
            break
        if event_key=="ULETTER":
            minimum_length+=1
            if minimum_length>maximum_length:
                maximum_length = minimum_length
            w['MINIMUM_LENGTH'].update(minimum_length)
            w['MAXIMUM_LENGTH'].update(maximum_length)
            xcurrent_password = current_password + uppercase_letter
            current_password=xcurrent_password
            w["CURRENT_PASSWORD_SET"].update(str(current_password))
            w["COMMAND"].update(make_command(minimum_length,maximum_length,current_password))
            w.refresh()
            w["EXAMPLES"].update("")
            for x in make_examples(xcurrent_password, minimum_length):
                w["EXAMPLES"].print(x)
            w.refresh()
        if event_key=="LLETTER":
            minimum_length+=1
            if minimum_length>maximum_length:
                maximum_length = minimum_length
            w['MINIMUM_LENGTH'].update(minimum_length)
            w['MAXIMUM_LENGTH'].update(maximum_length)
            xcurrent_password = current_password + lowercase_letter
            current_password=xcurrent_password
            w["CURRENT_PASSWORD_SET"].update(str(current_password))
            w["COMMAND"].update(make_command(minimum_length,maximum_length,current_password))
            w.refresh()
            w["EXAMPLES"].update("")
            for x in make_examples(xcurrent_password, minimum_length):
                w["EXAMPLES"].print(x)
            w.refresh()
        if event_key=="SCHARACTER":
            minimum_length+=1
            if minimum_length>maximum_length:
                maximum_length = minimum_length
            w['MINIMUM_LENGTH'].update(minimum_length)
            w['MAXIMUM_LENGTH'].update(maximum_length)
            xcurrent_password = current_password + special_character
            current_password=xcurrent_password
            w["CURRENT_PASSWORD_SET"].update(str(xcurrent_password))
            w["COMMAND"].update(make_command(minimum_length,maximum_length,current_password))
            w.refresh()
            w["EXAMPLES"].update("")
            for x in make_examples(current_password, minimum_length):
                w["EXAMPLES"].print(x)
            w.refresh()
        if event_key=="DIGIT":
            minimum_length+=1
            if minimum_length>maximum_length:
                maximum_length = minimum_length
            w['MINIMUM_LENGTH'].update(minimum_length)
            w['MAXIMUM_LENGTH'].update(maximum_length)
            xcurrent_password = current_password + digit_character
            current_password=xcurrent_password
            w["CURRENT_PASSWORD_SET"].update(str(current_password))
            w["COMMAND"].update(make_command(minimum_length,maximum_length,current_password))
            w.refresh()
            w["EXAMPLES"].update("")
            for x in make_examples(current_password, minimum_length):
                w["EXAMPLES"].print(x)
            w.refresh()
        if event_key=="MINIMUM_LENGTH":
            w['MAXIMUM_LENGTH'].update(maximum_length)
            w['MINIMUM_LENGTH'].update(minimum_length)
            minimum_length = values["MINIMUM_LENGTH"]
            w['MINIMUM_LENGTH'].update(minimum_length)
            if round(minimum_length) > round(maximum_length):
                w['MAXIMUM_LENGTH'].update(minimum_length)
                maximum_length = minimum_length
                w.refresh()
            w['COMMAND'].update(make_command(minimum_length,maximum_length,current_password))
            w.refresh()
        if event_key=="MAXIMUM_LENGTH":
            maximum_length = values["MAXIMUM_LENGTH"]
            w['MAXIMUM_LENGTH'].update(maximum_length)
            w.refresh()
            if minimum_length > maximum_length:
                w['MAXIMUM_LENGTH'].update(minimum_length)
                maximum_length = minimum_length
                w.refresh()
            w['COMMAND'].update(make_command(minimum_length,maximum_length,current_password))
            w.refresh()
            
        if event_key=="CURRENT_PASSWORD_SET":
            pass
        if event_key=="DOCUMENT_TYPE":
            pass
        if event_key=="CLEAR":
            minimum_length=0
            maximum_length=8
            w['MINIMUM_LENGTH'].update(minimum_length)
            w['MAXIMUM_LENGTH'].update(maximum_length)
            w["EXAMPLES"].update("")
            w['CURRENT_PASSWORD_SET'].update("")
            w.refresh()
            current_password = ""
        if event_key == 'BACKSPACE':
            minimum_length = minimum_length-1
            w['MINIMUM_LENGTH'].update(minimum_length)
            w.refresh()
            if minimum_length < 0:
                minimum_length = 0
            for x in digit_character:
                current_password = current_password[:-1]
            w["CURRENT_PASSWORD_SET"].update(current_password)
            if round(minimum_length) > round(maximum_length):
                w['MAXIMUM_LENGTH'].update(minimum_length)
                w.refresh()
            maximum_length = maximum_length
            if digit_character != 1:
                for x in make_examples(current_password, minimum_length):
                    w["EXAMPLES"].print(x)
                w.refresh()
            else:
                w['EXAMPLES'] = ""
                w.refresh()

        w.refresh()

        if round(minimum_length) > round(maximum_length):
            w['MAXIMUM_LENGTH'].update(minimum_length)
            maximum_length = minimum_length
            w.refresh()
        w['MINIMUM_LENGTH'].update(minimum_length)
        
main()