from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import forms

def index(request):
    context = {'fileForm': forms.ModelFileForm(), 'status': 0}
    if request.method == "POST":
        fileForm = forms.ModelFileForm(request.POST, request.FILES)
        if fileForm.is_valid():
            fileForm.save()
            context['status'] = 1
        else:
            context['status'] = -1
        return render(request, 'index.html', context)
    if request.method == "GET":
        return render(request, 'index.html', context)


