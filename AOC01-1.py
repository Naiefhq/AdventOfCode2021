from array import *
import numpy as np


def main():
  l = array('i',[1,2,3,4])
  count = 0
  for i in range(0, len(l)-1): 
    if l[i] < l[i+1]:
        count += 1
  print(count)
         

    


if __name__ == "__main__":
    main()   