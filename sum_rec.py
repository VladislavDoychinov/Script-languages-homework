def sum_rec(l, i, vsum):
    if i < len(l):
        vsum += l[i]
        return sum_rec(l, i + 1, vsum)
    else:
        return vsum

l = [1, 2, 3, 4]
print(sum_rec(l, 0, 0))
        
