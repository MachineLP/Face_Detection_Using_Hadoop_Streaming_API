import numpy as np
import base64
import json
import sys


def b64ImgEncode(image):
    return json.dumps([base64.b64encode(image).decode("utf-8"), str(image.dtype),
                       image.shape])


def b64ImgDecode(encoded_object):
    (en_object, dtype, shape) = json.loads(encoded_object)

    if sys.version_info.major == 3:
        en_object = bytes(en_object, encoding="utf-8")

    de_object = np.frombuffer(base64.decodestring(en_object), dtype).reshape(shape)

    return de_object

