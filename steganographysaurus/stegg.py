from PIL import Image
import os.path


def hide(payload, channel, carrier=None):
    """
    Hides the payload(message/file) in the channel(image file) and outputs
    to the carrier (to stdout as byte string or save as image file to
    filesystem)
    :param payload:
    :param channel: relative or absolute filepath
    :param carrier:
    :return:
    """
    try:
        # 1. get the payload as a bytes object
        payload = _convert_payload(payload)

        # 2. get the image to hide the payload in (aka: channel)
        channel = os.path.abspath(channel)
        print(channel)
        if os.path.isfile(channel):
            # https://pillow.readthedocs.io/en/latest/
            image = Image.open(channel)
            image_output = image.copy()
            width, height = image_output.size
            payload_length = len(payload)

            size = width * height
            # 3 bits per pixel, plus 8 bytes for the  payload length
            if (payload_length * 8 * 3) + 8 >= size:
                raise Barf("payload too large for carrier: {0} and {" \
                           "1}".format(
                    payload_length, size), 2)
        else:
            raise Barf("channel does not exist: {0}".format(channel), 3)

    except Barf as e:
        raise
    except Exception as e:
        raise Barf("other error: {0}".format(e), 6)
    else:
        pass
    finally:
        pass


def _convert_payload(payload):
    """
    converts the payload to bytes
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
            raise Barf('unable to open file: {0}'.format(e), 4)
    elif isinstance(payload, str):
        # create a bytes object from the payload
        output_payload = payload.encode('utf-8')
    else:
        raise Barf('payload is neither a file nor a string', 5)

    return output_payload


def retrieve(carrier, file=None):
    # make sure the file is not executable
    pass
    # http://www.devdungeon.com/content/working-binary-data-python



class Barf(Exception):
    """
    Stegg had a bad lunch. Barfff.
    """

    def __init__(self, message, code):
        super(Barf, self).__init__(message)
        self.code = code
