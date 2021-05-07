def swapFiles():
    t = input("Enter the file name you need to swap: ")
    u = input("Enter the file name you need to swap with: ")

    with open(t,"r") as a:
        data_a = a.read()
    
    with open(u,"r") as b:
        data_b = b.read()
    
    with open(t,"w") as a:
        a.write(data_b)
    
    with open(u,"w") as b:
        b.write(data_a)

swapFiles()