import sys
from collections import Counter
 
def solve():
    try:
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
    except:
        return
 
    counts = Counter(a)
    
    total_deleted = 0
    
    if 0 in counts:
        total_deleted += counts[0]
        del counts[0]
 
    for x in list(counts.keys()): 
        count_x = counts[x]
        
        if count_x >= x:
            deleted_from_x = count_x - x
            total_deleted += deleted_from_x
        else:
            deleted_from_x = count_x
            total_deleted += deleted_from_x
 
    print(total_deleted)
 
def main():
    try:
        t = int(sys.stdin.readline())
        for _ in range(t):
            solve()
    except:
        pass
 
main()