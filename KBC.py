
question_list = [
 "1.How many continents are there?",
 "2.What is the capital of India?",
 "3.NG mei kaun se course padhaya jaata hai?",
 "4.How many council member in navgurukul?"
]
options_list = [
 ["1.Four", "2.Nine", "3.Seven", "4.Eight"],
 ["1.Chandigarh", "2.Delhi", "3.Chennai", "4.Bhopal"],
 ["1.Software Engineering", "2.Counsiling", "3.Tourism", "4.Agriculture"],
 ["1.Ten","2.Nine","3.Five","4.Six"]
]
ans=[3,2,1,4]
_50_50=[["1.Four","2.Seven"],["1.Bhopal","2.Delhi"],["1.Software Engineering","2.counsiling"],["1.Six","2.Nine"]]
_ans=[2,2,1,2]
a=0
Rs=0
count=1
while a<len(question_list):
    print(question_list[a])
    c=0
    while c<len(options_list[a]):
        print(options_list[a][c])
        c+=1
    if count<=1:
        life_line=input("Are you needed life line:-")
        if "yes"==life_line or "YES"==life_line or "Yes"==life_line:
            d=0
            while d<len(_50_50[a]):
                print(_50_50[a][d])
                d+=1
            _ans1=int(input("enter your answer:-"))
            if _ans[a]==_ans1:
                Rs+=2000
                count+=1
                print("Answer is correct")
                print("Your wining amount is",Rs)
            else:
                print("Answer is not correct")
                break
        else:
            print("now,i don't needed life_line")
            ans1=int(input("Enter your answer:-"))
            if ans[a]==ans1:
                Rs+=2000
                print("Answer is correct")
                print("your wining amount is",Rs)
            else:
                print("Answer is incorrect")
                break
    else:
        ans1=int(input("enter your answer:-"))
        if ans[a]==ans1:
            Rs+=2000
            print("Answer is correct")
            print("your wining amount is",Rs)
        else:
            print("your answer is incorrect")
            break
    a+=1
print("Your wining amount is",Rs)