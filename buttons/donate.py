from telethon import TelegramClient,events,Button
import requests,os
from dotenv import load_dotenv
import time,json,paramiko,psutil,ipaddress
load_dotenv()
MESSWAIT=os.getenv('MESSWAIT')
MESSDONE=os.getenv('MESSDONE')
async def donet(event):
	A=event;await A.edit(MESSWAIT);B=await A.get_sender();D=A.sender_id
	try:await A.edit(f"""**HELO SIR {B.first_name}**

Thank you for treating me to a cup of coffee and cromboloni bread

Upi noobxmethod@axl 

LTC ltc1q8uxwmt0rta8rad5g9ncrkqkmp8nq2j3p04mqnz""")
	except Exception as C:await A.edit(f"An error occurred\n\n`{C}`")
	except FileNotFoundError:await A.edit('Sorry you not have server :( . Please contact @noob_je to buy server')
