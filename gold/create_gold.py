import pandas as pd
from pathlib import Path


def create_gold():

    project_root = Path(__file__).resolve().parents[1]

    silver_file = project_root / "silver" / "nhanes_demographics.parquet"
    gold_folder = project_root / "gold"
    gold_folder.mkdir(exist_ok=True)

    participant_output = (
        gold_folder / "participant_count_by_age_gender.parquet"
    )

    income_output = (
        gold_folder / "avg_income_poverty_by_age.parquet"
    )

    df = pd.read_parquet(silver_file)

    # Gold table 1: participant count by age and gender
    gold = (
        df.groupby(["age_group", "gender"])["participant_id"]
        .count()
        .reset_index()
    )

    gold = gold.rename(
        columns={"participant_id": "participant_count"}
    )

    gold.to_parquet(
        participant_output,
        index=False
    )

    # Gold table 2: average income-poverty ratio by age
    avg_income = (
        df.groupby("age_group")["income_poverty_ratio"]
        .mean()
        .reset_index()
    )

    avg_income = avg_income.rename(
        columns={
            "income_poverty_ratio":
            "avg_income_poverty_ratio"
        }
    )

    avg_income.to_parquet(
        income_output,
        index=False
    )

    print("Gold layer created successfully.")
    print(f"Participant table: {participant_output}")
    print(f"Income table: {income_output}")


if __name__ == "__main__":
    create_gold()