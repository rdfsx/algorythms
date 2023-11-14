def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key():
            print("found the key!")


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


if __name__ == "__main__":
    print(factorial(5))
