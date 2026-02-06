from typing import List


def constructLists(lines):
    left, right = [], []

    for line in lines:
        nums = line.split()
        left.append(int(nums[0]))
        right.append(int(nums[1]))

    return left, right


def calculateDistance(left, right):
    return sum(abs(x - y) for x, y in zip(left, right))


def calculateSimilarityScore(left: List[int], right: List[int]):
    return sum(x * right.count(x) for x in left)


def main(lines):
    left, right = constructLists(lines)

    print(f"Similarity Score: {calculateSimilarityScore(left, right)}")

    left.sort()
    right.sort()

    print(f"Total Distance: {calculateDistance(left, right)}")
