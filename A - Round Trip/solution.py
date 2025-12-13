import sys
 
def main():
    try:
        input_lines = sys.stdin.readlines()
        if not input_lines:
            return
 
        t = int(input_lines[0].strip())
        line_idx = 1
        
        results = []
 
        for _ in range(t):
            if line_idx >= len(input_lines):
                break
            
            try:
                R0, X, D, n = map(int, input_lines[line_idx].strip().split())
            except ValueError:
                line_idx += 1
                continue
            line_idx += 1
            
            if line_idx >= len(input_lines):
                break
            rounds = input_lines[line_idx].strip()
            line_idx += 1
 
            current_min = R0
            current_max = R0
            rated_count = 0
 
            for round_type in rounds:
                if round_type == '1':
                    rated_count += 1
                    
                    next_min = max(0, current_min - D)
                    next_max = current_max + D
                    
                    current_min = next_min
                    current_max = next_max
 
                else:
                    if current_min >= X:
                        pass
                    else:
                        rated_count += 1
                        
                        next_min = max(0, current_min - D)
                        
                        rated_R_max = min(current_max, X - 1)
                        next_max = rated_R_max + D
 
                        current_min = next_min
                        current_max = next_max
            
            results.append(str(rated_count))
        
        sys.stdout.write('\n'.join(results) + '\n')
 
    except Exception:
        pass
 
if __name__ == "__main__":
    main()