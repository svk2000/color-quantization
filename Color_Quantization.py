import sys
import numpy as np
from sklearn import cluster
from skimage import io
import os


def quantize(raster, n_colors):
    width, height, depth = raster.shape
    reshaped_raster = np.reshape(raster, (width * height, depth))

    model = cluster.KMeans(n_clusters=n_colors)
    labels = model.fit_predict(reshaped_raster)
    palette = model.cluster_centers_

    quantized_raster = np.reshape(palette[labels], (width, height, palette.shape[1]))

    return quantized_raster


def main():
    image_urls =['https://personal.utdallas.edu/~axn112530/cs6375/unsupervised/images/image1.jpg',
                 'https://personal.utdallas.edu/~axn112530/cs6375/unsupervised/images/image2.jpg',
                 'https://personal.utdallas.edu/~axn112530/cs6375/unsupervised/images/image3.jpg',
                 'https://personal.utdallas.edu/~axn112530/cs6375/unsupervised/images/image4.jpg',
                 'https://personal.utdallas.edu/~axn112530/cs6375/unsupervised/images/image5.jpg']
    kmeans_clusters =[8,16,32]
    path = 'quantizedImages'

    if not os.path.exists(path):
        os.makedirs(path)
    image_counter = 1
    for url in image_urls:
        raster = io.imread(url)
        for cluster_param in kmeans_clusters:
            quantized_raster = quantize(raster, cluster_param)
            io.imsave('./'+path+'/quantized_image_'+str(image_counter)+'_K_'+str(cluster_param)+'.png', quantized_raster);
            print(url)
            print(cluster_param)
        image_counter = image_counter + 1
        sys.exit()
main();
