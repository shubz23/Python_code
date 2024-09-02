import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load the dataset
cricket_players = pd.read_csv('cricket_players.csv')

# Split the dataset into features and labels
X = cricket_players[['Age', 'Fitness Level', 'Recent Batting Average', 'Recent Bowling Average', 'Injury Status']]
y = cricket_players['Role']

# Train a decision tree algorithm on the dataset
clf = DecisionTreeClassifier()
clf.fit(X, y)

# Take input from the user for player details
age = int(input("Enter player's age: "))
fitness = float(input("Enter player's fitness level (out of 10): "))
batting_avg = float(input("Enter player's recent batting average: "))
bowling_avg = float(input("Enter player's recent bowling average: "))
injury_status = input("Is the player injured (Yes/No): ").lower()

# Predict whether the player is fit or unfit
if fitness < 6 or injury_status == 'yes':
    print("The player is unfit for selection")
else:
    print("The player is fit for selection")

    # Predict the player's role in the team
    player = [[age, fitness, batting_avg, bowling_avg, 0 if injury_status == 'no' else 1]]
    role = clf.predict(player)
    print("The player's predicted role is:", role[0])
