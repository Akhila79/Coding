from argparse import ArgumentParser
import copy
import math

def main(infile):
    #this function reads from input file and returns 2d array and hay count
    def read(infile):
        emptyPlaces=[]
        inFile=open(infile,"r")
        lines=inFile.readlines()
        linecount=int(lines[0])
        farm=[]
        for i in range(linecount):
            row=[]
            line=lines[i+1].strip()
            for j in range(linecount):
                row.append(line[j])
                if line[j]=='.':
                    emptyPlaces.append(str(i)+"+"+str(j))
            farm.append(row)
        inFile.close()
        return farm,emptyPlaces
    #This function adds cows to random valid places and returns those positions in the form of string
    def putCows(farm, emptyPlaces):
        que=[]
        que.append(farm)
        count=0
        while len(que)!=0:
            farmNow=que.pop(0)
            if count==100000: return
            valid=[]
            for i in emptyPlaces:
                if farmNow[int(i.split('+')[0])][int(i.split('+')[1])]!='C':    valid.append(i)
            for pos in valid:
                row,col=int(pos.split("+")[0]),int(pos.split("+")[1])   
                if farmNow[row][col]=='.':
                    farmNow[row][col]='C'
                    sc=giveScore(farmNow)
                    print(sc)
                    if sc>=7:
                        # print(sc,farm)
                        return sc,farmNow
                    que.append(copy.deepcopy(farmNow))
                    farmNow[row][col]='.'
            count+=1
        return 0,farm

        
    #Scoring function returns score for the cows placement
    def giveScore(farm):
        #This function checks for cows in neighbohood and modifies score accordingly
        def checkNeighboringCows(row,col):
            dim=len(farm)
            if ((row-1>=0) and ((farm[row-1][col]=='C')or(col-1>=0 and farm[row-1][col-1]=='C')or(col+1<dim and farm[row-1][col+1]=='C')))or \
                ((row+1<dim) and ((farm[row+1][col]=='C')or (col-1>=0 and farm[row+1][col-1]=='C')or (col+1<dim and farm[row+1][col+1]=='C'))) or \
                   (col-1>=0 and farm[row][col-1]=='C') or \
                    (col+1<dim and farm[row][col+1]=='C') :
                return -3
            return 0
        #This function checks for hay and ponds in neighborhood and modifies score accordingly
        def checkNeighboringSources(row,col):
            neighbors=set()
            sco=0
            dim=len(farm)
            if row-1>=0:    neighbors.add(farm[row-1][col])
            if col-1>=0:    neighbors.add(farm[row][col-1])
            if row+1<dim:   neighbors.add(farm[row+1][col])
            if col+1<dim:   neighbors.add(farm[row][col+1])
            if '@' in neighbors:
                sco=1
                if '#' in neighbors:    sco=3
            return sco
        score=0       
        for i in range(len(farm)**2):
            # pos=i.split('+')
            col=i%len(farm)
            row=math.floor(i/len(farm))
            if farm[row][col]=='C':
                score+=checkNeighboringSources(row,col)
                score+=checkNeighboringCows(row,col)
        return score 
    farm, emptyPlaces=read(infile)
    totalScore, farm=putCows(farm,emptyPlaces)
    return farm, totalScore

# parser = ArgumentParser()
# parser.add_argument("infile", type=str, help="Input file name")
# parser.add_argument("outfile", type=str, help="Output file name")
# args = parser.parse_args()
# farm,sc=main(args.infile)
# outfile=open(args.outfile,'w')
farm,sc=main('sample_in.txt')
outfile=open('b.txt','w')
content= str(len(farm))+"\n"
for i in farm:
    for j in i: content+=j
    content+="\n"
content+=str(sc)
outfile.write(content)
outfile.close()