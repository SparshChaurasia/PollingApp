from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Candidate

@login_required(login_url="/login")
def index(request):
    candidates = Candidate.objects.all()
    head_boy = candidates.filter(Post="head_boy")
    head_girl = candidates.filter(Post="head_girl")
    activity_captain = candidates.filter(Post="activity_captain")
    sports_captain = candidates.filter(Post="sports_captain")

    data = {
        "head_boy": head_boy, 
        "head_girl": head_girl, 
        "activity_captain": activity_captain,
        "sports_captain": sports_captain,
    }

    return render(request, "form.html", data)