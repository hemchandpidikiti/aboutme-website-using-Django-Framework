from django.db import models

# Create your models here.
class Project(models.Model):
    images=models.ImageField(upload_to='images/')
    summary=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    def __str__(self):
        return self.summary
class Skill(models.Model):
    skill_name=models.CharField(max_length=100)
    def __str__(self):
        return self.skill_name
