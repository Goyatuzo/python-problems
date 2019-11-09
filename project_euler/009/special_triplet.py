def solve():
    answer = None

    for i in range(1, 1001):
        for j in range(i, 1001):
            if i + j > 1000:
                break

            for k in range(j, 1001):
                if i + j + k > 1000:
                    break

                if i ** 2 + j ** 2 == k ** 2 and i + j + k == 1000:
                    answer = (i, j, k)

    return answer

if __name__ == '__main__':
    a, b, c = solve()
    print(a * b * c)