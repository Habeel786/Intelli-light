from django.shortcuts import render
from django.http import HttpRequest
from .models import Ask

def index(request):
    stmt= Ask.objects.all()
    msg="none"
    params = {"statements": stmt, "message":msg}
    if request.method=="POST":
        msg = "query sent successfully"
        name = request.POST.get("name")
        email = request.POST.get("email")
        query = request.POST.get("query")
        print(name)
        print(email)
        print(query)
        ask=Ask()
        ask.name=name
        ask.email=email
        ask.query=query
        ask.save()
        params = {"statements": stmt, "message":msg}
        return render(request, 'smart/index.html', params)
    else:
        return render(request, "smart/index.html",params)



