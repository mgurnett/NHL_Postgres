from core.models import *
from .read_api import *

def load_divisions (**kwargs):  # set to True if you wnat it to effect the database
    if kwargs['database']:
        Division.objects.all().delete()
    data = read_api ('divisions')
    # print (data)
    for record in data ['divisions']:
        d = Division (
            name = record['name'],
            nhl_id = record['id'],
            conference = Conference.objects.get(name = record['conference'].get('name')),
            nameshort = record['nameShort'],
            abbreviation = record['abbreviation'],
        )
        if kwargs['database']:
            d.save()
        if kwargs['is_print']:
            print (d)
    return

def load_teams (**kwargs):  # set to True if you wnat it to effect the database
    # if kwargs['database']:
    #     Division.objects.all().delete()
    data = read_api ('teams')
    # print (data)
    for record in data ['teams']:
        # print (record)
        t = Team (
            name = record['name'],
            nhl_id = record['id'],
            division = Division.objects.get(name = record['division'].get('name')),
            teamName = record['teamName'],
            abbreviation = record['abbreviation'],
            venue = record['venue'].get('name'),
            city = record['venue'].get('city'),
            locationName = record['locationName'],
            officialSiteUrl = record['officialSiteUrl'],
        )
        if kwargs['database']:
            t.save()
        if kwargs['is_print']:
            print (t)
    return

def run():
    # load_divisions ( database = False, is_print = True)
    load_teams ( database = False, is_print = True)

    fullName = models.CharField(max_length = 100)
    nhl_id = models.IntegerField ()
    jerseyNumber = models.IntegerField ()
    city = models.CharField(max_length = 100)
    position_name = models.CharField(max_length = 100)
    position_type = models.CharField(max_length = 100)
    position_ab = models.CharField(max_length = 100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)