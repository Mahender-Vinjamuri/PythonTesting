itemsInCart = 0
if itemsInCart != 2:
    pass
    #raise Exception("Products count in cart is not matched")

assert (itemsInCart == 0)

# try, catch/except - 1
# try:
#     with open("test.txt", 'r') as reader:
#         reader.read()
#         print("i am in try block")
#
# except:
#     print("iam in exception block")
#
# try, catch/except - 2
# try:
#     with open("filelog.txt", 'r') as reader:
#         reader.read()
#         print("i am in try block")
#
# except:
#     print("iam in exception block")

#try, catch/except - 3
try:
    with open("filelog.txt", 'r') as reader:
        reader.read()
        print("i am in try block")

except Exception as e:
    print(e)

finally:
    print("this code will execute whether the test is Pass/Fail")
