from django.db import models


class Classes(models.TextChoices):
    _9A = "9A"
    _9B = "9B"
    _10A = "10A"
    _10B = "10B"
    _11A = "11A"
    _11B = "11B"
    _11C = "11C"
    _12A = "12A"
    _12B = "12B"

class Posts(models.TextChoices):
    head_boy = "head_boy"
    head_girl = "head_girl"
    sports_captain = "sports_captain"
    activity_captain = "activity_captain"

class Student(models.Model):
    StudentName = models.CharField(max_length=100)
    StudentId = models.CharField(max_length=100)
    StudentClass = models.CharField(max_length=3, choices=Classes.choices)
    Roll = models.IntegerField()
    Voted = models.BooleanField(default=False)

    def __str__(self):
        return self.StudentName
    

class Candidate(models.Model):
    CandidateName = models.CharField(max_length=100)
    CandidateId = models.AutoField(primary_key=True)
    CandidateClass = models.CharField(max_length=3, choices=Classes.choices)
    Post = models.TextField(choices=Posts.choices)
    Votes = models.IntegerField()

    def __str__(self):
        return self.CandidateName
    

