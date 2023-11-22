def main():
    """ The function starts a loop for taking customer input"""
    print("Our beloved customer, Please welcome to our Chatbot!")
    while True:
        user_input = input("User: ")
        answer = "Chattin:  we don't know, please help me"
        if str(user_input).lower() == "cancel":
            break
        print(answer)
    print("You cancelled, thanks and be back another time")

if __name__ == "__main__":
    main()