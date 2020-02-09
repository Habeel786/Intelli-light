from django.shortcuts import render
from django.http import HttpRequest
from .models import Ask

def index(request):
    butt = request.GET.get("button", "off")
    stmt= Ask.objects.all()
    n= len(stmt)
    params = {"number_of_query": n, "statements": stmt, "range": range(1, n)}
    if not butt == "off":
        name = request.GET.get("name")
        email = request.GET.get("email")
        query = request.GET.get("query")
        print(name)
        print(email)
        print(query)
        ask=Ask()
        ask.name=name
        ask.email=email
        ask.query=query
        ask.save()
        params = {"number_of_query": n, "statements": stmt, "range": range(1, n)}
        return render(request, 'smart/index.html', params)
    else:
        return render(request, "smart/index.html",params)



