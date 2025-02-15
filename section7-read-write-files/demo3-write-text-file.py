
# read lines from a file
# write to a file in reverse order
lines=""
with open("test.txt", "r") as reader:
    lines = reader.readlines()
    lines.reverse()

with open("test.txt", "w") as writer:
    for line in lines:
        writer.write(line)