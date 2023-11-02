pyramid_height = int(input("Введіть висоту піраміди: "))
for i in range(1,pyramid_height+1):
    space = " " * (pyramid_height-i)
    stars = "*" * (2*i-1)
    print(space+stars)