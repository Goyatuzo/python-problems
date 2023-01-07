def progress_bar(word: str) -> str:
	pass

if __name__ == '__main__':
    n = int(input())

    for _ in range(n):
        print(progress_bar([int(num) for num in input().split()]))
