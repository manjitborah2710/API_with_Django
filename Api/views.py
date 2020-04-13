from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework.decorators import api_view
import json
# Create your views here.

@api_view(http_method_names=['POST'])
def homeView(request):
    if(request.method=='POST'):
        if "hello" in request.POST.keys():
            print("hello ",request.POST["hello"])
            d={
                'value':request.POST['hello']
            }
            return JsonResponse(d)
    return JsonResponse({'value':None})
    # return HttpResponse(json.dumps(d),content_type="application/json")