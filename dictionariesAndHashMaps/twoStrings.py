def twoStrings(s1, s2):
    """Solution to Two Substrings challenge on Hacker Rank"""
    letters = {}
    for letter in s1:
        letters[letter]=letters.get(letter,0)+1
    
    result = "NO"

    for letter in s2:
        if letter in letters:
            result = "YES"
            break
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        print(result)