from array import *
def main():
    a =  [0,0,0,0,0,0,0,0,0,0,0,0]
    b =  [0,0,0,0,0,0,0,0,0,0,0,0]    
    print("Hello World!")
    power=0
    with open('input.txt') as f:
        lines = f.readlines()
        for i in range(0,12):
            ones=0
            zeros=0
            for line in lines:
                if(int(line[i]) == 1):
                    ones+=1
                if(int(line[i]) == 0):
                    zeros+=1
            if (ones>zeros):
                a[i]=1
                b[i]=0
            else:
                a[i]=0
                b[i]=1    
    res_gamma = int("".join(str(x) for x in a), 2)
    res_epsilon = int("".join(str(x) for x in b), 2)
    print(res_gamma*res_epsilon)

        

if __name__ == "__main__":
    main() 