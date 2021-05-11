import requests
from .models import User
from . import sendemail
import datetime
import json

def handle_all(request):
    all_pincodes = User.objects.values("pincode").distinct()

    print(all_pincodes)

    # Iterate through each pincode:
    for pincode_rs in all_pincodes:
        pincode = pincode_rs['pincode']
        ## get all users with given pincode whom we have not notified 5 or more times
        users = User.objects.filter(notified__lte=5, pincode=pincode)
        for user in users:
            name = user.name
            email = user.email

            base = datetime.datetime.today() # + datetime.timedelta(days=1)
            date_str = base.strftime("%d-%m-%Y")

            URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pincode, date_str)

            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}

            response = requests.get(URL, headers=headers)
            data = json.loads(response.text)

            if len(data.get('centers', [])) == 0:
                continue

            total_available = 0

            for center in data['centers']:
                for session in center['sessions']:
                    total_available += session["available_capacity"]

            if total_available == 0:
                continue
            try:
                sendemail.send_email(name, email, pincode)
                user.notified = user.notified + 1
            except:
                sendemail.send_email(name, email, pincode)
            user.save()

    return True

    # POST_CODE = pincode
    # base = datetime.datetime.today() # + datetime.timedelta(days=1)
    # date_str = base.strftime("%d-%m-%Y")
    #
    # URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(
    #     POST_CODE, date_str)
    #
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8',
    #     'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    #     'Accept-Encoding': 'none',
    #     'Accept-Language': 'en-US,en;q=0.8',
    #     'Connection': 'keep-alive'}
    #
    # response = requests.get(URL, headers=headers)
    # data = json.loads(response.text)