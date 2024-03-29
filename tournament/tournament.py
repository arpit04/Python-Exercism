points = {'win': 3, 'draw': 1, 'loss': 0}
tableformat = '{:<31}|{:>3} |{:>3} |{:>3} |{:>3} |{:>3}'


def tally(data):
    scores = {}
    for data in datas:
        for match_result in filter(None, data.split('\n')):
            team1, team2, result = match_result.split(';')
            for team in team1, team2:
                if team not in scores:
                    scores[team] = {'matches_played': 0,
                                    'win': 0,
                                    'draw': 0,
                                    'loss': 0,
                                    'points': 0}

            if result == 'win':
                scores[team1]['win'] += 1
                scores[team2]['loss'] += 1
            elif result == 'draw':
                scores[team1]['draw'] += 1
                scores[team2]['draw'] += 1
            elif result == 'loss':
                scores[team1]['loss'] += 1
                scores[team2]['win'] += 1

            for team in team1, team2:
                scores[team]['matches_played'] += 1
                scores[team]['points'] = scores[team]['win'] * points['win'] + scores[team]['draw'] * points['draw']

        sorted_teams = sorted(sorted(scores), key=lambda x: -scores[x]['points'])
        header = [tableformat.format('Team', 'MP', 'W', 'D', 'L', 'P')]
        table = [tableformat.format(team,
                                    scores[team]['matches_played'],
                                    scores[team]['win'],
                                    scores[team]['draw'],
                                    scores[team]['loss'],
                                    scores[team]['points']) for team in sorted_teams]
    return '\n'.join(header + table)

datas = ['Allegoric Alaskans;Blithering Badgers;win','Devastating Donkeys;Courageous Californians;draw','Devastating Donkeys;Allegoric Alaskans;win'
         ,'Courageous Californians;Blithering Badgers;loss','Blithering Badgers;Devastating Donkeys;loss','Allegoric Alaskans;Courageous Californians;win'
         ,'mumbai indians;chennai super king;loss']


print(tally(datas))