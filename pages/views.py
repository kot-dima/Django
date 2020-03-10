from django.template.response import TemplateResponse

# Create your views here.


def home(request):
    return TemplateResponse(request, "home.html")


def about(request):
    return TemplateResponse(request, "about.html")


def pages1(request):
    return TemplateResponse(request, "pages1.html")


def pages2(request):
    return TemplateResponse(request, "pages2.html")


def pages3(request):
    return TemplateResponse(request, "pages3.html")
