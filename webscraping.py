import requests
import json

# Funkcja do pobierania danych o misjach SpaceX
def fetch_spacex_missions():
    url = "https://api.spacexdata.com/v5/launches"
    response = requests.get(url)
    
    # Sprawdzanie, czy wszystko git z pobraniem danych
    if response.status_code != 200:
        print(f"Nie udało się pobrać danych, status code {response.status_code}")
        return None
    # Zwrot danych w formacie JSON
    return response.json()

# Funkcja do przetworzenia danych
def process_missions_data(data):
    processed_data = []
    
    for mission in data:
        # Wybor ze strony tylko interesujacych danych flight_number, name, date_utc => scraping
        mission_data = {
            'flight_number': mission.get('flight_number'),
            'name': mission.get('name'),
            'date_utc': mission.get('date_utc')
        }
        processed_data.append(mission_data)
    
    return processed_data

# Funkcja do zapisu danych do pliku JSON
def save_to_json(data, filename):
    if data:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Dane zostały zapisane do {filename}")
    else:
        print("Brak danych do zapisu.")


if __name__ == "__main__":
    missions = fetch_spacex_missions()
    if missions:
        processed_missions = process_missions_data(missions)
        save_to_json(processed_missions, 'spacex_missions.json')
