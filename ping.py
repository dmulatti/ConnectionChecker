import shlex
import subprocess
import time
import smtplib
import datetime
import os

def mail(subject, msg):
	from email.mime.text import MIMEText

	msg = MIMEText(msg)

	sender = 'noreply@necio.ca'
	receiver = 'dmulatti@gmail.com'
	msg['Subject'] = subject
	msg['From'] = sender
	msg['To'] = receiver

	s = smtplib.SMTP('localhost')
	s.sendmail(sender, [receiver], msg.as_string())
	s.quit()

def ping (a):
	cmd=shlex.split("ping -c1 %s" % a)
	try:
	   output = subprocess.check_output(cmd)
	except subprocess.CalledProcessError,e:
		return False
	else:
		return True

def connectionDown (a):
	time.sleep(5)
	if not ping (a):
		mail (	'Your internet is down!', 
				'Looks like your internet is down. You\'ll get an email when it\'s back up again.\n\n-Your friendly python script')

		while not ping(a):
			time.sleep(20)
		
		mail('Your internet is back up!', 'Looks like it\'s up and running again!\n\n-Your friendly python script')



while (1):
	time.sleep(60)
	if not ping ('home.mulatti.ca'):	
		log=open('./log.txt', 'a')
		log.write("Connection DOWN as of %s\n" %(str(datetime.datetime.now())))
		log.close()	
		connectionDown('home.mulatti.ca')
	#delete log file if it is over 1MB
	if (os.path.getsize('./log.txt')) > 1000000:
		os.remove('./log.txt') 
	log=open('./log.txt', 'a')
	log.write("Connection up as of %s\n" % (str(datetime.datetime.now())))
	log.close()
