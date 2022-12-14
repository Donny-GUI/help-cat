Documents = {
    'MD4':'900',
    'MD5':'0',
    'SHA1':'100',
    'SHA2-224':'1300',
    'SHA2-256':'1400',
    'SHA2-384':'10800',
    'SHA2-512':'1700',
    'SHA3-224':'17300',
    'SHA3-256':'17400',
    'SHA3-384':'17500',
    'SHA3-512':'17600',
    'RIPEMD-160':'6000',
    'BLAKE2b-512':'600',
    'GOST R 34.11-2012 (Streebog) 256-bit, big-endian':'11700',
    'GOST R 34.11-2012 (Streebog) 512-bit, big-endian':'11800',
    'GOST R 34.11-94':'6900',
    'GPG (AES-128/AES-256 (SHA-1($pass)))':'17010',
    'Half MD5':'5100',
    'Keccak-224':'17700',
    'Keccak-256':'17800',
    'Keccak-384':'17900',
    'Keccak-512':'18000',
    'Whirlpool':'6100',
    'SipHash':'10100',
    'md5(utf16le($pass))':'70',
    'sha1(utf16le($pass))':'170',
    'sha256(utf16le($pass))':'1470',
    'sha384(utf16le($pass))':'10870',
    'sha512(utf16le($pass))':'1770',
    'md5($pass.$salt)':'10',
    'md5($salt.$pass)':'20',
    'md5($salt.$pass.$salt)':'3800',
    'md5($salt.md5($pass))':'3710',
    'md5($salt.md5($pass.$salt))':'4110',
    'md5($salt.md5($salt.$pass))':'4010',
    'md5($salt.sha1($salt.$pass))':'21300',
    'md5($salt.utf16le($pass))':'40',
    'md5(md5($pass))':'2600',
    'md5(md5($pass).md5($salt))':'3910',
    'md5(md5(md5($pass)))':'3500',
    'md5(sha1($pass))':'4400',
    'md5(sha1($pass).md5($pass).sha1($pass))':'20900',
    'md5(sha1($salt).md5($pass))':'21200',
    'md5(strtoupper(md5($pass)))':'4300',
    'md5(utf16le($pass).$salt)':'30',
    'sha1($pass.$salt)':'110',
    'sha1($salt.$pass)':'120',
    'sha1($salt.$pass.$salt)':'4900',
    'sha1($salt.sha1($pass))':'4520',
    'sha1($salt.sha1($pass.$salt))':'24300',
    'sha1($salt.utf16le($pass))':'140',
    'sha1($salt1.$pass.$salt2)':'19300',
    'sha1(CX)':'14400',
    'sha1(md5($pass))':'4700',
    'sha1(md5($pass).$salt)':'4710',
    'sha1(md5($pass.$salt))':'21100',
    'sha1(md5(md5($pass)))':'18500',
    'sha1(sha1($pass))':'4500',
    'sha1(sha1($pass).$salt)':'4510',
    'sha1(sha1($salt.$pass.$salt))':'5000',
    'sha1(utf16le($pass).$salt)':'130',
    'sha256($pass.$salt)':'1410',
    'sha256($salt.$pass)':'1420',
    'sha256($salt.$pass.$salt)':'22300',
    'sha256($salt.sha256($pass))':'20720',
    'sha256($salt.utf16le($pass))':'1440',
    'sha256(md5($pass))':'20800',
    'sha256(sha256($pass).$salt)':'20710',
    'sha256(sha256_bin($pass))':'21400',
    'sha256(utf16le($pass).$salt)':'1430',
    'sha384($pass.$salt)':'10810',
    'sha384($salt.$pass)':'10820',
    'sha384($salt.utf16le($pass))':'10840',
    'sha384(utf16le($pass).$salt)':'10830',
    'sha512($pass.$salt)':'1710',
    'sha512($salt.$pass)':'1720',
    'sha512($salt.utf16le($pass))':'1740',
    'sha512(utf16le($pass).$salt)':'1730',
    'HMAC-MD5 (key = $pass)':'50',
    'HMAC-MD5 (key = $salt)':'60',
    'HMAC-SHA1 (key = $pass)':'150',
    'HMAC-SHA1 (key = $salt)':'160',
    'HMAC-SHA256 (key = $pass)':'1450',
    'HMAC-SHA256 (key = $salt)':'1460',
    'HMAC-SHA512 (key = $pass)':'1750',
    'HMAC-SHA512 (key = $salt)':'1760',
    'HMAC-Streebog-256 (key = $pass), big-endian':'11750',
    'HMAC-Streebog-256 (key = $salt), big-endian':'11760',
    'HMAC-Streebog-512 (key = $pass), big-endian':'11850',
    'HMAC-Streebog-512 (key = $salt), big-endian':'11860',
    'CRC32':'11500',
    'CRC32C':'27900',
    'CRC64Jones':'28000',
    'Java Object hashCode()':'18700',
    'MurmurHash':'25700',
    'MurmurHash3':'27800',
    '3DES (PT = $salt, key = $pass)':'14100',
    'DES (PT = $salt, key = $pass)':'14000',
    'AES-128-ECB NOKDF (PT = $salt, key = $pass)':'26401',
    'AES-192-ECB NOKDF (PT = $salt, key = $pass)':'26402',
    'AES-256-ECB NOKDF (PT = $salt, key = $pass)':'26403',
    'ChaCha20':'15400',
    'Linux Kernel Crypto API (2.4)':'14500',
    'Skip32 (PT = $salt, key = $pass)':'14900',
    'PBKDF2-HMAC-MD5':'11900',
    'PBKDF2-HMAC-SHA1':'12000',
    'PBKDF2-HMAC-SHA256':'10900',
    'PBKDF2-HMAC-SHA512':'12100',
    'scrypt':'8900',
    'phpass':'400',
    'TACACS+':'16100',
    'SIP digest authentication (MD5)':'11400',
    'IKE-PSK MD5':'5300',
    'IKE-PSK SHA1':'5400',
    'SNMPv3 HMAC-MD5-96':'25100',
    'SNMPv3 HMAC-MD5-96/HMAC-SHA1-96':'25000',
    'SNMPv3 HMAC-SHA1-96':'25200',
    'SNMPv3 HMAC-SHA224-128':'26700',
    'SNMPv3 HMAC-SHA256-192':'26800',
    'SNMPv3 HMAC-SHA384-256':'26900',
    'SNMPv3 HMAC-SHA512-384':'27300',
    'WPA-EAPOL-PBKDF2':'2500',
    'WPA-EAPOL-PMK':'2501',
    'WPA-PBKDF2-PMKID+EAPOL':'22000',
    'WPA-PMK-PMKID+EAPOL':'22001',
    'WPA-PMKID-PBKDF2':'16800',
    'WPA-PMKID-PMK':'16801',
    'IPMI2 RAKP HMAC-SHA1':'7300',
    'CRAM-MD5':'10200',
    'JWT (JSON Web Token)':'16500',
    'Kerberos 5, etype 17, TGS-REP':'19600',
    'Kerberos 5, etype 17, Pre-Auth':'19800',
    'Kerberos 5, etype 18, TGS-REP':'19700',
    'Kerberos 5, etype 18, Pre-Auth':'19900',
    'Kerberos 5, etype 23, AS-REQ Pre-Auth':'7500',
    'Kerberos 5, etype 23, TGS-REP':'13100',
    'Kerberos 5, etype 23, AS-REP':'18200',
    'NetNTLMv1 / NetNTLMv1+ESS':'5500',
    'NetNTLMv1 / NetNTLMv1+ESS (NT)':'27000',
    'NetNTLMv2':'5600',
    'NetNTLMv2 (NT)':'27100',
    'iSCSI CHAP authentication, MD5(CHAP)':'4800',
    'RACF':'8500',
    'AIX smd5':'6300',
    'AIX ssha1':'6700',
    'AIX ssha256':'6400',
    'AIX ssha512':'6500',
    'LM':'3000',
    'QNX /etc/shadow (MD5)':'19000',
    'QNX /etc/shadow (SHA256)':'19100',
    'QNX /etc/shadow (SHA512)':'19200',
    'DPAPI masterkey file v1':'15300',
    'DPAPI masterkey file v2':'15900',
    'GRUB 2':'7200',
    'MS-AzureSync PBKDF2-HMAC-SHA256':'12800',
    'BSDi Crypt, Extended DES':'12400',
    'NTLM':'1000',
    'Radmin2':'9900',
    'Samsung Android Password/PIN':'5800',
    'Windows Hello PIN/Password':'28100',
    'Windows Phone 8+ PIN/password':'13800',
    'Cisco-ASA MD5':'2410',
    'Cisco-IOS $8$ (PBKDF2-SHA256)':'9200',
    'Cisco-IOS $9$ (scrypt)':'9300',
    'Cisco-IOS type 4 (SHA256)':'5700',
    'Cisco-PIX MD5':'2400',
    'Citrix NetScaler (SHA1)':'8100',
    'Citrix NetScaler (SHA512)':'22200',
    'Domain Cached Credentials (DCC), MS Cache':'1100',
    'Domain Cached Credentials 2 (DCC2), MS Cache 2':'2100',
    'FortiGate (FortiOS)':'7000',
    'FortiGate256 (FortiOS256)':'26300',
    'ArubaOS':'125',
    'Juniper IVE':'501',
    'Juniper NetScreen/SSG (ScreenOS)':'22',
    'Juniper/NetBSD sha1crypt':'15100',
    'iPhone passcode (UID key + System Keybag)':'26500',
    'macOS v10.4, macOS v10.5, macOS v10.6':'122',
    'macOS v10.7':'1722',
    'macOS v10.8+ (PBKDF2-SHA512)':'7100',
    'bcrypt $2*$, Blowfish (Unix)':'3200',
    'md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5)':'500',
    'descrypt, DES (Unix), Traditional DES':'1500',
    'sha256crypt $5$, SHA256 (Unix)':'7400',
    'sha512crypt $6$, SHA512 (Unix)':'1800',
    'SQLCipher':'24600',
    'MSSQL (2000)':'131',
    'MSSQL (2005)':'132',
    'MSSQL (2012, 2014)':'1731',
    'MongoDB ServerKey SCRAM-SHA-1':'24100',
    'MongoDB ServerKey SCRAM-SHA-256':'24200',
    'PostgreSQL':'12',
    'PostgreSQL CRAM (MD5)':'11100',
    'Oracle H: Type (Oracle 7+)':'3100',
    'Oracle S: Type (Oracle 11+)':'112',
    'Oracle T: Type (Oracle 12+)':'12300',
    'MySQL $A$ (sha256crypt)':'7401',
    'MySQL CRAM (SHA1)':'11200',
    'MySQL323':'200',
    'MySQL4.1/MySQL5':'300',
    'Sybase ASE':'8000',
    'DNSSEC (NSEC3)':'8300',
    'KNX IP Secure - Device Authentication Code':'25900',
    'CRAM-MD5 Dovecot':'16400',
    'SSHA-256(Base64), LDAP SSHA256':'1411',
    'SSHA-512(Base64), LDAP SSHA512':'1711',
    'Dahua Authentication MD5':'24900',
    'RedHat 389-DS LDAP (PBKDF2-HMAC-SHA256)':'10901',
    'FileZilla Server >= 0.9.55':'15000',
    'ColdFusion 10+':'12600',
    'Apache $apr1$ MD5, md5apr1, MD5 (APR)':'1600',
    'Episerver 6.x < .NET 4':'141',
    'Episerver 6.x >= .NET 4':'1441',
    'hMailServer':'1421',
    'nsldap, SHA-1(Base64), Netscape LDAP SHA':'101',
    'nsldaps, SSHA-1(Base64), Netscape LDAP SSHA':'111',
    'SAP CODVN B (BCODE)':'7700',
    'SAP CODVN B (BCODE) from RFC_READ_TABLE':'7701',
    'SAP CODVN F/G (PASSCODE)':'7800',
    'SAP CODVN F/G (PASSCODE) from RFC_READ_TABLE':'7801',
    'SAP CODVN H (PWDSALTEDHASH) iSSHA-1':'10300',
    'PeopleSoft':'133',
    'PeopleSoft PS_TOKEN':'13500',
    'SolarWinds Orion':'21500',
    'SolarWinds Orion v2':'21501',
    'SolarWinds Serv-U':'24',
    'Lotus Notes/Domino 5':'8600',
    'Lotus Notes/Domino 6':'8700',
    'Lotus Notes/Domino 8':'9100',
    'OpenEdge Progress Encode':'26200',
    'Oracle Transportation Management (SHA256)':'20600',
    'Huawei sha1(md5($pass).$salt)':'4711',
    'AuthMe sha256':'20711',
    'AES Crypt (SHA256)':'22400',
    'VMware VMX (PBKDF2-HMAC-SHA1 + AES-256-CBC)':'27400',
    'LUKS':'14600',
    'VeraCrypt RIPEMD160 + XTS 512 bit':'13711',
    'VeraCrypt RIPEMD160 + XTS 1024 bit':'13712',
    'VeraCrypt RIPEMD160 + XTS 1536 bit':'13713',
    'VeraCrypt RIPEMD160 + XTS 512 bit + boot-mode':'13741',
    'VeraCrypt RIPEMD160 + XTS 1024 bit + boot-mode':'13742',
    'VeraCrypt RIPEMD160 + XTS 1536 bit + boot-mode':'13743',
    'VeraCrypt SHA256 + XTS 512 bit':'13751',
    'VeraCrypt SHA256 + XTS 1024 bit':'13752',
    'VeraCrypt SHA256 + XTS 1536 bit':'13753',
    'VeraCrypt SHA256 + XTS 512 bit + boot-mode':'13761',
    'VeraCrypt SHA256 + XTS 1024 bit + boot-mode':'13762',
    'VeraCrypt SHA256 + XTS 1536 bit + boot-mode':'13763',
    'VeraCrypt SHA512 + XTS 512 bit':'13721',
    'VeraCrypt SHA512 + XTS 1024 bit':'13722',
    'VeraCrypt SHA512 + XTS 1536 bit':'13723',
    'VeraCrypt Streebog-512 + XTS 512 bit':'13771',
    'VeraCrypt Streebog-512 + XTS 1024 bit':'13772',
    'VeraCrypt Streebog-512 + XTS 1536 bit':'13773',
    'VeraCrypt Streebog-512 + XTS 512 bit + boot-mode':'13781',
    'VeraCrypt Streebog-512 + XTS 1024 bit + boot-mode':'13782',
    'VeraCrypt Streebog-512 + XTS 1536 bit + boot-mode':'13783',
    'VeraCrypt Whirlpool + XTS 512 bit':'13731',
    'VeraCrypt Whirlpool + XTS 1024 bit':'13732',
    'VeraCrypt Whirlpool + XTS 1536 bit':'13733',
    'BestCrypt v3 Volume Encryption':'23900',
    'FileVault 2':'16700',
    'VirtualBox (PBKDF2-HMAC-SHA256 & AES-128-XTS)':'27500',
    'VirtualBox (PBKDF2-HMAC-SHA256 & AES-256-XTS)':'27600',
    'DiskCryptor SHA512 + XTS 512 bit':'20011',
    'DiskCryptor SHA512 + XTS 1024 bit':'20012',
    'DiskCryptor SHA512 + XTS 1536 bit':'20013',
    'BitLocker':'22100',
    'Android FDE (Samsung DEK)':'12900',
    'Android FDE <= 4.3':'8800',
    'Apple File System (APFS)':'18300',
    'TrueCrypt RIPEMD160 + XTS 512 bit':'6211',
    'TrueCrypt RIPEMD160 + XTS 1024 bit':'6212',
    'TrueCrypt RIPEMD160 + XTS 1536 bit':'6213',
    'TrueCrypt RIPEMD160 + XTS 512 bit + boot-mode':'6241',
    'TrueCrypt RIPEMD160 + XTS 1024 bit + boot-mode':'6242',
    'TrueCrypt RIPEMD160 + XTS 1536 bit + boot-mode':'6243',
    'TrueCrypt SHA512 + XTS 512 bit':'6221',
    'TrueCrypt SHA512 + XTS 1024 bit':'6222',
    'TrueCrypt SHA512 + XTS 1536 bit':'6223',
    'TrueCrypt Whirlpool + XTS 512 bit':'6231',
    'TrueCrypt Whirlpool + XTS 1024 bit':'6232',
    'TrueCrypt Whirlpool + XTS 1536 bit':'6233',
    'eCryptfs':'12200',
    'PDF 1.1 - 1.3 (Acrobat 2 - 4':'10400',
    'PDF 1.1 - 1.3 (Acrobat 2 - 4), collider #1':'10410',
    'PDF 1.1 - 1.3 (Acrobat 2 - 4), collider #2':'10420',
    'PDF 1.4 - 1.6 (Acrobat 5 - 8':'10500',
    'PDF 1.4 - 1.6 (Acrobat 5 - 8) - user and owner pass':'25400',
    'PDF 1.7 Level 3 (Acrobat 9':'10600',
    'PDF 1.7 Level 8 (Acrobat 10 - 11':'10700',
    'MS Office 2007':'9400',
    'MS Office 2010':'9500',
    'MS Office 2013':'9600',
    'MS Office 2016 - SheetProtection':'25300',
    'MS Office <= 2003 $0/$1, MD5 + RC4':'9700',
    'MS Office <= 2003 $0/$1, MD5 + RC4, collider #1':'9710',
    'MS Office <= 2003 $0/$1, MD5 + RC4, collider #2':'9720',
    'MS Office <= 2003 $3, SHA1 + RC4, collider #1':'9810',
    'MS Office <= 2003 $3, SHA1 + RC4, collider #2':'9820',
    'MS Office <= 2003 $3/$4, SHA1 + RC4':'9800',
    'Open Document Format (ODF) 1.2 (SHA-256, AES':'18400',
    'Open Document Format (ODF) 1.1 (SHA-1, Blowfish':'18600',
    'Apple Secure Notes':'16200',
    'Apple iWork':'23300',
    '1Password, agilekeychain':'6600',
    '1Password, cloudkeychain':'8200',
    'Password Safe v2':'9000',
    'Password Safe v3':'5200',
    'LastPass + LastPass sniffed':'6800',
    'KeePass 1 (AES/Twofish) and KeePass 2 (AES)':'13400',
    'Bitwarden':'23400',
    'Ansible Vault':'16900',
    'Mozilla key3.db':'26000',
    'Mozilla key4.db':'26100',
    'Apple Keychain':'23100',
    '7-Zi':'11600',
    'RAR3-hp':'12500',
    'RAR3-p (Compressed':'23800',
    'RAR3-p (Uncompressed':'23700',
    'RAR5':'13000',
    'PKZIP (Compressed Multi-File':'17220',
    'PKZIP (Compressed':'17200',
    'PKZIP (Mixed Multi-File':'17225',
    'PKZIP (Mixed Multi-File Checksum-Only':'17230',
    'PKZIP (Uncompressed':'17210',
    'PKZIP Master Key':'20500',
    'PKZIP Master Key (6 byte optimization':'20510',
    'SecureZIP AES-128':'23001',
    'SecureZIP AES-192':'23002',
    'SecureZIP AES-256':'23003',
    'WinZip':'13600',
    'Android Backup':'18900',
    'Stuffit5':'24700',
    'AxCrypt 1':'13200',
    'AxCrypt 1 in-memory SHA1':'13300',
    'AxCrypt 2 AES-128':'23500',
    'AxCrypt 2 AES-256':'23600',
    'iTunes backup < 10.0':'14700',
    'iTunes backup >= 10.0':'14800',
    'WBB3 (Woltlab Burning Board)':'8400',
    'PHPS':'2612',
    'SMF (Simple Machines Forum) > v1.1':'121',
    'MediaWiki B type':'3711',
    'Redmine':'4521',
    'Umbraco HMAC-SHA1':'24800',
    'Joomla < 2.5.18':'11',
    'OpenCart':'13900',
    'PrestaShop':'11000',
    'Tripcode':'16000',
    'Drupal7':'7900',
    'PunBB':'4522',
    'MyBB 1.2+, IPB2+ (Invision Power Board)':'2811',
    'vBulletin < v3.8.5':'2611',
    'vBulletin >= v3.8.5':'2711',
    'bcrypt(md5($pass)) / bcryptmd5':'25600',
    'bcrypt(sha1($pass)) / bcryptsha1':'25800',
    'osCommerce, xt:Commerce':'21',
    'TOTP (HMAC-SHA1)':'18100',
    'STDOUT':'2000',
    'Plaintext':'99999',
    'Web2py pbkdf2-sha512':'21600',
    'Django (PBKDF2-SHA256':'10000',
    'Django (SHA-1':'124',
    'Atlassian (PBKDF2-HMAC-SHA1':'12001',
    'Ruby on Rails Restful-Authentication':'19500',
    'Ruby on Rails Restful Auth (one round, no sitekey':'27200',
    'Python passlib pbkdf2-sha512':'20200',
    'Python passlib pbkdf2-sha256':'20300',
    'Python passlib pbkdf2-sha1':'20400',
    'PKCS#8 Private Keys (PBKDF2-HMAC-SHA1 + 3DES/AES)':'24410',
    'PKCS#8 Private Keys (PBKDF2-HMAC-SHA256 + 3DES/AES':'24420',
    'JKS Java Key Store Private Keys (SHA1)':'15500',
    'RSA/DSA/EC/OpenSSH Private Keys ($0$)':'22911',
    'RSA/DSA/EC/OpenSSH Private Keys ($6$)':'22921',
    'RSA/DSA/EC/OpenSSH Private Keys ($1, $3$)':'22931',
    'RSA/DSA/EC/OpenSSH Private Keys ($4$)':'22941',
    'RSA/DSA/EC/OpenSSH Private Keys ($5$)':'22951',
    'XMPP SCRAM PBKDF2-SHA1':'23200',
    'Telegram Desktop < v2.1.14 (PBKDF2-HMAC-SHA1)':'22600',
    'Telegram Desktop >= v2.1.14 (PBKDF2-HMAC-SHA512)':'24500',
    'Telegram Mobile App Passcode (SHA256)':'22301',
    'Skype':'23',
    'MetaMask Wallet':'26600',
    'BitShares v0.x - sha512(sha512_bin(pass))':'21000',
    'Bitcoin/Litecoin wallet.dat':'11300',
    'Electrum Wallet (Salt-Type 1-3)':'16600',
    'Electrum Wallet (Salt-Type 4)':'21700',
    'Electrum Wallet (Salt-Type 5)':'21800',
    'Blockchain, My Wallet':'12700',
    'Blockchain, My Wallet, V2':'15200',
    'Blockchain, My Wallet, Second Password (SHA256)':'18800',
    'Stargazer Stellar Wallet XLM':'25500',
    'Ethereum Pre-Sale Wallet, PBKDF2-HMAC-SHA256':'16300',
    'Ethereum Wallet, PBKDF2-HMAC-SHA256':'15600',
    'Ethereum Wallet, SCRYPT':'15700',
    'MultiBit Classic .key (MD5)':'22500',
    'MultiBit Classic .wallet (scrypt)':'27700',
    'MultiBit HD (scrypt)':'22700'
}