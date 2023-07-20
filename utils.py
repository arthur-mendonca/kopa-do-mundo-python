from ast import arg
from exceptions import validate_title, check_cup_year, validate_titles
from datetime import datetime


def data_processing(team_info=arg):
    name = team_info.get("name")
    titles = team_info.get("titles")
    top_scorer = team_info.get("top_scorer")
    fifa_code = team_info.get("fifa_code")
    first_cup_str = team_info.get("first_cup")

    if first_cup_str is not None:
        first_cup = datetime.strptime(first_cup_str, "%Y-%m-%d").date()
        first_cup_year = first_cup.year
        check_cup_year(first_cup_year)

        now = datetime.now()
        disputed_cups = (now.year - first_cup_year) / 4

        validate_titles(titles, disputed_cups)

        validate_title(titles)

    # return f"Team name: {name}, titles: {titles}, top scorer: {top_scorer}, fifa code: {fifa_code}, first cup: {first_cup}"


# print(data_processing(name="Brazil", titles=522,
#       top_scorer="Ronaldo", fifa_code="BRA", first_cup=1930))
