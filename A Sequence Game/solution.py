import sys
 
def solve():
    try:
        sys.stdin.readline()
        a = list(map(int, sys.stdin.readline().split()))
        x = int(sys.stdin.readline())
    except:
        return
 
    min_a = min(a)
    max_a = max(a)
 
    if min_a <= x and x <= max_a:
        print("YES")
    else:
        print("NO")
 
def main():
    try:
        t = int(sys.stdin.readline())
        for _ in range(t):
            solve()
    except:
        pass
 
if __name__ == "__main__":
    main()