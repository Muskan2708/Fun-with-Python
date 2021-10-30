def extract_from_text(text):
    n=[]
    for t in text.split(' '):
        try:
            n.append(float(t))
        except ValueError:
            pass
    return n

def lcm(a,b):
    if a>b:
        L=a
    else:L=b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1

def hcf(a,b):
    if a<b:
        H=a
    else:H=b
    while H>=1:
        if H%a==0 and H%b==0:
            return H
        H-=1

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

def end():
    print('Thank you for having me....\n')
    input('enter key to exit')
    exit()
def undetermined():
    print('Sorry I am not able to understand this query\n')

operations={'ADD':add,'PLUS':add,'SUM':add,'ADDITION':add,'SUB':sub,'SUBTRACT':sub,'DIFFERENCE':sub,'MINUS':sub,'HCF':hcf,'LCM':lcm,'PRODUCT':mul,'MULTIPLICATION':mul,'MULTIPLY':mul,'DIVISION':div,'DIVIDE':div,'MOD':mod,'REMAINDER':mod,'MODULAS':mod}

commands={'EXIT':exit,'LEAVE':exit,'END':exit,'CLOSE':exit}
print('Hello I am your smart calculator. I am here to help you...\n')
while True:
    text=input('what do you want to calculate: ')
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                n=extract_from_text(text)
                o=operations[word.upper()] (n[0],n[1])
                print(o)
            except:
                print('something went wrong, please try again...')
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()] ()
            break
    else:
        undetermined()
