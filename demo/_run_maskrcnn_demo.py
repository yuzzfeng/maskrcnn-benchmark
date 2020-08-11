import os, sys
ROOT_DIR = os.path.abspath("../")
sys.path.append(os.path.join(ROOT_DIR))  # To find local version

import matplotlib.pyplot as plt
import matplotlib.pylab as pylab

import requests
from io import BytesIO
from PIL import Image
import numpy as np

# this makes our figures bigger
pylab.rcParams['figure.figsize'] = 20, 12

from maskrcnn_benchmark.config import cfg
from predictor import COCODemo