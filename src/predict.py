"""Deliberately broken: this file should be at the top of the repo."""

import pandas as pd

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
guess = train["hours_spent"].mean()
pd.DataFrame({"project_id": test["project_id"], "hours_spent": guess}).to_csv("predictions.csv", index=False)
