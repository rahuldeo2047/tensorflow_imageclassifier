echo $1 && echo $2 && python $2/tensorflow/examples/image_retraining/retrain.py \
--bottleneck_dir=/tf_files/$1/bottlenecks \
--how_many_training_steps 100 \
--model_dir=/tf_files/$1/inception \
--output_graph=/tf_files/$1/retrained_graph.pb \
--output_labels=/tf_files/$1/retrained_labels.txt \
--image_dir /tf_files/$1/data


# cd tf_files/
# sh train.sh classifier1/ ../tensorflow
# sh guess.sh <<image file>>
