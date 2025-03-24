from django.shortcuts import render


def auth_forms(request):
    return render(request, "auth_forms.html")
    
def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "signup.html")  

def course(request):
    return render(request, "course.html")

def certificate(request):
    return render(request, "certificate.html")

def help_page(request):
    return render(request, "help.html")

def employerdashboard(request):
    return render(request, "employerdashboard.html")

def userdashboard(request):
    return render(request, "userdashboard.html")

def AI_course(request):
    return render(request, "AI_course.html")

def ngo(request):  # Fix indentation
    return render(request, "ngo.html")

def jobposting(request):
    return render(request, "jobposting.html")

def joblisting(request):
    return render(request, "joblisting.html")  # Removed duplicate

def payment(request):
    return render(request, "payment.html")  # Removed duplicate
