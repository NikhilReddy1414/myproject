from django.http import HttpResponse

def hi(request):
    return HttpResponse("HI")