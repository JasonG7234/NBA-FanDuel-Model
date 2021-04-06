class NBAGame:


    team_id_mapper = {'Atlanta Hawks': 1610612737, 'Boston Celtics': 1610612738, 'Cleveland Cavaliers': 1610612739, 'New Orleans Pelicans': 1610612740, 'Chicago Bulls': 1610612741,
                  'Dallas Mavericks': 1610612742, 'Denver Nuggets': 1610612743, 'Golden State Warriors': 1610612744, 'Houston Rockets': 1610612745, 'Los Angeles Clippers': 1610612746,
                  'Los Angeles Lakers': 1610612747, 'Miami Heat': 1610612748, 'Milwaukee Bucks': 1610612749, 'Minnesota Timberwolves': 1610612750, 'Brooklyn Nets': 1610612751,
                  'New York Knicks': 1610612752, 'Orlando Magic': 1610612753, 'Indiana Pacers': 1610612754, 'Philadelphia 76ers': 1610612755, 'Phoenix Suns': 1610612756,
                  'Portland Trail Blazers': 1610612757, 'Sacramento Kings': 1610612758, 'San Antonio Spurs': 1610612759, 'Oklahoma City Thunder': 1610612760, 'Toronto Raptors': 1610612761,
                  'Utah Jazz': 1610612762, 'Memphis Grizzlies': 1610612763, 'Washington Wizards': 1610612764, 'Detroit Pistons': 1610612765, 'Charlotte Hornets': 1610612766}


    def __init__(self, home_team="HOME", away_team="AWAY", home_spread=None, #
    away_spread=None, home_moneyline="0", away_moneyline="0", #
    over=None, under=None):
        self.home_team = home_team
        self.away_team = away_team
        self.home_spread = home_spread
        self.away_spread = away_spread
        self.home_moneyline = home_moneyline
        self.away_moneyline = away_moneyline
        self.over = over
        self.under = under

    def set_home_team(self, home_team):
        self.home_team = home_team

    def get_home_team(self):
        return self.home_team
    
    def get_home_team_id(self):
        return team_id_mapper[self.home_team]

    def set_away_team(self, away_team):
        self.away_team = away_team

    def get_away_team(self):
        return self.away_team

    def get_away_team_id(self):
        return team_id_mapper[self.away_team]

    def set_home_spread(self, spread, odds):
        self.home_spread = [spread, odds]

    def get_home_spread(self):
        return self.home_spread
    
    def get_home_spread_handicap(self):
        return self.home_spread[0]

    def get_home_spread_odds(self):
        return self.home_spread[1]

    def set_away_spread(self, spread, odds):
        self.away_spread = [spread, odds]

    def get_away_spread(self):
        return self.away_spread

    def get_away_spread_handicap(self):
        return self.away_spread[0]

    def get_away_spread_odds(self):
        return self.away_spread[1]

    def set_home_moneyline(self, moneyline):
        self.home_moneyline = moneyline

    def get_home_moneyline(self):
        return self.home_moneyline

    def set_away_moneyline(self, moneyline):
        self.away_moneyline = moneyline

    def get_away_moneyline(self):
        return self.away_moneyline

    def set_over(self, total, odds):
        self.over = [total, odds]

    def get_over(self):
        return self.over
    
    def get_over_total(self):
        return self.over[0]

    def get_over_odds(self):
        return self.over[1]

    def set_under(self, total, odds):
        self.under = [total, odds]

    def get_under(self):
        return self.under

    def get_under_total(self):
        return self.under[0]

    def get_under_odds(self):
        return self.under[1]