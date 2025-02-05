names = ("Gavin", "Nathan", "Muntag","Shahood","Mason","Leo","Christopher","Marcos","Aidan","Ryan")
nicks = ("Mr. Carnival","Nate","Muntag","Shahood","Mason","Leo","Chris","Marcos","Aidan","Ryan")
dob = ("unknown","unknown","unknown","unknown","unknown","unknown","unknown","unknown","unknown")
phone = ("1+###-###-####","1+###-###-####","1+###-###-####","1+###-###-####","1+###-###-####","1+###-###-####","1+###-###-####","1+###-###-####","1+###-###-####")
email = ("267764@burlcoschools.org","268021@burlcoschools.org","268154@burlcoschools.org","267741@burlcoschools.org","268262@burlcoschools.org","268095@burlcoschools.org","268359@burlcoschools.org","267895@burlcoschools.org","267922@burlcoschools.org","267947@burlcoschools.org")
person = input("Enter Index (0-9): ")

print("Subject name:",names[int(person)],
" Nickname:",nicks[int(person)],
"  Date of Birth:",dob[int(person)],
"  Phone number:",phone[int(person)],
"  Email:",email[int(person)])