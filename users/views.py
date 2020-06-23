from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

from .models import User

class GetPost(View):
    # GET HTTP request (Get and list all users)
    def get(self, request):
        user_list = list(User.objects.values())
        return JsonResponse(user_list, safe=False)

    # to turn off CSRF validation(not recomended on production)(for sake of simplicity)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(GetPost, self).dispatch(request, *args, **kwargs)

    # POST HTTP request (Create a new user)
    def post(self, request):
        data = request.body.decode('utf8')
        data = json.loads(data)
        try: 
            new_user = User(fname = data["fname"], lname = data["lname"], email = data["email"], phone = data["phone"])
            new_user.save()
            return JsonResponse({"created": data}, safe=False)
        except:
            return JsonResponse({"error": "not a valid data"}, safe=False)   

class GetPutDelete(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(GetPutDelete, self).dispatch(request, *args, **kwargs)

    # GET HTTP request (Get a single user)
    def get(self, request, pk):
        user_list = {"User": list(User.objects.filter(pk=pk).values())}
        return JsonResponse(user_list,safe=False)

    # PUT HTTP request (Update a user)
    def put(self, request, pk):
        data = request.body.decode('utf8')
        data = json.loads(data)
        try:
            new_user = User.objects.get(pk=pk)
            data_key = list(data.keys())
            for key in data_key:
                if key == "fname":
                    new_user.fname = data[key]
                if key == "lname":
                    new_user.lname = data[key]
                if key == "email":
                    new_user.email = data[key]
                if key == "phone":
                    new_user.phone = data[key]
            new_user.save()
            return JsonResponse({"update": data}, safe=False)
        except User.DoesNotExist:
            return JsonResponse({"error": "Your user having provided primary key does not exist"}, safe=False)
        except:
            return JsonResponse({"error": "not a valid data"}, safe=False)

    # DELETE HTTP request (Delete a user)
    def delete(self, request, pk):
        try:
            new_user = User.objects.get(pk=pk)
            new_user.delete()
            return JsonResponse({"delete": True}, safe=False)
        except:
            return JsonResponse({"error": "not a valid primary key"}, safe=False)