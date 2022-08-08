import chardet

def get_encoding(file):
    with open(file, 'rb') as f:
        data = f.read()
        return chardet.detect(data)['encoding']

def calacc(file1, file2):
    c_cor = c_all = 0
    s_cor = s_all = 0
    with open(file1, "r", encoding=get_encoding(file1)) as f1:
        with open(file2, "r", encoding=get_encoding(file2)) as f2:
            s1 = f1.readline()
            s2 = f2.readline()
            while s1 and s2:
                s_cor += s1==s2
                s_all += 1

                if len(s1) != len(s2):
                    print("Err: Character number is not equal", s1, s2)
                    continue
                for i in range(len(s1)):
                    c1,c2 = s1[i],s2[i]
                    c_cor += c1==c2
                    c_all += 1
                
                s1 = f1.readline()
                s2 = f2.readline()

            if s1 or s2:
                print("Err: Line number is not equal")
    
    print("character accuracy = {}/{} = {}%".format(c_cor, c_all, 100.0*c_cor/c_all))
    print("sentense  accuracy = {}/{} = {}%".format(s_cor, s_all, 100.0*s_cor/s_all))
