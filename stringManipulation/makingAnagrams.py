
# Refer to HackerRank for problem statement
def makeAnagram(a, b):
    di = {}
    count = 0

    # make hash map of first string
    for letter in a:
        di[letter] = di.get(letter,0)+1

    # make subtract letters from second string
    for letter in b:
        if di.get(letter,0) > 0:
            di[letter] -= 1
        else:
            count += 1

    return count+sum(di.values())


if __name__ == '__main__':

    a = input("Enter the first string:")

    b = input("Enter the second string:")

    res = makeAnagram(a, b)

    print(res)