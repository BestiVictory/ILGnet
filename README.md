# ILGnet

This is an open-source project for the aesthetic evaluation of images based on the deep learning-caffe framework, which we completed in our BestiVictory team lab.
The Internet

The Deep Convolutional Neural Network (DCNN) method has recently yielded the desired image aesthetic assessment results. At present, a powerful model is presented, which shows very high performance in binary classification. We propose a new DCNN structure, which is named ILGNet, for image aesthetics classification, the concept of inception introduction ,the middle part of the local layer to connect to the global level for output. In addition, we used CNN to trained the image classification with ImageNet dat...(line truncated)...

The AVA dataset

For a fair comparison, we adopted same strategy to construct
two sub dataset of AVA as the previous work.

• AVA1: We chose the score of 5 as the boundary to divide
the dataset into high quality class and low quality class.
In this way, there are 74,673 images in low quality and
180,856 images in high quality. the training and test sets
contain 235,529 and 20000 images.

• AVA2: to increase the gap between images with high
aesthetic quality and images with low aesthetic quality,
we firstly sort all images by their mean scores. Then we
pick out the top 10% images as good and the bottom 10%
images as bad. Thus, we select 51,106 images form the
AVA dataset. And all images are evenly and randomly
divided into training set and test set, which contains
25,553 images.

The way of test
please use caffe test tools to test accuracy.

The Accuracy 
The accuracy we achieve in the  AVA1 dataset is 81.68% with δ=0.
The accuracy we achieve in the  AVA1 dataset is 85.50%.
We achieve the state of the art of the aesthetic classification accuracy.

our paper link:http://jinxin.me/downloads/papers/019-WCSP2016a/ILGNet-Final.pdf

If you find our model/method/dataset useful, please cite our work:

*************************************************************************************
@inproceedings{DBLP:conf/wcsp/JinCPTYL16,
  author    = {Xin Jin and
               Jingying Chi and
               Siwei Peng and
               Yulu Tian and
               Chaochen Ye and
               Xiaodong Li},
  title     = {Deep image aesthetics classification using inception modules and fine-tuning
               connected layer},
  booktitle = {8th International Conference on Wireless Communications {\&} Signal
               Processing, {WCSP} 2016, Yangzhou, China, October 13-15, 2016},
  pages     = {1--6},
  year      = {2016},
  crossref  = {DBLP:conf/wcsp/2016},
  url       = {http://dx.doi.org/10.1109/WCSP.2016.7752571},
  doi       = {10.1109/WCSP.2016.7752571},
  timestamp = {Fri, 16 Dec 2016 12:48:17 +0100},
  biburl    = {http://dblp.uni-trier.de/rec/bib/conf/wcsp/JinCPTYL16},
  bibsource = {dblp computer science bibliography, http://dblp.org}
}
***************************************************************************************


Latest edit
Jan 15, 2017




