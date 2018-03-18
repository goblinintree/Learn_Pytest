#coding=utf-8
from __future__ import print_function
import sys
import os
sys.path.append(os.path.join(os.getcwd()))
reload(sys)
sys.setdefaultencoding('utf-8')

import time
import shutil
import getopt
import webbrowser

def search_clear(rootdir,search_dir_name):
    if os.path.isdir(rootdir):
        list_new = os.listdir(rootdir)
        for  it in list_new:
            if it == search_dir_name: 
                #os.rmdir(os.path.join(rootdir,it)) #不能删除有文件的文件夹
                shutil.rmtree(os.path.join(rootdir,it))
            else:
                search_clear(os.path.join(rootdir,it),search_dir_name)

def main(argv):
    cases_package = ""
    cases_report = ""
    print(u"环境中python版本号: "+str(sys.version_info))
    argv_len = len(sys.argv)
    if argv_len > 1:
        print('Number of arguments:', len(sys.argv))
        print('argv are:', str(sys.argv))
        
    try:
        # 这里的 h 就表示该选项无参数，i:表示 i 选项后需要有参数
        opts, args = getopt.getopt(argv, "hp:r:",["package=", "report="])
    except getopt.GetoptError:
        print('Error: test_arg.py -p <package names> -r <report path>')
        print('\t\tor: test_arg.py --package=<inputfile> --report=<outputfile>')
        sys.exit(2)
    else:
        if args:
            print(args)
        pass

    for opt, arg in opts:
        if opt == "-h":
            print('Error: test_arg.py -p <package names> -r <report path>')
            print('\t\tor: test_arg.py --package=<inputfile> --report=<outputfile>')
            sys.exit()

        elif opt in ("-p", "--package"):
            cases_package = arg.replace(';', ' ')
        elif opt in ("-r", "--report"):
            cases_report = arg
    pass
    if not cases_package:
        cases_package = " cases"
        pass
    if cases_report:
        if not cases_report.endswith('.html'):
            cases_report = cases_report + "/report.html"
            pass
    else:
        cases_report=" --html=path/report.html"
        pass
    print("*" * 80)
    return cases_package, cases_report 

def do_exec():
    cases_package, cases_report  = main(sys.argv[1:])
    print(cases_report)
    package_list = cases_package.split(' ')
    for pak in package_list:
        search_clear(pak, "__pycache__")
        pass
    entry = "import pytest;  pytest.cmdline.main(\" "+ cases_package + " " + cases_report+" \")"

    print(entry)
    exec(entry, locals())
    return cases_report 

if __name__ == "__main__":
    cases_report = do_exec()
    report_file=cases_report[8:]
    print(">" * 80 + cases_report)
    webbrowser.open_new_tab(os.path.join(os.getcwd(), report_file))
    pass