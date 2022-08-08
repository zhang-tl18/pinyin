import sys
import json

# python main.py -r <chars_file> <pinyin_file> [<save_file>]

def read_char(char_file, pinyin_file, save_file="./dic.json"):
    chars = []
    char2id = {}
    pinyins = []
    pinyin2cids = {}
    with open(char_file, "r") as cf:
        chars = list(''.join(cf.readlines()))
        char2id = {c:id for id,c in enumerate(chars)}
        print("Characters processed")
    
    with open(pinyin_file, "r") as pf:
        for line in pf.readlines():
            arr = line.replace('\n','').replace('\r','').split(' ')
            pinyins.append(arr[0])
            pinyin2cids[arr[0]] = [char2id[i] for i in arr[1:]]
        print("Pinyin processed")

    dic = {}
    dic["chars"] = chars
    dic["char2id"] = char2id
    dic["pinyins"] = pinyins
    dic["pinyin2cids"] = pinyin2cids
    with open(save_file, "w") as df:
        json.dump(dic, df)
    print("File saved")

if __name__ == "__main__":
    read_char(sys.argv[1], sys.argv[2])
