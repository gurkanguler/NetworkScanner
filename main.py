import os
import sys
import platform
import argparse

# checkOs
def checkOs():
	return platform.system()

# clearScreen()
def clearScreen():
	if checkOs() == "Windows":
		print("It is not for Windows")
	else:
		os.system("clear")

# ErrorMessage
def ErrorMessage(msg):
	print("\033[1;31m[-] %s \033[0m\n" % msg)

# resetColor
def resetColor():
	print("\033[0m")

# banner
def banner():
	clearScreen()
	try:
		import pyfiglet
	except ImportError as err:
		ErrorMessage(err)
		os.system("sudo pip3 install pyfiglet")
	finally:
		f = pyfiglet.figlet_format("Network\nScanner", font="small")
		print("\033[1;32m")
		print(f)
		print(">>> Coded by gurkan <<<")
		resetColor()


def NetworkScan(ip):
	banner()
	arp_request_packet = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
	broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
	combined_packet = broadcast_packet/arp_request_packet
	(answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1)
	answered_list.summary()


if __name__ == '__main__':
	try:
		import scapy.all as scapy
	except ImportError as err:
		ErrorMessage(err)
		os.system("sudo pip3 install scapy")
	finally:
		args = argparse.ArgumentParser()
		args.add_argument("-i","--ip", help="Enter to ip address")
		user_args = vars(args.parse_args())
		ip_addr = user_args["ip"]
		NetworkScan(str(ip_addr))