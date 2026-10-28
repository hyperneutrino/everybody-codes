import math

total = 0

for pinecones in map(int, input().split(",")):
    # We can pretend the 1x1 hole doesn't exist by adding one to our existing pinecone count and
    # then calculate the side length from that.
    side_length_maybe_even = math.ceil((pinecones + 1) ** 0.5)

    # We'll then ensure an odd number by halving, flooring, doubling, and adding one, so an odd
    # number stays as itself and an even number is incremented.
    side_length = math.floor(side_length_maybe_even / 2) * 2 + 1

    area = side_length ** 2 - 1
    required = area - pinecones
    total += required

print(total)