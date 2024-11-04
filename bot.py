# Note
# Jangan diubah bro lu ubah dikit eror kodenya kalo ngeyel eror jangan salahin gua
_P='/del_subdo'
_O='/add_subdo'
_N='/server'
_M='/tlsmax'
_L='/bypass'
_K='/start'
_J=b'donet'
_I=b'servku'
_H=b'confdomen'
_G='Domain not found.'
_F='result'
_E='application/json'
_D='Content-Type'
_C='X-Auth-Key'
_B='X-Auth-Email'
_A='You do not have permission to use this feature.'
from telethon import TelegramClient,events,Button
import requests,os
from dotenv import load_dotenv
import time,json,paramiko,psutil,ipaddress
from func.mix import mixmax
from func.cfbypass import cfpeler
from func.server import tesserver
from func.tls import tlsmax
from buttons.myserver import myserv
from buttons.donate import donet
load_dotenv()
MESSWAIT=os.getenv('MESSWAIT')
MESSDONE=os.getenv('MESSDONE')
CLOUDFLARE_EMAIL=os.getenv('CLOUDFLARE_EMAIL')
CLOUDFLARE_API_KEY=os.getenv('CLOUDFLARE_API_KEY')
YOUR_USER_ID=int(os.getenv('YOUR_USER_ID'))
GLOBAL_CH=os.getenv('CHANNEL_URL')
domen=''
cpunya=psutil.cpu_percent()
memorinya=psutil.virtual_memory().percent
menunya=f"""
🤖 **CLOUDBOT** 🤖

**💻CPU USAGE** {cpunya}%
**💻RAM USAGE** {memorinya}%

**__SITE MENU__**
☞**/start**
◍ __Start Using Bots__

☞**/antiddos**
◍ __Activate Under Attacks Mode__

☞**/server**
◍ __Setup Your Server To Bot__

☞**/add_subdo**
◍ __Add Subdo To Your Domain__

☞**/del_subdo**
◍ __Delete Subdo To Your Domain__

**__DDoS MENU__**
**/mix | /bypass | /tlsmax**
◍ __DDoS Target Website__"""
menuanim1='🤖**CLOUDBOT MENU**'
menuanim2='🤖**CLOUDBOT MENU**\n/start - __Configuration Domain__'
menuanim3='🤖**CLOUDBOT MENU**\n/start - __Configuration Domain__\n/add_subdo - __Add Subdo To Your Domain__'
menuanim4='🤖**CLOUDBOT MENU**\n/start - __Configuration Domain__\n/add_subdo - __Add Subdo To Your Domain__\n/del_subdo - __Delete Subdo To Your Domain__'
menuanim4='\n🤖 **CLOUDBOT** 🤖\n\n**💻CPU USAGE** CHECKING\n**💻RAM USAGE** CHECKING\n\n\n**__SITE MENU__**\n**/start**\n◍ __Configuration Domain__\n**/add_subdo**\n◍ __Add Subdo To Your Domain__\n**/del_subdo**\n◍ __Delete Subdo To Your Domain__\n**/antiddos**\n◍ __Activate Under Attacks Mode__\n**/server**\n◍ __Setup Your Server To Bot__\n**/mix | /bypass**\n◍ __DDoS Target Website__\n'
def get_domain_list():
	B='https://api.cloudflare.com/client/v4/zones';C={_B:CLOUDFLARE_EMAIL,_C:CLOUDFLARE_API_KEY,_D:_E};A=requests.get(B,headers=C)
	if A.ok:D=[A['name']for A in A.json()[_F]];return D
	else:return[]
def add_dns_record(domain,record_type,name,content):
	C=f"https://api.cloudflare.com/client/v4/zones?name={domain}";A={_B:CLOUDFLARE_EMAIL,_C:CLOUDFLARE_API_KEY,_D:_E};B=requests.get(C,headers=A)
	if B.ok:
		D=B.json()[_F][0]['id'];E=f"https://api.cloudflare.com/client/v4/zones/{D}/dns_records";F={'type':record_type,'name':name,'content':content};G=requests.post(E,headers=A,json=F)
		if G.ok:return'DNS record added successfully.'
		else:return'Gagal menambahkan DNS record.'
	else:return _G
def delete_dns_record(domain,record_id):
	C=f"https://api.cloudflare.com/client/v4/zones?name={domain}";A={_B:CLOUDFLARE_EMAIL,_C:CLOUDFLARE_API_KEY,_D:_E};B=requests.get(C,headers=A)
	if B.ok:
		D=B.json()[_F][0]['id'];E=f"https://api.cloudflare.com/client/v4/zones/{D}/dns_records/{record_id}";F=requests.delete(E,headers=A)
		if F.ok:return'The DNS record has been successfully deleted.'
		else:return'Failed to delete DNS record.'
	else:return _G
