"""
Makes a folder in the format 'code - name' which contains following 3 file:
- code.cpp (with basic starter code)
- code.in
- code.out

arguments:
'1: problem code'
'2: problem name'
'[3: path to make the folder in | last path used if missing]')
"""

import sys
import os
import cp_mod


try:
    # If help argument is passed
    if sys.argv[1] == 'help' or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        _help = ('arguments:\n'
                '-uva\n'
                    '1: problem code\n'
                    '2: problem name\n'
                    '[3: path to make the folder in | last path used if missing]')

        print(_help)

    # For uva problems
    elif sys.argv[1] == '-uva':
        try:
            path, problem_num, problem_name = cp_mod.get_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        except IndexError:
            path, problem_num, problem_name = cp_mod.get_data(sys.argv[1], sys.argv[2], sys.argv[3])

        path = path + problem_num + '-' + problem_name + '\\'

        cp_mod.make_uva_folder(path, problem_num)

    # For Kattis problems
    elif sys.argv[1] == '-k':
        try:
            path, problem_num, problem_name = cp_mod.get_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        except IndexError:
            path, problem_num, problem_name = cp_mod.get_data(sys.argv[1], sys.argv[2], sys.argv[3])

        path = path + problem_num + '-' + problem_name + '\\'

        cp_mod.make_kattis_folder(path, problem_num)

    # For Kattis debug all
    elif sys.argv[1] == '-kda':
        path, problem_num, problem_name = cp_mod.get_data(sys.argv[1])
        path = path + problem_num + '-' + problem_name + '\\'

        cp_mod.debug_full(path, problem_num)

    # For kattis just output n test cases
    elif sys.argv[1] == '-ko' and int(sys.argv[2]) > 0:
        path, problem_num, problem_name = cp_mod.get_data(sys.argv[1])
        path = path + problem_num + '-' + problem_name + '\\'

        cp_mod.output(int(sys.argv[2]), path, problem_num)

    # For kattis output all
    elif sys.argv[1] == '-koa':
        path, problem_num, problem_name = cp_mod.get_data(sys.argv[1])
        path = path + problem_num + '-' + problem_name + '\\'

        cp_mod.output(-1, path, problem_num)

    # For Kattis output on terminal
    elif sys.argv[1] == '-kot' and int(sys.argv[2]) > 0:
        path, problem_num, problem_name = cp_mod.get_data(sys.argv[1])
        path = path + problem_num + '-' + problem_name + '\\'

        cp_mod.output_termial(int(sys.argv[2]), path, problem_num)

    # For kattis output all on termial
    elif sys.argv[1] == '-koat' or sys.argv[1] == '-kota':
        path, problem_num, problem_name = cp_mod.get_data(sys.argv[1])
        path = path + problem_num + '-' + problem_name + '\\'

        cp_mod.output_termial(-1, path, problem_num)

    # View current problem
    elif '-v' in sys.argv[1]:
        path, problem_num, problem_name = cp_mod.get_data(sys.argv[1])
        print("PROBLEM ID:", problem_num)
        print("PROBLEM NAME:", problem_name)
        if 'a' in sys.argv[1]:
            print("PROBLEM PATH:", path)

            
    # Set current problem -su for uva, -sk for kattis
    elif '-s' in sys.argv[1]:
        try:
            path, problem_num, problem_name = cp_mod.get_data(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        except IndexError:
            path, problem_num, problem_name = cp_mod.get_data(sys.argv[1], sys.argv[2], sys.argv[3])

    else:
        print("Invalid Arguments. Exiting...")

except IndexError or ValueError:
    print("Invalid Arguments. Exiting...")
