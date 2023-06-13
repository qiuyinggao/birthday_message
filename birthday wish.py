print ("Recipient's Name: ")
recipient_name = input()

print("Year of Birth: ")
year_of_birth = int(input())

print("Personalised Message: ")
personal_message = input()

print("Sender's Name: ")
sender_name = input()

age = 2023 - year_of_birth

print(f"{recipient_name}, let's celebrate your {age} years of awesomeness! \nWishing you a day filled with joy and laughter as you turn {age}! \n\n{personal_message} \n\nWith love and best wishes, \n{sender_name}")