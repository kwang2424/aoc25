def check(s):
    s = str(s)
    return (s+s).index(s, 1) < len(s)

text = ""
with open('./day2/input.txt') as f:
    text = f.readline()

split_text = text.split(',')

def new_sol(split_text):
    total = 0
    for t in split_text:
        comma_split = t.split('-')
        l, r = int(comma_split[0]), int(comma_split[1])
        for i in range(l, r+1):
            if check(i):
                # print(i)
                total += i
    return total

print(new_sol(split_text))
def old_sol(split_text):
    total = 0
    for t in split_text:
        split_input = t.split('-')
        l, r = split_input[0].strip(), split_input[1].strip()
        
        if len(l) <= len(r):
            # print(l, r, len(l) // 2, len(r) // 2, len(l) < len(r))
            # if l and r are diff size, there has to be even somewhere (even if both odd, or one even/odd).
            while len(l) < len(r):
                if len(l) % 2 == 0 and len(l) > 0:
                    l_mid = len(l) // 2
                    r_mid = len(r) // 2
                    l_l, l_r = int(l[:l_mid]), int(l[l_mid:])
                    r_l, r_r = int(r[:r_mid]), int(r[r_mid:])
                    while l_l < (10**(l_mid)):

                        if l_l >= l_r:
                            
                            invalid_id = l_l * (10 ** (l_mid)) + l_l
                            # print('invalid id', invalid_id, 10**(l_mid), l, r)
                            total += invalid_id
                        l_l += 1
                        l_r = 0
                l = '1' + ('0' * len(l))
            # print('after equalizing', l, r)
            if len(l) % 2 != 0:
                continue
            else:
                l_mid = len(l) // 2
                r_mid = len(r) // 2
                l_l, l_r = int(l[:l_mid]), int(l[l_mid:])
                r_l, r_r = int(r[:r_mid]), int(r[r_mid:])
                # print(l_l, l_r, r_l, r_r)
                while l_l <= r_l:
                    if l_l >= l_r:
                        if l_l == r_l and l_l > r_r:
                            break
                        invalid_id = l_l * (10 ** (l_mid)) + l_l
                        # print('invalid id', invalid_id, l, r, l_l, r_r, l_r)
                        invalid_id = l_l * (10 ** (l_mid)) + l_l
                        total += invalid_id
                    l_l += 1
                    l_r = 0
    return total

# print(old_sol(split_text))