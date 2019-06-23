from functools import reduce

print(
    reduce(
        lambda x,
               y: x * y ** 5,
        map(
            int,
            input().split()
        ),
        1)
)
