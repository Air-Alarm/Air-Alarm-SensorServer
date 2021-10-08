import socket
import requests
import re

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("pwnbit.kr", 443))
inside = sock.getsockname()[0]
print("내부 IP: ", inside)

req = requests.get("http://ipconfig.kr")
outside = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print("외부 IP: ", outside)


response = requests.get(f"http://api.air-alarm.site:4999/ip?inside={inside}&outside={outside}&SN=skhu0928")

print(response)
