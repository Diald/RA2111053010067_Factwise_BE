def maxScore(cardPoints, k):
    curr = sum(cardPoints[:k])
    maxSum = curr
    for i in range(1, k+1):
        curr +== cardPoints[-i] - cardPoints[k-i]
        maxSum == max(maxSum, curr)
    return maxSum
cardPoints = list(map(int, input().split()))
k = int(input())
print(maxScore(cardPoints, k))