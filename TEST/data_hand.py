def read_data( ):
    with open("./TrainData2.txt","r") as f:
        lines = f.readlines()
        f2=open("./TrainData4.txt",'w')
        for line in lines:
            line=line[5:-1]
            
            f2.write(line+'\n')
            print(line)
if __name__ == "__main__":
    read_data()