
import socket

s=socket.socket()
_IP_=input("Enter The IP Address: ")
_PORT_=input("Enter The Port: ")
s.connect((_IP_,int(_PORT_)))
answer = s.recv(1024)
print (answer)
print("    __  ___          __        ____           ____ ")
print("   /  |/  /___ _____/ /__     / __ )__  __   / __ \____ ___  ____ ______")
print("  / /|_/ / __ `/ __  / _ \   / __  / / / /  / / / / __ `__ \/ __ `/ ___/")
print(" / /  / / /_/ / /_/ /  __/  / /_/ / /_/ /  / /_/ / / / / / / /_/ / /    ")
print("/_/  /_/\__,_/\__,_/\___/  /_____/\__, /   \____/_/ /_/ /_/\__,_/_/     ")
print("                                 /____/                                 ")
print("    ____       ____           ")
print("   / __ \___  / __/___ ___  __")
print("  / /_/ / _ \/ /_/ __ `/ / / /")
print(" / _, _/  __/ __/ /_/ / /_/ / ")
print("/_/ |_|\___/_/  \__,_/\__, /  ")
print("                     /____/   ")

s.close
