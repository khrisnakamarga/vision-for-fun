__version__ = "0.1.0"

from cv2 import rotate
from . import palm_detect
from . import rotate_image
from . import snapchat_filter

snapchat_filter.sunglasses()
# palm_detect.camera_detect_palm()