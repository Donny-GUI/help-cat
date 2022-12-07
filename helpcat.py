import PySimpleGUI as sg
import random
from string import ( 
    ascii_lowercase, 
    ascii_uppercase, 
    digits, 
    punctuation)
from lib import (
    max_lengths, 
    min_lengths, 
    uppercase_letter, 
    lowercase_letter, 
    digit_character, 
    special_character,
    flags,
    positionals,
    attack_types)
from documents import Documents

document_names = list(Documents.keys())
current_password = ""
flag_flags = list(flags.keys())
flag_desc = list(flags.values())
attacks = list(attack_types.values())
attacks_number = list(attack_types.keys())
added_flags = []
attack_type = []


def get_attack_from_desc(attack_description:str):
    global attack_type
    attack_type = []
    for index, a in enumerate(attacks):
        if a == attack_description:
            return attacks_number[index]
    return None
            
    
def search_box(search_input:str):
    search_box = [x for x in document_names if x.startswith(search_input.lower()) or x.startswith(search_input.upper())]
    try:
        return search_box[0]
    except:
        return None

def get_flag_From_desc(desc:str):
    for index, flag in enumerate(flag_desc):
        if desc == flag:
            return flag_flags[index]
    return None

def search_flags(search_input:str):
    flags_search = [x for x in flag_desc if x.startswith(search_input.lower()) or x.startswith(search_input.upper())]
    try:
        return flags_search[0]
    except:
        return None

def make_sequence(string):

    sequences = []
    sequence = str(string).split(']')
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

def make_command(length,maximum, statusbar_sequence, document_type):
    global attack_type
    flagsx = " ".join([x for x in added_flags if x != None])
    if attack_type == [] or attack_type[0] == None:
        attack = ""
    else:
        attack = f"-a {attack_type[0]}"
    sbs = statusbar_sequence.split("]")
    my_sequence = []
    m_tag = '-m'
    if document_type == '':
        m_tag = ''
        docu = ''
    else:
        docu=Documents[document_type]
        
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
    cmdstr = f"hashcat {attack} -1 ?l?u?d?s -i {flagsx} --increment-min={length} --increment-max={maximum} {m_tag} {docu} <hash> {x}"
    return cmdstr 


