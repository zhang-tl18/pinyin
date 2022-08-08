import json
import os

# python main.py -t <dic_file> <train_path> [<save_file>]

def train(dic_file, train_path, save_file="./train.json"):
    chars = []
    char2id = {}
    with open(dic_file, "r") as rf:
        dic = json.load(rf)
        chars = dic["chars"]
        char2id = dic["char2id"]
    
    mode = [{'times':1, 'next':{}} for i in range(len(chars))]
    list_dir = os.listdir(train_path)
    for file_name in list_dir:
        if not os.path.isfile(train_path+'/'+file_name):
            continue
        with open(train_path+'/'+file_name, "r") as f:
            print("Train file: " + file_name)
            lines = f.readlines()
            for line in lines:
                try:
                    sentense = json.loads(line)["html"]
                except:
                    continue
                char_cur=char_last=''
                id_cur=id_last=-1
                for char_cur in sentense:
                    if char_cur in char2id:
                        id_cur = char2id[char_cur]
                        mode[id_cur]['times'] += 1
                        if char_last in char2id:
                            id_last = char2id[char_last]
                            mode[id_last]['next'][id_cur] = mode[id_last]['next'][id_cur]+1 if id_cur in mode[id_last]['next'] else 1
                        char_last = char_cur
                    else:
                        char_last = ''
    print("All files trained")
    with open(save_file, "w") as wf:
        json.dump(mode, wf)

if __name__ == "__main__":
    train("./dic.json", "./data/train")
