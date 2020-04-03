import time
from datetime import datetime as dt

host_path = r"C:\Windows\System32\drivers\etc"
redirects = "127.0.0.1"
web_list = ["https://www.instagram.com/", "https://www.netflix.com/in/"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 0) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 1):
        print("go studyy")
        with open(host_path, "r+") as hfile:
            content = hfile.read()
            for websites in web_list:
                if websites in content:
                    pass
                else:
                    hfile.write(redirects+" "+websites+"\n")
    else:
        print("Just chill!!")
        with open(host_path, "r+") as hfile:
            content = hfile.readlines()
            hfile.seek(0)
            for line in content:
                if not any(websites in line for websites in web_list):
                    hfile.write(line)
            hfile.truncate()
    time.sleep(5)




