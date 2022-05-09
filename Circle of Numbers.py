# silk-hyacinth / phyr
# 9 may 2022
# https://codeforces.com/contest/263/problem/C

def solve(memo) -> list:
    '''
    :param memo: dict of each int
    :return: the order of the circle
    '''
    if len(memo) == 5:
        print(" ".join(list(memo.keys())))
    elif len(memo) == 6:
        k = list(memo.keys())
        opplink = {}
        for key in k:
            vals = memo[key]
            for val in k:
                if val not in vals and val is not key and val not in opplink:
                    opplink[key] = val
        final = []
        for val in opplink:
            final.append(val)
        for val in opplink.values():
            final.append(val)
        print(" ".join(final))
    else:
        try:
            link = {}
            for num in memo:
                local = memo[num]
                for guess in local:
                    compare = set(memo[guess])
                    # print(compare,  guess, num)
                    if num in compare:
                        current = set(local)
                        compare.remove(num)
                        if len(compare.intersection(current)) == 2:
                            if num in link:
                                link[num].append(guess)
                            else:
                                link[num] = [guess]

            # unlinking
            k = list(link.keys())
            current = k[0]
            final = [current]
            for i in range(len(link)-1):
                guess = link[current][0]
                if guess not in final:
                    current = guess
                    final.append(current)
                else:
                    current = link[current][1]
                    final.append(current)


            if len(set(final)) != len(final):
                print("-1")
            else:
                print(" ".join(final))
        except:
            print("-1")
if __name__ == '__main__':
    n = int(input())
    memo = {}
    for i in range(2*n):
        s, e = input().split()
        if s in memo:
            memo[s].append(e)
        else:
            memo[s] = [e]
        if e in memo:
            memo[e].append(s)
        else:
            memo[e] = [s]
    solve(memo)
