import os
from os import system

banner = """┌─┐┌─┐┌┐┌  ┬  ┌─┐┌─┐┬┌─┬ ┬┌─┐
├─┤└─┐│││  │  │ ││ │├┴┐│ │├─┘
┴ ┴└─┘┘└┘  ┴─┘└─┘└─┘┴ ┴└─┘┴
"""

asn = input(banner + "\n➞ ")
os.system(f'curl https://api.hackertarget.com/aslookup/?q=%s' % asn)
print("\n\nHave a nice day!")
