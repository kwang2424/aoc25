with open('input.txt') as f:
    curr = 50
    cnt = 0
    # scenarios are if it goes to 0, goes over, or goes under
    # if goes under: want to count if 
    for line in f.readlines():
        dir = line[0]
        num = int(line[1:])
        if curr == 0 or curr == 100:
            if num % 100 != 0:
                cnt += 1
            if dir == 'L' and curr == 0:
                curr += 100
            elif dir == 'R' and curr == 100:
                curr -= 100
        if num > 100:
            cnt += num // 100
            num = num % 100
        if dir == 'L':
            curr -= num
            if curr < 0:
                cnt += 1
                curr += 100
        else:
            curr += num
            if curr > 100:
                cnt += 1
                curr -= 100
        print(curr, cnt, num)
    if curr == 0:
        cnt += 1
    print(cnt)

