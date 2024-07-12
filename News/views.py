from django.shortcuts import render
import requests

# Create your views here.


def index(request):
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey=087471d0792a4529937f70973381d41c"
    data = requests.get(url)
    response = data.json()
    articles = response["articles"]
    context = {"articles": articles}
    return render(request, "index.html", context)


def category(request, name):
    url = f"https://newsapi.org/v2/top-headlines?category={name}&apiKey=087471d0792a4529937f70973381d41c"
    data = requests.get(url)
    response = data.json()
    articles = response["articles"]
    context = {"articles": articles, "category": name}
    return render(request, "category.html", context)


def search(request):
    search_term = request.GET["search"]
    url = f"https://newsapi.org/v2/everything?q={search_term}&apiKey=087471d0792a4529937f70973381d41c"
    data = requests.get(url)
    response = data.json()
    articles = response["articles"]
    context = {"articles": articles, "search": search_term}
    return render(request, "search.html", context)

def home(request):
    return render(request, "index.html")