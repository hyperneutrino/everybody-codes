import math

total = 0

for pinecones in map(int, input().split(",")):
    side_length = math.ceil(math.sqrt(pinecones))
    area = side_length ** 2
    required = area - pinecones
    total += required

print(total)