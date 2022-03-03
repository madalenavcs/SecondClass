try:
    age = input("how old are you?")
    print("in 2032 you will be", int(age) + 10)
    print(100/int(age))
except ValueError:
    print("Hey, that's not a number")
except ZeroDivisionError:
    print("you cannot devide by 0")
except:
    print("this is a new error that I did not see")
finally:
    print("this is what we do after all is done")
