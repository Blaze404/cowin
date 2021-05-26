from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from . import logic as F
import json


# Create your views here.
def index(request):
    print('here')
    return render(request, 'index22.html', {})


def add(request):
    if request.method == 'GET':
        all_agents = json.dumps(F.get_unique_agents())
        print('sending list: ', all_agents)
        return render(request, 'transactions.html', {'all_agents': all_agents})
    if request.method == 'POST':
        print(request.POST)
        # print('####', len(request.POST))
        F.add_transaction(request)
        return render(request, 'index22.html', {'transaction_add': True})


@csrf_exempt
def add_agent(request):
    if request.method == "GET":
        return render(request, 'addagent.html', {})
    if request.method == "POST":
        # print(request.POST)
        F.add_agent(request)
        return render(request, 'index22.html', {'agent_add': True})


def show_all(request):
    context = F.get_all_data()
    return render(request, 'showagents.html', context)
