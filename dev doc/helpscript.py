example = '<li><div class="vbox"><div class="velement" id=" IDValue "> elValue </div>'
example = '<div>T<span class="sub"> elIndex </span></div></div></li>'
l0 = '<li>'
s0 = '<div class="vbox" id="stage3S' 
IDValue = 0;
s1 = '"><div class="velement">'
elValue = 0;
s2 = '</div><div>S<span class="sub">'
elIndex = 0;
s3 = '</span></div></div>'
l1 = '</li>'

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
    for x in range(3, 253):
        xstr = str(x)
        vectors = l0 + s0 + xstr + s1 + xstr + s2 + xstr + s3 + l1 + '\n'
        with open("canvas5.txt", "a") as f:
            f.write(vectors)
        
def f4 ():
    for x in range(253, 256):
        xstr = str(x)
        vectors = s0 + xstr + s1 + xstr + s2 + xstr + s3 + '\n'
        with open("canvas7.txt", "a") as f:
            f.write(vectors)        
        
        

f4()
