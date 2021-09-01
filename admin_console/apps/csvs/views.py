from django.shortcuts import render
from django.http import HttpResponse
from .forms import CsvModelForm


def upload_file_view(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
    return render(request, 'csvs/upload.html', {'form': form})
