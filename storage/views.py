from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import FileModel
from .forms import FileForm


def file_handler(request, slug):
    if request.method == 'GET':
        print('get')
        return HttpResponse('get')

    elif request.method == 'POST':
        print('post')
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save()
            # print(file.read())
        return HttpResponse('post')

    elif request.method == 'DELETE':
        print('delete')
        return HttpResponse('delete')

    else:
        return HttpResponseNotAllowed(['GET', 'POST', 'DELETE'])
