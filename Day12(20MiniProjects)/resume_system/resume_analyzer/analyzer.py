# analyzer.py

applicant_data = {}

def add_resume(applicant_id, name, resume_text):
    key = (applicant_id,)
    keywords = extract_keywords(resume_text)
    
    applicant_data[key] = {
        "name": name,
        "resume_text": resume_text,
        "skills": keywords
    }

    print(f"Resume added for {name}. Extracted skills: {keywords}\n")

def extract_keywords(text):
    # Simple skill keywords for demo
    skill_keywords = {"python", "java", "sql", "html", "css", "javascript", "django", "flask", "react"}
    words = set(word.lower() for word in text.split())
    return words.intersection(skill_keywords)

def show_all_resumes():
    print("📄 Applicant Resumes & Skills:")
    for aid, data in applicant_data.items():
        print(f"ID: {aid}, Name: {data['name']}, Skills: {', '.join(data['skills'])}")
    print()
