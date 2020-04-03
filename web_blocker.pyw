import time
from datetime import datetime as dt

host_path = r"C:\Windows\System32\drivers\etc"
redirects = "127.0.0.1"
# you can add websites which distracts you in this list below..
web_list = ["https://www.instagram.com/", "https://www.netflix.com/in/"]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 10) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("go studyy")
        with open(host_path, "r+") as hfile:
            content = hfile.read()
            # here we check for the presence of websites in the file and if not we write it
            for websites in web_list:
                if websites in content:
                    pass
                else:
                    hfile.write(redirects+" "+websites+"\n")
    else:
        print("Just chill!!")
        with open(host_path, "r+") as hfile:
            content = hfile.readlines()
            # now we made list of lines in the file and here we take the pointer at the beginning 
            hfile.seek(0)
            for line in content:
                if not any(websites in line for websites in web_list):
                    hfile.write(line)
            hfile.truncate()
            # at the end if the websites are found it is deleted..
    time.sleep(5)




