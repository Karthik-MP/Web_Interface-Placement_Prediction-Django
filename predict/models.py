from django.db import models

class education(models.Model):
    Gender=models.CharField(max_length=30)
    Age=models.CharField(max_length=30)
    HistoryOfBacklogs=models.CharField(max_length=30)
    Certification=models.CharField(max_length=30)
    CGPA=models.CharField(max_length=30)
    Stream=models.CharField(max_length=30)
    Internships=models.CharField(max_length=30)
    