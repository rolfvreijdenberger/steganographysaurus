from PIL import Image
import codecs
import os.path
import sys



def hide(payload, channel, carrier=None):
    """
    Hides the payload(message/file) in the channel(image file) and outputs
    to the carrier (to stdout as byte string or save as image file)
    :param payload:
    :param channel:
    :param carrier:
    :return:
    """
    try:
        # 1. get the payload as a bytes object
        payload = _convert_payload(payload)

        # 2. get the image to hide the payload in (aka: channel)
        if os.path.isfile(channel):
            # https://pillow.readthedocs.io/en/latest/
            image = Image.open(channel)
            image_output = image.copy()
            width, height = image_output.size
            payload_length = len(payload)
            size = width * height
            if payload_length * 3 > size:
                print(
                    "payload too large for carrier: {0} and {1}".format(
                        payload_length, size), file=sys.stderr)
            sys.exit(2)
        else:
            print("channel does not exist: {0}".format(channel),
                  file=sys.stderr)
            sys.exit(3)

    except Exception as e:
        # https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting
        # stderr: https://docs.python.org/3.0/whatsnew/3.0.html#print-is-a-function
        print(" {0}".format(str(e)), file=sys.stderr)
        sys.exit(1)
    else:
        pass
    finally:
        pass


def _convert_payload(payload):
    """
    converts the payload to binary
    :param payload: either a file or text
    :return:bytes
    """
    if os.path.isfile(payload):
        # what about /etc/passwd?
        try:
            # https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
            size = os.path.getsize(payload)
            file = open(payload, mode='rb')
            # tricky: big files take up memory
            output_payload = file.read()
            file.close()
        except IOError as e:
            print('unable to open file: {0}'.format(e), file=sys.stderr)
            sys.exit(4)
    elif isinstance(payload, str):
        # create a bytes object from the payload
        output_payload = payload.encode('utf-8')
    else:
        print('payload is neither a file nor a string', file=sys.stderr)
        sys.exit(5)

    return output_payload


def retrieve(carrier, file=None):
    # make sure the file is not executable
    pass

    # http://www.devdungeon.com/content/working-binary-data-python
    text = ''
    binary_text = text.encode('utf-8')
