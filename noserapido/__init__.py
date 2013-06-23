"""
Rapid feedback notifier for Nose

Colors your terminal (green|blue) or red depending on test result.
For better experience, use with a watch tool such as nose-watch
"""

VERSION = (0, 0, 2)


def get_version():
    """
    Returns shorter version (digit parts only) as string.
    """
    return '.'.join((str(each) for each in VERSION[:4]))
