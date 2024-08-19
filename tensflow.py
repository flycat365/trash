import tensorflow as tf
tf.autograph.set_verbosity(0)
physical_devices = tf.config.experimental.list_physical_devices('GPU')
print(physical_devices)
config = tf.config.experimental.set_memory_growth(physical_devices[0], True)