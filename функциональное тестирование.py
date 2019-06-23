print(
    all(
        map(
            lambda x: x > 0,
            map(
                int,
                input().split()
            )
        )
    )
)
