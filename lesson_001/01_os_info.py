import platform
import sys

info='OS info in \n{}\n\nPython vmcaion in {} {}'.format(
    platform.uname(),sys.version,platform.architecture())
print(info)

with open('os_info.txt','w') as ff:
    ff.write(info)