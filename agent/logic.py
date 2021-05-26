from .models import Agent, Transactions

def add_agent(request):
    name = request.POST.get('name')
    amount = request.POST.get('amount')
    safety = request.POST.get('safety')

    agent = Agent()

    agent.agent_name = name
    agent.agent_investment = amount
    agent.agent_current_value = amount
    agent.safety = safety

    agent.save()

    return True


def add_transaction(request):

    total = len(request.POST) // 2
    print('total is: ', total)
    for i in range(total):
        tr = Transactions()
        agent = request.POST.get( "agent." + str(i) )
        amount = request.POST.get( "amount." + str(i) )

        tr.agent_name = agent
        tr.agent_current_value = amount

        tr.save()

        # print(agent, amount, '@@@@@@@')
    return Transactions


def get_unique_agents():
    agents = []
    for agent in Agent.objects.order_by().values_list('agent_name').distinct():
        agents.append(agent[0])
    return agents


def get_all_data():
    all_agents = Agent.objects.all()
    all_transations = Transactions.objects.all()
    return {'agents': all_agents, 'transactions': all_transations }


def get_all_transactions():
    all = Transactions.objects.all()
    return {'data': all}