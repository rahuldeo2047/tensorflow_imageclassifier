# tensorflow_imageclassifier
Clone https://github.com/llSourcell/tensorflow_image_classifier

Go through: https://www.youtube.com/watch?v=QfNvhPx5Px8

link for output_graph.pb gdrive: https://drive.google.com/open?id=0B8bmagS876BFb1JGNjh2d0VTcHc

<p>
<h3>Get it up<h3>
</p>
  - Ubuntu 16.04 LTS
  - installation and working procedure : https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/
  - docker run -it -v $HOME/tf_files:/tf_files  gcr.io/tensorflow/tensorflow:latest-devel
  - cd tensorflow
  - follow page #4 : https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#4

<p>
Or if using scripts
</p>
  - docker run -it -v $HOME/tf_files:/tf_files  gcr.io/tensorflow/tensorflow:latest-devel
  - cd tf_files/
  - sh train.sh classifier1/ ../tensorflow
  - sh guess.sh < " image file " >

<h3>Image reference<h3> 

![retrained](https://github.com/rahuldeo2047/tensorflow_imageclassifier/blob/master/Screenshot%20from%202016-09-13%2008-04-12.png)
![output](https://github.com/rahuldeo2047/tensorflow_imageclassifier/blob/master/Screenshot%20from%202016-09-13%2008-05-36.png)



