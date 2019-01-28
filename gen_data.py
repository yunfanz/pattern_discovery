import numpy as np
from skimage.draw import (line, polygon, circle,
                          circle_perimeter,
                          ellipse, ellipse_perimeter,
                          bezier_curve)
n_img = 100
shape0 = (32, 512)
p_ellip = 0.5; ellp_pop = np.random.uniform(size=n_img)<p_ellip  #labels
p_line = 0.2; line_pop = np.random.uniform(size=n_img)<p_line
img = np.random.normal(size=n_img*64*256).reshape(n_img, 32, 512)

for i in range(n_img):
    
    if line_pop[i]:
        start, length = np.random.randint(low=0, high=479), 32
        print('line', i, start, length)
        rr, cc = line(0, start, 31, start+length)
        img[i, rr, cc] += np.random.uniform(low=0.5, high=3)
    if ellp_pop[i]:
        x, y = np.random.randint(low=0, high=31), np.random.randint(low=0, high=511)
        rr, cc = ellipse(x, y, 5, 20, img.shape[1:], rotation=np.pi/6)
        print('ellp', i, x, y)
        img[i, rr, cc] += np.random.uniform(low=0.5, high=2)
        
        
np.save("./data.npy", img)
