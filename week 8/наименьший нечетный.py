print(
    min(
        list(
            filter(
                lambda x : x % 2,
                list(
                    map(
                        int,
                        input().split()
                    )
                )
            )
        )
    )
)
