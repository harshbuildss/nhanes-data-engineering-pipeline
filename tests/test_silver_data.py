from pathlib import Path

import pandas as pd


def test_participant_ids_are_unique():
    project_root = Path(__file__).resolve().parent.parent
    silver_file = project_root / "silver" / "nhanes_demographics.parquet"

    df = pd.read_parquet(silver_file)

    assert "participant_id" in df.columns, (
        "The participant_id column is missing."
    )

    assert df["participant_id"].is_unique, (
        "Duplicate participant IDs were found in the silver dataset."
    )


def test_participant_ids_are_not_missing():
    project_root = Path(__file__).resolve().parent.parent
    silver_file = project_root / "silver" / "nhanes_demographics.parquet"

    df = pd.read_parquet(silver_file)

    assert df["participant_id"].notna().all(), (
        "Missing participant IDs were found in the silver dataset."
    )
def test_required_columns_exist():
    project_root = Path(__file__).resolve().parent.parent
    silver_file = project_root / "silver" / "nhanes_demographics.parquet"

    df = pd.read_parquet(silver_file)

    required_columns = [
        "participant_id",
        "age",
        "gender",
        "age_group",
    ]

    for column in required_columns:
        assert column in df.columns, f"Missing required column: {column}"
        
def test_ages_are_within_valid_range():
    project_root = Path(__file__).resolve().parent.parent
    silver_file = project_root / "silver" / "nhanes_demographics.parquet"

    df = pd.read_parquet(silver_file)

    assert df["age"].notna().all(), "Missing ages were found."

    assert df["age"].between(0, 120).all(), (
        "Ages outside the valid range of 0–120 were found."
    )