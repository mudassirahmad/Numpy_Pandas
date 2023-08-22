import numpy as np
import matplotlib.pyplot as plt

class Checker:
    
    def __init__ (self, resolution, tile_size):
        self.resolution = resolution
        self.tile_size= tile_size
        if resolution % (tile_size*2) != 0:
            raise ValueError("The resolution must be divisible by 2 times the tile size.")
        
        self.output= np.zeros((resolution,resolution))
    
    def draw(self):
        pattern = np.indices((self.resolution // self.tile_size, self.resolution // self.tile_size)).sum(axis=0)%2
        # Reshape and tile the pattern to create a full checkerboard
        checkerboard = np.tile(np.repeat(pattern, self.tile_size, axis=0).repeat(self.tile_size, axis=1), (1, 1))
        self.output = checkerboard
        return self.output.copy()
    
    def show(self):
        plt.imshow(self.output, cmap='gray',extent=[0, self.resolution, 0, self.resolution])
        plt.show()
    

class Circle:
    
    def __init__(self, resolution, radius, position):
        self.resolution= resolution
        self.radius= radius
        self.position=position
        self.output = np.zeros((resolution, resolution))
    
    def draw(self):
        x, y = np.meshgrid(np.arange(self.resolution), np.arange(self.resolution))
        distance = np.sqrt((x - self.position[0])**2 + (y - self.position[1])**2)
        self.output = (distance <= self.radius).astype(int)
        return self.output.copy()

    def show(self):
        plt.imshow(self.output, cmap='gray', extent=[0, self.resolution, 0, self.resolution])
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()
        
        
class Spectrum:
    
    def __init__(self, resolution):
        self.resolution=resolution
        self.output=None
    
    def draw(self):
        x = np.linspace(0, 1, self.resolution)
        y = np.linspace(0, 1, self.resolution)
        X, Y = np.meshgrid(x, y)
        R = X
        G = Y
        B = X[:, ::-1]
        print(R,G,B)
        self.output = np.stack([R, G, B], axis=-1)
        return self.output.copy()
    
    def show(self):
        plt.imshow(self.output, cmap='jet', vmin=0, vmax=1)
        plt.show()
