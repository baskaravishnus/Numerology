def findNameNumber(name):
    name_number=0    
    lname=name.lower().replace(".", "").replace(" ", "")
    for letter in lname:            
        if((letter=="a")|(letter=="i")|(letter=="j")|(letter=="q")|(letter=="y")):
            name_number+=1
        if((letter=="b")|(letter=="k")|(letter=="r")):
            name_number+=2
        if((letter=="c")|(letter=="g")|(letter=="l")|(letter=="s")):
            name_number+=3
        if((letter=="d")|(letter=="m")|(letter=="t")):
            name_number+=4
        if((letter=="e")|(letter=="h")|(letter=="n")|(letter=="x")):
            name_number+=5
        if((letter=="u")|(letter=="v")|(letter=="w")):
            name_number+=6
        if((letter=="o")|(letter=="z")):
            name_number+=7
        if((letter=="f")|(letter=="p")):
            name_number+=8
    total_name_number=name_number
    while (total_name_number>9):
        total_name_number_string=str(total_name_number)
        total_name_number=0
        for st in total_name_number_string:
            total_name_number+=int(st)
    return(name_number,total_name_number)




suitable_name_numbers = [[[] for i in range(15)] for j in range(15)]
avoid_name_numbers = [[[] for i in range(15)] for j in range(15)]

suitable_names=[]
avoid_names=[]
other_names=[]

f=open("BdNames.txt")
day=int(f.readline())
month=int(f.readline())
year=int(f.readline())


print("day="+str(day))
print("month="+str(month))
print("year="+str(year))
print("\n")
sum_number=0

day_number=0        #day_number=birth number
if(day<9):
    day_number=day
else:
    d1=day%10
    n=day//10
    day_number=d1+n

if(month<9):
    month_number=month
else:
    d1=month%10
    n=month//10
    month_number=d1+n

year_number=0
year_string=str(year)
for sn in year_string:
    year_number+=int(sn)

total_number=day_number+month_number+year_number

while (total_number>9):
    total_number_string=str(total_number)
    total_number=0
    for st in total_number_string:
        total_number+=int(st)    
sum_number=total_number   

print("Birth number="+str(day_number))
# print("Month number="+str(month_number))
# print("Year number="+str(year_number))
print("Sum number="+str(sum_number))






















