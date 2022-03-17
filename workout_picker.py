import pandas as pd

df = pd.read_csv('exercises.csv')

lower_df = df[df.upper_lower=='lower']
lower_pick = lower_df.sample(weights = lower_df.freq)

upper_df = df[df.upper_lower=='upper']

if int(lower_pick['grip']) == 1:
    upper_df = upper_df[upper_df.grip == 0]

upper_pick = upper_df.sample(weights = upper_df.freq)

print("Today's workout will consist of the following:")
print(str(lower_pick.exercise.iloc[0]))
print(str(upper_pick.exercise.iloc[0]))