#TfLite Converter for our H5 models
import tensorflow as tf
from keras.models import load_model

model = load_model("models\LeafModel_best.h5", compile=False)
model.compile(
    optimizer = tf.keras.optimizers.RMSprop(learning_rate = 0.00013),
    loss = tf.keras.losses.BinaryCrossentropy(),
    metrics = ['accuracy',
               'Precision',
               'Recall'
              ]
)
model.summary()
converter = tf.lite.TFLiteConverter.from_keras_model(
    model = model
)

#converter_SpinachClassify.optimizations = [tf.lite.Optimize.DEFAULT]

lite_model = converter.convert()

with open("models\lite_LeafModel_best.tflite","wb") as f:
    f.write(lite_model)