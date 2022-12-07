
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

flags = {
    '--quiet': 'Suppress output',
    '--hex-charset': 'Assume charset is given in hex',
    '--hex-salt': 'Assume salt is given in hex',
    '--hex-wordlist': 'Assume words in wordlist are given in hex',
    '--force': 'Ignore warnings',
    '--deprecated-check-disable': 'Enable deprecated plugins',
    '--status': 'Enable automatic update of the status screen',
    '--status-json': 'Enable JSON format for status output',
    '--status-timer ':'Sets seconds between status screen updates to X',
    '--stdin-timeout-abort':'Abort if there is no input from stdin for X seconds',
    '--machine-readable ':'Display the status view in a machine-readable format ',
    '--keep-guessing':'Keep guessing the hash after it has been cracked ',
    '--self-test-disable':'Disable self-test functionality on startup ',
    '--loopback ':'Add new plains to induct directory ',
    '--markov-hcstat2 ':'Specify hcstat2 file to use',
    '--markov-disable ':'Disables markov-chains, emulates classic brute-force ',
    '--markov-classic ':'Enables classic markov-chains, no per-position ',
    '--runtime':'Abort session after X seconds of runtime',
    '--session':'Define specific session name',
    '--restore':'Restore session from --session',
    '--restore-disable':'Do not write restore file ',
    '--restore-file-path':'Specific path to restore file ',
    '--outfile':'Define outfile for recovered hash ',
    '--outfile-format ':'Outfile format to use, separated with commas',
    '--outfile-autohex-disable':'Disable the use of $HEX[] in output plains',
    '--outfile-check-timer':'Sets seconds between outfile checks to X',
    '--wordlist-autohex-disabl':'Disable the conversion of $HEX[] from the wordlist',
    '--separator':'Separator char for hashlists and outfile',
    '--stdout ':'Do not crack a hash, instead print candidates only',
    '--show ':'Compare hashlist with potfile; show cracked hashes',
    '--left ':'Compare hashlist with potfile; show uncracked hashes',
    '--username ':'Enable ignoring of usernames in hashfile',
    '--remove ':'Enable removal of hashes once they are cracked',
    '--remove-timer ':'Update input hash file each X seconds ',
    '--potfile-disable':'Do not write potfile',
    '--potfile-path ':'Specific path to potfile',
    '--encoding-from':'Force internal wordlist encoding from X ',
    '--encoding-to':'Force internal wordlist encoding to X ',
    '--debug-mode ':'Defines the debug mode (hybrid only by using rules) ',
    '--debug-file ':'Output file for debugging rules ',
    '--induction-dir':'Specify the induction directory to use for loopback ',
    '--outfile-check-dir':'Specify the outfile directory to monitor for plains ',
    '--logfile-disable':'Disable the logfile ',
    '--hccapx-message-pair':'Load only message pairs from hccapx matching X',
    '--nonce-error-corrections':'The BF size range to replace APs nonce last bytes',
    '--keyboard-layout-mapping':'Keyboard layout mapping table for special hash-modes',
    '--truecrypt-keyfiles ':'Keyfiles to use, separated with commas',
    '--veracrypt-keyfiles ':'Keyfiles to use, separated with commas',
    '--veracrypt-pim-start':'VeraCrypt personal iterations multiplier start',
    '--veracrypt-pim-stop ':'VeraCrypt personal iterations multiplier stop ',
    '--benchmark':'Run benchmark of selected hash-modes',
    '--benchmark-all':'Run benchmark of all hash-modes (requires -b) ',
    '--speed-only ':'Return expected speed of the attack, then quit',
    '--progress-only':'Return ideal progress step size and time to process ',
    '--segment-size ':'Sets size in MB to cache from the wordfile to X ',
    '--bitmap-min ':'Sets minimum bits allowed for bitmaps to X',
    '--bitmap-max ':'Sets maximum bits allowed for bitmaps to X',
    '--cpu-affinity ':'Locks to CPU devices, separated with commas ',
    '--hook-threads ':'Sets number of threads for a hook (per compute unit)',
    '--hash-info':'Show information for each hash-mode ',
    '--example-hashes ':'Alias of --hash-info',
    '--backend-ignore-cuda':'Do not try to open CUDA interface on startup',
    '--backend-ignore-opencl':'Do not try to open OpenCL interface on startup',
    '--backend-info ':'Show info about detected backend API devices',
    '--backend-devices':'Backend devices to use, separated with commas ',
    '--opencl-device-types':'OpenCL device-types to use, separated with commas ',
    '--optimized-kernel-enable':'Enable optimized kernels (limits password length) ',
    '--multiply-accel-disable ':'Disable multiply kernel-accel with processor count',
    '--workload-profile ':'Enable a specific workload profile, see pool below',
    '--kernel-accel ':'Manual workload tuning, set outerloop step size to X',
    '--kernel-loops ':'Manual workload tuning, set innerloop step size to X',
    '--kernel-threads ':'Manual workload tuning, set thread count to X ',
    '--backend-vector-width ':'Manually override backend vector-width to X ',
    '--spin-damp':'Use CPU for device synchronization, in percent',
    '--hwmon-disable':'Disable temperature and fanspeed reads and triggers ',
    '--hwmon-temp-abort ':'Abort if temperature reaches X degrees Celsius',
    '--scrypt-tmto':'Manually override TMTO value for scrypt to X',
    '--skip ':'Skip X words from the start ',
    '--limit':'Limit X words from the start + skipped words',
    '--keyspace ':'Show keyspace base:mod values and quit',
    '--rule-left':'Single rule applied to each word from left wordlist ',
    '--rule-right ':'Single rule applied to each word from right wordlist',
    '--rules-file ':'Multiple rules applied to each word from wordlists',
    '--generate-rules ':'Generate X random rules ',
    '--generate-rules-func-min':'Force min X functions per rule',
    '--generate-rules-func-max':'Force max X functions per rule',
    '--generate-rules-func-sel':'Pool of rule operators valid for random rule engine ',
    '--generate-rules-seed':'Force RNG seed set to X ',
    '--custom-charset1':'User-defined charset ?1 ',
    '--custom-charset2':'User-defined charset ?2 ',
    '--custom-charset3':'User-defined charset ?3 ',
    '--custom-charset4':'User-defined charset ?4 ',
    '--identify ':'Shows all supported algorithms for input hashes ',
    '--increment':'Enable mask increment mode',
    '--increment-min':'Start mask incrementing at X',
    '--increment-max':'Stop mask incrementing at X ',
    '--slow-candidates':'Enable slower (but advanced) candidate generators ',
    '--brain-server ':'Enable brain server ',
    '--brain-server-timer ':'Update the brain server dump each X seconds (min:60)',
    '--brain-client ':'Enable brain client, activates -S ',
    '--brain-client-features':'Define brain client features, see below ',
    '--brain-host ':'Brain server host (IP or domain)',
    '--brain-port ':'Brain server port ',
    '--brain-password ':'Brain server authentication password',
    '--brain-session':'Overrides automatically calculated brain session',
    '--brain-session-whitelist':'Allow given sessions only, separated with commas',
}

