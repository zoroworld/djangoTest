from django.http import HttpResponse

def mywebname(request, name):
    return HttpResponse(f"<h1 style='font-size:100px'>Hello my name is {name}</h1>") 