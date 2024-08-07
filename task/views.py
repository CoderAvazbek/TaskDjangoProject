from django.shortcuts import render


def home(request):
    data = {
        "message_taxt": "This is Home Page"
    }
    return render(request, 'todolist.html', data)

def about(request):
    data = {
        "message_taxt": "This is About Page"
    }
    return render(request, 'about.html', data)

def contact(request):
    data = {
        "message_taxt": "This is Contact Page"
    }
    return render(request, 'contact.html', data)