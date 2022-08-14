from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.vote.models import Student

@login_required(login_url="/login")
def index(request):
    if request.method != "POST":
        return render(request, "dashboard.html")
    
    s_class = request.POST.get("class")
    students = Student.objects.filter(StudentClass=s_class)

    data = {f"student{i}":{"name":s.StudentName, "roll":s.Roll, "status":s.Voted} for i, s in enumerate(students)}

    return render(request, "dashboard.html", {"class": data})

# def status(request):
#     s_class = request.GET.get("class")
#     students = Student.objects.filter(StudentClass=s_class)
#     print(students)
#     return redirect("/", students=students) 