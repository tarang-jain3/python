x=input('calculater\n for adding enter a\nfor subtraction enter s\nfor division enter d\nfor multipication enter m'
        '\nwhat do you want to do? ')
if x=="a":
    a = float(input('enter 1st number: '))
    b = float(input('enter second number: '))
    print(f"addtion of {a} and {b} is {a+b}")
elif x=="s":
    a = float(input('enter 1st number: '))
    b = float(input('enter second number: '))
    print(f"subtraction of {a} and {b} is {a-b}")
elif x=="d":
    a = float(input('enter 1st number: '))
    b = float(input('enter second number: '))
    print(f"division of {a} and {b} is {a/b}")
elif x=="m":
    a = float(input('enter 1st number: '))
    b = float(input('enter second number: '))
    print(f"multiplication of {a} and {b} is {a*b}")
else:
  print("invald input")