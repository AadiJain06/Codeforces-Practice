def solve():
    n = int(input())
    s = input()
 
    if n == 0:
        print(0)
        return
 
    target = s[n - 1]
    operations = 0
 
    for i in range(n - 2, -1, -1):
        if s[i] != target:
            operations += 1
            
    print(operations)
 
def main():
    try:
        t = int(input())
        for _ in range(t):
            solve()
    except EOFError:
        pass
    except Exception:
        pass
 
if __name__ == "__main__":
    main()