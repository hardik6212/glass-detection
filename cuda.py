import tensorflow as tf

# Check if TensorFlow detects GPU
print(f"GPU Available: {tf.config.list_physical_devices('GPU')}")

# Check TensorFlow CUDA version
print(f"Built with CUDA: {tf.test.is_built_with_cuda()}")
print(f"GPU Device Name: {tf.test.gpu_device_name()}")
