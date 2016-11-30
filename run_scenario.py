#! /usr/bin/env python
# -*- coding: utf-8 -*-

# for Python3 print function
from __future__ import print_function

import sys
import yaml
from pprint import pprint, pformat
from argparse import ArgumentParser

# timestamp
from datetime import datetime

# clolor font
import colorama
from colorama import Fore, Back, Style

# PyEZ
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

# JSNAPy
from jnpr.jsnapy import SnapAdmin

from router import Router

def main():
    """main function."""

    # Parse argment
    parser = ArgumentParser(description='run scenario_file')
    parser.add_argument('-f', '--file',
                        type=str,
                        help='scenario file',
                        required=True)
    args = parser.parse_args()

    #Set color font
    colorama.init(autoreset=True)
    
    # Read router infomation file
    try:
        with open(args.file, 'r') as f:
            param_yaml = f.read()
    except (IOError, IndexError):
        sys.stderr.write('Cannot open file : ' + args.file + '\n')
        sys.exit(1)

    # Convert yaml format to python_type
    try:
        param = yaml.load(param_yaml)
    except ValueError as error:
        sys.stderr.write('YAML format error : \n')
        sys.stderr.write(param_yaml)
        sys.stderr.write(str(error))
        sys.exit(1)

    print(param['hosts']['management_ipaddress'])
    print(param['hosts']['username'])
    print(param['hosts']['password'])


    router1 = Router(
            ipaddress   = param['hosts']['management_ipaddress'],
            username    = param['hosts']['username'],
            password    = param['hosts']['password'])

    

    print('########## Run Senario : ' + args.file + ' ##########')

    print('operator : '         + param['operator'])
    print('operation_date : '   + str(param['operation_date']))
    print('hostname : '         + param['hosts']['hostname'])
    print('purpose :')
    print(param['purpus'])
    
    print('Operation Start : ', end='')
    print(Fore.GREEN + 'OK')


    print('Connect to ' + param['hosts']['hostname'] + ' : ', end='')
    router1.open()
    print(Fore.GREEN + 'OK')

    print('Lock configure mode : ', end='')
    router1.lock()
    print(Fore.GREEN + 'OK')

    print('Unlock configure mode : ', end='')
    router1.unlock()
    print(Fore.GREEN + 'OK')

    print('Close the connection to ' + param['hosts']['hostname'] + ' : ', end='')
    router1.close()
    print(Fore.GREEN + 'OK')

'''
    dev1 = Device(
            host = param['hosts']['device'],
            user = param['hosts']['username'],
            password = param['hosts']['password'],
            port = 22)
    dev1.open()
    dev1.bind(cu=Config)
    dev1.cu.lock()
    

    
    jsnapy = SnapAdmin()

    for menue in param['scenario']:
        pprint(menue)
        if 'test_' in menue:
            if menue ==  'test_hostname':
                run_test(device=dev1,jsnapy=jsnapy, menue=menue)
            elif menue == 'test_cpu':
                run_test(device=dev1,jsnapy=jsnapy, menue=menue)
        elif 'set_' in menue:
            #pass
            print(Fore.GREEN + 'set_')
        else:
            pass
            print(Fore.GREEN + 'else')
    
       
            
            

    print('Closing conection to ' + param['hosts']['hostname'] + ' : ', end='')

    dev1.cu.unlock()
    dev1.close()
    print(Fore.GREEN + 'OK')
'''

if __name__ == '__main__':
    main()

