"""
NOTE: replace all 'H:\\Documents\\Scripts\\CP\\data\\cp.dat' to 'H:\\Documents\\Scripts\\CP\\data\\cp.dat'
      before using final build.
"""

import os
import dload

def parse_num(num):
    """
    Parses a < 5 digit number into a 5 digit number

    Example: 282 to 00282
    """

    num = str(num)
    
    try:
        num = int(num)
        num = str(num)
        if len(num) < 5:
            return ( ( '0'*(5 - len(num)) ) + num)

    except ValueError:
        return num

    return num


def parse_name(arg, problem_name = ""):
    problem_name = problem_name.replace(' ', '_')
    if 'k' in arg:
        problem_name = problem_name + '_Kattis'

    return problem_name


def get_data(arg, problem_num = "", problem_name = "", path_arg = ""):
    """
    Returns path
    The path is saved if sys.argv[3] exists
    else reads the last path.
    """
    path = str()
    
    if problem_num != "" and problem_name != "" and path_arg != "":
        path = path_arg + '\\'
        problem_num = parse_num(problem_num)
        problem_name = parse_name(arg, problem_name)

        data_file = open('H:\\Documents\\Scripts\\CP\\data\\cp.dat', 'w')

        # Writing path
        data_file.write(path + '\n')

        # Writing problem code
        data_file.write(problem_num + '\n')

        # Writing prblem name
        data_file.write(problem_name + '\n')

        data_file.close()

        return (path, problem_num, problem_name)

    elif problem_num != "" and problem_name != "" and path_arg == "":
        data = open('H:\\Documents\\Scripts\\CP\\data\\cp.dat', 'r').readlines()
        path = data[0].rstrip('\n')
        problem_num = parse_num(problem_num)
        problem_name = parse_name(arg, problem_name)

        
        data_file = open('H:\\Documents\\Scripts\\CP\\data\\cp.dat', 'w')

        # Writing path
        data_file.write(path + '\n')

        # Writing problem code
        data_file.write(problem_num + '\n')

        # Writing prblem name
        data_file.write(problem_name + '\n')

        data_file.close()

        return (path, problem_num, problem_name)

    else:
        data = open('H:\\Documents\\Scripts\\CP\\data\\cp.dat', 'r').readlines()
        data[0] = data[0].rstrip('\n')
        data[1] = data[1].rstrip('\n')
        data[2] = data[2].rstrip('\n')

        return tuple(data)



def make_cpp_file(path, problem_num, flag = '-u'):
    """
    Makes a .cpp file with:
    - bits/stdc++.h imported
    - using namespace std
    - [freopen req. I/O] only if flag == -u
    - an empty main() function returning 0
    """
    cpp = open(path + problem_num + '.cpp', "w")

    if flag == '-u':
        code = ('#include <bits/stdc++.h>\n\n'
                'using namespace std;\n\n'
                'int main()\n'
                '{\n\n'
                '    freopen("' + problem_num + '.in", "r", stdin);\n'
                '    freopen("' + problem_num + '.out", "w", stdout);\n'
                '\n\n\n'
                '    return 0;\n'
                '}')

        cpp.write(code)
        cpp.close()
    elif flag == '-k':
        code = ('#include <bits/stdc++.h>\n\n'
                'using namespace std;\n\n'
                'int main()\n'
                '{\n'
                '\n\n'
                '    return 0;\n'
                '}')

        cpp.write(code)
        cpp.close()


def make_uva_folder(path, problem_num):
    try:
        # Creates problem folder
        os.mkdir(path)

        # C++ file
        make_cpp_file(path, problem_num)

        # Input file
        open(path + problem_num + '.in', "w").close()

        # Output file
        open(path + problem_num + '.out', "w").close()

    except FileExistsError:
        # If folder exists do nothing
        print ("Folder", path, "already exists. Exiting...")


def make_kattis_folder(path, problem_num):
    try:
        # Creates problem folder
        os.mkdir(path)

        # C++ file
        make_cpp_file(path, problem_num, '-k')

        # Creates test data folder
        test_data = path + 'Test_Data\\'
        os.mkdir(test_data)

    except FileExistsError:
        # If folder exists do nothing
        print ("Folder", path, "already exists. Exiting...")

    url = 'https://open.kattis.com/problems/' + problem_num + '/file/statement/samples.zip'
    dload.save_unzip(url, test_data, True)


def compare_output(ans, out, tc, path):

    if tc == 1:
        open(path + 'debug.txt', "w").close()


    log = open(path + 'debug.txt', "a")
    log.write("TESTCASE " + str(tc) + ':')


    line_no = err = 0
    for line1, line2 in zip(ans, out):
        line_no += 1

        line1 = line1.rstrip('\n')
        line2 = line2.rstrip('\n')
        if line1 != line2:
            err = 1
            log.write('\n' + str(line_no) + ':  ' + line2 + '  !=  ' + line1)

    
    if err == 0:
        log.write('\nAC')

    log.write('\n\n\n')


def compile_cpp(path, problem_num):
    _compile = 'g++ "' + path + problem_num + '.cpp" -o "' + path + problem_num + '.exe"'
    os.system('powershell.exe ' + _compile)


def output(total_outputs, path, problem_num):
    compile_cpp(path, problem_num)

    test_data_path = path + 'Test_Data\\'
    files = os.listdir(test_data_path)
    for file_name in files:
        if '.in' in file_name and (total_outputs > 0 or total_outputs == -1):
            name = file_name[0:-3]
            command = '("' + path + problem_num + '.exe" < "' \
                          + test_data_path + name + '.in") > "' \
                          + test_data_path + name + '.out"'

            if total_outputs > 0:
                total_outputs -= 1

            os.system(command)

def output_termial(total_outputs, path, problem_num):
    compile_cpp(path, problem_num)

    test_data_path = path + 'Test_Data\\'
    files = os.listdir(test_data_path)

    tc = 1

    for file_name in files:
        if '.in' in file_name and (total_outputs > 0 or total_outputs == -1):
            print("TESTCASE " + str(tc) + ":")
            name = file_name[0:-3]
            command = '("' + path + problem_num + '.exe" < "' \
                          + test_data_path + name + '.in")'

            if total_outputs > 0:
                total_outputs -= 1

            os.system(command)
            tc += 1
            print('\n')


def debug_full(path, problem_num):
    """
    Compiles c++ code, runs it against all test cases,
    and returns non-matching answers.

    path -> path to .cpp file
    problem_num -> name of the cpp file
    """

    # Generating output for all
    output(-1, path, problem_num)

    
    # Comparing outputs
    tc = 1
    test_data_path = path + 'Test_Data\\'
    files = os.listdir(test_data_path)
    for i in range(0, len(files), 3):
        ans = test_data_path + files[i]
        out = test_data_path + files[i + 2]

        ans = open(ans, "r")
        out = open(out, "r")

        compare_output(ans, out, tc, path)
        tc += 1


