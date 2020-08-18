from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Books, Author
from .serializer import BooksSerializer, AuthorSerializer


class BooksAPI(APIView):

    def post(self, request):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id is None:
            book = Books.objects.all()
            return Response([{"name": _.name, "author": _.author.name}for _ in book])

        _ = Books.objects.filter(id=id).first()
        return Response([{"name": _.name, "author": _.author.name}])


class Author(APIView):

    def get(self, request, author_name):
        author = Author.objects.filter(name=author_name).first()
        return author.object.all()

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


