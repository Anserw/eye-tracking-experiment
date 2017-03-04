from Experiment import Experiment
import logging
import sys
import argparse

def set_log_format():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(threadName)-12s %(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='experiment.log',
                        filemode='a')

    console = logging.StreamHandler(sys.stdout)
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(filename)-12s line:%(lineno)d: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    console_err = logging.StreamHandler(sys.stderr)
    console_err.setLevel(logging.ERROR)
    formatter = logging.Formatter('%(filename)-12s line:%(lineno)d: %(levelname)-8s %(message)s')
    console_err.setFormatter(formatter)
    logging.getLogger('').addHandler(console_err)

def main():
    parser = argparse.ArgumentParser(description="Assign task for a user based on the data in DB.")

    parser.add_argument("-w", "--workpath", type=str, help="work path")
    parser.add_argument("-i", "--interpreter", type=str, help="interpreter such as python")
    parser.add_argument("-t", "--task", type=str, help="binary file or script")
    parser.add_argument("-c", "--continue", type=int, help="continue from i th video")
    set_log_format()
    exp = Experiment()
    exp.start()

if __name__ == '__main__':
    main()