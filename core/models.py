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
        
class Player(models.Model):
    fullName = models.CharField(max_length = 100)
    nhl_id = models.IntegerField ()
    jerseyNumber = models.IntegerField ()
    position_name = models.CharField(max_length = 100)
    position_type = models.CharField(max_length = 100)
    position_ab = models.CharField(max_length = 100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        ordering = ['jerseyNumber']

    def __str__ (self):
        return f"{self.fullName} of the {self.team.name} is a {self.position_name}"
        
class Player_stats(models.Model):
    player = models.OneToOneField( Player, on_delete=models.CASCADE, primary_key=True, )
    firstName = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)
    birthDate = models.DateField()
    birthCity = models.CharField(max_length = 100)
    birthStateProvince = models.CharField(max_length = 100)
    birthCountry = models.CharField(max_length = 100)
    nationality = models.CharField(max_length = 100)
    height = models.CharField(max_length = 100)
    weight = models.CharField(max_length = 100)
    active = models.BooleanField()
    alternateCaptain = models.BooleanField()
    captain = models.BooleanField()
    rookie = models.BooleanField()
    shootsCatches = models.CharField(max_length = 2)
    rosterStatus = models.CharField(max_length = 100)

    class Meta:
        ordering = ['firstName']

    def __str__ (self):
        return f"{self.firstName} {self.lastName} shoots {self.shootsCatches}"
    
