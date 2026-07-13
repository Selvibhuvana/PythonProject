# Import the numpy package as np
import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
print (np_baseball)

# Print out type of np_baseball
print (type(np_baseball))

################2d numpy arrays#########################################

import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
print (np_baseball)
# Print out the type of np_baseball
print (type(np_baseball))

# Print out the shape of np_baseball
print (np_baseball.shape)


#############subsetting 2d numpy arrays
import numpy as np

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print (np_baseball[3]) # or print (np_baseball[3,:])
print(np_baseball[3, :])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Print out height of 124th player
print (np_baseball[123][0]) #or print (np_baseball[123,0])

######## operations on 2d numpy array
import numpy as np

np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print (np_baseball+updated)

# Create numpy array: conversion
conversion = np.array([0.0254,0.453592,1])
print (conversion)

# Print out product of np_baseball and conversion
print (np_baseball*conversion)