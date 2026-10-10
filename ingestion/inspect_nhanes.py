import pandas as pd

df = pd.read_sas("raw/DEMO_L.xpt")

print(df.shape)
print(df.columns)
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df["RIAGENDR"].unique())
print(df["RIAGENDR"].value_counts())

df["gender"] = df["RIAGENDR"].map({
    1: "Male",
    2: "Female"
})

print(df[["RIAGENDR", "gender"]].head())
print(df["gender"].isnull().sum())
print(df["RIDAGEYR"].min())
print(df["RIDAGEYR"].max())
print(df["RIDAGEYR"].sort_values().head(10))
print(df.loc[df["RIDAGEYR"] < 1, ["SEQN", "RIDAGEYR", "RIDAGEMN"]].head(10))
print((df["RIDAGEYR"] < 1).sum())
print(df.loc[df["RIDAGEYR"] < 1, "RIDAGEMN"].notna().sum())
print(df["RIDAGEYR"].value_counts().sort_index().tail(10))

def get_age_group(age):
    if age < 18:
        return "0-17"
    elif age < 40:
        return "18-39"
    elif age < 60:
        return "40-59"
    elif age < 80:
        return "60-79"
    else:
        return "80+"
    
df["age_group"] = df["RIDAGEYR"].apply(get_age_group)
print(df[["RIDAGEYR", "age_group"]].head(10))


print(df["age_group"].value_counts().sort_index())
print(df["INDFMPIR"].head())

print(df["INDFMPIR"].isnull().sum())

print(df["INDFMPIR"].min())

print(df["INDFMPIR"].max())

print(df.groupby("age_group")["INDFMPIR"].mean())

result = df.groupby("age_group")["INDFMPIR"].mean()
result = result.reset_index()
print(result)

result = result.rename(columns={
    "INDFMPIR": "avg_income_poverty_ratio"
})

print(result)

result.to_parquet(
    "gold/avg_income_poverty_by_age.parquet",
    index=False
)

check = pd.read_parquet(
    "gold/avg_income_poverty_by_age.parquet"
)

print(check)
print(check.info())


