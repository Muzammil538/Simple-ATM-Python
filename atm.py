
#These are the users or Account holders of the BAnk
Holders_cdno = {12345678}
Holders_pass = {1234}
#here we will take the input of the user card number
ac = int(input("Enter your Card Number : "))


def ac_cardChk():
    if ac in Holders_cdno:
            print("Welcome")
    else:
        print("You are non-existing User")
        quit()
ac_cardChk()
# print(ac_cardChk())
# ac_decl = (ac , "is your card number")
# print(ac_decl)
# ac_clar = input("if your card number is correct , enter 1, if not enter 2 : ")
# def ac_check():
#     if ac_clar == "1":
#         print("Thanks")
#     else:
#         quit()
# print(ac_check())
ac_pass = int(input("Enter your PIN : "))
def ac_pass_Chk():
    if ac_pass in Holders_pass:
        pass
    else:
        print("INcorrect PIN")
        quit()
ac_pass_Chk()

print('''What do you want to do 
\n 1.Withdraw \n 2. Check Balance \n 3. Add Balance \n''')
x = input(" : ")
balc = 10000
limit = 5000
#from withdraw import witdr_ac
def option():
    if x == '1':
        print('''Welcome , Here you Can Withdraw Your Ammount \n''')
        witdr = int(input("Enter The Amount : "))

        def witdr_ac():
            if witdr < balc:
                print("Transaction Successfull ")
            else:
                print("In-safficiant Balance")
                quit()
        witdr_ac()
    elif x == '2':
        print(balc)
    elif x == '3':
        print('AB')
    else:
        quit()
option()
print(f"Thanks for coming.")