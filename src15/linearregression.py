

import tensorflow as tf
import os

# Session / log
tf.logging.set_verbosity(tf.logging.ERROR)
sess = tf.Session()

def defineGraph():
  a = tf.constant(2.5, name='first_val')
  b = tf.constant(4.5, name='second_val')

  sum = a + b;

  print(tf.get_default_graph().get_operations())
  print(tf.get_default_graph().get_tensor_by_name('first_val:0'))

  # add to save graph
  # tf.train.write_graph(tf.get_default_graph(), os.getcwd(), 'out/graph.dat')

  # Create operations that generate summary data
  tf.summary.scalar("a", a)
  tf.summary.scalar("b", b)
  tf.summary.scalar("total sum", sum)

  # Merge the operations into a single operation
  merged_op = tf.summary.merge_all()
  with tf.Session() as sess:
    _, summary = sess.run([sum, merged_op])

  custom_summary = tf.Summary(value=[
      tf.Summary.Value(tag="num_tag", simple_value=5.0),
  ])
  tf.summary.FileWriter("out", graph=tf.get_default_graph())

def showVectors():
  data1 = [[1,2],[3,4]]
  data2 = [[6,7],[8,9]]

  tensorData1 = tf.constant(data1)
  tensorData2 = tf.constant(data2)

  tensSum = tensorData1 + tensorData2;
  tensDot = tf.tensordot(tensorData1,tensorData2,1)

  print(sess.run(tensDot))

def seelinear():
  x = tf.placeholder(tf.float32)
  y = tf.placeholder(tf.float32)

  a = tf.Variable([2], dtype=tf.float32)
  b = tf.Variable([-1], dtype=tf.float32)

  linear_model = a*x + b 

  init = tf.global_variables_initializer()
  sess.run(init)

  print(sess.run(linear_model, {x:[0,1,2,3,4,5]}))

def linearregression():
  x = tf.placeholder(tf.float32)
  y = tf.placeholder(tf.float32)

  feed_dict = {
    x:[0,1,2,3,4,5],
    y:[-1,  1,  3,  5,  7,  9]
  }

  # to be found
  A = tf.Variable(tf.random_normal([]))
  B = tf.Variable(tf.random_normal([]))

  model = A*x + B
  loss = tf.reduce_mean(tf.pow(model - y, 2))

  init = tf.global_variables_initializer()
  sess.run(init)

  optimizer = tf.train.GradientDescentOptimizer(0.1)
  optimizer_op = optimizer.minimize(loss)

  for step in range(50):
    print(sess.run([A,B]))
    sess.run(optimizer_op, feed_dict)

  optimizer2 = tf.train.GradientDescentOptimizer(0.001)
  optimizer_op2 = optimizer.minimize(loss)

  for step in range(150):
    sess.run(optimizer_op2, feed_dict)

  print("END")
  print(sess.run([A,B]))

linearregression()
