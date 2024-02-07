#by default python has a dynamic typing nature, at any time ypu can change the value of the number to a different type like a string, etc.
num: int = 100
lst: list[int] = [1, 2, 3, 4]
lst.append("str")
dt: dict[str, int] = {"key": 0 }


def root(num):
    return pow(num, .5)