import sys, getopt
import pre, train, core, accuracy

def main(argv):
    usage = "main.py [-h]\n        [-r <pinyin_file> [<save_file>]]\n        [-t <dic_file> <train_path> [<save_file>]]\n        [-s [-i] [-f] <dic_file> <mode_file> [<input_file> <output_file>]]\n        [-a <file1> <file2>]"

    try:
        opts, args = getopt.getopt(argv[1:], "hrtsaif", ["help", "read", "train", "solve", "accuracy"])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)

    if len(opts)==0:
        print(usage)
        sys.exit(2)

    opt, arg = opts[0]
    # python main.py -h
    if opt in ('-h', '--help'):
        print(usage)
        sys.exit()

    # python main.py -r <chars_file> <pinyin_file> [<save_file>]
    if opt in ('-r', '--read'):
        if len(args) == 2:
            pre.read_char(args[0], args[1])
        elif len(args) == 3:
            pre.read_char(args[0], args[1], args[2])
        else:
            print("main.py -r <chars_file> <pinyin_file> [<save_file>]")
        sys.exit()

    # python main.py -t <dic_file> <train_path> [<save_file>]
    if opt in ('-t', '--train'):
        if len(args) == 2:
            train.train(args[0], args[1])
        elif len(args) == 3:
            train.train(args[0], args[1], args[2])
        else:
            print("main.py -t <dic_file> <train_path> [<save_file>]")
        sys.exit()
    
    # python main.py -s [-i] [-f] <dic_file> <mode_file> [<input_file> <output_file>]
    if opt in ('-s', '--solve'):
        if len(opts)==1 or len(args)==0:
            print("main.py -s [-i] [-f] <dic_file> <mode_file> [<input_file> <output_file>]")
            sys.exit(2)

        opt1, arg1 = opts[1]
        mycore = core.core(0.99999)
        mycore.load(args[0], args[1])
        if opt1 == '-i':
            mycore.translate_while_input()
        elif opt1 == '-f':
            mycore.translate_file(args[2], args[3])
        else:
            print("main.py -s [-i] [-f] <dic_file> <mode_file> [<input_file> <output_file>]")
        sys.exit()

    # python main.py -a <file1> <file2>
    if opt in ('-a', '--accuracy'):
        if len(args) == 2:
            accuracy.calacc(args[0], args[1])
        else:
            print("main.py -a <file1> <file2>")
        sys.exit()

    else:
        print(usage)
        sys.exit()


if __name__ == "__main__":
    main(sys.argv)
