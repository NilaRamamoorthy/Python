from textutils.analyze import summary_report
from textutils.utils import print_report

def main():
    text = input("Enter text to analyze:\n")
    report = summary_report(text)
    print_report(report)

if __name__ == "__main__":
    main()
