import sys
 
def solve():
    try:
        sys.stdin.readline()
        a = list(map(int, sys.stdin.readline().split()))
    except:
        return
 
    s = set(a)
    m = 0
    
    while True:
        if m not in s:
            print(m)
            return
        m += 1
 
def main():
    try:
        t = int(sys.stdin.readline())
        for _ in range(t):
            solve()
    except:
        pass
 
main()