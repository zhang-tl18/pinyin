from accuracy import calacc
from core import core


def test(pre_file, train_file, input_file, output_file, ans_file):
    for lamb in (0.9, 0.99, 0.999, 0.9999, 0.99999, 0.999999, 0.9999999):
        print(lamb)
        mycore = core(lamb)
        mycore.load(pre_file, train_file)
        mycore.translate_file(input_file, output_file)
        calacc(output_file, ans_file)