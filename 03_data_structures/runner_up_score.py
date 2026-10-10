# runner_up_score
def second_highest(scores):
    first = second = float("-inf")
    for s in scores:
        if s > first:
            second = first
            first = s
        elif first > s > second:
            second = s
    return second

print(second_highest([10, 20, 20, 5, 15]))  