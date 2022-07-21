# Twitch SMS Notifications

This is a simple python program that pushes a sms message when the desired streamer is live

---
## Author

WhimsicalDragon1337 [Twitter](https://twitter.com/Whimsical1337)
You could've watched me code this live on [Twitch](https://www.twitch.tv/whimsicaldragon1337) ~~if my internet had been working when I was coding this~~

---
## Usage

To use this you will need a few api keys.

1. Setup your google account to use an app password: [Link](https://support.google.com/accounts/answer/185833?hl=en)
2. Get your Twitch Client ID and Client Secret: [Link](https://dev.twitch.tv/docs/api/get-started)
3. Enter these details as well as your phone number and carrier into a config.py file. You can use the exconfig.py for reference. (Carrier names are defined in the sms.py file. They are "att","tmobile","verizon", and "sprint". You may need to define a new carrier, and this may not work at all if you are outside of the US)
4. Set the desired streamer name CHANNEL variable.
5. Set the desired message in the message variable
6. Run the program. It will automatically check if the streamer is live every 15 minutes. You can change this time by changing the sleep calls.  It will automatically stop making checks once they go live, so you will have to restart the program or edit it if this is not the desired behavior.

---
## Details & Caveats

This program makes a twitch API call every 15 minutes until the desired streamer is live. If it fails due to an invalid OAuth token it will reup the token and try again. If it fails a 2nd time it will automatically quit. This program requires that the cell phone carrier have a way to send a message thru email. This is not always the case. This program could be hosted and used as a webapp, but I have no money for hosting and also don't want to be responsible for holding onto people's phone numbers.

---
## Support

I am a starving graduate student. Please give me money so I can keep coding dumb stuff. Also if I get enough money I can host this as webapp so you don't have to run it yourself! You can do that [here](https://ko-fi.com/whimsicaldragon1337)