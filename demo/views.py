from django.shortcuts import render

def Index(request):
    return render(request, 'demo/index.html')
