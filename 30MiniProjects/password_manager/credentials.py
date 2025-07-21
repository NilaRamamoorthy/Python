# credentials.py

from typing import Dict, Set, Tuple

# site_name → (username, password, tags)
accounts: Dict[str, Tuple[str, str, Set[str]]] = {}

def add_credential(site: str, username: str, password: str, tags: Set[str]):
    if site in accounts:
        print("Site already exists. Use update instead.")
        return
    accounts[site] = (username, password, tags)
    print(f"Credential added for {site}.")

def update_credential(site: str, username: str = None, password: str = None, tags: Set[str] = None):
    if site not in accounts:
        print("No such site found.")
        return
    current = list(accounts[site])
    if username:
        current[0] = username
    if password:
        current[1] = password
    if tags:
        current[2] = tags
    accounts[site] = tuple(current)
    print(f"Credential updated for {site}.")

def delete_credential(site: str):
    if site in accounts:
        del accounts[site]
        print(f"Credential deleted for {site}.")
    else:
        print("Site not found.")

def search_by_tag(search_tag: str):
    results = {}
    for site, (username, password, tags) in accounts.items():
        if search_tag in tags:
            results[site] = (username, password)
    return results

def search_by_site(site: str):
    return accounts.get(site, "No data found.")
