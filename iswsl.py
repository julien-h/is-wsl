import sys
import platform

# Relevant doc
# https://docs.python.org/3.7/library/sys.html#sys.platform
# https://docs.python.org/3.7/library/platform.html#platform.release

def is_wsl():
    if sys.platform in ['win32', 'cygwin', 'darwin']:
        return False

    if 'Microsoft' in platform.release():
        return True

    try:
        if 'Microsoft' in open('/proc/version').read():
            return True
    except:
        pass

    return False
