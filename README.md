# convnets-keras

This repo is regrouping some of of the most used CNN, pre-trained on the ImageNet Dataset, all of them implemented in Keras framework : 
- AlexNet : https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf
- VGG16 and VGG19 : http://arxiv.org/pdf/1409.1556.pdf


We also propose a heatmap option, which allow to detect the location of an object from a given synset.

<img src=https://raw.githubusercontent.com/heuritech/convnets-keras/master/examples/cars.jpg width="400px">

Here, we detect all the objects linkd to the synsets cars, and we produce a heatmap : 

<img src=https://raw.githubusercontent.com/heuritech/convnets-keras/master/examples/heatmap.png width="400px">

## Credits

## Install
The only dependencies are h5py, Theano and Keras. Run the following commands
```
pip install --user cython h5py
pip install --user git+https://github.com/Theano/Theano.git
pip install --user git+https://github.com/fchollet/keras.git
```
## Get the weights of the pre-trained networks
The weights can be found here : 
* <a href="http://files.heuritech.com/weights/alexnet_weights.h5">AlexNet weights</a>
* <a href="http://files.heuritech.com/weights/vgg16_weights.h5">VGG16 weights</a>
* <a href="http://files.heuritech.com/weights/vgg19_weights.h5">VGG19 weights</a>


## How to use the convnets

## Performances on ImageNet

## How to use the heatmap

## Get the links with the ImageNet synsets
