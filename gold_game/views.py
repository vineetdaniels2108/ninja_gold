from django.shortcuts import render, redirect, HttpResponse
import random
from datetime import datetime

# Create your views here.

gold_map = {
    'farm' : (10,20),
    'cave' : (5,10),
    'house' : (2,5),
    'casino' : (0,50)
}

def index(request):
    if 'gold' not in request.session or 'activities' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []    
    return render(request, 'home.html')


def reset(request): 
    request.session.flush()
    return redirect('/')


def farm_earn(request):
    if request.method == 'GET':
        return redirect ('/')
    
    building_name = request.POST['building']
    building = gold_map[building_name]
    gold_value = random.choice(building)
    time = datetime.now().strftime("%m/%d/%Y %I:%M%p")
    
    if building_name == 'casino':
        mylist = [0,1]
        result = random.choice(mylist)
        if result == 0:
            gold_value = random.choice(building) * -1
            message = f"Earned {gold_value} from the {building_name} at time {time}"
        else:
            gold_value = random.choice(building)
            message = f"Earned {gold_value} from the {building_name} at time {time}"
    else:
        gold_value = random.choice(building)
        message = f"Earned {gold_value} from the {building_name} at time {time}"
        
    
    request.session['gold'] += gold_value
    
    request.session['activities'].append({'message': message})
    
    return redirect('/')
    
    
        
        
