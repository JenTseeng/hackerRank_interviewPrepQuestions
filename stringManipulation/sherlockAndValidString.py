from collections import Counter

def isValid(s):
    """Solution for Sherlock and Valid String problem on Hacker Rank"""
    letter_counts = Counter(s)
    frequencies = Counter(letter_counts.values())
    unique_counts = len(frequencies)

    # all chars have same count
    if unique_counts==1:
        return "YES"
    
    # more than 2 different character frequencies
    elif unique_counts > 2:
        return "NO"
    
    # 
    else:
        larger = max(frequencies.keys())
        smaller = min(frequencies.keys())
        if frequencies[larger]==1 and larger-smaller == 1:
            return "YES"
        elif frequencies[smaller]==1 and smaller ==1:
            return "YES"
        else:
            return "NO"
        

if __name__ == '__main__':

    s = input("Please input string")

    result = isValid(s)

    print(result)