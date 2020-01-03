#if statement. conditional

is_male = False
is_tall = True
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male or tall")

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("you are a short male")
elif not(is_male) and is_tall:
    print("you are a not male but you are tall")
else:
    print("You are either not male or not tall or both")

#if statements and comparisons

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

result = max_num(3, 36534, 4)
print(result)