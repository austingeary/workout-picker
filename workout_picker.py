import pandas as pd
import random as rd

df = pd.read_csv('exercises.csv')

lower_df = df[df.upper_lower=='lower']
upper_df = df[df.upper_lower=='upper']
aux_df = df[df.upper_lower=='aux']

#Get list of all types
lower_types = lower_df.type.unique().tolist()

#Pick on type at random
lower_type_pick = lower_types[round(rd.random()*(len(lower_types)-1))]
print(lower_type_pick)

#filter lower dataframe for exercises of this types only
lower_df = lower_df[lower_df.type == lower_type_pick]

#Pick exercise of this type at random given freq weights
lower_pick = lower_df.sample(weights = lower_df.freq)

#If this exercise taxes the grip, make sure not to choose an upper that taxes the grip as well
if lower_type_pick == 'push':
    upper_df = upper_df[upper_df.type.isin(['horizontal pull','vertical pull'])]
else:
    upper_df = upper_df[upper_df.type.isin(['horizontal push','vertical push'])]

#Get list of all types
upper_types = upper_df.type.unique().tolist()

#Pick on type at random
upper_type_pick = upper_types[round(rd.random()*(len(lower_types)-1))]
print(upper_type_pick)

#filter upper dataframe for exercises of this types only
upper_df = upper_df[upper_df.type == upper_type_pick]

upper_pick = upper_df.sample(weights = upper_df.freq)

aux_pick = aux_df.sample(weights = aux_df.freq)

print("Today's workout will consist of the following:")
if rd.random() <= .2:
    print(str(aux_pick.exercise.iloc[0]))
else:
    print(str(lower_pick.exercise.iloc[0]))
    print(str(upper_pick.exercise.iloc[0]))