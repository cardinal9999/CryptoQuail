try:
  import requests
except ModuleNotFoundError:
  print("You need to install a requests on your Python.")
  print("Go to your command prompt and type:")
  print("pip install requests")
  quit()
wordlist1 = requests.get("https://raw.githubusercontent.com/redacted/XKCD-password-generator/master/xkcdpass/static/eff-long")
a = []
for chunk in wordlist1:
  a.append(chunk.decode())
wordlist = "\n".join(a)
 
