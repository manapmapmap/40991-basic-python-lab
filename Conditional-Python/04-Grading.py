Score_1 = int(input("คะแนนเก็บ"))
Score_2 = int(input("คะแนนสอบกลางภาค"))
Score_3 = int(input("คะแนนสอบปลายภาค"))
Total = Score_1 + Score_2 + Score_3

if (Total>=80):
    print("A")
elif(Total<=75):
    print("B+")
elif(Total<=70):
    print("B+")
