from django.shortcuts import render, redirect
from django.http import JsonResponse
from . import logic as logic
from . import task
import datetime

# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html', {})
    else:
        context = {
            "success": False,
            "message": request.method + " not supported, please send GET request"
        }
        return JsonResponse(context)

def index_marathi(request):
    if request.method == 'GET':
        return render(request, 'index_m.html', {})
    else:
        context = {
            "success": False,
            "message": request.method + " not supported, please send GET request"
        }
        return JsonResponse(context)

def index_hindi(request):
    if request.method == 'GET':
        return render(request, 'index_h.html', {})
    else:
        context = {
            "success": False,
            "message": request.method + " not supported, please send GET request"
        }
        return JsonResponse(context)

def get_vaccine(request):
    if request.method == 'POST':
        pincode = request.POST.get('pincode', '')
        context = logic.avaialibility_handler(pincode)
        if context['success']:
            return render(request, 'show_vaccines.html', context)
        else:
            return render(request, 'something.html', context)
    else:
        data = logic.avaialibility_handler("110001")
        return render(request, 'show_vaccines.html', data)


def get_vaccine_marathi(request):
    if request.method == 'POST':
        pincode = request.POST.get('pincode', '')
        context = logic.avaialibility_handler(pincode)
        if context['success']:
            return render(request, 'show_vaccines_m.html', context)
        else:
            return render(request, 'something_m.html', context)
    else:
        data = logic.avaialibility_handler("110001")
        return render(request, 'show_vaccines_m.html', data)
    
def get_vaccine_hindi(request):
    if request.method == 'POST':
        pincode = request.POST.get('pincode', '')
        context = logic.avaialibility_handler(pincode)
        if context['success']:
            return render(request, 'show_vaccines_h.html', context)
        else:
            return render(request, 'something_h.html', context)
    else:
        data = logic.avaialibility_handler("110001")
        return render(request, 'show_vaccines_h.html', data)


def update_notification(request):
    if request.method == 'POST':
        save_success = logic.save_to_notify(request)
        pincode = request.POST.get('pincode', '')
        context = logic.avaialibility_handler(pincode)
        context['save_success'] = save_success
        context['save_process'] = True
        if context['success']:
            return render(request, 'show_vaccines.html', context)
        else:
            return render(request, 'something.html', context)
    else:
        context = {
            "success": False,
            "message": request.method + " not supported, please send POST request"
        }
        return JsonResponse(context)

def update_notification_marathi(request):
    if request.method == 'POST':
        save_success = logic.save_to_notify(request)
        pincode = request.POST.get('pincode', '')
        context = logic.avaialibility_handler(pincode)
        context['save_success'] = save_success
        context['save_process'] = True
        if context['success']:
            return render(request, 'show_vaccines_m.html', context)
        else:
            return render(request, 'something_m.html', context)
    else:
        context = {
            "success": False,
            "message": request.method + " not supported, please send POST request"
        }
        return JsonResponse(context)


def update_notification_hindi(request):
    if request.method == 'POST':
        save_success = logic.save_to_notify(request)
        pincode = request.POST.get('pincode', '')
        context = logic.avaialibility_handler(pincode)
        context['save_success'] = save_success
        context['save_process'] = True
        if context['success']:
            return render(request, 'show_vaccines_h.html', context)
        else:
            return render(request, 'something_h.html', context)
    else:
        context = {
            "success": False,
            "message": request.method + " not supported, please send POST request"
        }
        return JsonResponse(context)

def not_available(request):
    if request.method == 'POST':
        pincode = request.POST.get('pincode', '')
        context = logic.avaialibility_handler(pincode)
        if context['success']:
            return render(request, 'show_vaccines.html', context)
        else:
            return render(request, 'something.html', context)
    else:
        data = logic.avaialibility_handler("110001")
        return render(request, 'something.html', data)

def show_all(request):
    if request.method == 'GET':
        context = logic.get_all_users()
        return render(request, 'showall.html', context)
    else:
        context = {
            "success": False,
            "message": request.method + " not supported, please send POST request"
        }
        return JsonResponse(context)

def ping(request):
    print('ping: ', datetime.datetime.now())
    task.handle_all(request)
    return JsonResponse({'hello': 'world'})
