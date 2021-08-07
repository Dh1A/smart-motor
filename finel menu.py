
#TODO : 
#Clean Definitions 
#Separate Temp Reading & Relay Control functions in Files Then Import them
#Clean Menu


import RPi.GPIO as GPIO
import time
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD

lcd = LCD()

clk = 22                                                                                                                                                                                                                                                                                                                                                
dt = 27
button1= 17
step = 1
buttonSt = 0
counter = 0
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
counter = 0


def safe_exit(signum, frame):
    exit(1)

signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

lcd.text("Raspberry Pi ", 1)
lcd.text("menu test", 2)
time.sleep(1.5)
lcd.text("ready",1)
def boutton_pos() :
    global buttonSt
        
    if GPIO.input(button1) == 0 :
            buttonSt = 1
            time.sleep(0.5)
    else :
        buttonSt = 0
            
def counter_pos(first, last ):
    global counter
    
    if GPIO.input(button1) == 0 :
        buttonSt = 1 
    if GPIO.input(clk) == 1 and GPIO.input(dt) == 0:
        counter = counter + 1
        if counter >= last :
            counter = last
        time.sleep(1)             
    if GPIO.input(clk) == 0 and GPIO.input(dt) == 1:
        counter = counter - 1
        if counter <= first :
            counter = first
        time.sleep(1)
     
            
def principal_menu() :
    counter_pos(1, 2)
    lcd.text(" relay", 1)
    lcd.text(" temp", 2)
    lcd.text(">",counter)
    
    if buttonSt == 1 and counter == 1 :
        while True :
            relay_menu()
            
import RPi.GPIO as GPIO
import time
from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD

lcd = LCD()

clk = 22                                                                                                                                                                                                                                                                                                                                                
dt = 27
button1= 17
step = 1
buttonSt = 0
counter = 0
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)
counter = 0



def safe_exit(signum, frame):
    exit(1)

signal(SIGTERM, safe_exit)
signal(SIGHUP, safe_exit)

lcd.text("Raspberry Pi ", 1)
lcd.text("menu test", 2)
time.sleep(1.5)
lcd.text("ready",1)
def boutton_pos() :
    global buttonSt
        
    if GPIO.input(button1) == 0 :
            buttonSt = 1
            time.sleep(0.5)
    else :
        buttonSt = 0
            
def counter_pos(first, last ):
    global counter
    
    if GPIO.input(button1) == 0 :
        buttonSt = 1 
    if GPIO.input(clk) == 1 and GPIO.input(dt) == 0:
        counter = counter + 1
        if counter >= last :
            counter = last
        time.sleep(1)             
    if GPIO.input(clk) == 0 and GPIO.input(dt) == 1:
        counter = counter - 1
        if counter <= first :
            counter = first
        time.sleep(1)
     
            
def principal_menu() :
    counter_pos(1, 2)
    lcd.text(" relay", 1)
    lcd.text(" temp", 2)
    lcd.text(">",counter)
    
    if buttonSt == 1 and counter == 1 :
        while True :
            relay_menu()
            
        
    if buttonSt == 1 and counter == 2 :
        while True :
            temp_menu()
            
            
            
            
    
        
def temp_menu()  :
    #print ("Counter ", counter)
    #print ("botton ", buttonSt)
    boutton_pos()
    lcd.text("the temp is:40 C°", 1)
    lcd.text(">back", 2)
    time.sleep(0.05)
    if buttonSt == 1 :
        counter = 1
        principal_menu()
        
    

def relay_menu() :
        print ("Counter ", counter)
        print ("botton ", buttonSt)
        lcd.text("relay 1 : ON", 1)
        lcd.text("relay 2 : OFF", 2)
        
    

while True:
    
    principal_menu()
    boutton_pos()


    #temp_menu()
    print ("Counter ", counter)
    print ("botton ", buttonSt)
        
            
    

