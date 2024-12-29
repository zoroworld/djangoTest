from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from myproject.models.User import User
import json

@csrf_exempt
def users(request: HttpRequest) -> HttpResponse:
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