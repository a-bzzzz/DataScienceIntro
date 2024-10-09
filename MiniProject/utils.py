import requests
import numpy as np
import json

def download_and_save_file(url, target_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(target_path, 'wb') as f:
            f.write(response.content)
    except Exception as e:
        print('ERROR occurred: ', e)


def create_year_list(start_year: int, end_year: int) -> np.ndarray[str]|None:
    if start_year and end_year:
        return np.arange(start_year, end_year+1).astype(str)
    return None


import json

def json_to_text(json_file, text_output_path):
    try:
        pretty_json_str = json.dumps(json_file, indent=4)

        with open(text_output_path, 'w', encoding='utf-8') as text_file:
            text_file.write(pretty_json_str)

        print(f"JSON data has been successfully written to {text_output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
