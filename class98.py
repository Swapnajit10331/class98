def countwordsfromfile():
    filename=input("enter the file name")
    numberofWords=0
    file=open(filename,"r")
    
    for line in file:
        words=line.split()
        numberofWords=numberofWords+len(words)

    print("numberofWords")
    print(numberofWords)

countwordsfromfile()
    