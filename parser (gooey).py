# asdasd
# Notes:
# root = surfaces
# children (relevant) = surface (12)
# grandchildren (relevant) = name, bscan (200 per surface, each bscan tag contains 200 y values)

# goal = create np 200x200 array then plot using heatmap (matplotlib)

# next steps = make it so that you can enter the xml file name + write code for 3d visualisation
# useful site: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.contour.html

# gui?
# https://realpython.com/pysimplegui-python/
# done

from gooey import Gooey, GooeyParser

@Gooey
def main():
    import xml.etree.ElementTree as ET
    import matplotlib.pyplot as plt
    import numpy as np

    parser = GooeyParser()

    parser.add_argument("xml_file_path", action = "store", help = "Enter the exact XML file name (including file extension and ensure that the file is in the same folder that this python file is in): ")
    # parser.add_argument("surface_plot", action = "store", help = "Enter the number which corresponds to the respective surface you wish the plot. 1. ILM (ILM), 2. RNFL-GCL (RNFL-GCL), 3. GCL-IPL (GCL-IPL), 4. IPL-INL (IPL-INL), 5. INL-OPL (INL-OPL), 6. OPL-Henles fiber layer (OPL-HFL), 7. Boundary of myoid and ellipsoid of inner segments (BMEIS), 8. IS/OS junction (IS/OSJ), 9. Inner boundary of OPR (IB_OPR), 10. Outer boundary of OPR (OB_OPR), 11. Inner boundary of RPE (IB_RPE), 12. Outer boundary of RPE (OB_RPE)")
    parser.add_argument("surface_plot", choices = ["ILM (ILM)", "RNFL-GCL (RNFL-GCL)", "GCL-IPL (GCL-IPL)", "IPL-INL (IPL-INL)", "INL-OPL (INL-OPL)", "OPL-Henles fiber layer (OPL-HFL)", "Boundary of myoid and ellipsoid of inner segments (BMEIS)", "IS/OS junction (IS/OSJ)", "Inner boundary of OPR (IB_OPR)", "Outer boundary of OPR (OB_OPR)", "Inner boundary of RPE (IB_RPE)", "Outer boundary of RPE (OB_RPE)"], help = "Select the surface that you wish to plot.")
    # parser.add_argument("method_plot", action = "store", help = "Enter the number which corresponds to the respective visualisation you wish to plot the surface. 1. Heatmap, 2. 3D Surface Plot, 3. Contour Plot, 4. Pcolormesh Plot")
    parser.add_argument("method_plot", choices = ["Heatmap", "Contour Plot", "Pcolormesh"], help = "Select the visualisation method that you wish to use to plot the surface.")
    # xml_file_path = '1020Macular Cube 200x200_5-17-2012_14-58-7_OS_sn3395_cube_z_Surfaces_Retina-JEI-Final.xml'
    # xml_file_path = input("Enter the exact XML file name (including file extension and ensure that the file is in the same folder that this python file is in): ")

    args = parser.parse_args()

    tree = ET.parse(args.xml_file_path)
    root = tree.getroot()

    # tags. surface
    surface_counter = 0

    surfaces_lst = [] # contains the actual surfaces
    surfaces_lst_names = [] # contains the names of the surfaces -> use this to find index

    for surface in root.findall('surface'):
        surface_counter += 1
        surfaces_lst.append(surface)

    print(f"Surfaces (amount {surface_counter}):")

    label1 = 1
    for surface in root.findall('surface'):
        print(f"{label1}. {surface[1].text}")
        surfaces_lst_names.append(surface[1].text)
        label1 += 1

    surfaces_lst_index = surfaces_lst_names.index(args.surface_plot)

    print("")
    print(surfaces_lst_names) # print debugging
    print(surfaces_lst_index) # print debugging

    selected_surface = surfaces_lst[int(surfaces_lst_index)] # now with drop downs surfaces_plot contains a string

    print(f'{selected_surface[1].text} selected.') # print debugging

    plotting_methods = ["Heatmap", "Contour Plot", "Pcolormesh"]

    print("")
    label2 = 1
    for method in plotting_methods:
        print(f"{label2}. {method}")
        label2 += 1

    print("")

    # surfaces start at index 7 of root

    arr = [] # numpy arrays or regular lists?

    counter = 1
    for tg in root[7 + int(surfaces_lst_index)]: # iterating over bscan tags, error is here for last surface.
        # ("quack")
        if counter <= 3:
            counter += 1
            continue
        else:
            temp_lst = []
            for y in tg: # iterating over y tags
                temp_lst.append(int(y.text))
            arr.append(temp_lst)

    numpy_arr = np.array(arr) # does this actually do anything
    print(numpy_arr)

    method_plot_index = plotting_methods.index(args.method_plot)

    print("")
    print(plotting_methods) # print debugging
    print(args.method_plot) # print debugging
    print(method_plot_index) # print debugging

    if int(method_plot_index) == 0:
        print(args.method_plot)
        # print(type.args.method_plot)
        plt.imshow(numpy_arr)
        plt.colorbar()
        plt.title(f"Heatmap of {selected_surface[1].text} surface")
        plt.xlabel("x axis")
        plt.ylabel("y axis")
        plt.show()
    elif int(method_plot_index) == 1:
        print(args.method_plot)
        # print(type.args.method_plot)
        plt.contourf(numpy_arr)
        plt.colorbar()
        plt.title(f"Contour Plot of {selected_surface[1].text} surface")
        plt.xlabel("x axis")
        plt.ylabel("y axis")
        plt.show()
    elif int(method_plot_index) == 2:
        print(args.method_plot)
        # print(type.args.method_plot)
        plt.pcolormesh(numpy_arr)
        plt.colorbar()
        plt.title(f"Pcolormesh Plot of {selected_surface[1].text} surface")
        plt.xlabel("x axis")
        plt.ylabel("y axis")
        plt.show()


main()

