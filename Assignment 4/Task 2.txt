#Task 2 
user_input = input("Enter the data:")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")
print("your data is successfully written to output.txt. ")
    
additional_data = input("Enter the additional data to append:")
with open("output.txt", "a") as file:
    file.write(additional_data + "\n")
print("your data is append successfully.")

print("The final content of output.txt:")
with open("output.txt", "r") as file:
    content=file.read()
    print(content)
