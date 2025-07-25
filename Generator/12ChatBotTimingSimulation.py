import time

def typing_simulator(message):
    i = 0
    while i < len(message):
        char = message[i]
        override = yield char
        if override == 'skip':
            print("\n[Typing skipped]")
            return
        time.sleep(0.1)  # simulate typing delay
        i += 1

# Demo:
gen = typing_simulator("Hello, how are you?")
print("Chatbot typing:")
try:
    ch = next(gen)
    while True:
        print(ch, end="", flush=True)
        ch = gen.send(None)
except StopIteration:
    print("\nDone.")

# Example sending skip:
gen2 = typing_simulator("This will be skipped")
print("\nTyping again but skipping:")
print(next(gen2), end="", flush=True)
gen2.send('skip')
