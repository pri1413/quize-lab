qlist =[]#dic
print("Quiz Application-:")
print('''Select Your Choice:
1. Attempt Quiz
2. Add Question
3. Exit''')
ch=0
while(ch != 3):
	ch=int(input("Enter Your Choice"))
	if ch == 1:
		print("Attempt Quiz Now")
		for q in qlist:
			rans=0
			wans=0
			print(q['qt'])
			print(q['A'])
			print(q['B'])
			print(q['C'])
			print(q['D'])
			ans= input("Answer")
			if q['CAns']==ans:
				rans=rans+1
			else:
				wans=wans+1
			if ans != q:
				print("Choose correct option")
			print("your right answer" ,+rans)
			print("your wrong answer" ,+wans)

	if ch == 2:
		q={}
		q['qt']=input("Enter Question")
		q['A']=input("A")
		q['B']=input("B")
		q['C']=input("C")
		q['D']=input("D")
		q['CAns']=input("Correct Option")
		qlist.append(q)
		print("Add New Question Here:")
