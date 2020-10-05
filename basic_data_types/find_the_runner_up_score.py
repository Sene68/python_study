# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
# You are given n  scores. Store them in a list and find the score of the runner-up.

def print_score(n,arr):
    arr = sorted(arr, reverse=True)
    rank1 = arr[0]
    rank2 = False

    for i in arr:
        if(i < rank1 and rank2 == False):
            rank1 = i
            rank2 = True

    print(rank1)

if __name__ == '__main__':
    n = int(4)
    arr = [1,-1,-2,-1]
    print_score(n,arr)