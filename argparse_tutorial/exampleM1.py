import argparse
import matplotlib.pyplot as plt
import os
from skimage.io import imread, imshow


def main(root_v, name_v, enable_otsu):
    print("Hello "+name_v)
    if enable_otsu:
        print("Otsu enabled")
    else:
        print("Otsu not enabled: ", enable_otsu)

    print(root_v)
    
    image_location_1 = os.path.join(root_v, 'case1')
    # image_location_2 = root_v+'/case2/'

    print(image_location_1)
    img1 = imread(os.path.join(image_location_1, '1.jpg'))
    print(image_location_1)
    plt.imshow(img1)
    plt.show()


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-in', '--input', required=True, help="path to root input folder")
    ap.add_argument('-f', '--format', required=True, help="image format")
    ap.add_argument('-n', '--name', required=True,  type=str, help="enter your name please")
    ap.add_argument('-ot', '--otsu', action='store_true', help="enable otsu segmentation if not declared skip")

    args = vars(ap.parse_args())
    name = args["name"]
    otsu = args["otsu"]
    root = args["input"]
    print(args["format"])
    main(root, name, otsu)
