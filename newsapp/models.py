from django.db import models

# Create your models here.
class techCrunchHeadline(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class wallStreetJournalHeadline(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    desc = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.title

class theVergeHeadline(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class lastUpdated(models.Model):
    minutes = models.IntegerField()
    def __str__(self):
        return int(self.minutes)

class businessInsiderHeadline(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class seekingAlphaHeadline(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class wiredHeadline(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title