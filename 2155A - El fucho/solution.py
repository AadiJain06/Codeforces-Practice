import sys

def solve():
    try:
        n = int(sys.stdin.readline())
    except EOFError:
        return
    except ValueError:
        return
    
    total_matches = 2 * n - 2
    
    print(total_matches)

def main():
    try:
        t_line = sys.stdin.readline()
        if not t_line:
            return
        t = int(t_line)
    except EOFError:
        return
    except ValueError:
        return

    for _ in range(t):
        solve()

main()