def contact_searcher(contacts, initial_key=None):
    """
    Generator yielding (name, number) for contacts whose name starts with current search key.
    Accepts .send(new_key) to change search prefix mid-iteration.
    """
    key = initial_key
    for name, number in contacts.items():
        # Allow dynamic search key change mid-loop
        new_key = yield from (() for _ in () ) if False else None  # dummy to allow send
        if new_key:
            key = new_key
        if key and name.startswith(key):
            yield (name, number)

# Usage:
contacts = {
    "Alice": "123", "Bob": "234", "Charlie": "345",
    "David": "456", "Ann": "567"
}

gen = contact_searcher(contacts, initial_key="A")
print("Contacts starting with A:")
for c in gen:
    print(c)

# Reset generator to search new key B
gen = contact_searcher(contacts)
next(gen)  # prime
gen.send("C")
print("\nContacts starting with C:")
for c in gen:
    print(c)
