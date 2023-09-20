import random

prisoners = list(range(1, 101))
random.shuffle(prisoners)
boxes = list(range(1, 101))
random.shuffle(boxes)

count = 0
for prisoner in prisoners:
    current_box = prisoner
    for _ in range(50):
        if boxes[current_box - 1] == prisoner:
            count += 1
            break
        else:
            current_box = boxes[current_box - 1]

if count == 100:
    print("All prisoners found their own number!")
else:
    print("Not all prisoners found their own number.")