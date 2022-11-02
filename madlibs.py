from colored import fg
blue = fg('blue')
yellow = fg('yellow')
red = fg('red')
print(yellow + "*HALLOWEEN THEMED* madlibs.")

ADJ1 = red + input("Adjective: ")
ADJ2 = red + input("Adjective: ")
N = red + input("Noun: ")
VB = red + input("Verb that ends in 'g': ")

madlibs = blue + f"Halloween is my favourite holiday. It's so {ADJ1}! "
line2= blue + f"This year, I'm going to dress up as a {ADJ2} {N}."
line3= blue + f"After that me and my friends will go {VB}."
line4 = blue + f"SPOOKY!."

print(madlibs + line2 + line3 + line4)
