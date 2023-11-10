from django.shortcuts import render
from django.http import JsonResponse
from .models import KitchenData
from django.utils import timezone


# Create your views here.
# http://127.0.0.1:8000/chart_data_api/?bim=15&temperature=16&spo2=18&strick=20&bp=16
def api_view(request): #chart_data_view
    temperature = request.GET.get('temperature', None)
    gas_level = request.GET.get('gas_level', None)
    flame = request.GET.get('flame', None)
    relay1 = request.GET.get('relay1', None)
    relay2 = request.GET.get('relay2', None)
    switch1 = request.GET.get('switch1', None)
    switch2 = request.GET.get('switch2', None)

 
    # Create a dictionary to store the data you want to save
    data_to_save = {
        'datetime': timezone.now(),
        'temperature': temperature,
        'gas_level': gas_level,
        'flame': flame,
        'relay1': relay1,
        'relay2': relay2,
        'relay1': relay1,
        'relay2': relay2,
        'switch1' :switch1,
        'switch2':switch2,
    }

    # Remove None values from the dictionary
    data_to_save = {k: v for k, v in data_to_save.items() if v is not None}

    # Create a new entry in the database using the data
    KitchenData.objects.create(**data_to_save)

    return JsonResponse({"message": "Data saved successfully"})

# display chart,table and cards
def display_view(request):
    kitchen_data = KitchenData.objects.all()
    return render(request, 'kitchen_app/dashboard_view.html', {'kitchen_data': kitchen_data})

