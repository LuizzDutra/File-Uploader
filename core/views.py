from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from . import models
from . import forms
import os, io
import zipfile

def index(request):
    context = {'fileForm': forms.ModelFileForm(), 'status': 0}
    if request.method == "POST":
        fileForm = forms.ModelFileForm(request.POST, request.FILES)
        files = request.FILES.getlist('file')
        if fileForm.is_valid():
            for f in files:
                instance = models.FileModel(file=f)
                instance.save()
            context['status'] = 1
        else:
            context['status'] = -1
        return render(request, 'index.html', context)
    if request.method == "GET":
        return render(request, 'index.html', context)

def get_servings(request):
    if request.method == "GET":
        servings_path = os.path.join(os.getcwd(), 'servings')
        s = io.BytesIO()
        with zipfile.ZipFile(s, 'w') as zipf:
            for file in os.listdir(servings_path):
                print(os.path.basename(os.path.join(servings_path, file)))
                zipf.write(os.path.join(servings_path, file), file)

        response = HttpResponse(s.getvalue(), content_type='application/x-zip-compressed')
        response['Content-Disposition'] = 'attachment; filename=files.zip'
        
        return response
