# tensorflow_imageclassifier
Clone https://github.com/llSourcell/tensorflow_image_classifier

Go through: https://www.youtube.com/watch?v=QfNvhPx5Px8

1. link for output_graph.pb gdrive: https://drive.google.com/open?id=0B8bmagS876BFb1JGNjh2d0VTcHc
  - Label : Darth Vader
  - Label : Darth Maul
2. link for output_graph.pb gdrive: https://drive.google.com/drive/u/1/folders/0B8bmagS876BFMm9Ua0Y0SlQwZEU
  - Label : Chekov
  - Label : Kirk
  - Label : Spock
  
  
<p>Platform</p>
  - Ubuntu 16.04 LTS
  - installation and working procedure : https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/

<p>
Get it up
</p>
  - docker run -it -v $HOME/tf_files:/tf_files  gcr.io/tensorflow/tensorflow:latest-devel
  - cd tensorflow
  - follow page #4 : https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#4

<p>
Or if using scripts
</p>
  - docker run -it -v $HOME/tf_files:/tf_files  gcr.io/tensorflow/tensorflow:latest-devel
  - cd tf_files/
  - sh train.sh classifier1/ ../tensorflow
  - sh guess.sh < " image file " > classifier1/
  - sh bash batch_guess.sh < " path for all images " > /tf_files/classifier1 /tf_files/

</hr>
Folder and files
  - tf_files/
  - tf_files/classifier1/ 
  - tf_files/classifier1/data/
  - tf_files/classifier1/data/class1/
  - tf_files/classifier1/data/class1/<"IMAGES">
  - tf_files/classifier1/data/class2/
  - tf_files/classifier1/data/class2/<"IMAGES">
  - train.sh
  - guess.sh
  - batch_guess.sh
</hr>

<h3>Image reference<h3> 

![retrained](https://github.com/rahuldeo2047/tensorflow_imageclassifier/blob/master/Screenshot%20from%202016-09-13%2008-04-12.png)
![output](https://github.com/rahuldeo2047/tensorflow_imageclassifier/blob/master/Screenshot%20from%202016-09-13%2008-05-36.png)



