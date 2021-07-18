import requests
import argparse
from Generate import Functions
import random
import names
from threading import Thread
import json

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--total", required=True,help="Total number of request to send")
ap.add_argument("-d", "--debug", required=False,help="Debug mode, does not send request")
args = vars(ap.parse_args())
gen = Functions()
url = "https://secure.plhcharge.com/payment/eyJwIjo0OTgwNTc0NCwiYyI6IjQ2OTBkYzhhZmY5NjQxYTFmMzNmODdhMjllMTkwYWRjYTBlYWU3YjEifSAg"
payload='cardNumber=5437%200303%209809%209449&country=US&csc=361&email=ndswndiw%40gmail.com&expires_month=06&expires_year=23&holder_name=lol%20kappa&paymentId=49805744&submit=&threeds=eyJqYXZhX2VuYWJsZWQiOmZhbHNlLCJicm93c2VyX2xhbmd1YWdlIjoiZW4tVVMiLCJicm93c2VyX2NvbG9yX2RlcHRoIjozMCwiYnJvd3Nlcl9zY3JlZW5faGVpZ2h0Ijo5MDAsImJyb3dzZXJfc2NyZWVuX3dpZHRoIjoxNDQwLCJicm93c2VyX3R6IjozMDB9&zip=78641'
cardNum = ""        
csc = ""
email = ""
expM = ""
expY = ""
name = ""
payID = ""
zipCode = ""
headers = {
  'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
  'Accept': '*/*',
  'DNT': '1',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5376e Safari/8536.25',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty'
}

def Spam():
  for x in range(int(args["total"])):

    cardNum = gen.luhn( str("559436") )
    csc = str(random.randint(000,999))
    email = gen.email()
    expM = gen.expM()
    expY = str(random.randint(22,25))
    name = names.get_first_name() + "%20" + names.get_last_name()
    payID = str(random.randint(49805744,99999999))
    zipCode = str(random.randint(75001,88589))


    payload='cardNumber=%s&country=US&csc=%s&email=%s&expires_month=%s&expires_year=%s&holder_name=%s&paymentId=%s&submit=&threeds=eyJqYXZhX2VuYWJsZWQiOmZhbHNlLCJicm93c2VyX2xhbmd1YWdlIjoiZW4tVVMiLCJicm93c2VyX2NvbG9yX2RlcHRoIjozMCwiYnJvd3Nlcl9zY3JlZW5faGVpZ2h0Ijo5MDAsImJyb3dzZXJfc2NyZWVuX3dpZHRoIjoxNDQwLCJicm93c2VyX3R6IjozMDB9&zip=%s' % (cardNum,csc,email,expM,expY,name,payID,zipCode)

    if (args["debug"] != "false"):
      response = requests.request("POST", url, headers=headers, data=payload)
      # print(response.text)
    outcome = json.loads(response.text)
    print("[" + str(x) + "]" +  outcome["message"])




Spam()