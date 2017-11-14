# ILGnet

This is an open-source project for the aesthetic evaluation of images based on the deep learning-caffe framework, which we completed in the [Victory team of Besti](http://kislab.besti.edu.cn/victory/).


In this paper we investigate the image aesthetics classification problem, aka, automatically classifying an image into low or high aesthetic quality, which is quite a challenging problem beyond image recognition. Deep convolutional neural network (DCNN) methods have recently shown promising results for image aesthetics assessment. Currently, a powerful inception module is proposed which shows very high performance in object classification. However, the inception module has not been taken into consideration for the image aesthetics assessment problem. In this paper, we propose a novel DCNN structure codenamed ILGNet for image aesthetics classification, which introduces the Inception module and connects intermediate Local layers to the Global layer for the output. Besides, we use a pre-trained image classification CNN called GoogLeNet on the ImageNet dataset and fine tune our connected local and global layer on the large scale aesthetics assessment AVA dataset [1]. The experimental results show that the proposed ILGNet outperforms the state of the art results in image aesthetics assessment in the AVA benchmark.

**The AVA dataset**

For a fair comparison, we adopted same strategy to construct two sub datasets of AVA as the previous work.

[1] Naila Murray, Luca Marchesotti, Florent Perronnin. AVA: A Large-Scale Database for Aesthetic Visual Analysis. Computer Vision and Pattern Recognition (CVPR), 2012.

• AVA1: We chose the score of 5 as the boundary to divide the dataset into high quality class and low quality class. In this way, there are 74,673 images in low quality and 180,856 images in high quality. the training and test sets contain 235,529 and 20000 images.

• AVA2: to increase the gap between images with high aesthetic quality and images with low aesthetic quality, we firstly sort all images by their mean scores. Then we pick out the top 10% images as good and the bottom 10% images as bad. Thus, we select 51,106 images form the AVA dataset. And all images are evenly and randomly divided into training set and test set, which contains 25,553 images.


**The way of test**

please use caffe test tools to test accuracy.

**The Accuracy of this random partition in the './data'**

The accuracy we achieve in the  AVA1 dataset is 81.68% with δ=0.And the accuracy is up to 82.66% using Inception V4.

The accuracy we achieve in the  AVA2 dataset is 85.50%.And the accuracy is up to 85.53% using Inception V4.

We achieve the state of the art of the aesthetic classification accuracy.

The random partition programs are in the './src'

**The Trained Models**

The size of the trained model is above 500MB. 


You can download them from the BaiduYun cloud disk or Google Drive:


BaiduYun Links:

[ILGnet-AVA1.caffemodel](https://pan.baidu.com/s/1slMv4yp)

[ILGnet-AVA2.caffemodel](https://pan.baidu.com/s/1bpBsIZH)


Google Drive Links:

[ILGnet-AVA1.caffemodel](https://drive.google.com/file/d/0B-wWngvfWr7WekNRX04xSzJEWlE/view?usp=sharing)

[ILGnet-AVA2.caffemodel](https://drive.google.com/file/d/0B-wWngvfWr7WRDl4YUFNTmJqenM/view?usp=sharing)

**Plus:The deploy.prototxt before is wrong. Now we upload the correct file, and thanks for your suggestion.**

**Our paper**

Xin Jin, Jingying Chi, Siwei Peng, Yulu Tian, Chaochen Ye and Xiaodong Li. **Deep Image Aesthetics Classification using Inception Modules and Fine-tuning Connected Layer**. The 8th International Conference on Wireless Communications and Signal Processing (**WCSP**), Yangzhou, China, 13-15 October, 2016 **[pdf](http://jinxin.me/downloads/papers/019-WCSP2016a/ILGNet-Final.pdf)**(5.94MB)  **[oral presentation](http://jinxin.me/downloads/papers/019-WCSP2016a/WCSP2016-ILGNet-presentation.pdf)**(19.1MB) **[arXiv](https://arxiv.org/abs/1610.02256)**(1610.02256)  **[[Project]](http://kislab.besti.edu.cn/victory/?p=242)** 


<img src="http://jinxin.me/downloads/pics/WCSP2016-Classification.jpg", width='700'>

<img src="http://jinxin.me/downloads/pics/WCSP2016-Accuracy.jpg", width='700'>

If you find our model/method/dataset useful, please cite our work:

*************************************************************************************

@inproceedings{DBLP:conf/wcsp/JinCPTYL16,

  author    = {Xin Jin and 
              Jingying Chi and
              Siwei Peng and
              Yulu Tian and
              Chaochen Ye andXiaodong Li},

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




