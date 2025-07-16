# Initial resumes data
resumes = {
    1: {"skills": ["Python", "Django", "SQL"], "experience": 3},
    2: {"skills": ["HTML", "CSS", "JavaScript"], "experience": 2},
    3: {"skills": ["Python", "Flask"], "experience": 1},
    4: {"skills": ["Java", "Spring"], "experience": 4}
}

# 1. Search by skill
required_skill = "Python"
print(f"Resumes with skill '{required_skill}':")
for rid, info in resumes.items():
    if required_skill in info["skills"]:
        print(f"Resume ID: {rid}, Skills: {info['skills']}")

# 2. Filter by experience
min_experience = 2
print(f"\nResumes with experience >= {min_experience} years:")
for rid, info in resumes.items():
    if info["experience"] >= min_experience:
        print(f"Resume ID: {rid}, Experience: {info['experience']} years")
