from telethon import events,Button
import requests,os,time,json,paramiko,psutil,ipaddress
from dotenv import load_dotenv
load_dotenv()
MESSWAIT=os.getenv('MESSWAIT')
MESSDONE=os.getenv('MESSDONE')
def is_valid_ipv4_address(address):
	try:ipaddress.IPv4Address(address);return True
	except ipaddress.AddressValueError:return False
async def tesserver(event):
	C=event
	try:
		A=await C.reply(MESSWAIT);D=C.sender_id;B=C.raw_text.split()
		if len(B)==4:
			E=B[1];F=B[2];G=B[3]
			if is_valid_ipv4_address(E):
				H={'user_id':D,'server_host':E,'server_username':F,'server_password':G}
				with open(f"./database/{D}.json",'w')as I:json.dump(H,I)
				await A.edit('Successfully Save Your Server Information')
			else:await A.edit('The host server must be a valid ip4')
		else:await A.edit('Use format: /server <server_host> <server_username> <server_password>')
	except Exception as J:await A.edit(f"An error occurred\n\n`{J}`")