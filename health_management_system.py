print("log or retrieve")
log_retrieve = int(input("1 for log, 2 for retrieve:  "))
f_e = int(input("1 for ex and 2 for food: "))
customer = int(input("1:harry,2:parva,3:swapnil: "))

if log_retrieve==1:
    if f_e==1:
        if customer==1:
            with open("harry_ex.txt","a") as f:
                ex= input("enter ex : ")
                f.write(ex + "\n")
if log_retrieve==1 and f_e==1 and customer==2:
    with open("parva_ex.txt","a") as f:
        ex= input("enter ex name: ")
        f.write(ex + "\n")

if log_retrieve==1 and f_e==1 and customer==3:
    with open("swapnil_ex.txt","a") as f:
        ex = input("enter ex name: ")
        f.write(ex + "\n")

if log_retrieve==1 and f_e==2 and customer==1:
    with open("harry_f.txt","a") as f:
        food = input("enter food: ")
        f.write(food + "\n")

if log_retrieve==1 and f_e==2 and customer==2:
    with open("parva_f.txt","a") as f:
        food = input("enter food: ")
        f.write(food + "\n")
if log_retrieve==1 and f_e==2 and customer==3:
    with open("swapnil_f.txt","a") as f:
        food = input("enter food: ")
        f.write(food + "\n")

if log_retrieve==2 and f_e==1 and customer==1:
    f=open("harry_ex.txt")
    print(f.read())
    f.close

if log_retrieve==2 and f_e==1 and customer==2:
    f=open("parva_ex.txt")
    print(f.read())
    f.close

if log_retrieve==2 and f_e==1 and customer==3:
    f=open("swapnil_ex.txt")
    print(f.read())
    f.close

if log_retrieve==2 and f_e==2 and customer==1:
    f=open("harry_f.txt")
    print(f.readline())
    f.close

if log_retrieve==2 and f_e==2 and customer==2:
    f=open("parva_f.txt")
    print(f.read())
    f.close

if log_retrieve==2 and f_e==2 and customer==3:
    f=open("swapnil_f.txt")
    print(f.read())
    f.close