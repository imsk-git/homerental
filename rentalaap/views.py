from django.shortcuts import render, HttpResponse, redirect
from .models import Property
from django.contrib.auth.models import User
from .forms import PropertyForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    try:
        properties = Property.objects.filter(user = request.user)
    except:
        properties = []
    context = {
        'properties':properties
    }
    return render(request,'home.html',context)


@login_required(login_url="login")
def create(request):
    form = PropertyForm()
    if request.method == 'POST':
        print(request.POST)
        form = PropertyForm(request.POST,request.FILES)
        if form.is_valid():
            property = form.save(commit = False)
            if request.user.is_authenticated:
                property.user = request.user
                form.save()
                return redirect('home')
            else:
                return HttpResponse("You must be logged in to create a property.")
    context = {
        'form' :form
    }
    return render (request,'create.html',context)

@login_required(login_url="login")
def update(request,id):
    property = Property.objects.get(id=id)
    if property.user != request.user:
        return redirect('home')
    form = PropertyForm (instance = property)
    if request.method == 'POST':
        print (request.POST)
        form = PropertyForm(request.POST, instance = property)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form' : form
    }
    return render(request,'create.html',context)

def delete(request,id):
    property = Property.objects.get(id=id)
    property.delete()


def detailView(request,id):
    try:
        property = Property.objects.get(id = id)
        context = {
            'property' : property
        }
        return render(request, 'details.html',context)
    except:
        return redirect('/home')


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        User.objects.create_user(username = username,
                                password = password,
                                email = email)
        
#         a = request.POST.get('username')
#         b = request.POST.get('password')
#         c = request.POST.get('email')
#         User.objects.create_user(username = a,
#                                 password = b,
#                                 email = c)
        return redirect('home')

    return render(request,'register.html')

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,
                          password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,'login.html')

def logoutPage(request):
    logout(request)
    return redirect('home')

def book(request,id):
    return render(request,'book.html',{})