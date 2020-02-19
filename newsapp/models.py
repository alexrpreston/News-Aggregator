from django.db import models

# Create your models here.
class techCrunchHeadline(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    desc = models.TextField()

    def __str__(self):
        return self.title

class wallStreetJournalHeadline(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    desc = models.TextField()
    

    def __str__(self):
        return self.title

class theVergeHeadline(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    desc = models.TextField()

    def __str__(self):
        return self.title



class lastUpdated(models.Model):
    minutes = models.CharField(max_length=60)
    def __str__(self):
        return self.minutes