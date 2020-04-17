import argparse
import re
from .vazha_to_eng import *

cmd_parser = argparse.ArgumentParser(fromfile_prefix_chars='@')

cmd_parser.add_argument('script', type=open,help='python script file')

cmd_parser.add_argument('-v',
                       '--verbose',
                       action='store_true',
                       help='an optional argument')

# Execute parse_args()
args,unknown_args = cmd_parser.parse_known_args()

def compile():
    python_script = args.script.read()
    for i in keywords:
        python_script = re.sub(i,keywords[i],python_script)
    for i in built_ins:
        python_script = re.sub(i,built_ins[i],python_script)
    exec(python_script)


    