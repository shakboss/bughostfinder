### Subdomain Finder ###
import requests, urllib.request
from requests.exceptions import ConnectionError
from urllib.error import HTTPError, URLError
from prettytable import PrettyTable
from colorama import init, Fore, Back
from tqdm import tqdm

subdomains = []
init(autoreset=True)
x = PrettyTable(["domain", "status code", "server"])

def getSubdomains(urlRequest):
  response = requests.get(urlRequest).json()
  list__ofDomain = response['result'].get('records')
  for subdomain in list__ofDomain:
    if 'domain' in subdomain:
     subdomains.append(subdomain["domain"])
    
def responseDomains():
  progressbar = tqdm(total=len(subdomains))
  socket = "https://"
  for domains in subdomains:
    try:
      response = requests.get(f"{socket}{domains}", timeout=5)
      respwn = urllib.request.urlopen(f"{socket}{domains}", timeout=5)
      server_header = respwn.getheader('Server')
      x.add_row([domains, response.status_code, server_header])
    except:
      pass
    finally:
      progressbar.update(1)
  progressbar.close()
  print(x)
  
if __name__ == "__main__":
  print(Fore.RED + 'ini mungkin memerlukan sedikit waktu')
  print(f'jika ada kendala hub : {Back.GREEN} +62895603555736')
  domain = input("Masukkan hostname (ruangguru.com): ")
  print(Fore.YELLOW + 'tunggu yaa, jangan dicancel ...')
  urlRequest = f"https://subdomains.whoisxmlapi.com/api/v1?apiKey=at_XroRwkGimSVtuawqrEW2B0AXXU49L&domainName={domain}"
  getSubdomains(urlRequest)
  responseDomains()