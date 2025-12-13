
import sys
 
def solve():
    try:
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
    except:
        return
 
    max_avg = 0
    
    for l in range(n):
        current_sum = 0
        for r in range(l, n):
            current_sum += a[r]
            length = r - l + 1
            
            current_avg = current_sum // length
            
            if current_avg > max_avg:
                max_avg = current_avg
 
    print(max_avg)
 
def main():
    try:
        t = int(sys.stdin.readline())
        for _ in range(t):
            solve()
    except:
        pass
 
main()