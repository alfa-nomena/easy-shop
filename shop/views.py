from django.shortcuts import render

def home(request):
    template = "shop/index.html"
    context={}
    return render(request, template, context)
