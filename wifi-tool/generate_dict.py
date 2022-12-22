import itertools as its
# a set of password characters
words = "1234567890abcdefghijklmnopqrstuvwxyz"
# random combination of 9 characters
r =its.product(words,repeat=9)
# store wifi combinations in file
dic = open("pwd.txt","a")
for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))
dic.close()