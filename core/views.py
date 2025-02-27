from django.shortcuts import render
from django.http import HttpResponse, FileResponse, HttpResponseRedirect, HttpRequest
from . import models
from . import forms
import os
from .utils import zip_files


class MainPage:
    context = {'fileForm': forms.ModelFileForm(), 'status': 0, 'download_status': 1}

    @staticmethod
    def index(request: HttpRequest) -> HttpResponse | None:
        if request.method == "POST":
            file_form = forms.ModelFileForm(request.POST, request.FILES)
            files = request.FILES.getlist('file')
            if file_form.is_valid():
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

    @staticmethod
    def get_servings(request: HttpRequest) -> HttpResponse | HttpResponseRedirect | FileResponse | None:
        if request.method == "GET":
            servings_path: str = os.path.join(os.getcwd(), 'servings')
            listed_files: list[str] = os.listdir(servings_path)
            if len(listed_files) == 0:
                MainPage.context['download_status'] = 0
                return HttpResponseRedirect('/')
            elif len(listed_files) == 1:
                file: str = listed_files[0]
                return FileResponse(open(os.path.join(servings_path, file), 'rb'), filename=file,
                                    as_attachment=True)
            else:
                zipped = zip_files(servings_path, listed_files)
                response: HttpResponse = HttpResponse(zipped.getvalue(), content_type='application/x-zip-compressed')
                response['Content-Disposition'] = 'attachment; filename=files.zip'
                return response
