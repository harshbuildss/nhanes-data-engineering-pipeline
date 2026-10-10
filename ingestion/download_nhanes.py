import requests
from pathlib import Path


def download_nhanes():

    url = "https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.xpt"

    project_root = Path(__file__).resolve().parents[1]
    raw_folder = project_root / "raw"
    raw_folder.mkdir(exist_ok=True)

    output_file = raw_folder / "DEMO_L.xpt"

    response = requests.get(url)
    response.raise_for_status()

    with open(output_file, "wb") as file:
        file.write(response.content)

    print("NHANES data downloaded successfully.")


if __name__ == "__main__":
    download_nhanes()
    
