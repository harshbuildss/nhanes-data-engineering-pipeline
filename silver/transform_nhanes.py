import pandas as pd
from pathlib import Path


def transform_nhanes():

    project_root = Path(__file__).resolve().parents[1]

    raw_file = project_root / "raw" / "DEMO_L.xpt"
    silver_folder = project_root / "silver"
    silver_folder.mkdir(exist_ok=True)

    output_file = silver_folder / "nhanes_demographics.parquet"

    df = pd.read_sas(raw_file)

    print(df.shape)

    df = df[
        [
            "SEQN",
            "RIDAGEYR",
            "RIAGENDR",
            "RIDRETH3",
            "DMDEDUC2",
            "INDFMPIR"
        ]
    ]

    df = df.rename(columns={
        "SEQN": "participant_id",
        "RIDAGEYR": "age",
        "RIAGENDR": "gender_code",
        "RIDRETH3": "race_ethnicity_code",
        "DMDEDUC2": "education_code",
        "INDFMPIR": "income_poverty_ratio"
    })

    df["gender"] = df["gender_code"].map({
        1: "Male",
        2: "Female"
    })

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

    df["age_group"] = df["age"].apply(get_age_group)

    df["race_ethnicity"] = df["race_ethnicity_code"].map({
        1: "Mexican American",
        2: "Other Hispanic",
        3: "Non-Hispanic White",
        4: "Non-Hispanic Black",
        6: "Non-Hispanic Asian",
        7: "Other Race - Including Multi-Racial"
    })

    df["education"] = df["education_code"].map({
        1: "Less than 9th grade",
        2: "9-11th grade",
        3: "High school graduate/GED",
        4: "Some college or AA degree",
        5: "College graduate or above",
        9: "Don't know"
    })

    df["education"] = df["education"].fillna("Unknown")

    df = df.drop(columns=[
        "gender_code",
        "race_ethnicity_code",
        "education_code"
    ])

    df.to_parquet(output_file, index=False)

    print("Silver transformation completed.")
    print(f"Saved to: {output_file}")
    print(f"Shape: {df.shape}")


if __name__ == "__main__":
    transform_nhanes()