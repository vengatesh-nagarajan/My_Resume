# -*- coding: utf-8 -*-
import time
import sys
def show():
	print "Name: Vengatesh.N"
	print "EmailID: vengat9487@gmail.com"
	print "linkedin: https://in.linkedin.com/in/vengatesh-nagarajan-610086bb"
def TS():
	print "Successfully completed CCNA Routing and Switching certification held by CISCO"
	time.sleep(0.2)
	print "Successfully completed CCNA Security certification held by CISCO"
	time.sleep(0.2)
	print "Experience on windows, Linux server auditing-checking for best practices"
	time.sleep(0.2)
	print "Experience with working on Nessus, Metasploit Framework, Nexpose, Nmap, kali linux"
	time.sleep(0.2)
	print "Experience in developing custom Penetration Testing scripts in Python"
	time.sleep(0.2)
	print "Developed a Tool which generates list of Windows Patches missing in Remote Windows Systems"
def IT():
	print "Computer Networks"
	time.sleep(0.2)
	print "Network Security"
	time.sleep(0.2)
	print "Computer Hardware"
def WE():
	print "Working for Cyber Security Works Pvt. Ltd. at Chennai from June -2014 Till Date"
def EQ():
	list1 = ["B.TECH", "SASTRA University-SRC" "Kumbakonam.", "6.9 (CGPA)"]
	list2 = ["12th", "Dr. GS KalyanaSundram Mat. Hr. Sec. School, Pazhyagudalur.", "86.50"]
	list3 = ["10th", "Sri Sankara Mat. Hr. Sec. School, Peralam.", "77.20"]
	print ', '.join(list1)
	time.sleep(0.2)
	print ', '.join(list2)
	time.sleep(0.2)
	print ', '.join(list3)
	time.sleep(0.2)
def CS():
	print "NMAP-Accessor"
	print "https://github.com/vengatesh-nagarajan/NMAP_ASSESSOR"
	print "In-built switches to scan target which avoids unnecessary time on mentioning the switches of nmap"
	time.sleep(0.2)
	print "Ping_Scanner"
	print "https://github.com/vengatesh-nagarajan/Ping_Scanner"
	print "Finds number of IPs Alive in a particular subnet by one-shot"
	time.sleep(0.2)
def SM():
	time.sleep(0.2)
	print "presented 5+ talks and conducted A Full day hands-on session on network securiy"
	print "https://null.co.in/profile/1488-vengatesh"
def ID():
	print "Router#"
	i4 = str(raw_input())
	return i4

print "Router>"
for i in range(1,10):
	print"Router>"
	time.sleep(0.5)
i1 = str(raw_input())
print i1
if i1 == "?":
	print "Router> enable show"
i2 = str(raw_input())
if i2 == "show":
	show()
	for i in range(1,5):
		print"Router>"
		time.sleep(0.5)
	i2 = str(raw_input())
if i2 == "enable":
	for i in range(1,5):
		print"Router#"
		time.sleep(0.5)
i3 = str(raw_input())
if i3 == "?":
	flag = 1
	print "Router# Interests Technical-Skills Work-Experience Educational-Qualifications Speech-Making Custom-Scripts Exit"
	while (flag == 1):
		i4 = ID()
		if i4 == "Technical-Skills":
			TS()
		if i4 == "Interests":
			IT()
		if i4 == "Work-Experience":
			WE()
		if i4 == "Educational-Qualifications":
			EQ()
		if i4 == "Custom-Scripts":
			CS()
		if i4 == "Speech-Making":
			SM()
		if i4 == "Exit":
			flag =0
			sys.exit(0)



