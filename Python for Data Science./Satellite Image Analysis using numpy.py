#1
%matplotlib inline
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

#2
from skimage import data
photo_data = misc.imread('./wifire/sd-3layers.jpg')
type(photo_data)

#3
plt.figure(figsize=(15,15))
plt.imshow(photo_data)

#4
photo_data.shape
#print(photo_data)

#5
photo_data.size

#6
photo_data.min(),  photo_data.max()

#7
photo_data.mean()

#8
photo_data[150,250]

#9
photo_data[150,250,1]

#10
photo_data[150,250] = 0
plt.figure(figsize=(10,10))
plt.imshow(photo_data)

#11
photo_data = misc.imread('./wifire/sd-3layers.jpg')

#photo_data[200:800, : ] = 0
plt.figure(figsize=(10,10))
plt.imshow(photo_data)

#12
photo_data = misc.imread('./wifire/sd-3layers.jpg')

print("Shape of photo data: ", photo_data.shape)
low_value_filter = photo_data < 200
print("Shape of low value filter: ", low_value_filter.shape)

#13
#import random
plt.figure(figsize=(10,10))
plt.imshow(photo_data)
photo_data[low_value_filter] = 0
plt.figure(figsize=(10,10))
plt.imshow(photo_data)

#14
rows_range = np.arange(len(photo_data))
cols_range = rows_range
print(type(rows_range))

#15
photo_data[rows_range,cols_range] = 255

#16
plt.figure(figsize=(15,15))
plt.imshow(photo_data)

#17
total_rows, total_cols, total_layers = photo_data.shape
#print("Photo data: ",photo_data.shape)
X, Y = np.ogrid[:total_rows, :total_cols]
#print("X = ", X.shape, "Y = ", Y.shape)

#18
center_row, center_col = total_rows / 2, total_cols / 2
#print("Center row = ",center_row, " and center colom = ", center_col)
#print(X - center_row)
#print(Y - center_col)
dist_from_center = (X - center_row)**2 + (Y - center_col)**2
#print(dist_from_center)
radius = (total_rows/2)**2
#print("Radius = ", radius)
circular_mask = (dist_from_center > radius)
print(circular_mask)
#print(circular_mask[1500:1700, 2000:2200])

#19
photo_data = misc.imread('./wifire/sd-3layers.jpg')

photo_data[circular_mask] = 0
plt.figure(figsize=(10,10))
plt.imshow(photo_data)

#20
X, Y = np.ogrid[:total_rows, :total_cols]
half_upper = X < center_row 
half_upper_mask = np.logical_and(half_upper,circular_mask)

#21
photo_data = misc.imread('./wifire/sd-3layers.jpg')

photo_data[half_upper_mask] = 255
#photo_data[half_upper_mask] = random.randint(200,255)
plt.figure(figsize=(15,15))
plt.imshow(photo_data)

#22
photo_data = misc.imread('./wifire/sd-3layers.jpg')
red_mask = photo_data[:, :, 0] < 150

photo_data[red_mask] = 0
plt.figure(figsize=(15,15))
plt.imshow(photo_data)

#23
photo_data = misc.imread('./wifire/sd-3layers.jpg')
green_mask = photo_data[:, :, 1] < 150

photo_data[green_mask] = 0
plt.figure(figsize=(15,15))
plt.imshow(photo_data)

#24
photo_data = misc.imread('./wifire/sd-3layers.jpg')
blue_mask = photo_data[:, :, 2] < 150

photo_data[blue_mask] = 0
plt.figure(figsize=(15,15))
plt.imshow(photo_data)

#25
photo_data = misc.imread('./wifire/sd-3layers.jpg')

red_mask   = photo_data[:, :, 0] < 150
green_mask = photo_data[:, :, 1] > 100
blue_mask  = photo_data[:, :, 2] < 100

final_mask = np.logical_and(red_mask,green_mask,blue_mask)

photo_data[final_mask] = 0
plt.figure(figsize=(15,15))
plt.imshow(photo_data)