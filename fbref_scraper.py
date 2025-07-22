import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_filtered_matches():
    # Example source URL - replace with actual FBref page for upcoming matches
    url = "https://fbref.com/en/comps/9/schedule/Premier-League-Scores-and-Fixtures"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Placeholder: simulate 3 upcoming matches for now
    matches = [
        {"date": "2025-07-23", "home": "Man City", "away": "Liverpool", "tip": "Over 1.5 Goals"},
        {"date": "2025-07-24", "home": "Arsenal", "away": "Chelsea", "tip": "Double Chance (Away/Draw)"},
        {"date": "2025-07-25", "home": "Tottenham", "away": "Newcastle", "tip": "Over 1.5 Goals"},
    ]

    df = pd.DataFrame(matches)
    return df.to_dict(orient="records")
### paste fbref_scraper.py here ###