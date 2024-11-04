from telethon import TelegramClient,events,Button
import requests,os
from dotenv import load_dotenv
import time,json,paramiko,psutil,ipaddress
load_dotenv()
MESSWAIT=os.getenv('MESSWAIT')
MESSDONE=os.getenv('MESSDONE')
async def myserv(event):
	K='Sorry you not have server :( . Please contact @maapple to buy server';J='user_id';A=event;await A.edit(MESSWAIT);H=await A.get_sender();I=A.sender_id
	try:
		with open(f"./database/{I}.json",'r')as L:B=json.load(L)
		if J in B and B[J]==int(I):
			await A.edit('You have server!! Wait Checking Status');time.sleep(2);C=B['server_host'];D=13181;E=B['server_username'];F=B['server_password']
			try:G=paramiko.SSHClient();G.set_missing_host_key_policy(paramiko.AutoAddPolicy());G.connect(C,port=D,username=E,password=F);G.close();await A.edit(f"""**SERVER FROM {H.first_name}**

🟢**__STATUS: Online__**

💻HOST: {C}
🤖PORT: {D}
⛔USERNAME: {E}
⛔PASSWORD: {F}
""")
			except Exception as M:await A.edit(f"""**SERVER FROM {H.first_name}**

**__🔴STATUS: Offline__**

💻HOST: {C}
🤖PORT: {D}
⛔USERNAME: {E}
⛔PASSWORD: {F}
""")
		else:await A.edit(K)
	except FileNotFoundError:await A.edit(K)
