#!/usr/bin/python3

from base64 import b16encode, b16decode, b32encode, b32decode, b64encode, b64decode, b85encode, b85decode, encode, decode
from colorama import Fore
from binascii import Error
import argparse

parser = argparse.ArgumentParser(usage = 'base -h', add_help = False)
parser.add_argument('-h', '--help', action = 'store_true')
parser.add_argument('-b16', action = 'store_true')
parser.add_argument('-b32', action = 'store_true')
parser.add_argument('-b64', action = 'store_true')
parser.add_argument('-b85', action = 'store_true')
parser.add_argument('-e', '--encode')
parser.add_argument('-d', '--decode')
args = parser.parse_args()

def banner():
    return f'''\n{Fore.RED}             _                    
            | |                   
            | |__   __ _ ___  ___ 
            | '_ \ / _` / __|/ _ /
            | |_) | (_| \__ \  __/
            |_.__/ \__,_|___/\___|
            

                  {Fore.BLUE}by z3ox1s
                    v0.0.1{Fore.WHITE}\n'''

def encode16(string):
    encodedBytes = b16encode(string.encode('ascii'))
    encodedString = encodedBytes.decode('ascii')
    print(f'{Fore.BLUE}Method: {Fore.WHITE}\n   Base16 Encode\n\n{Fore.BLUE}Result:\n   {Fore.WHITE}{encodedString}\n')

def decode16(string):
    decodedBytes = b16decode(string.encode('ascii'))
    decodedString = decodedBytes.decode('ascii')
    print(f'{Fore.BLUE}Method: {Fore.WHITE}\n   Base16 Decode\n\n{Fore.BLUE}Result:\n   {Fore.WHITE}{decodedString}\n')

def encode32(string):
    encodedBytes = b32encode(string.encode('ascii'))
    encodedString = encodedBytes.decode('ascii')
    print(f'{Fore.BLUE}Method: {Fore.WHITE}\n   Base32 Encode\n\n{Fore.BLUE}Result:\n   {Fore.WHITE}{encodedString}\n')

def decode32(string):
    decodedBytes = b32decode(string.encode('ascii'))
    decodedString = decodedBytes.decode('ascii')
    print(f'{Fore.BLUE}Method: {Fore.WHITE}\n   Base32 Decode\n\n{Fore.BLUE}Result:\n   {Fore.WHITE}{decodedString}\n')

def encode64(string):
    encodedBytes = b64encode(string.encode('ascii'))
    encodedString = encodedBytes.decode('ascii')
    print(f'{Fore.BLUE}Method: {Fore.WHITE}\n   Base64 Encode\n\n{Fore.BLUE}Result:\n   {Fore.WHITE}{encodedString}\n')

def decode64(string):
    decodedBytes = b64decode(string.encode('ascii'))
    decodedString = decodedBytes.decode('ascii')
    print(f'{Fore.BLUE}Method: {Fore.WHITE}\n   Base64 Decode\n\n{Fore.BLUE}Result:\n   {Fore.WHITE}{decodedString}\n')

def encode85(string):
    encodedBytes = b85encode(string.encode('ascii'))
    encodedString = encodedBytes.decode('ascii')
    print(f'{Fore.BLUE}Method: {Fore.WHITE}\n   Base85 Encode\n\n{Fore.BLUE}Result:\n   {Fore.WHITE}{encodedString}\n')

def decode85(string):
    decodedBytes = b85decode(string.encode('ascii'))
    decodedString = decodedBytes.decode('ascii')
    print(f'{Fore.BLUE}Method: {Fore.WHITE}\n   Base85 Decode\n\n{Fore.BLUE}Result:\n   {Fore.WHITE}{decodedString}\n')

print(banner())

try:
    if args.help == True:
        print(f'''
{Fore.GREEN}Help:{Fore.WHITE}
 {Fore.YELLOW}-h, --help         Help message.
 -b16               Base16 option.
 -b32               Base32 option.
 -b64               Base64 option.
 -b85               Base85 option.
 -e, --encode       Encode statement.
 -d, --decode       Decode statement.{Fore.WHITE}

{Fore.GREEN}Examples:{Fore.WHITE}
 {Fore.YELLOW}base -b64 -e 'Test'
 base -b64 -d 'VGVzdA=='{Fore.WHITE}
''')

    if args.b16 == True:
        if args.encode:
            encode16(args.encode)

        elif args.decode:
            decode16(args.decode)

    elif args.b32 == True:
        if args.encode:
            encode32(args.encode)

        elif args.decode:
            decode32(args.decode)

    elif args.b64 == True:
        if args.encode:
            encode64(args.encode)

        elif args.decode:
            decode64(args.decode)

    elif args.b85 == True:
        if args.encode:
            encode85(args.encode)

        elif args.decode:
            decode85(args.decode)

except Error:
    print(f'[{Fore.RED}-{Fore.WHITE}] {Fore.RED}Incorrect input!{Fore.WHITE}\n')

except:
    print(f'[{Fore.RED}-{Fore.WHITE}] {Fore.RED}An error has occurred!{Fore.WHITE}\n')
