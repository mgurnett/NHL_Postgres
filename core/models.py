from django.db import models

class Conference(models.Model):
    name = models.CharField(max_length = 100)
    nhl_id = models.IntegerField ()
    
    class Meta:
        ordering = ['name']

    def __str__ (self):
        return self.name
        
class Division(models.Model):
    name = models.CharField(max_length = 100)
    nhl_id = models.IntegerField ()
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    nameshort = models.CharField(max_length = 10)
    abbreviation = models.CharField(max_length = 1)
    
    class Meta:
        ordering = ['name']

    def __str__ (self):
        return f"{self.name} that is in the {self.conference.name} conference"
        
class Team(models.Model):
    name = models.CharField(max_length = 100)
    nhl_id = models.IntegerField ()
    venue = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    locationName = models.CharField(max_length = 100)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    teamName = models.CharField(max_length = 50)
    abbreviation = models.CharField(max_length = 20)
    officialSiteUrl = models.URLField(max_length=200)

    class Meta:
        ordering = ['division', 'name']

    def __str__ (self):
        return f"{self.name} that is in the {self.division.name} division"
    
