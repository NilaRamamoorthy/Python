import json
import functools
from datetime import datetime

def param_logger(log_file="cli_params.json"):
    history = []

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log_entry = {
                "function": func.__name__,
                "timestamp": datetime.now().isoformat(),
                "args": args,
                "kwargs": kwargs
            }
            history.append(log_entry)

            # Write the latest history to file
            with open(log_file, "w") as f:
                json.dump(history, f, indent=4, default=str)

            return func(*args, **kwargs)
        return wrapper
    return decorator

# Example CLI tool simulation
@param_logger()
def cli_tool(command, **options):
    print(f"Executing: {command} with options {options}")

# Sample calls
cli_tool("backup", path="/home/user", compress=True)
cli_tool("restore", path="/backup", overwrite=False)
