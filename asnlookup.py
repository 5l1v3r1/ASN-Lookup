import os
import sys


name = input('┌─┐┌─┐┌┐┌  ┬  ┌─┐┌─┐┬┌─┬ ┬┌─┐\n├─┤└─┐│││  │  │ ││ │├┴┐│ │├─┘\n┴ ┴└─┘┘└┘  ┴─┘└─┘└─┘┴ ┴└─┘┴  \n\n➞ ')
os.system('curl https://api.hackertarget.com/aslookup/?q=%s' % name)
