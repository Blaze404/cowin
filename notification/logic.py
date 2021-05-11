import datetime
import requests
import json
from .models import User

def avaialibility_handler(pincode):
    POST_CODE = pincode
    base = datetime.datetime.today() # + datetime.timedelta(days=1)
    date_str = base.strftime("%d-%m-%Y")

    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(
        POST_CODE, date_str)


    proxy = {
    "https": 'https://116.203.190.255',
    "http": 'https://116.73.14.16'
}

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    not_json = False
    response = requests.get(URL, headers=headers, proxies=[roxy])
    try:
        data = json.loads(response.text)
    except:
        not_json = True
        data = {}

    if len(data.get('centers', [])) == 0 or not_json :
        context = {'success': False}
        context['pincode'] = pincode
        context['total_available'] = 0
        context['avail_color'] = 0
        return context

    total_available = 0

    for center in data['centers']:
        for session in center['sessions']:
            total_available += session["available_capacity"]

    data['total_available'] = total_available

    if total_available > 100:
        print('here')
        data['avail_color'] = 2
    elif total_available > 10 and total_available <= 100:
        data['avail_color'] = 1
    else:
        data['avail_color'] = 0

    data['pincode'] = pincode
    data['success'] = True

    return data


def save_to_notify(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    age = request.POST.get('age')
    pincode = request.POST.get('pincode')
    notify_type = request.POST.get('notify_type')

    user = User()
    user.name = name
    user.email = email
    user.age = age
    user.pincode = pincode
    user.notify_type = notify_type
    user.notified = 0

    try:
        user.save()
    except:
        return False

    return True


def get_all_users():
    all = User.objects.all()
    return {'users': all}