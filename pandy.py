import pandas as pd

df = pd.read_csv("train.csv")

avg_age = df["Age"].mean()
print(f"Average Age: {avg_age:.2f}")

survival_avg_age = df[df["Survived"] == 1]["Age"].mean()
print(f"Average Age of Survivors: {survival_avg_age:.2f}")

survival_rate = df.groupby("Pclass")["Survived"].mean() * 100
print("\nSurvival Rate by Class:")
print(survival_rate)

passenger_count = df.groupby("Pclass")["Survived"].count()
print("\nPassenger Count by Class:")
print(passenger_count)

sex_survival = df.groupby("Sex")["Survived"].mean() * 100
print("\nSurvival Rate by Sex:")
print(sex_survival)

survival = df[df["Survived"] == 1]
survival.to_csv("survivors.csv", index=False)

print("\nsurvivors.csv created successfully!")