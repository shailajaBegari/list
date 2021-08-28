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
sl=[3, 4, 1]
i=0
j=0
count=0
while i<len(q) and j<len(o[i]):
    print("this is your",i+1,"question")
    print(i+1,q[i])
    print('these are your options:')
    print(j+1,o[j])
    j=j+1
    n=int(input('select your options:'))
    if n==sl[i]:
        print('congratsss.......')
    else:
        print("wrong answer")    
    i=i+1     