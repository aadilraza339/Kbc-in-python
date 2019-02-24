answer_key =[1,3,1,1]
question_list = [ "Q.1 Which country is Delhi located in?", "Q.2 What is the capital of India?", "Q.3 what in my name?", "Q.4 what is my fovret phone"]
first_options_list=["1 India", "1 Chandigarh", "1 aadil", "1 oppo", ]
second_options_list=["2 usa", "2 bhopal", "2 parkash", "2 sumsamg"]
third_options_list=["3 france", "3 delhi","3 sunil", "3 vivo"]
fourth_options_list=[ "4 Czech Republic", "4 jaipur", "4 pareet", "4 nokia"]
all_options_list=["first_options_list", "second_options_list", "third_options_list", "fourth_options_list"]
a=0
while a<len("list"):
	print question_list[a]
	print first_options_list[a]
	print second_options_list[a]
	print third_options_list[a]
	print fourth_options_list[a]
	user=int(raw_input("chose your answer 1 2 3 4 >"))
	if user==answer_key[a]:
		print "answer sahi hai "
	else:
		print "worge anwer"
		break
	a=a+1
	