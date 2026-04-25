from django.shortcuts import render


def hello_en(request):
    return render(request, 'viewapp/hello.html', {'message': 'Hello, World!'})


def hello_fr(request):
    return render(request, 'viewapp/hello.html', {'message': 'Bonjour, le monde!'})


def hello_de(request):
    return render(request, 'viewapp/hello.html', {'message': 'Hallo, Welt!'})


def hello_es(request):
    return render(request, 'viewapp/hello.html', {'message': '¡Hola, Mundo!'})
