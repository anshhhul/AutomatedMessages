from xvfbwrapper import Xvfb
import pywhatkit as kit
import random

vdisplay = Xvfb()
vdisplay.start()

def send_whatsapp_group_message(group_id, message, hour, minute):
    try:
        kit.sendwhatmsg_to_group(group_id, message, hour, minute)
        print("Message scheduled successfully!")
    except Exception as e:
        print (f"An error occured: {e}")

group_id = ""
message = "Good Morning \n Jay Shree Krishna"
hour = random.randint(18,23)
minute = random.randint(0,59)
send_whatsapp_group_message(group_id, message, hour, minute)

vdisplay.stop()