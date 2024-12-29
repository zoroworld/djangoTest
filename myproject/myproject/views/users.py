from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from myproject.models.User import User
from django.shortcuts import get_object_or_404
import json


def users(request):
    return HttpResponse("hello users")

@csrf_exempt
def get_post_users(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        users = User.objects.all()
        serialize_users = [user.name for user in users]
        return HttpResponse(json.dumps(serialize_users))
    
    # for post request
    if request.method == "POST":
        body = json.loads(request.body)
        user = User(username=body['username'] , name=body['name'], email=body['email'], address=body['address'])
        user.save()
        return HttpResponse(json.dumps({'id': user.id, 'name': user.name, 'email': user.email}))

@csrf_exempt
def update_delete_users(request: HttpRequest, id : int) -> HttpResponse:
      
    # get by single product
    if request.method == 'GET':
        user = get_object_or_404(User, id=id)
        return HttpResponse(json.dumps({'id': user.id, 'name': user.name, 'email': user.email}))
      
    # update the user
    if request.method == "PUT":
        body = json.loads(request.body)
        # user = User.objects.get(id=id)
        user = get_object_or_404(User, id=id)
        user.name = body['name']
        user.email = body['email']
        user.address = body['address']
        user.save()
        return HttpResponse(json.dumps({'id': user.id, 'name': user.name, 'email': user.email}))
    
    if request.method == "DELETE":
        body = json.loads(request.body)
        user = User.objects.get(id=id)
        user.delete();
        return HttpResponse(json.dumps({'id': user.id, 'name': user.name, 'email': user.email}))