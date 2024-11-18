text = "My path name is c:\\users\\Mahi"
print(text)  #My path name is c:\users\Mahi

# text1 = "My path name is c:\users\Mahi"
# print(text1)  #Error : single slash is interpreted as an escape character

text2 = r"My path name is c:\users\Mahi"
print(text2)  #My path name is c:\users\Mahi - Here r will tell python that not to treat \ as escape character

text3 = "0"
bool1 = bool(text3)
print(bool1)   #True : Non-empty String value

text4 = ""
bool2 = bool(text4)
print(bool2)   #False : Empty String value

i_am_None = None
print(i_am_None) #None
print(type(i_am_None)) #NoneType
print(bool(i_am_None)) #False

