# Gym Membership Management

class Member:
    total_members = 0  # Class variable to track total members

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sessions = []
        Member.total_members += 1

    def register_sessions(self, *args):
        for session in args:
            self.sessions.append(session)
        print(f"{self.name} registered for: {', '.join(self.sessions)}")

    def view_details(self):
        print(f"\nMember: {self.name}, Age: {self.age}")
        print(f"Sessions: {', '.join(self.sessions)}")

class Trainer:
    def __init__(self, name, expertise):
        self.name = name
        self.expertise = expertise

    def assign(self, member):
        print(f"Trainer {self.name} assigned to {member.name} for {', '.join(member.sessions)}")

class Schedule:
    def __init__(self):
        self.schedule = {}

    def book_slot(self, member, day):
        if day not in self.schedule:
            self.schedule[day] = []
        self.schedule[day].append(member.name)
        print(f"{member.name} booked on {day}")

    def view_schedule(self):
        print("\nSchedule:")
        for day, members in self.schedule.items():
            print(f"{day}: {', '.join(members)}")

class Subscription:
    def __init__(self, member, plan):
        self.member = member
        self.plan = plan

    def details(self):
        print(f"{self.member.name} has subscribed to {self.plan} plan")

# Sample usage
if __name__ == "__main__":
    m1 = Member("Arun", 25)
    m2 = Member("Divya", 30)

    m1.register_sessions("Yoga", "Cardio")
    m2.register_sessions("Weight Training")

    trainer1 = Trainer("Ravi", "Fitness")
    trainer1.assign(m1)
    trainer1.assign(m2)

    schedule = Schedule()
    schedule.book_slot(m1, "Monday")
    schedule.book_slot(m2, "Tuesday")
    schedule.view_schedule()

    sub1 = Subscription(m1, "Gold")
    sub2 = Subscription(m2, "Silver")
    sub1.details()
    sub2.details()

    m1.view_details()
    m2.view_details()

    print(f"\nTotal Members Registered: {Member.total_members}")
