from resume.input import get_user_info
from resume.template import format_resume
from resume.export import export_resume

def main():
    data = get_user_info()
    style = input("Choose output style (text/markdown): ").strip().lower()
    filename = input("Enter filename (with .txt or .md): ")
    content = format_resume(data, style)
    export_resume(content, filename)

if __name__ == "__main__":
    main()
