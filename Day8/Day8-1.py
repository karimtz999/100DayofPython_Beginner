import math

def point_calc(height, width, cover):
    area = height * width
    num_of_cons = math.ceil(area / cover)
    print(f"You'll need {num_of_cons} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
point_calc(height=test_h, width=test_w, cover=coverage)

