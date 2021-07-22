from django.shortcuts import render,redirect
from .forms import CutenessForm
# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def pictures(request):
    return render(request, 'pictures.html')

def ambassador(request):
    return render(request, 'ambassador.html')

def laszlo(request):
    return render(request, 'laszlo.html')

def contact(request):
    form = CutenessForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("")

    context = {
        "form": form
    }

    return render(request, 'contact.html', context)