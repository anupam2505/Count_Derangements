def count_rearrangement(n):
    subproblem = [1,0,1]
    for i in range (3,n+1):
        sub = (i-1)*(subproblem[i-1]+subproblem[i-2])
        subproblem.append(sub)
    print subproblem[n]    
    
def main():
    var = raw_input("Please enter a number: ")
    count_rearrangement(int(var))

if __name__ == '__main__':
    main()