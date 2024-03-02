
from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("home page requested")
    test=['abc']
    return JsonResponse(test,safe=False)