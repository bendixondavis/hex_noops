from django.shortcuts import render
import requests
import json


# Create your views here.
def my_color(request):
    data = requests.get('https://api.noopschallenge.com/hexbot?count=2').text #this gets a hex color value
    data = json.loads(data)
    
    for item in data['colors']:
        color = str(item['value'])
    return render(request, 'test_app/my_color.html', {'color': color})
