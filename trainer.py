import numpy as np


def ReadImage(file_name):
    input_vector = []
    with open(file_name, "r") as cfile:
        for i in range(0, 20):
            line = cfile.readline().strip().split(" ")
            for j in range(0, len(line)):
                line[j] = int(line[j])
                input_vector.append(line[j])
    return input_vector


counter = 1
num_correct = 0
num_images = 12
while num_correct < num_images:
    # READ IN THE IMAGE----------------------------------------------------------------------
    image_vector = ReadImage("image" + str(counter) + ".txt")
    circle = bool(image_vector.pop(len(image_vector) - 1))  # 1 = circle, 0 = rectangle
    image_vector.append(1)  # x0, the x for the bias, is 1

    # READ IN THE WEIGHTS--------------------------------------------------------------------
    weight_vector = ReadImage("weights.txt")
    bias = weight_vector[len(weight_vector) - 1]

    # MAKE GUESS-----------------------------------------------------------------------------
    activation = 0
    for i in range(0, len(image_vector)):
        activation += image_vector[i] * weight_vector[i]

    if activation >= bias:
        print("GUESS: 1, ANSWER: " + str(circle))
    else:
        print("GUESS: 0, ANSWER: " + str(circle))
    # ADJUST WEIGHTS AS NEEDED---------------------------------------------------------------
    if circle and activation < 0:
        weight_vector = np.add(weight_vector, image_vector)
        num_correct = 0
    if (not circle) and activation >= 0:
        weight_vector = np.subtract(weight_vector, image_vector)
        num_correct = 0
    if (circle and activation >= 0) or ((not circle) and activation < 0):
        num_correct += 1

    # WRITE TO WEIGHTS.TXT-------------------------------------------------------------------
    with open("weights.txt", "w") as write_file:
        count = 0
        for i in range(0, len(weight_vector)):
            write_file.write(str(weight_vector[i]) + " ")
            count += 1
            if count % 20 == 0 and count < 400:
                write_file.write("\n")

    counter += 1
    if counter > num_images:
        counter = 1

# make it look nice for finalweights
with open("finalweights.txt", "w") as write_file:
    count = 0
    for i in range(0, len(weight_vector)):
        if (weight_vector[i] < 0):
            write_file.write(str(weight_vector[i]) + " ")
        else:
            write_file.write(" " + str(weight_vector[i]) + " ")
        count += 1
        if count % 20 == 0 and count < 400:
            write_file.write("\n")