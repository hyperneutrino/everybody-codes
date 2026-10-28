import math

total = 0

for pinecones in map(int, input().split(",")):
    side_length_minus_one = max(math.ceil(pinecones / 4), 2) # Minimum 3x3, so side_length - 1 >= 2
    final_pinecones_needed = side_length_minus_one * 4
    required = final_pinecones_needed - pinecones
    total += required

print(total)