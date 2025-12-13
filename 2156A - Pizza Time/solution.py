import sys
 
def solve():
    try:
        n = int(sys.stdin.readline())
    except:
        return
 
    total_hao_slices = 0
    
    while n >= 3:
        m1 = n // 3
        total_hao_slices += m1
        
        # Optimal choice for m3 is n - 2 * m1
        n = n - 2 * m1
        
    print(total_hao_slices)
 
def main():
    try:
        t = int(sys.stdin.readline())
        for _ in range(t):
            solve()
    except:
        pass
 
main()