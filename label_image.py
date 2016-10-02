import tensorflow as tf, sys


image_path = sys.argv[1]
classifier_path = sys.argv[2]

from contextlib import contextmanager
import sys, os

@contextmanager
def suppress_stdout():
    with open(os.devnull, "w") as devnull:
        old_stdout = sys.stdout
        sys.stdout = devnull
        try:  
            yield
        finally:
            sys.stdout = old_stdout
#from contextlib import redirect_stdout

#f = io.StringIO()
#with redirect_stdout(f):

# Read in the image_data
image_data = tf.gfile.FastGFile(image_path, 'rb').read()

# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line 
	           in tf.gfile.GFile(classifier_path + "/retrained_labels.txt")]

# Unpersists graph from file
with tf.gfile.FastGFile(classifier_path + "/retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')
    #sys.stdout.flush()
#print("hello1")
with tf.Session() as sess:
    # Feed the image_data as input to the graph and get first prediction
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    #sys.stdout.flush()
    #print("hello1.5")
    with suppress_stdout():
        #print("hello1.6")
    	predictions = sess.run(softmax_tensor, \
             {'DecodeJpeg/contents:0': image_data})
        #print("hello2")
    # Sort to show labels of first prediction in order of confidence
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
    
    for node_id in top_k:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        print('%s (score = %.5f)' % (human_string, score))

