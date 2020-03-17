
# TODO write all of this to a file and have main read it (#preprocessing!)

import json
import numpy as np
from numpy.linalg import norm
from math import sqrt, acos, atan2
from itertools import combinations

# icosidodecahedron
# coordinates = [(1,-1.618033988749895,-2.618033988749895),(0.75,-1.2135254915624212,-2.7725424859373686),(0.5,-0.8090169943749475,-2.9270509831248424),(0.25,-0.4045084971874737,-3.081559480312316),(0,0,-3.23606797749979),(-0.25,0.4045084971874737,-3.081559480312316),(-0.5,0.8090169943749475,-2.9270509831248424),(-0.75,1.2135254915624212,-2.7725424859373686),(-1,1.618033988749895,-2.618033988749895),(-1.1545084971874737,1.868033988749895,-2.213525491562421),(-1.3090169943749475,2.118033988749895,-1.8090169943749475),(-1.4635254915624212,2.368033988749895,-1.4045084971874737),(-1.618033988749895,2.618033988749895,-1),(-1.618033988749895,2.618033988749895,-0.5),(-1.618033988749895,2.618033988749895,0),(-1.618033988749895,2.618033988749895,0.5),(-1.618033988749895,2.618033988749895,1),(-1.4635254915624212,2.368033988749895,1.4045084971874737),(-1.3090169943749475,2.118033988749895,1.8090169943749475),(-1.1545084971874737,1.868033988749895,2.213525491562421),(-1,1.618033988749895,2.618033988749895),(-0.75,1.2135254915624212,2.7725424859373686),(-0.5,0.8090169943749475,2.9270509831248424),(-0.25,0.4045084971874737,3.081559480312316),(0,0,3.23606797749979),(-0.25,-0.4045084971874737,3.081559480312316),(-0.5,-0.8090169943749475,2.9270509831248424),(-0.75,-1.2135254915624212,2.7725424859373686),(-1,-1.618033988749895,2.618033988749895),(-1.1545084971874737,-1.868033988749895,2.213525491562421),(-1.3090169943749475,-2.118033988749895,1.8090169943749475),(-1.4635254915624212,-2.368033988749895,1.4045084971874737),(-1.618033988749895,-2.618033988749895,1),(-1.2135254915624212,-2.7725424859373686,0.75),(-0.8090169943749475,-2.9270509831248424,0.5),(-0.4045084971874737,-3.081559480312316,0.25),(0,-3.23606797749979,0),(0.4045084971874737,-3.081559480312316,0.25),(0.8090169943749475,-2.9270509831248424,0.5),(1.2135254915624212,-2.7725424859373686,0.75),(1.618033988749895,-2.618033988749895,1),(1.4635254915624212,-2.368033988749895,1.4045084971874737),(1.3090169943749475,-2.118033988749895,1.8090169943749475),(1.1545084971874737,-1.868033988749895,2.213525491562421),(1,-1.618033988749895,2.618033988749895),(0.75,-1.2135254915624212,2.7725424859373686),(0.5,-0.8090169943749475,2.9270509831248424),(0.25,-0.4045084971874737,3.081559480312316),(0,0,3.23606797749979),(0.25,0.4045084971874737,3.081559480312316),(0.5,0.8090169943749475,2.9270509831248424),(0.75,1.2135254915624212,2.7725424859373686),(1,1.618033988749895,2.618033988749895),(1.4045084971874737,1.4635254915624212,2.368033988749895),(1.8090169943749475,1.3090169943749475,2.118033988749895),(2.213525491562421,1.1545084971874737,1.868033988749895),(2.618033988749895,1,1.618033988749895),(2.7725424859373686,0.75,1.2135254915624212),(2.9270509831248424,0.5,0.8090169943749475),(3.081559480312316,0.25,0.4045084971874737),(3.23606797749979,0,0),(3.081559480312316,0.25,-0.4045084971874737),(2.9270509831248424,0.5,-0.8090169943749475),(2.7725424859373686,0.75,-1.2135254915624212),(2.618033988749895,1,-1.618033988749895),(2.213525491562421,1.1545084971874737,-1.868033988749895),(1.8090169943749475,1.3090169943749475,-2.118033988749895),(1.4045084971874737,1.4635254915624212,-2.368033988749895),(1,1.618033988749895,-2.618033988749895),(0.5,1.618033988749895,-2.618033988749895),(0,1.618033988749895,-2.618033988749895),(-0.5,1.618033988749895,-2.618033988749895),(-1,1.618033988749895,-2.618033988749895),(-1.4045084971874737,1.4635254915624212,-2.368033988749895),(-1.8090169943749475,1.3090169943749475,-2.118033988749895),(-2.213525491562421,1.1545084971874737,-1.868033988749895),(-2.618033988749895,1,-1.618033988749895),(-2.618033988749895,0.5,-1.618033988749895),(-2.618033988749895,0,-1.618033988749895),(-2.618033988749895,-0.5,-1.618033988749895),(-2.618033988749895,-1,-1.618033988749895),(-2.213525491562421,-1.1545084971874737,-1.868033988749895),(-1.8090169943749475,-1.3090169943749475,-2.118033988749895),(-1.4045084971874737,-1.4635254915624212,-2.368033988749895),(-1,-1.618033988749895,-2.618033988749895),(-0.5,-1.618033988749895,-2.618033988749895),(0,-1.618033988749895,-2.618033988749895),(0.5,-1.618033988749895,-2.618033988749895),(1,-1.618033988749895,-2.618033988749895),(1.1545084971874737,-1.868033988749895,-2.213525491562421),(1.3090169943749475,-2.118033988749895,-1.8090169943749475),(1.4635254915624212,-2.368033988749895,-1.4045084971874737),(1.618033988749895,-2.618033988749895,-1),(1.618033988749895,-2.618033988749895,-0.5),(1.618033988749895,-2.618033988749895,0),(1.618033988749895,-2.618033988749895,0.5),(1.618033988749895,-2.618033988749895,1),(1.868033988749895,-2.213525491562421,1.1545084971874737),(2.118033988749895,-1.8090169943749475,1.3090169943749475),(2.368033988749895,-1.4045084971874737,1.4635254915624212),(2.618033988749895,-1,1.618033988749895),(2.7725424859373686,-0.75,1.2135254915624212),(2.9270509831248424,-0.5,0.8090169943749475),(3.081559480312316,-0.25,0.4045084971874737),(3.23606797749979,0,0),(3.081559480312316,-0.25,-0.4045084971874737),(2.9270509831248424,-0.5,-0.8090169943749475),(2.7725424859373686,-0.75,-1.2135254915624212),(2.618033988749895,-1,-1.618033988749895),(2.368033988749895,-1.4045084971874737,-1.4635254915624212),(2.118033988749895,-1.8090169943749475,-1.3090169943749475),(1.868033988749895,-2.213525491562421,-1.1545084971874737),(1.618033988749895,-2.618033988749895,-1),(1.2135254915624212,-2.7725424859373686,-0.75),(0.8090169943749475,-2.9270509831248424,-0.5),(0.4045084971874737,-3.081559480312316,-0.25),(0,-3.23606797749979,0),(-0.4045084971874737,-3.081559480312316,-0.25),(-0.8090169943749475,-2.9270509831248424,-0.5),(-1.2135254915624212,-2.7725424859373686,-0.75),(-1.618033988749895,-2.618033988749895,-1),(-1.4635254915624212,-2.368033988749895,-1.4045084971874737),(-1.3090169943749475,-2.118033988749895,-1.8090169943749475),(-1.1545084971874737,-1.868033988749895,-2.213525491562421),(-1,-1.618033988749895,-2.618033988749895),(-0.75,-1.2135254915624212,-2.7725424859373686),(-0.5,-0.8090169943749475,-2.9270509831248424),(-0.25,-0.4045084971874737,-3.081559480312316),(0,0,-3.23606797749979),(0.25,0.4045084971874737,-3.081559480312316),(0.5,0.8090169943749475,-2.9270509831248424),(0.75,1.2135254915624212,-2.7725424859373686),(1,1.618033988749895,-2.618033988749895),(1.1545084971874737,1.868033988749895,-2.213525491562421),(1.3090169943749475,2.118033988749895,-1.8090169943749475),(1.4635254915624212,2.368033988749895,-1.4045084971874737),(1.618033988749895,2.618033988749895,-1),(1.2135254915624212,2.7725424859373686,-0.75),(0.8090169943749475,2.9270509831248424,-0.5),(0.4045084971874737,3.081559480312316,-0.25),(0,3.23606797749979,0),(-0.4045084971874737,3.081559480312316,-0.25),(-0.8090169943749475,2.9270509831248424,-0.5),(-1.2135254915624212,2.7725424859373686,-0.75),(-1.618033988749895,2.618033988749895,-1),(-1.868033988749895,2.213525491562421,-1.1545084971874737),(-2.118033988749895,1.8090169943749475,-1.3090169943749475),(-2.368033988749895,1.4045084971874737,-1.4635254915624212),(-2.618033988749895,1,-1.618033988749895),(-2.7725424859373686,0.75,-1.2135254915624212),(-2.9270509831248424,0.5,-0.8090169943749475),(-3.081559480312316,0.25,-0.4045084971874737),(-3.23606797749979,0,0),(-3.081559480312316,0.25,0.4045084971874737),(-2.9270509831248424,0.5,0.8090169943749475),(-2.7725424859373686,0.75,1.2135254915624212),(-2.618033988749895,1,1.618033988749895),(-2.368033988749895,1.4045084971874737,1.4635254915624212),(-2.118033988749895,1.8090169943749475,1.3090169943749475),(-1.868033988749895,2.213525491562421,1.1545084971874737),(-1.618033988749895,2.618033988749895,1),(-1.2135254915624212,2.7725424859373686,0.75),(-0.8090169943749475,2.9270509831248424,0.5),(-0.4045084971874737,3.081559480312316,0.25),(0,3.23606797749979,0),(0.4045084971874737,3.081559480312316,0.25),(0.8090169943749475,2.9270509831248424,0.5),(1.2135254915624212,2.7725424859373686,0.75),(1.618033988749895,2.618033988749895,1),(1.4635254915624212,2.368033988749895,1.4045084971874737),(1.3090169943749475,2.118033988749895,1.8090169943749475),(1.1545084971874737,1.868033988749895,2.213525491562421),(1,1.618033988749895,2.618033988749895),(0.5,1.618033988749895,2.618033988749895),(0,1.618033988749895,2.618033988749895),(-0.5,1.618033988749895,2.618033988749895),(-1,1.618033988749895,2.618033988749895),(-1.4045084971874737,1.4635254915624212,2.368033988749895),(-1.8090169943749475,1.3090169943749475,2.118033988749895),(-2.213525491562421,1.1545084971874737,1.868033988749895),(-2.618033988749895,1,1.618033988749895),(-2.618033988749895,0.5,1.618033988749895),(-2.618033988749895,0,1.618033988749895),(-2.618033988749895,-0.5,1.618033988749895),(-2.618033988749895,-1,1.618033988749895),(-2.368033988749895,-1.4045084971874737,1.4635254915624212),(-2.118033988749895,-1.8090169943749475,1.3090169943749475),(-1.868033988749895,-2.213525491562421,1.1545084971874737),(-1.618033988749895,-2.618033988749895,1),(-1.618033988749895,-2.618033988749895,0.5),(-1.618033988749895,-2.618033988749895,0),(-1.618033988749895,-2.618033988749895,-0.5),(-1.618033988749895,-2.618033988749895,-1),(-1.868033988749895,-2.213525491562421,-1.1545084971874737),(-2.118033988749895,-1.8090169943749475,-1.3090169943749475),(-2.368033988749895,-1.4045084971874737,-1.4635254915624212),(-2.618033988749895,-1,-1.618033988749895),(-2.7725424859373686,-0.75,-1.2135254915624212),(-2.9270509831248424,-0.5,-0.8090169943749475),(-3.081559480312316,-0.25,-0.4045084971874737),(-3.23606797749979,0,0),(-3.081559480312316,-0.25,0.4045084971874737),(-2.9270509831248424,-0.5,0.8090169943749475),(-2.7725424859373686,-0.75,1.2135254915624212),(-2.618033988749895,-1,1.618033988749895),(-2.213525491562421,-1.1545084971874737,1.868033988749895),(-1.8090169943749475,-1.3090169943749475,2.118033988749895),(-1.4045084971874737,-1.4635254915624212,2.368033988749895),(-1,-1.618033988749895,2.618033988749895),(-0.5,-1.618033988749895,2.618033988749895),(0,-1.618033988749895,2.618033988749895),(0.5,-1.618033988749895,2.618033988749895),(1,-1.618033988749895,2.618033988749895),(1.4045084971874737,-1.4635254915624212,2.368033988749895),(1.8090169943749475,-1.3090169943749475,2.118033988749895),(2.213525491562421,-1.1545084971874737,1.868033988749895),(2.618033988749895,-1,1.618033988749895),(2.618033988749895,-0.5,1.618033988749895),(2.618033988749895,0,1.618033988749895),(2.618033988749895,0.5,1.618033988749895),(2.618033988749895,1,1.618033988749895),(2.368033988749895,1.4045084971874737,1.4635254915624212),(2.118033988749895,1.8090169943749475,1.3090169943749475),(1.868033988749895,2.213525491562421,1.1545084971874737),(1.618033988749895,2.618033988749895,1),(1.618033988749895,2.618033988749895,0.5),(1.618033988749895,2.618033988749895,0),(1.618033988749895,2.618033988749895,-0.5),(1.618033988749895,2.618033988749895,-1),(1.868033988749895,2.213525491562421,-1.1545084971874737),(2.118033988749895,1.8090169943749475,-1.3090169943749475),(2.368033988749895,1.4045084971874737,-1.4635254915624212),(2.618033988749895,1,-1.618033988749895),(2.618033988749895,0.5,-1.618033988749895),(2.618033988749895,0,-1.618033988749895),(2.618033988749895,-0.5,-1.618033988749895),(2.618033988749895,-1,-1.618033988749895),(2.213525491562421,-1.1545084971874737,-1.868033988749895),(1.8090169943749475,-1.3090169943749475,-2.118033988749895),(1.4045084971874737,-1.4635254915624212,-2.368033988749895),]
# rhombicosidodecahedron
coordinates = [(-1,1,-4.23606797749979),(-1,0.5,-4.23606797749979),(-1,0,-4.23606797749979),(-1,-0.5,-4.23606797749979),(-1,-1,-4.23606797749979),(-0.75,-1.4045084971874737,-4.0815594803123165),(-0.5,-1.8090169943749475,-3.9270509831248424),(-0.25,-2.213525491562421,-3.7725424859373686),(0,-2.618033988749895,-3.618033988749895),(-0.4045084971874737,-2.7725424859373686,-3.368033988749895),(-0.8090169943749475,-2.9270509831248424,-3.118033988749895),(-1.2135254915624212,-3.081559480312316,-2.868033988749895),(-1.618033988749895,-3.23606797749979,-2.618033988749895),(-2.0225424859373686,-3.081559480312316,-2.368033988749895),(-2.4270509831248424,-2.9270509831248424,-2.118033988749895),(-2.831559480312316,-2.7725424859373686,-1.868033988749895),(-3.23606797749979,-2.618033988749895,-1.618033988749895),(-3.48606797749979,-2.213525491562421,-1.4635254915624212),(-3.73606797749979,-1.8090169943749475,-1.3090169943749475),(-3.98606797749979,-1.4045084971874737,-1.1545084971874737),(-4.23606797749979,-1,-1),(-4.23606797749979,-0.5,-1),(-4.23606797749979,0,-1),(-4.23606797749979,0.5,-1),(-4.23606797749979,1,-1),(-4.23606797749979,1,-0.5),(-4.23606797749979,1,0),(-4.23606797749979,1,0.5),(-4.23606797749979,1,1),(-4.23606797749979,0.5,1),(-4.23606797749979,0,1),(-4.23606797749979,-0.5,1),(-4.23606797749979,-1,1),(-4.23606797749979,-1,0.5),(-4.23606797749979,-1,0),(-4.23606797749979,-1,-0.5),(-4.23606797749979,-1,-1),(-4.0815594803123165,-0.75,-1.4045084971874737),(-3.9270509831248424,-0.5,-1.8090169943749475),(-3.7725424859373686,-0.25,-2.213525491562421),(-3.618033988749895,0,-2.618033988749895),(-3.368033988749895,-0.4045084971874737,-2.7725424859373686),(-3.118033988749895,-0.8090169943749475,-2.9270509831248424),(-2.868033988749895,-1.2135254915624212,-3.081559480312316),(-2.618033988749895,-1.618033988749895,-3.23606797749979),(-2.7725424859373686,-1.868033988749895,-2.831559480312316),(-2.9270509831248424,-2.118033988749895,-2.4270509831248424),(-3.081559480312316,-2.368033988749895,-2.0225424859373686),(-3.23606797749979,-2.618033988749895,-1.618033988749895),(-3.081559480312316,-2.868033988749895,-1.2135254915624212),(-2.9270509831248424,-3.118033988749895,-0.8090169943749475),(-2.7725424859373686,-3.368033988749895,-0.4045084971874737),(-2.618033988749895,-3.618033988749895,0),(-2.213525491562421,-3.7725424859373686,-0.25),(-1.8090169943749475,-3.9270509831248424,-0.5),(-1.4045084971874737,-4.0815594803123165,-0.75),(-1,-4.23606797749979,-1),(-1.1545084971874737,-3.98606797749979,-1.4045084971874737),(-1.3090169943749475,-3.73606797749979,-1.8090169943749475),(-1.4635254915624212,-3.48606797749979,-2.213525491562421),(-1.618033988749895,-3.23606797749979,-2.618033988749895),(-1.868033988749895,-2.831559480312316,-2.7725424859373686),(-2.118033988749895,-2.4270509831248424,-2.9270509831248424),(-2.368033988749895,-2.0225424859373686,-3.081559480312316),(-2.618033988749895,-1.618033988749895,-3.23606797749979),(-2.213525491562421,-1.4635254915624212,-3.48606797749979),(-1.8090169943749475,-1.3090169943749475,-3.73606797749979),(-1.4045084971874737,-1.1545084971874737,-3.98606797749979),(-1,-1,-4.23606797749979),(-0.5,-1,-4.23606797749979),(0,-1,-4.23606797749979),(0.5,-1,-4.23606797749979),(1,-1,-4.23606797749979),(1,-0.5,-4.23606797749979),(1,0,-4.23606797749979),(1,0.5,-4.23606797749979),(1,1,-4.23606797749979),(0.75,1.4045084971874737,-4.0815594803123165),(0.5,1.8090169943749475,-3.9270509831248424),(0.25,2.213525491562421,-3.7725424859373686),(0,2.618033988749895,-3.618033988749895),(-0.4045084971874737,2.7725424859373686,-3.368033988749895),(-0.8090169943749475,2.9270509831248424,-3.118033988749895),(-1.2135254915624212,3.081559480312316,-2.868033988749895),(-1.618033988749895,3.23606797749979,-2.618033988749895),(-1.868033988749895,2.831559480312316,-2.7725424859373686),(-2.118033988749895,2.4270509831248424,-2.9270509831248424),(-2.368033988749895,2.0225424859373686,-3.081559480312316),(-2.618033988749895,1.618033988749895,-3.23606797749979),(-2.213525491562421,1.4635254915624212,-3.48606797749979),(-1.8090169943749475,1.3090169943749475,-3.73606797749979),(-1.4045084971874737,1.1545084971874737,-3.98606797749979),(-1,1,-4.23606797749979),(-0.5,1,-4.23606797749979),(0,1,-4.23606797749979),(0.5,1,-4.23606797749979),(1,1,-4.23606797749979),(1.4045084971874737,1.1545084971874737,-3.98606797749979),(1.8090169943749475,1.3090169943749475,-3.73606797749979),(2.213525491562421,1.4635254915624212,-3.48606797749979),(2.618033988749895,1.618033988749895,-3.23606797749979),(2.7725424859373686,1.868033988749895,-2.831559480312316),(2.9270509831248424,2.118033988749895,-2.4270509831248424),(3.081559480312316,2.368033988749895,-2.0225424859373686),(3.23606797749979,2.618033988749895,-1.618033988749895),(3.48606797749979,2.213525491562421,-1.4635254915624212),(3.73606797749979,1.8090169943749475,-1.3090169943749475),(3.98606797749979,1.4045084971874737,-1.1545084971874737),(4.23606797749979,1,-1),(4.23606797749979,0.5,-1),(4.23606797749979,0,-1),(4.23606797749979,-0.5,-1),(4.23606797749979,-1,-1),(3.98606797749979,-1.4045084971874737,-1.1545084971874737),(3.73606797749979,-1.8090169943749475,-1.3090169943749475),(3.48606797749979,-2.213525491562421,-1.4635254915624212),(3.23606797749979,-2.618033988749895,-1.618033988749895),(2.831559480312316,-2.7725424859373686,-1.868033988749895),(2.4270509831248424,-2.9270509831248424,-2.118033988749895),(2.0225424859373686,-3.081559480312316,-2.368033988749895),(1.618033988749895,-3.23606797749979,-2.618033988749895),(1.4635254915624212,-3.48606797749979,-2.213525491562421),(1.3090169943749475,-3.73606797749979,-1.8090169943749475),(1.1545084971874737,-3.98606797749979,-1.4045084971874737),(1,-4.23606797749979,-1),(1,-4.23606797749979,-0.5),(1,-4.23606797749979,0),(1,-4.23606797749979,0.5),(1,-4.23606797749979,1),(1.1545084971874737,-3.98606797749979,1.4045084971874737),(1.3090169943749475,-3.73606797749979,1.8090169943749475),(1.4635254915624212,-3.48606797749979,2.213525491562421),(1.618033988749895,-3.23606797749979,2.618033988749895),(1.868033988749895,-2.831559480312316,2.7725424859373686),(2.118033988749895,-2.4270509831248424,2.9270509831248424),(2.368033988749895,-2.0225424859373686,3.081559480312316),(2.618033988749895,-1.618033988749895,3.23606797749979),(2.213525491562421,-1.4635254915624212,3.48606797749979),(1.8090169943749475,-1.3090169943749475,3.73606797749979),(1.4045084971874737,-1.1545084971874737,3.98606797749979),(1,-1,4.23606797749979),(0.5,-1,4.23606797749979),(0,-1,4.23606797749979),(-0.5,-1,4.23606797749979),(-1,-1,4.23606797749979),(-1,-0.5,4.23606797749979),(-1,0,4.23606797749979),(-1,0.5,4.23606797749979),(-1,1,4.23606797749979),(-0.75,1.4045084971874737,4.0815594803123165),(-0.5,1.8090169943749475,3.9270509831248424),(-0.25,2.213525491562421,3.7725424859373686),(0,2.618033988749895,3.618033988749895),(0.4045084971874737,2.7725424859373686,3.368033988749895),(0.8090169943749475,2.9270509831248424,3.118033988749895),(1.2135254915624212,3.081559480312316,2.868033988749895),(1.618033988749895,3.23606797749979,2.618033988749895),(2.0225424859373686,3.081559480312316,2.368033988749895),(2.4270509831248424,2.9270509831248424,2.118033988749895),(2.831559480312316,2.7725424859373686,1.868033988749895),(3.23606797749979,2.618033988749895,1.618033988749895),(3.081559480312316,2.868033988749895,1.2135254915624212),(2.9270509831248424,3.118033988749895,0.8090169943749475),(2.7725424859373686,3.368033988749895,0.4045084971874737),(2.618033988749895,3.618033988749895,0),(2.213525491562421,3.7725424859373686,0.25),(1.8090169943749475,3.9270509831248424,0.5),(1.4045084971874737,4.0815594803123165,0.75),(1,4.23606797749979,1),(1.1545084971874737,3.98606797749979,1.4045084971874737),(1.3090169943749475,3.73606797749979,1.8090169943749475),(1.4635254915624212,3.48606797749979,2.213525491562421),(1.618033988749895,3.23606797749979,2.618033988749895),(1.868033988749895,2.831559480312316,2.7725424859373686),(2.118033988749895,2.4270509831248424,2.9270509831248424),(2.368033988749895,2.0225424859373686,3.081559480312316),(2.618033988749895,1.618033988749895,3.23606797749979),(2.213525491562421,1.4635254915624212,3.48606797749979),(1.8090169943749475,1.3090169943749475,3.73606797749979),(1.4045084971874737,1.1545084971874737,3.98606797749979),(1,1,4.23606797749979),(0.75,1.4045084971874737,4.0815594803123165),(0.5,1.8090169943749475,3.9270509831248424),(0.25,2.213525491562421,3.7725424859373686),(0,2.618033988749895,3.618033988749895),(-0.4045084971874737,2.7725424859373686,3.368033988749895),(-0.8090169943749475,2.9270509831248424,3.118033988749895),(-1.2135254915624212,3.081559480312316,2.868033988749895),(-1.618033988749895,3.23606797749979,2.618033988749895),(-2.0225424859373686,3.081559480312316,2.368033988749895),(-2.4270509831248424,2.9270509831248424,2.118033988749895),(-2.831559480312316,2.7725424859373686,1.868033988749895),(-3.23606797749979,2.618033988749895,1.618033988749895),(-3.081559480312316,2.868033988749895,1.2135254915624212),(-2.9270509831248424,3.118033988749895,0.8090169943749475),(-2.7725424859373686,3.368033988749895,0.4045084971874737),(-2.618033988749895,3.618033988749895,0),(-2.213525491562421,3.7725424859373686,0.25),(-1.8090169943749475,3.9270509831248424,0.5),(-1.4045084971874737,4.0815594803123165,0.75),(-1,4.23606797749979,1),(-0.5,4.23606797749979,1),(0,4.23606797749979,1),(0.5,4.23606797749979,1),(1,4.23606797749979,1),(1,4.23606797749979,0.5),(1,4.23606797749979,0),(1,4.23606797749979,-0.5),(1,4.23606797749979,-1),(0.5,4.23606797749979,-1),(0,4.23606797749979,-1),(-0.5,4.23606797749979,-1),(-1,4.23606797749979,-1),(-1.4045084971874737,4.0815594803123165,-0.75),(-1.8090169943749475,3.9270509831248424,-0.5),(-2.213525491562421,3.7725424859373686,-0.25),(-2.618033988749895,3.618033988749895,0),(-2.7725424859373686,3.368033988749895,-0.4045084971874737),(-2.9270509831248424,3.118033988749895,-0.8090169943749475),(-3.081559480312316,2.868033988749895,-1.2135254915624212),(-3.23606797749979,2.618033988749895,-1.618033988749895),(-3.081559480312316,2.368033988749895,-2.0225424859373686),(-2.9270509831248424,2.118033988749895,-2.4270509831248424),(-2.7725424859373686,1.868033988749895,-2.831559480312316),(-2.618033988749895,1.618033988749895,-3.23606797749979),(-2.868033988749895,1.2135254915624212,-3.081559480312316),(-3.118033988749895,0.8090169943749475,-2.9270509831248424),(-3.368033988749895,0.4045084971874737,-2.7725424859373686),(-3.618033988749895,0,-2.618033988749895),(-3.7725424859373686,0.25,-2.213525491562421),(-3.9270509831248424,0.5,-1.8090169943749475),(-4.0815594803123165,0.75,-1.4045084971874737),(-4.23606797749979,1,-1),(-3.98606797749979,1.4045084971874737,-1.1545084971874737),(-3.73606797749979,1.8090169943749475,-1.3090169943749475),(-3.48606797749979,2.213525491562421,-1.4635254915624212),(-3.23606797749979,2.618033988749895,-1.618033988749895),(-2.831559480312316,2.7725424859373686,-1.868033988749895),(-2.4270509831248424,2.9270509831248424,-2.118033988749895),(-2.0225424859373686,3.081559480312316,-2.368033988749895),(-1.618033988749895,3.23606797749979,-2.618033988749895),(-1.4635254915624212,3.48606797749979,-2.213525491562421),(-1.3090169943749475,3.73606797749979,-1.8090169943749475),(-1.1545084971874737,3.98606797749979,-1.4045084971874737),(-1,4.23606797749979,-1),(-1,4.23606797749979,-0.5),(-1,4.23606797749979,0),(-1,4.23606797749979,0.5),(-1,4.23606797749979,1),(-1.1545084971874737,3.98606797749979,1.4045084971874737),(-1.3090169943749475,3.73606797749979,1.8090169943749475),(-1.4635254915624212,3.48606797749979,2.213525491562421),(-1.618033988749895,3.23606797749979,2.618033988749895),(-1.868033988749895,2.831559480312316,2.7725424859373686),(-2.118033988749895,2.4270509831248424,2.9270509831248424),(-2.368033988749895,2.0225424859373686,3.081559480312316),(-2.618033988749895,1.618033988749895,3.23606797749979),(-2.868033988749895,1.2135254915624212,3.081559480312316),(-3.118033988749895,0.8090169943749475,2.9270509831248424),(-3.368033988749895,0.4045084971874737,2.7725424859373686),(-3.618033988749895,0,2.618033988749895),(-3.7725424859373686,-0.25,2.213525491562421),(-3.9270509831248424,-0.5,1.8090169943749475),(-4.0815594803123165,-0.75,1.4045084971874737),(-4.23606797749979,-1,1),(-3.98606797749979,-1.4045084971874737,1.1545084971874737),(-3.73606797749979,-1.8090169943749475,1.3090169943749475),(-3.48606797749979,-2.213525491562421,1.4635254915624212),(-3.23606797749979,-2.618033988749895,1.618033988749895),(-3.081559480312316,-2.368033988749895,2.0225424859373686),(-2.9270509831248424,-2.118033988749895,2.4270509831248424),(-2.7725424859373686,-1.868033988749895,2.831559480312316),(-2.618033988749895,-1.618033988749895,3.23606797749979),(-2.868033988749895,-1.2135254915624212,3.081559480312316),(-3.118033988749895,-0.8090169943749475,2.9270509831248424),(-3.368033988749895,-0.4045084971874737,2.7725424859373686),(-3.618033988749895,0,2.618033988749895),(-3.7725424859373686,0.25,2.213525491562421),(-3.9270509831248424,0.5,1.8090169943749475),(-4.0815594803123165,0.75,1.4045084971874737),(-4.23606797749979,1,1),(-3.98606797749979,1.4045084971874737,1.1545084971874737),(-3.73606797749979,1.8090169943749475,1.3090169943749475),(-3.48606797749979,2.213525491562421,1.4635254915624212),(-3.23606797749979,2.618033988749895,1.618033988749895),(-3.081559480312316,2.368033988749895,2.0225424859373686),(-2.9270509831248424,2.118033988749895,2.4270509831248424),(-2.7725424859373686,1.868033988749895,2.831559480312316),(-2.618033988749895,1.618033988749895,3.23606797749979),(-2.213525491562421,1.4635254915624212,3.48606797749979),(-1.8090169943749475,1.3090169943749475,3.73606797749979),(-1.4045084971874737,1.1545084971874737,3.98606797749979),(-1,1,4.23606797749979),(-0.5,1,4.23606797749979),(0,1,4.23606797749979),(0.5,1,4.23606797749979),(1,1,4.23606797749979),(1,0.5,4.23606797749979),(1,0,4.23606797749979),(1,-0.5,4.23606797749979),(1,-1,4.23606797749979),(0.75,-1.4045084971874737,4.0815594803123165),(0.5,-1.8090169943749475,3.9270509831248424),(0.25,-2.213525491562421,3.7725424859373686),(0,-2.618033988749895,3.618033988749895),(-0.4045084971874737,-2.7725424859373686,3.368033988749895),(-0.8090169943749475,-2.9270509831248424,3.118033988749895),(-1.2135254915624212,-3.081559480312316,2.868033988749895),(-1.618033988749895,-3.23606797749979,2.618033988749895),(-1.868033988749895,-2.831559480312316,2.7725424859373686),(-2.118033988749895,-2.4270509831248424,2.9270509831248424),(-2.368033988749895,-2.0225424859373686,3.081559480312316),(-2.618033988749895,-1.618033988749895,3.23606797749979),(-2.213525491562421,-1.4635254915624212,3.48606797749979),(-1.8090169943749475,-1.3090169943749475,3.73606797749979),(-1.4045084971874737,-1.1545084971874737,3.98606797749979),(-1,-1,4.23606797749979),(-0.75,-1.4045084971874737,4.0815594803123165),(-0.5,-1.8090169943749475,3.9270509831248424),(-0.25,-2.213525491562421,3.7725424859373686),(0,-2.618033988749895,3.618033988749895),(0.4045084971874737,-2.7725424859373686,3.368033988749895),(0.8090169943749475,-2.9270509831248424,3.118033988749895),(1.2135254915624212,-3.081559480312316,2.868033988749895),(1.618033988749895,-3.23606797749979,2.618033988749895),(2.0225424859373686,-3.081559480312316,2.368033988749895),(2.4270509831248424,-2.9270509831248424,2.118033988749895),(2.831559480312316,-2.7725424859373686,1.868033988749895),(3.23606797749979,-2.618033988749895,1.618033988749895),(3.081559480312316,-2.868033988749895,1.2135254915624212),(2.9270509831248424,-3.118033988749895,0.8090169943749475),(2.7725424859373686,-3.368033988749895,0.4045084971874737),(2.618033988749895,-3.618033988749895,0),(2.213525491562421,-3.7725424859373686,0.25),(1.8090169943749475,-3.9270509831248424,0.5),(1.4045084971874737,-4.0815594803123165,0.75),(1,-4.23606797749979,1),(0.5,-4.23606797749979,1),(0,-4.23606797749979,1),(-0.5,-4.23606797749979,1),(-1,-4.23606797749979,1),(-1.4045084971874737,-4.0815594803123165,0.75),(-1.8090169943749475,-3.9270509831248424,0.5),(-2.213525491562421,-3.7725424859373686,0.25),(-2.618033988749895,-3.618033988749895,0),(-2.7725424859373686,-3.368033988749895,0.4045084971874737),(-2.9270509831248424,-3.118033988749895,0.8090169943749475),(-3.081559480312316,-2.868033988749895,1.2135254915624212),(-3.23606797749979,-2.618033988749895,1.618033988749895),(-2.831559480312316,-2.7725424859373686,1.868033988749895),(-2.4270509831248424,-2.9270509831248424,2.118033988749895),(-2.0225424859373686,-3.081559480312316,2.368033988749895),(-1.618033988749895,-3.23606797749979,2.618033988749895),(-1.4635254915624212,-3.48606797749979,2.213525491562421),(-1.3090169943749475,-3.73606797749979,1.8090169943749475),(-1.1545084971874737,-3.98606797749979,1.4045084971874737),(-1,-4.23606797749979,1),(-1,-4.23606797749979,0.5),(-1,-4.23606797749979,0),(-1,-4.23606797749979,-0.5),(-1,-4.23606797749979,-1),(-0.5,-4.23606797749979,-1),(0,-4.23606797749979,-1),(0.5,-4.23606797749979,-1),(1,-4.23606797749979,-1),(1.4045084971874737,-4.0815594803123165,-0.75),(1.8090169943749475,-3.9270509831248424,-0.5),(2.213525491562421,-3.7725424859373686,-0.25),(2.618033988749895,-3.618033988749895,0),(2.7725424859373686,-3.368033988749895,-0.4045084971874737),(2.9270509831248424,-3.118033988749895,-0.8090169943749475),(3.081559480312316,-2.868033988749895,-1.2135254915624212),(3.23606797749979,-2.618033988749895,-1.618033988749895),(3.081559480312316,-2.368033988749895,-2.0225424859373686),(2.9270509831248424,-2.118033988749895,-2.4270509831248424),(2.7725424859373686,-1.868033988749895,-2.831559480312316),(2.618033988749895,-1.618033988749895,-3.23606797749979),(2.213525491562421,-1.4635254915624212,-3.48606797749979),(1.8090169943749475,-1.3090169943749475,-3.73606797749979),(1.4045084971874737,-1.1545084971874737,-3.98606797749979),(1,-1,-4.23606797749979),(0.75,-1.4045084971874737,-4.0815594803123165),(0.5,-1.8090169943749475,-3.9270509831248424),(0.25,-2.213525491562421,-3.7725424859373686),(0,-2.618033988749895,-3.618033988749895),(0.4045084971874737,-2.7725424859373686,-3.368033988749895),(0.8090169943749475,-2.9270509831248424,-3.118033988749895),(1.2135254915624212,-3.081559480312316,-2.868033988749895),(1.618033988749895,-3.23606797749979,-2.618033988749895),(1.868033988749895,-2.831559480312316,-2.7725424859373686),(2.118033988749895,-2.4270509831248424,-2.9270509831248424),(2.368033988749895,-2.0225424859373686,-3.081559480312316),(2.618033988749895,-1.618033988749895,-3.23606797749979),(2.868033988749895,-1.2135254915624212,-3.081559480312316),(3.118033988749895,-0.8090169943749475,-2.9270509831248424),(3.368033988749895,-0.4045084971874737,-2.7725424859373686),(3.618033988749895,0,-2.618033988749895),(3.7725424859373686,0.25,-2.213525491562421),(3.9270509831248424,0.5,-1.8090169943749475),(4.0815594803123165,0.75,-1.4045084971874737),(4.23606797749979,1,-1),(4.23606797749979,1,-0.5),(4.23606797749979,1,0),(4.23606797749979,1,0.5),(4.23606797749979,1,1),(4.0815594803123165,0.75,1.4045084971874737),(3.9270509831248424,0.5,1.8090169943749475),(3.7725424859373686,0.25,2.213525491562421),(3.618033988749895,0,2.618033988749895),(3.368033988749895,-0.4045084971874737,2.7725424859373686),(3.118033988749895,-0.8090169943749475,2.9270509831248424),(2.868033988749895,-1.2135254915624212,3.081559480312316),(2.618033988749895,-1.618033988749895,3.23606797749979),(2.7725424859373686,-1.868033988749895,2.831559480312316),(2.9270509831248424,-2.118033988749895,2.4270509831248424),(3.081559480312316,-2.368033988749895,2.0225424859373686),(3.23606797749979,-2.618033988749895,1.618033988749895),(3.48606797749979,-2.213525491562421,1.4635254915624212),(3.73606797749979,-1.8090169943749475,1.3090169943749475),(3.98606797749979,-1.4045084971874737,1.1545084971874737),(4.23606797749979,-1,1),(4.23606797749979,-0.5,1),(4.23606797749979,0,1),(4.23606797749979,0.5,1),(4.23606797749979,1,1),(3.98606797749979,1.4045084971874737,1.1545084971874737),(3.73606797749979,1.8090169943749475,1.3090169943749475),(3.48606797749979,2.213525491562421,1.4635254915624212),(3.23606797749979,2.618033988749895,1.618033988749895),(3.081559480312316,2.368033988749895,2.0225424859373686),(2.9270509831248424,2.118033988749895,2.4270509831248424),(2.7725424859373686,1.868033988749895,2.831559480312316),(2.618033988749895,1.618033988749895,3.23606797749979),(2.868033988749895,1.2135254915624212,3.081559480312316),(3.118033988749895,0.8090169943749475,2.9270509831248424),(3.368033988749895,0.4045084971874737,2.7725424859373686),(3.618033988749895,0,2.618033988749895),(3.7725424859373686,-0.25,2.213525491562421),(3.9270509831248424,-0.5,1.8090169943749475),(4.0815594803123165,-0.75,1.4045084971874737),(4.23606797749979,-1,1),(4.23606797749979,-1,0.5),(4.23606797749979,-1,0),(4.23606797749979,-1,-0.5),(4.23606797749979,-1,-1),(4.0815594803123165,-0.75,-1.4045084971874737),(3.9270509831248424,-0.5,-1.8090169943749475),(3.7725424859373686,-0.25,-2.213525491562421),(3.618033988749895,0,-2.618033988749895),(3.368033988749895,0.4045084971874737,-2.7725424859373686),(3.118033988749895,0.8090169943749475,-2.9270509831248424),(2.868033988749895,1.2135254915624212,-3.081559480312316),(2.618033988749895,1.618033988749895,-3.23606797749979),(2.368033988749895,2.0225424859373686,-3.081559480312316),(2.118033988749895,2.4270509831248424,-2.9270509831248424),(1.868033988749895,2.831559480312316,-2.7725424859373686),(1.618033988749895,3.23606797749979,-2.618033988749895),(1.4635254915624212,3.48606797749979,-2.213525491562421),(1.3090169943749475,3.73606797749979,-1.8090169943749475),(1.1545084971874737,3.98606797749979,-1.4045084971874737),(1,4.23606797749979,-1),(1.4045084971874737,4.0815594803123165,-0.75),(1.8090169943749475,3.9270509831248424,-0.5),(2.213525491562421,3.7725424859373686,-0.25),(2.618033988749895,3.618033988749895,0),(2.7725424859373686,3.368033988749895,-0.4045084971874737),(2.9270509831248424,3.118033988749895,-0.8090169943749475),(3.081559480312316,2.868033988749895,-1.2135254915624212),(3.23606797749979,2.618033988749895,-1.618033988749895),(2.831559480312316,2.7725424859373686,-1.868033988749895),(2.4270509831248424,2.9270509831248424,-2.118033988749895),(2.0225424859373686,3.081559480312316,-2.368033988749895),(1.618033988749895,3.23606797749979,-2.618033988749895),(1.2135254915624212,3.081559480312316,-2.868033988749895),(0.8090169943749475,2.9270509831248424,-3.118033988749895),(0.4045084971874737,2.7725424859373686,-3.368033988749895),(0,2.618033988749895,-3.618033988749895),(-0.25,2.213525491562421,-3.7725424859373686),(-0.5,1.8090169943749475,-3.9270509831248424),(-0.75,1.4045084971874737,-4.0815594803123165),]

