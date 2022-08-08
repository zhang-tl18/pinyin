from accuracy import calacc
from core import core


if __name__ == "__main__":
    for lamb in (0.9, 0.99, 0.999, 0.9999, 0.99999, 0.999999):
        print(lamb)
        mycore = core(lamb)
        mycore.load('./data/dic.json', './data/mode.json')
        mycore.translate_file('./data/test/input.txt', './data/test/output.txt')
        calacc('./data/test/ans.txt', './data/test/output.txt')