import os.path
import json
import scipy.misc
import numpy as np
import pprint
import matplotlib.pyplot as plt
import random
from skimage.transform import resize
class ImageGenerator:
    def __init__(self, file_path, label_path, batch_size, image_size, rotation=False, mirroring=False, shuffle=False):
        self.file_path = file_path
        self.label_path = label_path
        self.batch_size = batch_size
        self.image_size = image_size
        self.rotation = rotation
        self.mirroring = mirroring
        self.shuffle = shuffle
        self.class_dict = {0: 'airplane', 1: 'automobile', 2: 'bird', 3: 'cat', 4: 'deer', 5: 'dog', 6: 'frog', 7: 'horse', 8: 'ship', 9: 'truck'}
        
        with open(self.label_path, 'r') as label_file:
            self.labels = json.load(label_file)
        self.filenames = list(self.labels.keys())
        if self.shuffle:
            np.random.shuffle(self.filenames)
        
        self.index = 0
        self.epoch = 0

    def next(self):
        batch_filenames = self.filenames[self.index:self.index+self.batch_size]
        images = []
        labels = []
        
        for filename in batch_filenames:
            label = self.labels[filename]
            image = np.load(os.path.join(self.file_path, f"{filename}.npy"))
            
            if self.rotation:
                rotation_angle = np.random.choice([0, 90, 180, 270])
                image = np.rot90(image, k=rotation_angle // 90)
                
            if self.mirroring and np.random.rand() < 0.5:
                image = np.fliplr(image)
                
            image = resize(image, self.image_size)
            
            images.append(image)
            labels.append(label)
            
        self.index += self.batch_size
        if self.index >= len(self.filenames):
            self.index = 0
            self.epoch += 1
            if self.shuffle:
                np.random.shuffle(self.filenames)
        
        return np.array(images), np.array(labels)

    def current_epoch(self):
        return self.epoch

    def class_name(self, label):
        return self.class_dict[label]
    def show(self):
        # In order to verify that the generator creates batches as required, this functions calls next to get a
        # batch of images and labels and visualizes it.
        #TODO: implement show method
        images, labels = self.next()
        rows = int(np.sqrt(self.batch_size))
        cols = self.batch_size // rows
        fig, axes = plt.subplots(rows, cols, figsize=(10, 10))
        for i, ax in enumerate(axes.flat):
            ax.imshow(images[i])
            ax.set_title(self.class_dict[labels[i]])
            ax.axis('off')
        plt.subplots_adjust(wspace=0.2, hspace=0.5)
        plt.show()

#i=ImageGenerator('exercise_data','Labels.json',
#                 12,[250,250,3])

#i.next()
#i.show()