def toggle_under_attack(domain,status):
	B=status;A=domain;E=f"https://api.cloudflare.com/client/v4/zones?name={A}";C={_B:CLOUDFLARE_EMAIL,_C:CLOUDFLARE_API_KEY,_D:_E};D=requests.get(E,headers=C)
	if D.ok:
		F=D.json()[_F][0]['id'];G=f"https://api.cloudflare.com/client/v4/zones/{F}/settings/security_level";H={'value':'under_attack'if B=='on'else'medium'};I=requests.patch(G,headers=C,json=H)
		if I.ok:return f"The 'I'm Under Attack' feature has been successfully {'activated'if B=='on'else'deactivated'} for domain {A}."
		else:return'Failed to change security settings.'
	else:return _G
def generate_domain_keyboard():
	C=get_domain_list();A=[]
	for B in C:A.append([Button.inline(B,data=f"domain:{B}")])
	return A
async def check_domain(event,domen):
	if not domen:await event.reply("You haven't set up a domain yet. Please set the domain first.\n/start to set the domain");return False
	else:return True
api_id=os.getenv('TELEGRAM_API_ID')
api_hash=os.getenv('TELEGRAM_API_HASH')
bot_token=os.getenv('TELEGRAM_BOT_TOKEN')
client=TelegramClient('bot',api_id,api_hash).start(bot_token=bot_token)
@client.on(events.NewMessage(pattern=_K))
async def start(event):A=await event.reply(MESSWAIT);B=[[Button.inline(f"🌍 MANAGE DOMAIN",_H)],[Button.inline(f"💻 MY SAVED SERVER",_I)],[Button.inline(f"💰 DONATE PROJECTS",_J)],[Button.url(f"⏬ GET UPDATE",f"{GLOBAL_CH}")]];await A.edit(menuanim1);time.sleep(.4);await A.edit(menuanim2);time.sleep(.4);await A.edit(menuanim3);time.sleep(.4);await A.edit(menuanim4);time.sleep(.4);await A.edit(menunya,buttons=B)
@client.on(events.NewMessage(pattern='/mix'))
async def mix_handler(event):await mixmax(event)
@client.on(events.NewMessage(pattern=_L))
async def bypass_handler(event):await cfpeler(event)
@client.on(events.NewMessage(pattern=_M))
async def tlsmax_handler(event):await tlsmax(event)
@client.on(events.NewMessage(pattern=_N))
async def server_handler(event):await tesserver(event)
@client.on(events.NewMessage(pattern=_O))
async def add_record(event):
	A=event
	if A.sender_id==YOUR_USER_ID:
		B=A.raw_text.split()
		if await check_domain(A,domen):
			if len(B)==4:C=domen;D=B[1];E=B[2];F=B[3];G=add_dns_record(C,D,E,F);await A.reply(G)
			else:await A.reply('Use format: /add_subdo <record_type> <name> <content>')
	else:await A.reply(_A)
@client.on(events.NewMessage(pattern=_P))
async def delete_record(event):
	A=event
	if A.sender_id==YOUR_USER_ID:
		B=A.raw_text.split()
		if await check_domain(A,domen):
			if len(B)==2:C=domen;D=B[1];E=delete_dns_record(C,D);await A.reply(E)
			else:await A.reply('Use format: /del_subdo <record_id>')
	else:await A.reply(_A)
@client.on(events.NewMessage(pattern='/antiddos'))
async def toggle_attack(event):
	A=event
	if A.sender_id==YOUR_USER_ID:
		B=A.raw_text.split()
		if await check_domain(A,domen):
			if len(B)==2:C=domen;D=B[1];E=toggle_under_attack(C,D);await A.reply(E)
			else:await A.reply('Use format: /antiddos <on/off>')
	else:await A.reply(_A)
@client.on(events.NewMessage())
async def handle_address(event):
	G='Hello';F='Helo';E='Hallo';D='Halo';B=event;C=await B.get_sender();H=B.sender_id;A=B.raw_text;print(f"Message From\nID: {H}\nName: {C.first_name}\nUsername: {C.username}")
	if not(_K in A or'/mix'in A or _L in A or _N in A or _O in A or _P in A or D in A or E in A or F in A or G in A or'Hi'in A or'p'in A or _M in A):await B.reply("Sorry i'm not understand :(")
	elif D in A or E in A or F in A or G in A or'Hi'in A or'P'in A:await B.reply(f"Hello sir {C.first_name}🤗")
@client.on(events.CallbackQuery(pattern=_J))
async def donet_handler(event):await donet(event)
@client.on(events.CallbackQuery(pattern=_I))
async def myserver_handle(event):await myserv(event)
@client.on(events.CallbackQuery(pattern=_H))
async def domen(event):
	A=event;await A.edit(MESSWAIT)
	if A.sender_id==YOUR_USER_ID:
		B=get_domain_list();C=generate_domain_keyboard()
		if B:await A.edit(f"Berikut adalah daftar domain yang tersedia di akun Anda:",buttons=C)
		else:await A.edit('Tidak ada domain yang tersedia di akun Anda.')
	else:await A.edit(_A)
@client.on(events.CallbackQuery(pattern=b'domain:(.*)'))
async def choose_domain(event):
	A=event;global domen
	if A.sender_id==YOUR_USER_ID:B=A.data_match.group(1).decode('utf-8');await A.edit(f"Anda telah memilih domain: {B}");domen=f"{B}";time.sleep(.7);await A.edit(menunya)
	else:await A.edit(_A)
print('Bot online')
client.run_until_disconnected()