# suitable_name_numbers[birth number][sum number]=[]
# avoid_name_numbers[birth number][sum number]=[]
suitable_name_numbers[1][1]=[1,6,4]
avoid_name_numbers[1][1]=[8]
suitable_name_numbers[1][2]=[6,7]
avoid_name_numbers[1][2]=[8]
suitable_name_numbers[1][3]=[1,3,5,4]
avoid_name_numbers[1][3]=[8]
suitable_name_numbers[1][4]=[6,1,4]
avoid_name_numbers[1][4]=[2]
suitable_name_numbers[1][5]=[1,5,6]
avoid_name_numbers[1][5]=[8]
suitable_name_numbers[1][6]=[1,6,9]
avoid_name_numbers[1][6]=[3,8]
suitable_name_numbers[1][7]=[1,2,6]
avoid_name_numbers[1][7]=[8,9]
suitable_name_numbers[1][8]=[1,5,6]
avoid_name_numbers[1][8]=[8]
suitable_name_numbers[1][9]=[1,9,5]
avoid_name_numbers[1][9]=[8,3]
suitable_name_numbers[2][1]=[6,5,7]
avoid_name_numbers[2][1]=[2,8,9]
suitable_name_numbers[2][2]=[6,7]
avoid_name_numbers[2][2]=[9]
suitable_name_numbers[2][3]=[3,5,7]
avoid_name_numbers[2][3]=[6,9]
suitable_name_numbers[2][4]=[6,7]
avoid_name_numbers[2][4]=[3,8]
suitable_name_numbers[2][5]=[5,6,7]
avoid_name_numbers[2][5]=[9]
suitable_name_numbers[2][6]=[6,7]
avoid_name_numbers[2][6]=[9,8]
suitable_name_numbers[2][7]=[2,6,7]
avoid_name_numbers[2][7]=[9]
suitable_name_numbers[2][8]=[5,6,7]
avoid_name_numbers[2][8]=[9,8]
suitable_name_numbers[2][9]=[5,6]
avoid_name_numbers[2][9]=[9]
suitable_name_numbers[3][1]=[3,1]
avoid_name_numbers[3][1]=[6]
suitable_name_numbers[3][2]=[3,5,7]
avoid_name_numbers[3][2]=[6,9]
suitable_name_numbers[3][3]=[3,5,9]
avoid_name_numbers[3][3]=[6]
suitable_name_numbers[3][4]=[1,3]
avoid_name_numbers[3][4]=[6]
suitable_name_numbers[3][5]=[3,5,9]
avoid_name_numbers[3][5]=[6]
suitable_name_numbers[3][6]=[1,5,9]
avoid_name_numbers[3][6]=[3,6]
suitable_name_numbers[3][7]=[3,5]
avoid_name_numbers[3][7]=[6]
suitable_name_numbers[3][8]=[3,5]
avoid_name_numbers[3][8]=[6,8]
suitable_name_numbers[3][9]=[3,5,9]
avoid_name_numbers[3][9]=[2,6,7]
suitable_name_numbers[4][1]=[1,6]
avoid_name_numbers[4][1]=[8]
suitable_name_numbers[4][2]=[6,1]
avoid_name_numbers[4][2]=[8]
suitable_name_numbers[4][3]=[1,3]
avoid_name_numbers[4][3]=[8,6]
suitable_name_numbers[4][4]=[1,6]
avoid_name_numbers[4][4]=[8]
suitable_name_numbers[4][5]=[1,5,6,3]
avoid_name_numbers[4][5]=[8]
suitable_name_numbers[4][6]=[1,6]
avoid_name_numbers[4][6]=[3,8]
suitable_name_numbers[4][7]=[1,6]
avoid_name_numbers[4][7]=[8,9]
suitable_name_numbers[4][8]=[1,5,6]
avoid_name_numbers[4][8]=[8]
suitable_name_numbers[4][9]=[1,6,5]
avoid_name_numbers[4][9]=[2,7,8]
suitable_name_numbers[5][1]=[5,1,6]
avoid_name_numbers[5][1]=[7,8,9]
suitable_name_numbers[5][2]=[5,6,7]
avoid_name_numbers[5][2]=[9,8]
suitable_name_numbers[5][3]=[5,3,9]
avoid_name_numbers[5][3]=[6]
suitable_name_numbers[5][4]=[1,5,6]
avoid_name_numbers[5][4]=[4,8,7,9]
suitable_name_numbers[5][5]=[5,6,3]
avoid_name_numbers[5][5]=[7,8,9]
suitable_name_numbers[5][6]=[1,5,6]
avoid_name_numbers[5][6]=[3,8]
suitable_name_numbers[5][7]=[5,6,2]
avoid_name_numbers[5][7]=[9]
suitable_name_numbers[5][8]=[1,5,6]
avoid_name_numbers[5][8]=[8]
suitable_name_numbers[5][9]=[3,5,9]
avoid_name_numbers[5][9]=[2,7]
suitable_name_numbers[6][1]=[1,5,6]
avoid_name_numbers[6][1]=[3]
suitable_name_numbers[6][2]=[1,6,7,5]
avoid_name_numbers[6][2]=[3,9]
suitable_name_numbers[6][3]=[1,5,9]
avoid_name_numbers[6][3]=[3,6]
suitable_name_numbers[6][4]=[1,6]
avoid_name_numbers[6][4]=[3,8]
suitable_name_numbers[6][5]=[1,5,6]
avoid_name_numbers[6][5]=[3]
suitable_name_numbers[6][6]=[1,6,5,9]
avoid_name_numbers[6][6]=[3]
suitable_name_numbers[6][7]=[1,2,6]
avoid_name_numbers[6][7]=[3,8,9]
suitable_name_numbers[6][8]=[1,5,6]
avoid_name_numbers[6][8]=[3]
suitable_name_numbers[6][9]=[5,6,9]
avoid_name_numbers[6][9]=[3,7]
suitable_name_numbers[7][1]=[1,6]
avoid_name_numbers[7][1]=[8,9]
suitable_name_numbers[7][2]=[2,6]
avoid_name_numbers[7][2]=[8,9]
suitable_name_numbers[7][3]=[2,3,5]
avoid_name_numbers[7][3]=[9,6,8]
suitable_name_numbers[7][4]=[1,2.6]
avoid_name_numbers[7][4]=[8,9]
suitable_name_numbers[7][5]=[2,5,6]
avoid_name_numbers[7][5]=[9]
suitable_name_numbers[7][6]=[5,6,2]
avoid_name_numbers[7][6]=[3,8,9]
suitable_name_numbers[7][7]=[1,5,6]
avoid_name_numbers[7][7]=[7,8,9]
suitable_name_numbers[7][8]=[1,5,6,2]
avoid_name_numbers[7][8]=[8,9]
suitable_name_numbers[7][9]=[5,6,3]
avoid_name_numbers[7][9]=[8]
suitable_name_numbers[8][1]=[1,5,6]
avoid_name_numbers[8][1]=[8]
suitable_name_numbers[8][2]=[5,6]
avoid_name_numbers[8][2]=[8,9]
suitable_name_numbers[8][3]=[3,1,5]
avoid_name_numbers[8][3]=[8,6]
suitable_name_numbers[8][4]=[1,5,6]
avoid_name_numbers[8][4]=[8]
suitable_name_numbers[8][5]=[1,5,6]
avoid_name_numbers[8][5]=[8]
suitable_name_numbers[8][6]=[1,5,6]
avoid_name_numbers[8][6]=[3,8]
suitable_name_numbers[8][7]=[2,5,6]
avoid_name_numbers[8][7]=[8,9]
suitable_name_numbers[8][8]=[1,5,6]
avoid_name_numbers[8][8]=[8]
suitable_name_numbers[8][9]=[5,6]
avoid_name_numbers[8][9]=[2,8,7]
suitable_name_numbers[9][1]=[1,5,6,9]
avoid_name_numbers[9][1]=[2,7]
suitable_name_numbers[9][2]=[5,6]
avoid_name_numbers[9][2]=[8]
suitable_name_numbers[9][3]=[3,5,9]
avoid_name_numbers[9][3]=[2,7]
suitable_name_numbers[9][4]=[1,5,6,9]
avoid_name_numbers[9][4]=[2,7]
suitable_name_numbers[9][5]=[5,6,9]
avoid_name_numbers[9][5]=[2,7]
suitable_name_numbers[9][6]=[6,5,9]
avoid_name_numbers[9][6]=[3,2,7]
suitable_name_numbers[9][7]=[5,6]
avoid_name_numbers[9][7]=[8]
suitable_name_numbers[9][8]=[1,5,6]
avoid_name_numbers[9][8]=[2,7,8]
suitable_name_numbers[9][9]=[5,6,1]
avoid_name_numbers[9][9]=[2,7]


print("\n")
for line in f:    
    name=line.strip()
    if(len(name)>0):
        name_number,total_name_number=findNameNumber(name)
        name_strnt=name+" -> Name number="+str(name_number)+"("+str(total_name_number)+")"
        # print(name_strnt)
        if(total_name_number in suitable_name_numbers[day_number][sum_number]):
            suitable_names.append(name_strnt)
        elif(total_name_number in avoid_name_numbers[day_number][sum_number]):
            avoid_names.append(name_strnt)
        else:
            other_names.append(name_strnt)

f.close()
suitable_numbers_string=", ".join(map(str,suitable_name_numbers[day_number][sum_number]))
avoid_numbers_string=", ".join(map(str,avoid_name_numbers[day_number][sum_number]))
print("\nThe lucky numbers="+suitable_numbers_string)
print("The unlucky numbers="+avoid_numbers_string)
print("\n\nThe following names are suitable")
for name in suitable_names:
    print(name)
print("\n\n\nAvoid the following names")    
for name in avoid_names:
    print(name)
print("\n\n\nThe following names are not in above two categories")    
for name in other_names:
    print(name)
