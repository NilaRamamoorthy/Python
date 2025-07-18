def format_resume(data, style="text"):
    if style == "markdown":
        return f"""# {data['name']}

**Email:** {data['email']}  
**Phone:** {data['phone']}

## Summary
{data['summary']}

## Skills
- {"\n- ".join([skill.strip() for skill in data['skills']])}

## Experience
{data['experience']}

## Education
{data['education']}
"""
    else:
        return f"""Name: {data['name']}
Email: {data['email']}
Phone: {data['phone']}

Summary:
{data['summary']}

Skills:
{', '.join(data['skills'])}

Experience:
{data['experience']}

Education:
{data['education']}
"""
