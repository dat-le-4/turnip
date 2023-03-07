# h5p3.py
# This program determines the maximum possible turnip harvest for any planting strategy, where plot i has quality q[i].
# This is just starter code, you fill in maxTurnips(q)

import sys

def maxTurnips(q):
    memo = [0] * (len(q)+3)
    for i in range(len(q)-1, -1, -1):
        memo[i] = max(memo[i+1], q[i] + memo[i+3])
    return memo[0]


def main():
    s = sys.argv[1:]
    # If the user didn't pass in the list as arguments then
    # get the list of integers from the user
    if len(s)==0 :
        s = input("Enter integers separated by spaces: ")
    s = s.split()
    # Convert the input into an array of integers
    # Catch errors related to non-integer arguments
    try:
        s = [int(x) for x in s]
    except:
        print( "Problem with the input, try again next time!" )

    turnips = maxTurnips(s)
    print("There maximum harvest for these qualities is %d turnips."%turnips)

if __name__ == "__main__":
    main()
