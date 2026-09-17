# Notes:
# root = surfaces
# children (relevant) = surface (12)
# grandchildren (relevant) = name, bscan (200 per surface, each bscan tag contains 200 y values)

# goal = create np 200x200 array then plot using heatmap (matplotlib)

# next steps = make it so that you can enter the xml file name + write code for 3d visualisation
# useful site: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html

import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import numpy as np

#xml_file_path = '1020Macular Cube 200x200_5-17-2012_14-58-7_OS_sn3395_cube_z_Surfaces_Retina-JEI-Final.xml'
xml_file_path = input("Enter the exact XML file name (including file extension and ensure that the file is in the same folder that this python file is in): ")
tree = ET.parse(xml_file_path)
root = tree.getroot()

# tags. surface
surface_counter = 0

surfaces_lst = []

for surface in root.findall('surface'):
    surface_counter += 1
    surfaces_lst.append(surface)

# print(surfaces_lst)

print(f"Surfaces (amount {surface_counter}):")

label1 = 1
for surface in root.findall('surface'):
    print(f"{label1}. {surface[1].text}")
    label1 += 1

print("")
surface_plot = int(input("Please enter the number of the surface you wish to plot: "))

selected_surface = surfaces_lst[surface_plot - 1]

print(f'{selected_surface[1].text} selected.')

plotting_methods = ["Heatmap", "3D Surface Plot", "Contour Plot", "Pcolormesh Plot",]

print("")
label2 = 1
for method in plotting_methods:
    print(f"{label2}. {method}")
    label2 += 1

print("")
method_plot = int(input(f"Please enter the number of the method you wish to plot {selected_surface[1].text} with: "))

# surfaces start at index 7 of root

arr = [] # didn't use numpy arrays b uhh uhhhh uhhhhhh

counter = 1
for tg in root[6 + surface_plot]: # iterating over bscan tags
    if counter <= 3:
        counter += 1
        continue
    else:
        temp_lst = []
        for y in tg: # iterating over y tags
            temp_lst.append(int(y.text))
        arr.append(temp_lst)

numpy_arr = np.array(arr) # does this actually do anything

if method_plot == 1:
    plt.imshow(numpy_arr)
    plt.colorbar()
    plt.title(f"Heatmap of {selected_surface[1].text} surface")
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.show()
elif method_plot == 2:
    print('wip :(')
elif method_plot == 3:
    plt.contourf(numpy_arr)
    plt.colorbar()
    plt.title(f"Contour Plot of {selected_surface[1].text} surface")
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.show()
elif method_plot == 4:
    plt.pcolormesh(numpy_arr)
    plt.colorbar()
    plt.title(f"Pcolormesh Plot of {selected_surface[1].text} surface")
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.show()

