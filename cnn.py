from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Convolution2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import MaxPooling2D
from matplotlib import pyplot as plt

classifier = Sequential()

# 1st model

classifier.add(Convolution2D(512, (3, 3), input_shape=(64, 64, 3), activation='relu',strides=(3,3)))

classifier.add(MaxPooling2D(pool_size=(3, 3)))

classifier.add(Convolution2D(256, (2, 2), activation='relu'))

classifier.add(MaxPooling2D(pool_size=(1, 1)))

classifier.add(Flatten())

classifier.add(Dense(units=64, activation='relu'))

classifier.add(Dense(units=6, activation='softmax'))

classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1. / 255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)
print("\nTraining the data...\n")
training_set = train_datagen.flow_from_directory('C:\\Users\\Tejkiran\\Desktop\\major project\\CODE\\dataset\\train',
                                                 target_size=(64,64),
                                                 batch_size=12,
                                                 class_mode='categorical'
                                                 )

test_set = test_datagen.flow_from_directory('C:\\Users\\Tejkiran\Desktop\\major project\CODE\\dataset\\test',
                                            target_size=(64,64),
                                            batch_size=12,
                                            class_mode='categorical'
                                            )
print("\n Testing the data.....\n")

history=classifier.fit_generator(training_set,steps_per_epoch =30,epochs = 500,validation_data = test_set,verbose = 1)

classifier.save(r"CNN.h5")

# "Accuracy"

plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.xlabel('accuracy')
plt.ylabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.savefig(r"C:\Users\Tejkiran\Desktop\major project\CNN_acc.png")
plt.show()

# "Loss"
plt.plot(history.history['loss'])
plt.plot(history.history['loss'])
plt.title('model loss')
+plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper left')
plt.savefig(r"C:\Users\Tejkiran\Desktop\major project\CNN_loss.png")
plt.show()


vgg_acc=history.history['val_accuracy'][-1]
print(vgg_acc)