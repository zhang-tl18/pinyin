from math import log
import json

class core:
    def __init__(self, lamb = 0.99999):
        self.__chars = []
        self.__pinyin2cids = {}
        self.__mode = []
        self.__lamb = lamb

    def load(self, dic_file, mode_file):
        with open(dic_file, "r") as f:
            dic = json.load(f)
            self.__chars = dic["chars"]
            self.__pinyin2cids = dic["pinyin2cids"]

        with open(mode_file, "r") as f:
            self.__mode = json.load(f)

    def translate_pinyin(self, sentense):
        pinyin_list = sentense.replace('\n','').replace('\r','').split(' ')
        rounds = []
        for p in pinyin_list:
            rounds.append(self.__pinyin2cids[p])

        n = len(rounds)
        power_cur = power_last = {}
        from_mat = [{} for i in range(n)]

        for r in range(n):
            times_all = sum([self.__mode[i]['times'] for i in rounds[r]])
            for id_cur in rounds[r]:
                if r != 0:
                    d = 1e9
                    from_e = -1
                    for id_last in rounds[r-1]:
                        if id_cur in self.__mode[id_last]['next']:
                            tmp1 = self.__mode[id_last]['next'][id_cur]/self.__mode[id_last]['times']
                        elif str(id_cur) in self.__mode[id_last]['next']:
                            tmp1 = self.__mode[id_last]['next'][str(id_cur)]/self.__mode[id_last]['times']
                        else:
                            tmp1 = 0
                        tmp2 = self.__mode[id_cur]['times']/times_all if self.__mode[id_cur]['times']>0 else 1/times_all
                        dis = -log(self.__lamb*tmp1 + (1-self.__lamb)*tmp2)
                        if dis+power_last[id_last] < d or from_e == -1:
                            d = dis+power_last[id_last]
                            from_e = id_last
                    power_cur[id_cur] = d
                    from_mat[r][id_cur] = from_e
                else:
                    dis = self.__mode[id_cur]['times']/times_all if self.__mode[id_cur]['times']>0 else 1/times_all
                    dis = -log(dis)
                    power_cur[id_cur] = dis
                    from_mat[r][id_cur] = -1
            power_last = power_cur
            power_cur = {}

        e = -1
        for i in rounds[n-1]:
            if e == -1 or power_last[i] < power_last[e]:
                e = i
        
        ans = ''
        for i in range(n-1, -1, -1):
            c = self.__chars[e]
            ans = c + ans
            e=from_mat[i][e]

        return ans
    
    def translate_while_input(self):
        st = input()
        while st != 'q':
            print(self.translate_pinyin(st))
            st = input()

    def translate_file(self, in_file, out_file):
        with open(in_file, "r") as inf:
            with open(out_file, "w") as outf:
                st = inf.readline()
                while st:
                    outf.write(self.translate_pinyin(st)+'\n')
                    st = inf.readline()
