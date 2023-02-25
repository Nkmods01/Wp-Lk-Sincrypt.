import subprocess,time,os,random,csv,sys,getpass

r= "\u001b[31;1m"
a= "\u001b[32m"
y = "\u001b[33;1m"
b="\u001b[34;1m"
m="\u001b[35;1m"
c="\u001b[36;1m"
w="\033[37m"
g="\033[32m"

os.system('clear')
print (m+"Please wait...")
time.sleep(2)
os.system('clear')
print (a+"INSTALLING....")
time.sleep(4)
os.system('clear')
subprocess.run(["apt", "update"])
os.system('clear')
subprocess.run(["apt", "upgrade"])
os.system('clear')
subprocess.run(["pkg", "update"])
os.system('clear')
subprocess.run(["pkg", "upgrade"])
os.system('clear')
subprocess.run(["pkg", "install", "git"])
os.system('clear')
subprocess.run(["pkg", "install", "vim"])
os.system('clear')
subprocess.run(["pkg", "install", "curl"])
os.system('clear')
subprocess.run(["pkg", "install", "mailutils"])
os.system('clear')
subprocess.run(["pip", "install", "request"])
os.system('clear')
subprocess.run(["pip", "install", "pymailtm"])
os.system('clear')
print (c+"RESTARTING YOUR TERMINAL")
time.sleep(5)
os.system('clear')
os.system('login')