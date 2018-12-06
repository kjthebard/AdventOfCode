from shapely.geometry import Polygon, LinearRing, LineString, box
import matplotlib.pyplot as plt
import pandas as pd
myfile = open('/Users/kieran/PycharmProjects/adventofcode_day1/data3.txt', 'r')

contents = myfile.read().strip().splitlines()
myfile.close()

my_dict = {"_id":[], "x":[], "y":[] ,  "size":[]}
for item in contents:
    id, location_size = item.split('@')
    location, size = location_size.split(':')
    x, y = location.split(',')
    my_dict["_id"].append(id)
    my_dict["x"].append(x)
    my_dict["y"].append(y)
    my_dict["size"].append(size)

df = pd.DataFrame(my_dict, columns=["_id", "x", "y", "size"])
print(df)

def RectangleMaker(x, y, size):
    """
    
    :param x:  x is the x point of the top left rectangle
    :param y:  y is the y point of the top left rectangle
    :param size: is the  size of the recatangle should be in format x by y
    :return: 
    """

    length,width = size.split("x")

    l = int(length)
    w = int(width)


    bottom_left = (x, y)
    top_left = (x, (y + w))
    bottom_right = ((l + x), y)
    top_right = ((l + x), (w + y))

    return bottom_left, top_left, bottom_right, top_right, x, y, l+x, w+y

bottom_left, top_left, bottom_right, top_right, minx, miny, maxx, maxy = RectangleMaker(2, 4, "40x12")

rectangle = LineString([bottom_left, bottom_right, top_left, top_right])
rectangle = Polygon(rectangle)
area = rectangle.area
rectangle = box(minx, miny, maxx, maxy)

print(rectangle)
print(rectangle.area)
