#TfLite Converter for our H5 models
import tensorflow as tf
from keras.models import load_model

# modelLeafDetect = 
modelSpinachClassify = load_model("models\SFDNet_best_val_accuracy.h5")
converter_SpinachClassify = tf.lite.TFLiteConverter.from_keras_model(
    model = modelSpinachClassify
)

#converter_SpinachClassify.optimizations = [tf.lite.Optimize.DEFAULT]

lite_SpinachClassify = converter_SpinachClassify.convert()

with open("models\lite_SFDNet_model.tflite","wb") as f:
    f.write(lite_SpinachClassify)