def checkMagazine(magazine, note):
    """Python 3 solution to Hacker Rank ransom note challenge"""
    words = {}
    for word in magazine:
        words[word] = words.get(word,0)+1
    
    status = "Yes"
    for word in note:
        if word not in words or words[word] <= 0:
            status = "No"
            break
        
        else:
            words[word] -= 1
    
    print(status)


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)