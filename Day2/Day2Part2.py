def main():
    horizental=0
    depth=0
    aim=0
    with open('input.txt') as f:
        lines = f.readlines()
        for i in range(0,lines.__len__()):
            a = lines[i].split()
            if(a[0] == "forward"):
                if(aim!=0):
                    depth+=int(a[1])*aim
                horizental+=int(a[1])
            elif(a[0] == "up"):
                #depth-=int(a[1])   
                aim-=int(a[1])             
            else:
                #depth+=int(a[1])
                aim+=int(a[1])
                
    
    print(horizental*depth)

    

if __name__ == "__main__":
    main()