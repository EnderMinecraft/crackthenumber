import numpy
predefined = ['5', '1', '8', '9', '0']
mode = ""
num = ""
def check(inp,lim):
    if len(str(inp)) == lim:
        pass
    else:
        print(f"expected number to be {mode} character(s) long")
        start()

def logic(inp1, inp2):
    np1 = numpy.array(list(str(inp1)))
    np2 = numpy.array(inp2)
    correctarr = np1 == np2
    ret = correctarr.sum()
    print(f"{num}({ret})")

def guess(n,m):
    logic(num, predefined)
def start():
    global mode, num
    mode = int(input("choose how long is your number: "))
    num = int(input("choose ur number:"))
    check(num,mode)
    x= list(input("guess:"))
    guess(x,predefined)

start()

