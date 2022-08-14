# Generated by Django 4.0.5 on 2022-08-10 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_alter_candidate_candidatename_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='CandidateName',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='Post',
            field=models.CharField(choices=[('head_boy', 'Head Boy'), ('head_girl', 'Head Girl'), ('sports_captain', 'Sports Captain'), ('activity_captain', 'Activity Captain')], max_length=16),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='Votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='StudentId',
            field=models.CharField(max_length=7, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='student',
            name='StudentName',
            field=models.CharField(max_length=255),
        ),
    ]