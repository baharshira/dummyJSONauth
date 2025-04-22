import json

from auth.login import login
from plugins.evidence_runner import collect_all


def load_credentials():
    with open("dummy_db.json") as f:
        return json.load(f)["valid_credentials"][0]

def main():
    creds = load_credentials()
    token = login(creds)
    if not token:
        print("Authentication failed.")
        return
    results = collect_all(token)
    print(json.dumps(results, indent=2, default=str))

if __name__ == "__main__":
    main()