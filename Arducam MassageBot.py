#!/usr/bin/env python
# coding: utf-8

# In[89]:


from PIL import Image
import os
import numpy as np
import time


# # TO-DO:
#     - Have a list of colours
#     - Check if certain RGB value (+/- error) is in the centre of the image
#     
# ### Realtime Test Below:
#     - As images are captured and saved in the directory, the colour of the image is printed out.
#     - This depends if the centre pixel has the RGB value of a certain threshold. 
#     - If it is less than this threshold, the code returns 'dark,' otherwise it returns 'light.'

# In[ ]:


img_dir = os.getcwd()

def get_colour():
    original = dict([(f, None) for f in os.listdir(img_dir)[1:len(os.listdir(img_dir)) - 1]])
    while True:
        time.sleep(0.25)
        new = dict([(f, None) for f in os.listdir(img_dir)[1:len(os.listdir(img_dir)) - 1]])
        added = [f for f in new if not f in original]
        if added: print(print_shade(added[0]))
        original = new
    
def print_shade(img):
    i = Image.open(img)
    px = i.getpixel((np.array(i).shape[0] / 2, np.array(i).shape[1] / 2))
    if px[0] < 100: return 'New added picture is dark'
    else: return 'New added picture is light'
    
get_colour()

