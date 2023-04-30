import random
import sqlite3

countries = ['Азербайджан',
             'Словакия',
             'Германия',
             'Словения',
             'Англия',
             'Швеция',
             'Дания',
             'Россия',
             'Сербия',
             'Швейцария',
             'Норвегия',
             'Беларусь',
             'Армения'
             ]

team_levels = ['Слабая', 'Средняя', 'Сильная']

insert_team_sql = "INSERT INTO uefa_commands (command_number, command_name, command_country, command_level) VALUES (?, ?, ?, ?)"

insert_draw_sql = "INSERT INTO uefa_draw (command_number, group_number) VALUES (?, ?)"


def get_team_level_by_id(id: int):
    mod = id % 4
    if mod == 0:
        return "Слабая"
    if mod == 3:
        return "Сильная"
    return "Средняя"


def get_teams(groups_count):
    teams = []
    for i in range(groups_count * 4):
        name = f'Команда № {i + 1}'
        country = random.choice(countries)
        level = get_team_level_by_id(i)
        teams.append((i + 1, name, level, country))
    return teams


def get_team_groups(teams):
    groups = []
    teams_by_levels = dict()
    for level in team_levels:
        teams_by_levels[level] = [x for x in teams if x[2] == level]
    for i in range(groups_count):
        group = []
        team = random.choice(teams_by_levels['Слабая'])
        group.append(team)
        teams_by_levels['Слабая'].remove(team)
        for i in range(2):
            team = random.choice(teams_by_levels['Средняя'])
            group.append(team)
            teams_by_levels['Средняя'].remove(team)
        team = random.choice(teams_by_levels['Сильная'])
        group.append(team)
        teams_by_levels['Сильная'].remove(team)
        groups.append(group)
    return groups


def fill_team_data(cur, groups_count):
    cur.execute("DELETE FROM uefa_commands")
    cur.execute("DELETE FROM uefa_draw")
    teams = get_teams(groups_count)
    random.shuffle(teams)
    cur.executemany(insert_team_sql, teams)
    groups = get_team_groups(teams)
    draw = [(team[0], i + 1) for i, group in enumerate(groups) for team in group]
    cur.executemany(insert_draw_sql, draw)


def main():
    with sqlite3.connect("hw.db") as con:
        cur = con.cursor()
        groups_count = int(input('Количество групп в пределах от 4 до 16: '))
        fill_team_data(cur, groups_count)


if __name__ == "__main__":
    main()