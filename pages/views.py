from django.template.response import TemplateResponse

# Create your views here.


def home(request):
    data = {
        "h1": "Craft",
        "h2": "Cover your page.",
        "subtitle": "Cover is a one-page template for building simple and beautiful home pages. Download, edit the text, and add your own fullscreen background photo to make it your own.",
        

    }
    return TemplateResponse(request, "home.html", data)


def about(request):
    return TemplateResponse(request, "about.html")


def pages1(request):
    return TemplateResponse(request, "pages1.html")


def pages2(request):
    return TemplateResponse(request, "pages2.html")


def pages3(request):
    return TemplateResponse(request, "pages3.html")
