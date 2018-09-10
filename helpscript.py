

s0 = '<li><div class="vbox"><div class="velement">'
s1 = '</div><div>S<span class="sub">'
s2 = '</span></div></div></li>'

t0 = '<li><div class="vbox"><div class="velement"> </div><div>T<span class="sub">'
t1 = '</span></div></div></li>'

k1 = '<option value="'
k2 = '">'
k3 = '</option>'


def f1 ():
    for x in range(3,253):
        x = str(x)
        vectors = s0 + x + s1 + x + s2 + '\n'
        with open("canvas.txt", "a") as f:
            f.write(vectors)



def f2 ():
    for x in range(5,256):
        x = str(x)
        vectort = t0 + x + t1 + '\n'
        with open("canvas1.txt", "a") as f:
            f.write(vectort)



def f3 ():
    for x in range(4, 257):
        x = str(x)
        vectork = k1 + x + k2 + x + k3 + '\n'
        with open("canvas2.txt", "a") as f:
            f.write(vectork)
        
f3()
