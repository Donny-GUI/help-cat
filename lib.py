
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
digit_character =  '[int / digit ]'
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