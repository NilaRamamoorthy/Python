import json

def json_stream_processor(filepath, stop_key=None, stop_value=None):
    """
    Generator that reads a JSON-per-line file, yields objects one by one.
    Stops (raises StopIteration) when a JSON object contains stop_key == stop_value.
    """
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            yield obj
            if stop_key and obj.get(stop_key) == stop_value:
                return  # terminates generator

# Usage:
# Create example JSON lines in file
example = [
    {"id":1, "name":"A"},
    {"id":2, "name":"B"},
    {"id":3, "name":"STOP"},
    {"id":4, "name":"C"}
]
import json
with open('data.jsonl', 'w') as f:
    for o in example:
        f.write(json.dumps(o) + "\n")

print("Streaming JSON until stop:")
for obj in json_stream_processor('data.jsonl', stop_key="name", stop_value="STOP"):
    print(obj)