def main():
    global attack_type
    global current_password
    global added_flags
    sg.SetOptions(margins=(0,0), element_padding=(0,0))
    minimum_length = 0
    maximum_length = 8
    #
    ##
    ###  LAYOUT
    ##
    #
    layout = [
    [sg.T("Hashcat Helpcat", font='ubuntu 24', pad=(5,5))], # title
    [sg.HorizontalSeparator()],
    [sg.T("Search for hash type:"), sg.Input("", key='SEARCH', enable_events=True, pad=(5,5)), 
     sg.Combo(values=document_names, key='DOC', size=(50,30), enable_events=True)],           # document type
    [sg.T("Attack Type"), sg.Combo(attacks, enable_events=True, key='ATTACK')],
    [sg.T("Set minimum length:"),
     sg.Combo(                                   # minimum combo
        min_lengths, 
        default_value=minimum_length,
        enable_events=True,
        key='MINIMUM_LENGTH'),
     sg.T("Set maximum length:"),
     sg.Combo(                                   # maximum combo
        max_lengths, 
        enable_events=True, 
        default_value=maximum_length, 
        key="MAXIMUM_LENGTH")
    ],
    [sg.B("Uppercase Letter",                    # uppercase button 
          key="ULETTER"), 
     sg.B('Lowercase Letter',                    # lowercase button
          key='LLETTER'), 
     sg.B("Digit", key='DIGIT'), 
     sg.Button("Special Character",              # special character button
               key='SCHARACTER'),
     sg.B('Back Space', key="BACKSPACE"),        # backspace button
     sg.B("Clear",                               # clear button
          key="CLEAR")],
    [sg.StatusBar(current_password,              # description status box 
                  text_color="green", 
                  background_color='black', 
                  font='ubuntu 8', 
                  key='CURRENT_PASSWORD_SET', 
                  size=(200, 1))],
    [sg.T("Examples:", font='boldUbuntu 12')],
    [sg.Multiline("", 
                  size=(100, 4), 
                  key='EXAMPLES',
                  background_color='black',
                  text_color='red', 
                  font='italicubuntu 10')],
    [sg.T("Search for flags:"), sg.Input("", key='FLAGS_SEARCH', enable_events=True, pad=(5,5))],
    [sg.Button("Add Flag"), 
     sg.Combo(values=flag_desc, key='FLAGS', size=(50,30), enable_events=True),
     sg.Input("", key='HIDDEN POSITIONAL', visible=False)], 
    [sg.Input(f"", 
              key="COMMAND", 
              size=(200,1), 
              text_color='green', 
              background_color='black')],       # command output
    [sg.Exit()],]
    w = sg.Window("hash helper", layout)
    
    #
    ##
    ###     event loop    ####################################
    ##
    #
    document_type = ""
    
    while True:
        event_key, values = w.read()
        w.refresh()
        document_type=values['DOC']
        
        if event_key == 'ATTACK':
            atk_desc = values['ATTACK']
            atk = get_attack_from_desc(atk_desc)
            attack_type.append(atk)
            w['COMMAND'].update(make_command(
                        length=minimum_length, 
                        maximum=maximum_length, 
                        statusbar_sequence=current_password,
                        document_type=document_type))
        
        if not w['FLAGS'] == "":
            description = values['FLAGS']
            flag = get_flag_From_desc(description)
            if flag in positionals:
                w['HIDDEN POSITIONAL'].update(visible=True)
            else:
                w['HIDDEN POSITIONAL'].update(visible=False)
                w['HIDDEN POSITIONAL'].update("")
        
        if event_key == 'Add Flag':
            description = values['FLAGS']
            flag = get_flag_From_desc(description)
            if not flag in added_flags:
                
                added_flags.append(flag)
                if not w['HIDDEN POSITIONAL'] == '':
                    added_flags.append(values['HIDDEN POSITIONAL'])
                w['COMMAND'].update(make_command(
                        length=minimum_length, 
                        maximum=maximum_length, 
                        statusbar_sequence=current_password,
                        document_type=document_type))
                w.refresh()
        if event_key == 'SEARCH':
            w['SEARCH'].update(values['SEARCH'])
            w.refresh()
            search_for = values['SEARCH']
            if not search_for == '' or not search_for == None:
                search = search_box(search_for)
                w['DOC'].update(search)
                w['COMMAND'].update(make_command(
                    length=minimum_length, 
                    maximum=maximum_length, 
                    statusbar_sequence=current_password,
                    document_type=document_type))
            w.refresh()
        #
        #   update document
        #
        if event_key == 'DOC':
            w['DOC'].update(values['DOC'])
            w.refresh()
            w['COMMAND'].update(make_command(
                length=minimum_length, 
                maximum=maximum_length, 
                statusbar_sequence=current_password,
                document_type=document_type))
        #
        #   FLAG search
        #
        if event_key == 'FLAGS_SEARCH':
            w['FLAGS_SEARCH'].update(values['FLAGS_SEARCH'])
            w.refresh()
            search_for_flag = values['FLAGS_SEARCH']
            if not search_for_flag == '' or not search_for_flag == None:
                searchf = search_flags(search_for_flag)
                w['FLAGS'].update(searchf)
                adding_to_flags = get_flag_From_desc(search_for_flag)
                added_flags.append(adding_to_flags)
                w['COMMAND'].update(make_command(
                    length=minimum_length, 
                    maximum=maximum_length, 
                    statusbar_sequence=current_password,
                    document_type=document_type))
            w.refresh()
        #
        #   update flags
        #
        if event_key == 'FLAGS':
            w['FLAGS'].update(values['FLAGS'])
            w.refresh()
            w['COMMAND'].update(make_command(
                length=minimum_length, 
                maximum=maximum_length, 
                statusbar_sequence=current_password,
                document_type=document_type))
        #
        #   window close or exit
        #
        if event_key==sg.WINDOW_CLOSED or event_key=='Exit':
            w.close()
            break
        #
        #   uppercase letter button event
        #
        if event_key=="ULETTER":
            minimum_length+=1
            if minimum_length>maximum_length:
                maximum_length = minimum_length
            w['MINIMUM_LENGTH'].update(minimum_length)
            w['MAXIMUM_LENGTH'].update(maximum_length)
            xcurrent_password = current_password + uppercase_letter
            current_password=xcurrent_password
            w["CURRENT_PASSWORD_SET"].update(str(current_password))
            w["COMMAND"].update(make_command(minimum_length,
                maximum_length,
                current_password,
                document_type=document_type))
            w.refresh()
            w["EXAMPLES"].update("")
            for x in make_examples(xcurrent_password, minimum_length):
                w["EXAMPLES"].print(x)
            w.refresh()
        #
        #   lowercase letter button event
        #
        if event_key=="LLETTER":
            minimum_length+=1
            if minimum_length>maximum_length:
                maximum_length = minimum_length
            w['MINIMUM_LENGTH'].update(minimum_length)
            w['MAXIMUM_LENGTH'].update(maximum_length)
            xcurrent_password = current_password + lowercase_letter
            current_password=xcurrent_password
            w["CURRENT_PASSWORD_SET"].update(str(current_password))
            w["COMMAND"].update(make_command(minimum_length,
                maximum_length,
                current_password,
                document_type=document_type)
                )
            w.refresh()
            w["EXAMPLES"].update("")
            for x in make_examples(xcurrent_password, minimum_length):
                w["EXAMPLES"].print(x)
            w.refresh()
        #
        #   special character button event
        #
        if event_key=="SCHARACTER":
            minimum_length+=1
            if minimum_length>maximum_length:
                maximum_length = minimum_length
            w['MINIMUM_LENGTH'].update(minimum_length)
            w['MAXIMUM_LENGTH'].update(maximum_length)
            xcurrent_password = current_password + special_character
            current_password=xcurrent_password
            w["CURRENT_PASSWORD_SET"].update(str(xcurrent_password))
            w["COMMAND"].update(make_command(minimum_length,
                maximum_length,
                current_password,
                document_type=document_type)
                )
            w.refresh()
            w["EXAMPLES"].update("")
            for x in make_examples(current_password, minimum_length):
                w["EXAMPLES"].print(x)
            w.refresh()
        #
        #   digit button event
        #
        if event_key=="DIGIT":
            minimum_length+=1
            if minimum_length>maximum_length:
                maximum_length = minimum_length
            w['MINIMUM_LENGTH'].update(minimum_length)
            w['MAXIMUM_LENGTH'].update(maximum_length)
            xcurrent_password = current_password + digit_character
            current_password=xcurrent_password
            w["CURRENT_PASSWORD_SET"].update(str(current_password))
            w["COMMAND"].update(make_command(minimum_length,
                maximum_length,
                current_password,
                document_type=document_type)
                )
            w.refresh()
            w["EXAMPLES"].update("")
            for x in make_examples(current_password, minimum_length):
                w["EXAMPLES"].print(x)
            w.refresh()
        #
        #   minimum combo box event
        #
        if event_key=="MINIMUM_LENGTH":
            w['MAXIMUM_LENGTH'].update(maximum_length)
            w['MINIMUM_LENGTH'].update(minimum_length)
            minimum_length = values["MINIMUM_LENGTH"]
            w['MINIMUM_LENGTH'].update(minimum_length)
            if round(minimum_length) > round(maximum_length):
                w['MAXIMUM_LENGTH'].update(minimum_length)
                maximum_length = minimum_length
                w.refresh()
            w['COMMAND'].update(make_command(minimum_length,
                maximum_length,
                current_password, document_type=document_type)
                )
            w.refresh()
        #
        #   maximum combo box event
        #
        if event_key=="MAXIMUM_LENGTH":
            maximum_length = values["MAXIMUM_LENGTH"]
            w['MAXIMUM_LENGTH'].update(maximum_length)
            w.refresh()
            if minimum_length > maximum_length:
                w['MAXIMUM_LENGTH'].update(minimum_length)
                maximum_length = minimum_length
                w.refresh()
            w['COMMAND'].update(make_command(minimum_length,
                maximum_length,
                current_password,
                document_type=document_type))
            w.refresh()
            
        if event_key=="CURRENT_PASSWORD_SET":
            pass
        if event_key=="DOCUMENT_TYPE":
            pass
        #
        #   clear button event
        #
        if event_key=="CLEAR":
            minimum_length=0
            maximum_length=8
            added_flags = []
            w['MINIMUM_LENGTH'].update(minimum_length)
            w['MAXIMUM_LENGTH'].update(maximum_length)
            w["EXAMPLES"].update("")
            w['CURRENT_PASSWORD_SET'].update("")
            w['COMMAND'].update(make_command(minimum_length,
                maximum_length,
                current_password,
                document_type=document_type))
            w.refresh()
            current_password = ""
        #
        #   backspace combo event
        #
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