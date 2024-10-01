   

def hello_msg():
    t = '---OBFUSCATOR---'
    return t    


def intro_msg():
    t = "WHAT IS THE SECRET:"
    return t


def get_pass():
    t = input()
    return t


def check_pass(psw):
    if psw == "Lift the plane? How? Theres nothing to stand on":
        return homelander_name()
    else:
        return Butcher_name()
    

def homelander_name():
    return "homelander"

def Butcher_name():
    return "Butcher"


def get_out_msg():
    t = "I dont make mistakes. Im not just like the rest of you. Im STRONGER. Im SMARTER. Im BETTER, I AM BETTER!"
    return t

def win_msg():
    t = "I got to go run lines with Noir"
    return t

def flag_msg():
    t = "Here is your flag i can bother wrapping it do it you self:"
    return t

def give_flag(name):
    if name == "Butcher":
        return get_out_msg()
    else:
        e = ''
        f = [0x49,0x75,0x78,0x42,0x79,0x2e,0x2e,0x6d,0x42,0x69,0x2e,0x75,0x2e,0x42,0x7f,0x78,0x6e,0x69]
        for c in f:
            e += chr(c ^ 0x1d)
        print(win_msg())
        print(flag_msg())
        return e
        
        

def main():
    h = hello_msg()
    print(h)
    m = intro_msg()
    print(m)
    i = get_pass()
    p = check_pass(i)
    f = give_flag(p)
    print(f)
    
    
if __name__ == "__main__":
    main()