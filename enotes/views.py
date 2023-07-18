from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, logout, login


# Create your views here.

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def register(request):
    error = ""
    if request.method == 'POST':
        fn = request.POST['firstName']
        ln = request.POST['lastName']
        e = request.POST['email']
        p = request.POST['password']
        c = request.POST['ContactNo']
        ab = request.POST['About']
        role = "ROLE_USER"

        try:
            user = User.objects.create_user(username=e, password=p, first_name=fn, last_name=ln)
            Signup.objects.create(user=user, ContactNo=c, About=ab, Role=role)
            error = "no"
        except:
            error = "yes"
    return render(request, 'register.html', locals())

def user_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['email']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'user_login.html', locals())

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = User.objects.get(id=request.user.id)
    signup = Signup.objects.get(user=user)
    totalnotes = Notes.objects.filter(signup=signup).count()
    totalpasswords = Passwords.objects.filter(signup=signup).count()
    return render(request, 'dashboard.html', locals())

def profile(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = User.objects.get(id=request.user.id)
    signup = Signup.objects.get(user=user)

    if request.method == "POST":

        fname = request.POST['firstName']
        lname = request.POST['lastName']
        contactNo = request.POST['ContactNo']
        about = request.POST['About']

        signup.user.first_name = fname
        signup.user.last_name = lname
        signup.ContactNo = contactNo
        signup.About = about

        try:
            signup.save()
            signup.user.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'profile.html', locals())

def addNotes(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = User.objects.get(id=request.user.id)
    signup = Signup.objects.get(user=user)

    error = ""
    if request.method == "POST":
        title = request.POST['Title']
        content = request.POST['Content']

        try:
            Notes.objects.create(signup=signup, Title=title, Content=content)
            error = "no"
        except:
            error = "yes"
    return render(request, 'addNotes.html', locals())

def viewNotes(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = User.objects.get(id=request.user.id)
    signup = Signup.objects.get(user=user)
    notes = Notes.objects.filter(signup=signup)
    return render(request, 'viewNotes.html', locals())

def editNotes(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    notes = Notes.objects.get(id=pid)
    if request.method == "POST":
        title = request.POST['Title']
        content = request.POST['Content']

        notes.Title = title
        notes.Content = content

        try:
            notes.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'editNotes.html', locals())

def deleteNotes(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    notes = Notes.objects.get(id=pid)
    notes.delete()
    return redirect('viewNotes')

def addPasswords(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = User.objects.get(id=request.user.id)
    signup = Signup.objects.get(user=user)

    error = ""
    if request.method == "POST":
        title = request.POST['Title']
        content = request.POST['Content']
        content2 = request.POST['Content2']

        try:
            Passwords.objects.create(signup=signup, Title=title, Content=content,Content2=content2)
            error = "no"
        except:
            error = "yes"
    return render(request, 'addPasswords.html', locals())

def viewPasswords(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    user = User.objects.get(id=request.user.id)
    signup = Signup.objects.get(user=user)
    passwords = Passwords.objects.filter(signup=signup)
    return render(request, 'viewPasswords.html', locals())

def editPasswords(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    passwords= Passwords.objects.get(id=pid)
    if request.method == "POST":
        title = request.POST['Title']
        content = request.POST['Content']
        content2 = request.POST['Content2']

        passwords.Title = title
        passwords.Content = content
        passwords.Content2 = content2

        try:
            passwords.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'editPasswords.html', locals())

def deletePasswords(request,pid):
    if not request.user.is_authenticated:
        return redirect('user_login')
    passwords = Passwords.objects.get(id=pid)
    passwords.delete()
    return redirect('viewPasswords')


def changePassword(request):
    if not request.user.is_authenticated:
        return redirect('user_login')
    error = ""
    user = request.user
    if request.method == "POST":
        o = request.POST['oldpassword']
        n = request.POST['newpassword']
        try:
            u = User.objects.get(id=request.user.id)
            if user.check_password(o):
                u.set_password(n)
                u.save()
                error = "no"
            else:
                error = 'not'
        except:
            error = "yes"
    return render(request, 'changePassword.html', locals())

def Logout(request):
    logout(request)
    return redirect('index')
