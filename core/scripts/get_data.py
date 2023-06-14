from core.models import *
from .read_api import *

SEASON = 20222023
OILERS = 22

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
    team_list = []
    if kwargs['database']:
        Team.objects.all().delete()
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
        team_list.append(t)
        if kwargs['database']:
            t.save()
        if kwargs['is_print']:
            print (t)
    return team_list

def load_player_vitals (player, **kwargs):  # set to True if you wnat it to effect the database
    if kwargs['database']:
        Player_vitals.objects.get(id = player.id)

    record = read_api (f'people/{player.nhl_id}', print_url = False).get ('people')[0]

    v = Player_vitals (
        player = Player.objects.get(id = player.id),
        firstName = record ['firstName'],
        lastName = record ['lastName'],
        birthDate = record ['birthDate'],
        birthCity = record ['birthCity'],
        birthCountry = record ['birthCountry'],
        nationality = record ['nationality'],
        height = record ['height'],
        weight = record ['weight'],
        active = record ['active'],
        alternateCaptain = record ['alternateCaptain'],
        captain = record ['captain'],
        rookie = record ['rookie'],
        shootsCatches = record ['shootsCatches'],
        rosterStatus = record ['rosterStatus'],
    )
    if kwargs['database']:
        v.save()
    if kwargs['is_print']:
        print (v)
    return


def load_roster (team, **kwargs):  # set to True if you wnat it to effect the database
    if kwargs['database']:
        Player.objects.all().delete()
    data = read_api (f'teams/{team}?expand=team.roster&season={SEASON}')
    # print (data)
    for record in data ['teams'][0]['roster'].get('roster'):
        player_id = record.get('person')['id']
        try:
            jn = record['jerseyNumber']
        except:
            jn = 0
        r = Player (
            fullName = record.get('person')['fullName'],
            nhl_id = player_id,
            team = Team.objects.get(nhl_id = team),
            jerseyNumber = jn,
            position_name = record['position']['name'],
            position_type = record['position']['type'],
            position_ab = record['position']['abbreviation'],
        )
        if kwargs['database']:
            r.save()
        if kwargs['is_print']:
            print (r)
    return

def run():
    # load_divisions ( database = False, is_print = True)
    team_list = load_teams ( database = False, is_print = False)
    load_roster ( OILERS, database = False, is_print = False)


    players = Player.objects.all()
    for player in players:
        # print (f'{player} - {player.nhl_id} {type(player)}')
        load_player_vitals ( player, database = False, is_print = True)
        