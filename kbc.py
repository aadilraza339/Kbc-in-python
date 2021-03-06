answer_key =[1,3,1,1]
question_list = [ "Q.1 Which country is Delhi located in?", "Q.2 What is the capital of India?", "Q.3 what in my name?", "Q.4 what is my favourite  phone"]
first_options_list=["1 India", "1 Chandigarh", "1 aadil", "1 oppo", ]
second_options_list=["2 usa", "2 bhopal", "2 parkash", "2 sumsamg"]
third_options_list=["3 france", "3 delhi","3 sunil", "3 vivo"]
fourth_options_list=[ "4 Czech Republic", "4 jaipur", "4 pareet", "4 nokia"]
all_options_list=["first_options_list", "second_options_list", "third_options_list", "fourth_options_list"]
a=0
while a<len("list"):
	print (question_list[a])
	print (first_options_list[a])
	print (second_options_list[a])
	print (third_options_list[a])
	print (fourth_options_list[a])
	user=int(input("chose your answer 1 2 3 4 >"))
	if user==answer_key[a]:
		print ("answer sahi hai ")
	else:
		print ("worge anwer")
		break
	a=a+1
	
##################################################### KBC CODE WITH 5050 ###########################################

que_list=["Who Invented computer","Who invented Internet","When was python developed","what is the fullform of www."]
opt_list=[["Vint cerf","Mark Jukerberg","Charls babbage","Robert Vintage"],["Vint cerf","vinton cerf", "Guido","John babbage"],["21 feb","20 feb","20 march","19 jan"],["world web wide","world wide web","world web webside","world wide webside"]]
ans_list=[3,1,2,2]
fifty_list=[["Charls babbage","Robert Vintage"],["vint cef","guido"],["21 feb","20 feb"],["world web wide","world wide web"]]
sol_list=[1,1,2,2]  

lifelinecount = 0
def lifeline(index):  
    global lifelinecount
    j=0 
    if(lifelinecount==0): 
        while j<len(fifty_list[index]):
            print(j+1,fifty_list[index][j])
            j=j+1
        user_ans = int(input('.....'))
        lifelinecount+=1
        if user_ans==sol_list[index]:
            return True
        else:
            return False
    else:
        print('you Already used 5050')
        return 'pass'

def option(index):
    j=0
    while j<len(opt_list[index]):
        print(j+1,opt_list[index][j])
        j=j+1
    user_ans = int(input('.....'))
    if user_ans==ans_list[index]:
        return True
    if user_ans == 5050:
        return(lifeline(index))
    else:
        return False

def que():
    index=0
    while index<len(que_list):
        print("Q.",index+1,que_list[index],"?")
        Result = option(index)
        if Result=="pass":
            index-=1
        elif Result==True:
            print("Congractualtion")
        else:
            print("you Losse !")
            break    
        index+=1

def main():
    que()
main()




	
