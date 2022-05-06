import pandas as pd
import random as rd

def pick(df):
    pick = df.sample(weights = df.freq)
    pick_str = str(pick.exercise.iloc[0])
    return pick_str

df = pd.read_csv('exercises.csv')

workout_type = input('Enter workout type (primary/secondary):')

df = df[df.primacy == workout_type]

if workout_type == 'primary':
    lower_df = df[df.upper_lower=='lower']

    #Get list of all types
    lower_types = lower_df.type.unique().tolist()

    #Pick on type at random
    lower_type = rd.choice(lower_types)
    print(lower_type)

    #filter dataframe for exercises of this type only
    lower_df = lower_df[lower_df.type == lower_type]

    #Pick exercise of this type at random given freq weights
    lower_pick = pick(lower_df)

    upper_df = df[df.upper_lower=='upper']

    #If this exercise taxes the grip, make sure not to choose an upper that taxes the grip as well
    upper_type = 'push' if lower_type == 'pull' else 'pull'
    print(upper_type)

    #filter dataframe for exercises of this types only
    upper_df = upper_df[upper_df.type == upper_type]

    #Get list of directions
    upper_dirs = upper_df.direction.unique().tolist()

    #Pick direction at random
    upper_dir = rd.choice(upper_dirs)
    print(upper_dir)

    #filter upper dataframe for exercises of this types only
    upper_df = upper_df[upper_df.direction == upper_dir]

    upper_pick = pick(upper_df)

    workout = (lower_pick, upper_pick)

else:

    secondary_pick = pick(df)

    workout = secondary_pick

print("Today's workout will consist of: {}".format(workout))