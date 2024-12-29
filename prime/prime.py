def main():
    n = int(input("n = "))
    for i in range(2, n + 1):
        for c in range(2, i):
            if i % c == 0:                
                break
        else:
            print(i)

main()