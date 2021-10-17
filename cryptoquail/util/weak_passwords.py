from urllib.request import urlopen; weak_password_database = urlopen("https://raw.githubusercontent.com/cinno/weak_password_list/master/top_password_list.txt").read().decode().splitlines()
