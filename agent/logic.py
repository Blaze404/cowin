from .models import Agent, Transactions


## HYPER PARAMETERS
LAST_N = 15


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
        agent = request.POST.get("agent." + str(i) )
        amount = request.POST.get("amount." + str(i) )

        tr.agent_name = agent
        tr.agent_current_value = amount

        tr.save()

        ## add current money to agent also
        agent = Agent.objects.filter(agent_name=agent)[0]
        agent.agent_current_value = amount
        agent.save()


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



def get_last_transactions():
    agents = Agent.objects.all()

    context = {}

    for agent in agents:
        name = agent[0]
        transactions = Transactions.objects.filter(agent_name=agent.agent_name).order_by('-timestamp')
        if len(transactions) > LAST_N:
            transactions = transactions[:LAST_N]
        amounts = []
        for transaction in transactions:
            amounts.append(transaction.agent_current_value)
        amounts.reverse()
        context[agent.agent_name] = amounts

    ## give padding to amounts
    max_length = 0
    for l in context.values():
        if len(l) > max_length:
            max_length = len(l)

    for agent in context:
        if len(context[agent]) < max_length:
            padding_length = max_length - len(context[agent])
            temp = [0] * padding_length
            temp.extend(context[agent])
            context[agent] = temp

    print(context)
    return context