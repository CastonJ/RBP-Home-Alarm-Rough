import time
import smtplib
import RPi.GPIO as GPIO

TO= "xxxxxx@yahoo.com" # Put in an email address you want to send a text message to.
GMAIL_USER="xxxx" # Email address username
PASS= 'xxxx' # Password for email address login

SUBJECT = 'Alert!'
TEXT = 'Your Raspberry Pi detected an intruder!'


GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(17,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(24,GPIO.OUT)
GPIO.output(24,GPIO.HIGH)


def send_mail(): #the texting portion
    print ("Sending text")
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(GMAIL_USER,PASS)
    header = 'To: ' + TO + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject: ' + SUBJECT + '\n'
    print (header)
    msg = header + '\n' + TEXT + '\n\n'
    server.sendmail(GMAIL_USER,TO,msg)
    server.quit()
    time.sleep(1)
    print ("Text sent")

    
while True:
    
    if GPIO.input(12)==0: #trigger if sensor has detected something
        TEXT = 'Master Window'
        GPIO.output(24, 0)
        send_mail()
        time.sleep(100) #Sleep for 30 seconds
    else:
        time.sleep(.500) #check every 5 seconds

    if GPIO.input(12)==1: #trigger if sensor has detected something   
        GPIO.output(24, 1)

    if GPIO.input(25)==0: #trigger if sensor has detected something
        TEXT = 'Outside Garage Door'
        GPIO.output(24, 0)
        send_mail()
        time.sleep(100) #Sleep for 30 seconds
    else:
        time.sleep(.500) #check every 5 seconds

    if GPIO.input(25)==1: #trigger if sensor has detected something   
        GPIO.output(24, 1)
                            
    if GPIO.input(4)==0: #trigger if sensor has detected something
        TEXT = 'Sliding Glass Door'
        GPIO.output(24, 0)
        send_mail()
        time.sleep(100) #Sleep for 30 seconds
    else:
        time.sleep(.500) #check every 5 seconds
    
    if GPIO.input(4)==1: #trigger if sensor has detected something   
        GPIO.output(24, 1)
        
                
    if GPIO.input(17)==0: #trigger if sensor has detected something
        TEXT = 'Front Door'
        GPIO.output(24, 0)
        send_mail()
        time.sleep(100) #Sleep for 2 minutes
    else:
        time.sleep(.500) #check every 5 seconds

    if GPIO.input(17)==1: #trigger if sensor has detected something   
        GPIO.output(24, 1)

    if GPIO.input(27)==0: #trigger if sensor has detected something
        TEXT = 'Back Window'
        GPIO.output(24, 0)
        send_mail()
        time.sleep(100) #Sleep for 30 seconds
    else:
        time.sleep(.500) #check every 5 seconds

    if GPIO.input(27)==1: #trigger relay if sensor has detected something   
        GPIO.output(24, 1)

    if GPIO.input(22)==0: #trigger if sensor has detected something
        TEXT = 'Garage Door'
        GPIO.output(24, 0)
        send_mail()
        time.sleep(100) #Sleep for 2 minutes
    else:
        time.sleep(.500) #check every 5 seconds

    if GPIO.input(22)==1: #trigger relay if sensor has detected something   
        GPIO.output(24, 1)
        

GPIO.cleanup(24)
