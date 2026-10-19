def add_two_numbers() -> int:
    x=input()
    s=x.split(",")
    sum=0
    for i in s:
        sum+=int(i)

    return(sum)


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
