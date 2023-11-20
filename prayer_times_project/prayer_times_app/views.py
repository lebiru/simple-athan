import requests
from django.shortcuts import render

def get_prayer_times(request):
    prayer_times = None
    city = ""
    data = None  # Initialize data here


    # Geolocation parameters
    # lat = request.GET.get('lat')
    # lon = request.GET.get('lon')

    lat = None
    lon = None

    if lat and lon:
        # Call the API with latitude and longitude
        api_url = f"http://api.aladhan.com/v1/timings?latitude={lat}&longitude={lon}&method=2"  # Adjust the method as needed
        response = requests.get(api_url)
        data = response.json()
        city = data['data']['meta']['timezone']  # or any other relevant location information from the response
    elif request.method == 'POST':
        city = request.POST['city']
        api_url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country=YOUR_COUNTRY&method=YOUR_METHOD"
        response = requests.get(api_url)
        data = response.json()

    if data:
        prayer_times = {
            'fajr': data['data']['timings']['Fajr'],
            'dhuhr': data['data']['timings']['Dhuhr'],
            'asr': data['data']['timings']['Asr'],
            'maghrib': data['data']['timings']['Maghrib'],
            'isha': data['data']['timings']['Isha']
        }

    return render(request, 'index.html', {'prayer_times': prayer_times, 'city': city})

