n = int(input("Enter the number\n"))

if (n > 2):
    for i in range(0, n):
        for j in range(0, n-i-1):
            print(end = ' ')
        for j in range(0, i+1):
            if(i != n-1):
                if(j == 0 or j == i):
                    print("*", end = ' ')
                else:
                    print(" ", end = ' ')
            else:
                if(j == 0):
                    print(" ", end = '')
                elif(j == n-1):
                    print("*", end = ' ')
                else:
                    print("*" * 2, end = '')
        print()
else:
    print("Not Valid")
