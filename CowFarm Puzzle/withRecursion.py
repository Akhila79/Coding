import math
import random
from argparse import ArgumentParser

def main(infile):
    #this function reads from input file and returns 2d array and hay count
    def read(infile):
        emptyPlaces=''
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
    def putCows(score, farm, emptyPlaces, filled):
        cowPositions=[]
        for pos in emptyPlaces:
            if pos not in filled:
                row,col=pos.split("+")[0],pos.split("+")[1]
                farm[row][col]='C'
                cowPositions.append(pos)
                scoreNow=giveScore(farm, cowPositions)
                if scoreNow<=score:
                    farm[row][col]='.'
                    cowPositions.remove(pos)
                else:
                    filled.append(pos)
                    score=scoreNow
                    return putCows(score,farm, emptyPlaces.remove(pos), filled)
        return score,farm

        
    #Scoring function returns score for the cows placement
    def giveScore(farm, cowPositions):
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
        for i in cowPositions:
            pos=i.split('+')
            col=int(pos[1])
            row=int(pos[0])
            score+=checkNeighboringSources(row,col)
            score+=checkNeighboringCows(row,col)
        return score 
    farm, emptyPlaces=read(infile)
    totalScore, farm=putCows(0,farm,emptyPlaces,[])
    return farm, totalScore

parser = ArgumentParser()
parser.add_argument("infile", type=str, help="Input file name")
parser.add_argument("outfile", type=str, help="Output file name")
args = parser.parse_args()
farm,sc=main(args.infile)
outfile=open(args.outfile,'w')
content= str(len(farm))+"\n"
for i in farm:
    for j in i: content+=j
    content+="\n"
content+=str(sc)
outfile.write(content)
outfile.close()