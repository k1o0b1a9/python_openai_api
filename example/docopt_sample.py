from docopt import docopt

__doc__ = """
Usage:
chatai.py [--version] [--help]
chatai.py --chat 
Options:
-h --help       ヘルプを表示する。
--version       バージョンを表示する。
"""

args = docopt(__doc__)