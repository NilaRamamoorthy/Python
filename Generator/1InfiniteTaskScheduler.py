import itertools, time

def task_runner(task_list):
    """Infinite generator cycling through tasks."""
    for task in itertools.cycle(task_list):
        start = time.time()
        result = yield task  # yield task name
        duration = time.time() - start
        print(f"[LOG] Task '{task}' executed in {duration:.6f}s")

# Usage:
tasks = ["backup", "cleanup", "report", "sync"]
runner = task_runner(tasks)
gen = iter(runner)

print("Scheduler run (10 tasks):")
for _ in range(10):
    task = next(gen)
    print("Task:", task)
    # optionally could send back status: gen.send("done")
# To finalize generator
try:
    gen.close()
except:
    pass
