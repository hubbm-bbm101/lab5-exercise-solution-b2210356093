while True:
    mail = str(input(" --- Please enter a e-mail: "))
    if not("@" in mail) or not("." in mail):
        print(":( You entered a invalid e-mail")
    else:
        print(":) You entered a valid email.")
        break
input(" - Press any key to exit.")
