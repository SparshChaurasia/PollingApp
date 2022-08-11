from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import F
from .models import Candidate, Posts, Student

@login_required(login_url="/login")
def index(request):
    candidates = Candidate.objects.all()
    head_boy = candidates.filter(Post="head_boy")
    head_girl = candidates.filter(Post="head_girl")
    activity_captain = candidates.filter(Post="activity_captain")
    sports_captain = candidates.filter(Post="sports_captain")
    # posts = Posts.choices

    posts = [
        (head_boy, "Head Boy", "head_boy"), 
        (head_girl, "Head Girl", "head_girl"), 
        (activity_captain, "Activity Captain", "activity_captain"), 
        (sports_captain, "Sports Captain", "sports_captain")
    ]

    return render(request, "form.html", {"posts": posts})

def submit(request):
    if request.method != "POST":
        return HttpResponse("bad request method")

    student_class = request.POST.get("class")
    student_roll = request.POST.get("roll")
    student_id = request.POST.get("id")
    student_name = request.POST.get("name")

    head_boy_id = int(request.POST.get("head_boy"))
    head_girl_id = int(request.POST.get("head_girl"))
    activity_captain_id = int(request.POST.get("activity_captain"))
    sports_captain_id = int(request.POST.get("sports_captain"))

    if not all((student_class, student_roll, student_id, student_name)):
        return HttpResponse("please fill all the required fields")

    student = Student(StudentName=student_name, StudentId=student_id, Roll=student_roll, StudentClass=student_class)
    student.save()

    candidates = Candidate.objects.all()
    
    head_boy_candidate = candidates.filter(CandidateId=head_boy_id).first() 
    head_boy_candidate.vote()
    head_boy_candidate.save()
    
    head_girl_candidate = candidates.filter(CandidateId=head_girl_id).first() 
    head_boy_candidate.vote()
    head_girl_candidate.save()
    
    activity_captain_candidate = candidates.filter(CandidateId=activity_captain_id).first() 
    activity_captain_candidate.vote()
    activity_captain_candidate.save()
    
    sports_captain_candidate = candidates.filter(CandidateId=sports_captain_id).first() 
    sports_captain_candidate.vote()
    sports_captain_candidate.save()

    return redirect("/vote")
    