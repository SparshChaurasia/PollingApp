from django.shortcuts import render
from apps.vote.models import Candidate

def index(request):
    candidates = Candidate.objects.all()

    head_boy = candidates.filter(Post="head_boy").order_by("-Votes")
    head_boy_winner = head_boy.first()

    head_girl = candidates.filter(Post="head_girl").order_by("-Votes")
    head_girl_winner = head_girl.first()

    activity_captain = candidates.filter(Post="activity_captain").order_by("-Votes")
    activity_captain_winner = activity_captain.first()

    sports_captain = candidates.filter(Post="sports_captain").order_by("-Votes")
    sports_captain_winner = sports_captain.first()

    data = {
        "head_boy":{"name":"Head Boy", "candidates":head_boy, "winner":head_boy_winner}, 
        "head_girl":{"name":"Head Girl", "candidates":head_girl, "winner":head_girl_winner}, 
        "activity_captain":{"name":"Activity Captain", "candidates":activity_captain, "winner":activity_captain_winner}, 
        "sports_captain":{"name":"Sports Captain", "candidates":sports_captain, "winner":sports_captain_winner}
    }

    return render(request, "results.html", {"data":data})