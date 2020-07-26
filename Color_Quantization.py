import sys
import numpy as np
from sklearn import cluster
from skimage import io
import os


def quantize(image, cluster_param):
    width, height, depth = image.shape
    reshaped_image = np.reshape(image, (width * height, depth))
    model = cluster.KMeans(n_clusters=cluster_param)
    labels = model.fit_predict(reshaped_image)
    palette = model.cluster_centers_
    quantized_raster = np.reshape(palette[labels], (width, height, palette.shape[1]))
    return quantized_raster


def main():
    image_urls =['https://personal.utdallas.edu/~axn112530/cs6375/unsupervised/images/image1.jpg',
                 'https://personal.utdallas.edu/~axn112530/cs6375/unsupervised/images/image2.jpg',
                 'https://personal.utdallas.edu/~axn112530/cs6375/unsupervised/images/image3.jpg']
    kmeans_clusters = [4,8,12]
    path = 'quantizedImages'
    if len(sys.argv) > 1:
        kmeans_clusters = [int(i) for i in list(sys.argv[1].split(','))]
    if not os.path.exists(path):
        os.makedirs(path)
    image_counter = 1
    for url in image_urls:
        raster = io.imread(url).astype(np.uint8)
        for cluster_param in kmeans_clusters:
            quantized_raster = quantize(raster, cluster_param)
            io.imsave('./'+path+'/quantized_image_'+str(image_counter)+'_K_'+str(cluster_param)+'.jpg', quantized_raster);
            print('image URL :'+url)
            print('K-Value: '+ str(cluster_param))
        image_counter = image_counter + 1
    sys.exit(0)


main();
