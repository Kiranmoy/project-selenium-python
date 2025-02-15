
iteration = 0

while iteration <= 10:
    if iteration == 5:
        iteration += 1
        continue
    if iteration == 9:
        break
    print("Iteration {}".format(iteration))
    iteration += 1


print("while loop completed.")