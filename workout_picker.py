import pandas as pd
import random as rd

def pick(df):
    pick = df.sample(weights = df.freq)
    pick_str = str(pick.exercise.iloc[0])
    return pick_str

df = pd.read_csv('exercises.csv')

primacy = int(input('Enter workout type (1/2):'))

df = df[df.primacy == primacy]

if primacy == 1:

    lower_df = df[df.upper==0]

    #Decide on push/pull
    lower_push = round(rd.random())

    #Filter on push/pull
    lower_df = lower_df[lower_df.push == lower_push]

    #Pick exercise of this type at random given freq weights
    lower_pick = pick(lower_df)

    upper_df = df[df.upper==1]

    #If the lower body is push, do pull for upper body, and visa versa. This is to spare the grip.
    upper_push = 1 if lower_push == 0 else 0

    #Filter on push/pull
    upper_df = upper_df[upper_df.push == upper_push]

    #Decide on vertical/horizontal
    upper_vert = round(rd.random())

    #Filter on vertical/horizontal
    upper_df = upper_df[upper_df.vertical == upper_vert]

    #Pick exercise of this type at random given freq weights
    upper_pick = pick(upper_df)

    workout = (lower_pick, upper_pick)

else:

    secondary_pick = pick(df)
    workout = secondary_pick

print("Today's workout will consist of: {}".format(workout))