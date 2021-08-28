print('wellcome to kbc program:')
q=[
    "How many continents are there?",             
    "What is the capital of India?",            
    "NG mei kaun se course padhaya jaata hai?"   
]

o=[
    ["Four", "Nine", "Seven", "Eight"],
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
fifty=[['seven','four'],['chennai','delhi'],['software engineering','tourism']]
fs=[1,2,1]
sl=[3, 4, 1]
i=0
count=0
while i<len(q):
    print("this is your",i+1,"question")
    print(i+1,q[i])
    print('these are your options:')
    j=0
    while j<len(o[i]):
        print(j+1,o[i][j])
        j=j+1
    n=int(input('select your options:'))
    if n==sl[i]:
        print('congratsss.......')
    elif n==5050:
        if count==0:
            k=0
            while k<len(fifty[i]):
                print(k+1,fifty[i][k])
                k=k+1
            count=count+1
            n1=int(input('select your options:'))
            if n1==fs[i]:
                print('right answer..')
            else:
                print('your answer is wrong')
                print("quit")
                break
        else:
            print('sorry u r already used..')
            n2=int(input('select ur options..'))
            if n2==sl[i]:
                print('congtats..')
            else:
                print('wrong answer')
                break
    else:
        print("wrong answer you can quit your game")
        break
    i=i+1                        
        
    




