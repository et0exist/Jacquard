from django.shortcuts import render, get_object_or_404
from .models import FileModel
from django.http import HttpResponse, HttpResponseNotAllowed


def file_handler(request, slug):
    if request.method == 'GET':
        print('get')
        return HttpResponse('get')

    elif request.method == 'POST':
        print('post')
        return HttpResponse('post')

    elif request.method == 'DELETE':
        print('delete')
        return HttpResponse('delete')

    else:
        return HttpResponseNotAllowed(['GET', 'POST', 'DELETE'])
