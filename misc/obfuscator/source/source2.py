x = "'0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[\\]^_`{|}~ \n"

def hello_msg():
    t = x[73]+x[73]+x[73]+x[51]+x[38]+x[42]+x[57]+x[55]+x[39]+x[37]+x[56]+x[51]+x[54]+x[73]+x[73]+x[73]
    return t    


def intro_msg():
    t = x[59]+x[44]+x[37]+x[56]+x[93]+x[45]+x[55]+x[93]+x[56]+x[44]+x[41]+x[93]+x[55]+x[41]+x[39]+x[54]+x[41]+x[56]+x[76]
    return t


def get_pass():
    t = input()
    return t


def check_pass(psw):
    if psw == x[48]+x[19]+x[16]+x[30]+x[93]+x[30]+x[18]+x[15]+x[93]+x[26]+x[22]+x[11]+x[24]+x[15]+x[81]+x[93]+x[44]+x[25]+x[33]+x[81]+x[93]+x[56]+x[18]+x[15]+x[28]+x[15]+x[29]+x[93]+x[24]+x[25]+x[30]+x[18]+x[19]+x[24]+x[17]+x[93]+x[30]+x[25]+x[93]+x[29]+x[30]+x[11]+x[24]+x[14]+x[93]+x[25]+x[24]:
        return homelander_name()
    else:
        return Butcher_name()
    

def homelander_name():
    return x[18]+x[25]+x[23]+x[15]+x[22]+x[11]+x[24]+x[14]+x[15]+x[28]

def Butcher_name():
    return x[38]+x[31]+x[30]+x[13]+x[18]+x[15]+x[28]


def get_out_msg():
    t = x[45]+x[93]+x[14]+x[25]+x[24]+x[30]+x[93]+x[23]+x[11]+x[21]+x[15]+x[93]+x[23]+x[19]+x[29]+x[30]+x[11]+x[21]+x[15]+x[29]+x[74]+x[93]+x[45]+x[23]+x[93]+x[24]+x[25]+x[30]+x[93]+x[20]+x[31]+x[29]+x[30]+x[93]+x[22]+x[19]+x[21]+x[15]+x[93]+x[30]+x[18]+x[15]+x[93]+x[28]+x[15]+x[29]+x[30]+x[93]+x[25]+x[16]+x[93]+x[35]+x[25]+x[31]+x[74]+x[93]+x[45]+x[23]+x[93]+x[55]+x[56]+x[54]+x[51]+x[50]+x[43]+x[41]+x[54]+x[74]+x[93]+x[45]+x[23]+x[93]+x[55]+x[49]+x[37]+x[54]+x[56]+x[41]+x[54]+x[74]+x[93]+x[45]+x[23]+x[93]+x[38]+x[41]+x[56]+x[56]+x[41]+x[54]+x[72]+x[93]+x[45]+x[93]+x[37]+x[49]+x[93]+x[38]+x[41]+x[56]+x[56]+x[41]+x[54]+x[63]
    return t

def win_msg():
    t = x[45]+x[93]+x[17]+x[25]+x[30]+x[93]+x[30]+x[25]+x[93]+x[17]+x[25]+x[93]+x[28]+x[31]+x[24]+x[93]+x[22]+x[19]+x[24]+x[15]+x[29]+x[93]+x[33]+x[19]+x[30]+x[18]+x[93]+x[50]+x[25]+x[19]+x[28]
    return t

def flag_msg():
    t = x[44]+x[15]+x[28]+x[15]+x[93]+x[19]+x[29]+x[93]+x[35]+x[25]+x[31]+x[28]+x[93]+x[16]+x[22]+x[11]+x[17]+x[93]+x[19]+x[93]+x[13]+x[11]+x[24]+x[93]+x[12]+x[25]+x[30]+x[18]+x[15]+x[28]+x[93]+x[33]+x[28]+x[11]+x[26]+x[26]+x[19]+x[24]+x[17]+x[93]+x[19]+x[30]+x[93]+x[14]+x[25]+x[93]+x[19]+x[30]+x[93]+x[35]+x[25]+x[31]+x[93]+x[29]+x[15]+x[22]+x[16]+x[76]
    return t

def give_flag(name):
    if name == x[38]+x[31]+x[30]+x[13]+x[18]+x[15]+x[28]:
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
    
    
if __name__ == x[87]+x[87]+x[23]+x[11]+x[19]+x[24]+x[87]+x[87]:
    main()