#16. Feedback Collector
while True:
    feedback=input("Enter feedback: ").lower()
    length=len(feedback)
    if length<3:
        continue
    if feedback=="exit":
        break