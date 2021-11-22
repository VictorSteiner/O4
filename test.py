import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
from player import CSV, read_data, find, PlayerIndex, get

data = read_data(f"./data/{CSV.FIFA20.value}")

clubs = sorted(list(dict.fromkeys(get(data, PlayerIndex.club.value))))
list = []

for club in clubs:
    players = find(data, PlayerIndex.club.value, club)
    values = sum([player[PlayerIndex.wage_eur.value] for player in players])
    list.append(values)
