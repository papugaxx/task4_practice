from django.shortcuts import render
from django.utils import timezone


def index(request):
    now = timezone.localtime()
    hour = now.hour

    if 5 <= hour < 12:
        greeting = 'Доброго ранку!'
    elif 12 <= hour < 18:
        greeting = 'Добрий день!'
    else:
        greeting = 'Добрий вечір!'

    context = {
        'greeting': greeting,
        'current_date': now.strftime('%d.%m.%Y'),
        'current_time': now.strftime('%H:%M:%S'),
    }

    return render(request, 'viewapp/time.html', context)
