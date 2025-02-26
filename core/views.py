from django.shortcuts import render
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from . import models
from . import forms
import os
from .utils import zip_files


class MainPage:
    context = {'fileForm': forms.ModelFileForm(), 'status': 0, 'download_status': 1}
    def index(request):
        if request.method == "POST":
            fileForm = forms.ModelFileForm(request.POST, request.FILES)
            files = request.FILES.getlist('file')
            if fileForm.is_valid():
                for f in files:
                    instance = models.FileModel(file=f)
                    instance.save()
                MainPage.context['status'] = 1
            else:
                MainPage.context['status'] = -1
            return render(request, 'index.html', MainPage.context)
        if request.method == "GET":
            MainPage.context['status'] = 0
            return render(request, 'index.html', MainPage.context)

    def get_servings(request):
        if request.method == "GET":
            servings_path = os.path.join(os.getcwd(), 'servings')
            listed_files = os.listdir(servings_path)
            if len(listed_files) == 0:
                MainPage.context['download_status'] = 0
                return HttpResponseRedirect('/')
            elif len(listed_files) == 1:
                file = listed_files[0]
                response = FileResponse(open(os.path.join(servings_path, file), 'rb'), filename=file, as_attachment=True)
                return response
            else:
                zipped = zip_files(servings_path, listed_files)
                response = HttpResponse(zipped.getvalue(), content_type='application/x-zip-compressed')
                response['Content-Disposition'] = 'attachment; filename=files.zip'
                return response
            