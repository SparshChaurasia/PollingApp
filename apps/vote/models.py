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
    StudentName = models.CharField(max_length=255)
    StudentId = models.CharField(max_length=7, primary_key=True)
    StudentClass = models.CharField(max_length=3, choices=Classes.choices)
    Roll = models.IntegerField()
    Voted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.StudentName = self.StudentName.lower()
        self.Voted = True
        return super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return self.StudentName
    

class Candidate(models.Model):
    CandidateName = models.CharField(max_length=255)
    CandidateId = models.AutoField(primary_key=True)
    CandidateClass = models.CharField(max_length=3, choices=Classes.choices)
    Post = models.CharField(max_length=16, choices=Posts.choices)
    Votes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.CandidateName = self.CandidateName.lower()
        return super(Candidate, self).save(*args, **kwargs)

    def vote(self):
        self.Votes += 1
        return

    def __str__(self):
        return self.CandidateName
    

