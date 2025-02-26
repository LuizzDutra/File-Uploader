from django.shortcuts import render
from django.http import HttpResponse, FileResponse, HttpResponseRedirect
from . import models
from . import forms
import os, io
import zipfile


class MainPage:
    context = {'fileForm': forms.ModelFileForm(), 'status': 0}
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
            return render(request, 'index.html', MainPage.context)

    def get_servings(request):
        if request.method == "GET":
            servings_path = os.path.join(os.getcwd(), 'servings')
            listed_files = os.listdir(servings_path)
            if len(listed_files) == 0:
                return HttpResponse("No files")
            elif len(listed_files) > 1:
                s = io.BytesIO()
                with zipfile.ZipFile(s, 'w') as zipf:
                    for file in listed_files:
                        zipf.write(os.path.join(servings_path, file), file)
                response = HttpResponse(s.getvalue(), content_type='application/x-zip-compressed')
                response['Content-Disposition'] = 'attachment; filename=files.zip'
                return response
            else:
                file = listed_files[0]
                response = FileResponse(open(os.path.join(servings_path, file), 'rb'), filename=file, as_attachment=True)
                return response