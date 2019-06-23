def main():
    return len(list(i for i in map(int, input().split()) if i >= 0))


print(main())