coordinates = np.array(coordinates)

unique_to_dupes = []
unique_coords = []
index_to_unique = [0] * len(coordinates)


def add_coord(i, coord):
  for (j, dupes) in enumerate(unique_to_dupes):
    for dupe in dupes:
      if norm(coord - coordinates[dupe]) < 0.1:
        dupes.append(i)
        index_to_unique[i] = j
        return

  index_to_unique[i] = len(unique_to_dupes)
  unique_to_dupes.append([i])
  unique_coords.append(coord)

for (i, coord) in enumerate(coordinates):
  add_coord(i, coord)


neighbors = []

for (i, coord0) in enumerate(unique_coords):
  local_neighbors = []
  for (j, coord1) in enumerate(unique_coords):
    if i != j and norm(coord0 - coord1) < 0.51:
      local_neighbors.append(j)

  # eliminate triangle tip cross move
  if len(local_neighbors) == 3:
    for n0 in local_neighbors:
      if len(unique_to_dupes[n0]) > 1:
        expected_n1 = 2*coord0 - unique_coords[n0]
        for n1 in local_neighbors:
          if norm(unique_coords[n1] - expected_n1) < 0.1:
            local_neighbors = [n0, n1]
            break

        break

  neighbors.append(local_neighbors)

next_pixel = {}

for (i, local_neighbors) in enumerate(neighbors):
  for n in local_neighbors:
    expected_n2_coords = 2*unique_coords[n] - unique_coords[i]
    for n2 in neighbors[n]:
      if norm(unique_coords[n2] - expected_n2_coords) < 0.4:
        next_pixel[str((i,n))] = n2

def latlong(coord):
  return (acos(coord[2] / norm(coord)), atan2(coord[0], coord[1]))

latlongs = [latlong(coord) for coord in unique_coords]


counts = {}
for n in neighbors:
  count = len(n)
  if count not in counts:
    counts[count] = 0
  counts[count] += 1

print(len(unique_coords))
print(counts)


f = open("/home/pi/Rhomberman/pixels.json", "w")
f.write(json.dumps({
  "RAW_SIZE": len(coordinates),
  "SIZE": len(latlongs),
  "unique_to_dupes": unique_to_dupes,
  "unique_coords": [coord.tolist() for coord in unique_coords],
  # "latlongs": latlongs,
  "neighbors": neighbors,
  "next_pixel": next_pixel,
  } ))
f.close()