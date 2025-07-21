# search.py

from typing import List
from directory import employees

def search_by_name(name: str) -> List[dict]:
    return [emp for emp in employees if name.lower() in emp["name"].lower()]

def search_by_department(dept: str) -> List[dict]:
    return [emp for emp in employees if dept.lower() == emp["department"].lower()]

def list_departments() -> set:
    return {emp["department"] for emp in employees}
