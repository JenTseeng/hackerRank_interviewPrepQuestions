# refer to Hacker Rank for problem statement
def alternatingCharacters(s):
    count = 0

    for idx in range(len(s)-1):
        if s[idx] == s[idx+1]:
            count+=1
    
    return count

if __name__ == '__main__':

    q = int(input("How many strings?"))

    for q_itr in range(q):
        s = input("Please enter string:")

        result = alternatingCharacters(s)

        print(result)
