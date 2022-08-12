if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arra = list(dict.fromkeys(arr))
    maxnumber = max(arra)
    arra.remove(maxnumber)
    maxnumber2 = max(arra)
    print(maxnumber2)