import pandas as pd
import psycopg
from pathlib import Path
import os


def load_gold():

    project_root = Path(__file__).resolve().parents[1]

    participant_file = (
        project_root / "gold" / "participant_count_by_age_gender.parquet"
    )

    income_file = (
        project_root / "gold" / "avg_income_poverty_by_age.parquet"
    )

    participant_counts = pd.read_parquet(participant_file)
    avg_income = pd.read_parquet(income_file)

    conn = psycopg.connect(
        host="172.26.208.1",
        port=5432,
        dbname="nhanes_brfss",
        user="postgres",
        password=os.environ["POSTGRES_PASSWORD"]
    )

    print("Connected successfully!")

    cur = conn.cursor()

    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS participant_count_by_age_gender (
                age_group VARCHAR(10),
                gender VARCHAR(10),
                participant_count INT
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS avg_income_poverty_by_age (
                age_group VARCHAR(10),
                avg_income_poverty_ratio DOUBLE PRECISION
            )
        """)

        cur.execute("TRUNCATE TABLE participant_count_by_age_gender")
        cur.execute("TRUNCATE TABLE avg_income_poverty_by_age")

        for _, row in participant_counts.iterrows():
            cur.execute("""
                INSERT INTO participant_count_by_age_gender
                (age_group, gender, participant_count)
                VALUES (%s, %s, %s)
            """, (
                row["age_group"],
                row["gender"],
                row["participant_count"]
            ))

        for _, row in avg_income.iterrows():
            cur.execute("""
                INSERT INTO avg_income_poverty_by_age
                (age_group, avg_income_poverty_ratio)
                VALUES (%s, %s)
            """, (
                row["age_group"],
                row["avg_income_poverty_ratio"]
            ))

        conn.commit()

        print("Gold data loaded into PostgreSQL successfully.")

    except Exception:
        conn.rollback()
        raise

    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    load_gold()
