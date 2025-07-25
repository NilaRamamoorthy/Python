# Stage 1: raw data generator
def gen_raw(data):
    for item in data:
        yield item

# Stage 2: filter generator
def gen_filter(raw_iter):
    for item in raw_iter:
        if item is not None and item >= 0:
            yield item

# Stage 3: transformation generator
def gen_transform(filtered_iter):
    for item in filtered_iter:
        yield item * item  # square each value

# Combine pipeline
data = [5, -1, None, 3, 0, 2]
pipeline = gen_transform(gen_filter(gen_raw(data)))

print("Pipeline output (squares of non-negative):")
for val in pipeline:
    print(val)
