
def solution(s):
    alp_idx = {}
    result = []
    
    for idx, alp in enumerate(s):

        if alp not in alp_idx:    
            result.append(-1)
        else:    
            result.append(idx - alp_idx[alp])
            
        alp_idx[alp] = idx
        
    return result
