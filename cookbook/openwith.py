'''with open("./cookbook/hello.txt", "w") as my_file:
    my_file.write("Hello world \n")
    my_file.write("I hope you're doing well today \n")
    my_file.write("This is a text file \n")
    my_file.write("Have a nice time \n")'''

with open("./cookbook/hello.txt") as my_file:
    #print(type(my_file))
    for line in my_file:
        print(line)