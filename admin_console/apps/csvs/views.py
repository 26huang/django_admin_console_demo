from django.shortcuts import render
from django.http import HttpResponse
from .forms import CsvModelForm
from .models import Csv


def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(processed=False)
        try:
            print('file processed')
            obj.processed = True
            obj.save()

        except BaseException as e:
            print(e)


    return render(request, 'csvs/upload.html', {'form': form})
