from django.shortcuts import render, redirect
from .forms import CreateUserForm


def home(request):
    context ={}
    return render(request, "SocialPart/home.html")


def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm( request.POST )
        if form.is_valid():
            user = form.save()
            return redirect('login')

    context = {"form": form, }
    return render(request, "SocialPart/register_page.html", context)


def login(request):
    context = {}
    return render( request, "SocialPart/login_page.html", context )
