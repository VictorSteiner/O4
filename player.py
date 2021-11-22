import pandas as pd
from enum import Enum


def read_data(csv: str) -> list:
    return pd.read_csv(csv).values.tolist()


def get(list: list, index: int):
    return [item[index] for item in list]


def find(list: list, index: int, expression):
    out: list = []

    for item in list:
        if item[index] == expression:
            out.append(item)

    return out


class PlayerIndex(Enum):
    sofifa_id = 0
    player_url = 1
    short_name = 2
    long_name = 3
    age = 4
    dob = 5
    height_cm = 6
    weight_kg = 7
    nationality = 8
    club = 9
    overall = 10
    potential = 11
    value_eur = 12
    wage_eur = 13
    player_positions = 14
    preferred_foot = 15
    international_reputation = 16
    weak_foot = 17
    skill_moves = 18
    work_rate = 19
    body_type = 20
    real_face = 21
    release_clause_eur = 22
    player_tags = 23
    team_position = 24
    team_jersey_number = 25
    loaned_from = 26
    joined = 27
    contract_valid_until = 28


class CSV(Enum):
    FIFA15 = "players_15.csv"
    FIFA16 = "players_16.csv"
    FIFA17 = "players_17.csv"
    FIFA18 = "players_18.csv"
    FIFA19 = "players_19.csv"
    FIFA20 = "players_20.csv"
