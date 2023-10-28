# lim = 6
# for i in range(0, lim):
#     print("* "*i)

def main():
    lim = 10
    with open("star.txt", "w") as fl:
        for i in range(0, lim):
            content = "* "*i + "\n"
            fl.write(content)
            print(content)
    
main()