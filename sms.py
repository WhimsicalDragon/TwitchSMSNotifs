#If vs code doesn't chill with importing random stuff I'm going to lose it
import smtplib
from time import sleep
import requests
import config
 
CARRIERS = {
    "att": "@mms.att.net",
    "tmobile": "@tmomail.net",
    "verizon": "@vtex.com",
    "sprint": "@page.nextel.com" # I don't think sprint still exists but I left this here just in case
}

#SENSITIVE DATA DO NOT SHARE!!!! 
EMAIL = config.EMAIL
PASSWORD = config.PASSWORD
CID = config.CID
CS = config.CS
phone_number = config.phone_number
carrier = config.carrier
#Less sensitive
CHANNEL = "WhimsicalDragon1337"
message = "WhimsicalDragon1337 is live!"



def send_message(phone_number, carrier, message):
    recipient = phone_number + CARRIERS[carrier]
    auth = (EMAIL, PASSWORD)
 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
 
    server.sendmail(auth[0], recipient, message)
 
def revokeToken(CID):
    global TOKEN

    #cleanup tokens
    headers = {
        "Content-Type":"application/x-www-form-urlencoded",

    }


    data = "client_id=" + CID +"&token=" + TOKEN

    resp = requests.post("https://id.twitch.tv/oauth2/revoke", headers=headers, data=data)



    if resp.status_code != 200:
        print("Failed to revoke token:" + TOKEN)
        print(resp.status_code)
    else:
        print("Succesfully revoked:" + TOKEN)

def liveCheck(CID,CS):
    global TOKEN

    headers = {
    'Authorization':"Bearer " + TOKEN,
    'Client-Id': CID,
    }

    r = requests.get('https://api.twitch.tv/helix/streams?user_login=' + CHANNEL, headers=headers)

    if r.status_code == 401:
        
        #Reup token. retry and exit if still failing
        revokeToken(CID)
        genToken(CID,CS)

        r = requests.get('https://api.twitch.tv/helix/streams?user_login=catnaps' + CHANNEL, headers=headers)
        if r.status_code == 401:
            print("Issue with token")
            exit()

    elif r.status_code != 200:
        #idk what is wrong so quit
        print("Bad response: " + r.status_code)
        exit()

    if (r.json()['data']) != [] :
        return True #They are live
    else:
        return False #They are not live


def genToken(CID,CS):
    global TOKEN
    headers = {
        "Content-Type":"application/x-www-form-urlencoded",
    }

    data = "client_id=" + CID +"&client_secret=" + CS + "&grant_type=client_credentials"

    resp = requests.post("https://id.twitch.tv/oauth2/token", headers=headers, data=data)

    print(resp.json())

    TOKEN = resp.json()["access_token"]
    return TOKEN

#End functions

global TOKEN
genToken(CID,CS)

while(liveCheck(CID,CS) == False):
    print("Recheck in 15 mins")
    sleep(780)
    print("Recheck in 2 mins")
    sleep(120)
    print("Rechecking...")

send_message(phone_number, carrier, message)

revokeToken(CID)
