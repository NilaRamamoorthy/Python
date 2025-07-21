# utils.py

from typing import Tuple

def generate_emp_id(name: str, department: str) -> Tuple[str, str]:
    return (name.lower().replace(" ", ""), department.lower())
