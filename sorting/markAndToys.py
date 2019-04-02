# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices = sorted(prices)
    total = 0
    num_toys = 0

    for cost in prices:
        total += cost
        if total > k:
            break
        num_toys += 1
    
    return num_toys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()