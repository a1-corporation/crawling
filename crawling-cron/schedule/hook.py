import requests

def notify_with_json(fpath: str, url="http://127.0.0.1:8000/etl/"):
    """Notifies the web backend to start ETL with this json file
    Parameters:
    fpath: full json file path
    """
    files = {'file': open(fpath, 'rb')}

    try:
        response = requests.post(url, files=files)
        response.raise_for_status()
        print("It's all yours!")
    except requests.exceptions.RequestException as e:
        print(f"Failed to initiate ETL: {e}")