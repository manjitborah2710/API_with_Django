from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
from .models import Info
import json
# Create your views here.

@api_view(http_method_names=['GET'])
def homeView(request):
    if(request.method=='GET'):
        if "hello" in request.GET.keys():
            print("hello ",request.GET["hello"])
            val=request.GET['hello']
            Info.objects.create(text=val)
            d={
                'value':val
            }
            return JsonResponse(d)
    return JsonResponse({'value':None})
    # return HttpResponse(json.dumps(d),content_type="application/json")