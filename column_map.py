import pandas as pd

# We just want pitching data
df_pitch_post = pd.read_csv("pitchingpost.csv")
df_pit = pd.read_csv("pitching.csv")
df_pitch = pd.concat([df_pitch_post, df_pit], ignore_index=True)

# We can't add averages, so we will recompute with the data in the csv's

df_pitch = df_pitch.drop(columns=["era"]) 

# like before we want to the sum here based on player and year

df_pitch = df_pitch.groupby(['player_id', 'year_id']).sum(numeric_only = True)

in_pitched = df_pitch['outs_pitched'] / 3 # Converting outs to innings for ERA calculation
df_pitch['ERA'] = (df_pitch['earned_runs'] / in_pitched) *9 # ERA uses 9 innings (whole game)
df_pitch = df_pitch.reset_index()
df_pitch = df_pitch.round(2)

# we want to calculate age like we did before two

df_bios = pd.read_csv("people.csv")
df_bios = df_bios[['player_id', 'birth_year','name_given', 'weight', 'height', 'throws']]
df_pitch = pd.merge(df_pitch, df_bios, on='player_id')
df_pitch['Age'] = df_pitch['year_id'] - df_pitch['birth_year'] 
print(df_pitch.shape)

# clean up some things

# Less than 100 missing era's and birth years
df_pitch = df_pitch.dropna(subset=['ERA'])
df_pitch = df_pitch.dropna(subset=['birth_year'])
# about 380 missing height and weights. I have 40,000 + samples so I think it safe to discard them
df_pitch = df_pitch.dropna(subset=['height'])
df_pitch = df_pitch.dropna(subset=['weight'])
df_pitch = df_pitch.dropna(subset=['throws'])

# I want to keep the left right both throwing arm distinction
# But it is not numeric so we will encode it
df_throw_dum = pd.get_dummies(df_pitch['throws'], prefix='throws')
df_pitch = pd.concat([df_pitch, df_throw_dum], axis = 1)
print(df_pitch.isna().sum())