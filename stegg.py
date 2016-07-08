import argparse
from steganographysaurus import stegg






if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='python3 stegg.py', usage='%(prog)s [options]')
    parser.add_argument('-f', '--file', nargs='?', help='the output file')
    #https://en.wikipedia.org/wiki/Steganography#Additional_terminology
    parser.add_argument("payload", type=str, help="the payload you want to encode")
    parser.add_argument("channel", type=str, help="the jpg/png (image) file you want to hide the message in")
    parser.add_argument("carrier", type=str, help="the output jpg/png (image) file the message is hidden in")
    parser.parse_args()


    """
    todo:
    1. validation of parameters: files, extensions, paths, payload
    2. the payload must allow data of any kind. a preprocessor to the steganographysaurus might inject jpg data, gpg data, text data etc.
    3. probably least significant bits in RGB bits will be used
    4. use different strategies for selecting the bits (algorithm changes)
    5. usable by importing module and usable as a cli script via stegg.py
    6. pip
    7. output generation as data or as file
    8. no detection by steganalysis tools
    9. minimal dependencies (preferably only via standard python modules available on any system)
    10. file manipulation: http://python-pillow.org/ with numpy https://github.com/python-pillow/Pillow

    sudo easy_install pip
    pip3 install pillow
    """

    # https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting
    # stderr: https://docs.python.org/3.0/whatsnew/3.0.html#print-is-a-function
    #print(" {0}".format(str(e)), file=sys.stderr)
    #sys.exit(1)

    #https://docs.python.org/3/library/errno.html