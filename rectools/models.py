from django.db import models


class Skills(models.Model):
    skill_name = models.CharField(max_length=255)

    def __str__(self):
        return self.skill_name


class Candidate(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    bio = models.CharField(max_length=255)
    skills = models.ManyToManyField(Skills)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Recruiter(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.PROTECT)
    free_slots = models.IntegerField(default=5)
    experience = models.IntegerField(default=1)


class Job(models.Model):
    skills = models.ManyToManyField(Skills)
    jod_name = models.CharField(max_length=255)


class Interview(models.Model):
    jod = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
