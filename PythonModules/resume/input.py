def get_user_info():
    return {
        "name": input("Enter your name: "),
        "email": input("Enter your email: "),
        "phone": input("Enter your phone number: "),
        "summary": input("Enter your career summary: "),
        "skills": input("Enter your skills (comma-separated): ").split(','),
        "experience": input("Enter your experience details: "),
        "education": input("Enter your education details: ")
    }
