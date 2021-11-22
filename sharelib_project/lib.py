def try_me(name):
    if name == "Moritz":
        return("Oh, it's you")
    else:
        return("Hello, " + name + "!")

name = input("Please enter your name:")
print(try_me(name))
