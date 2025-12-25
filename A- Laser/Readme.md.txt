import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    ptr = 1
    results = []
    
    for _ in range(t):
        n = int(input_data[ptr])
        m = int(input_data[ptr + 1])
        x = int(input_data[ptr + 2])
        y = int(input_data[ptr + 3])
        ptr += 4
        
        # We just need to skip the coordinates since the answer is n + m
        ptr += n # Skip a_i
        ptr += m # Skip b_i
        
        results.append(str(n + m))
    
    sys.stdout.write('\n'.join(results) + '\n')

if __name__ == "__main__":
    solve()