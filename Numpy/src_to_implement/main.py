from pattern import Checker
from pattern import Circle
from pattern import Spectrum


class main:
    
    def drawCheckerboard():
        #for the checkerboard
        checkerboard = Checker(16,4)
        checkerboard.draw()
        checkerboard.show()
        
        
    def drawCircle():
        #for the Circle
        circle = Circle(64, 8.99, [30, 30])
        circle.draw()
        circle.show()
        
    def drawSpectrum():
        
        #testSpectrum = np.load('D:\backuped data\Data from HP\Personal Data\FAU Data Science\Semester 1\Deep Learning\exercise0_material\src_to_implement\reference_arrays\spectrum.npy')
        #for the color spectrum
        spectrum = Spectrum(64)
        spectrum.draw()
        spectrum.show()        
    
    
    
    
    if __name__ == '__main__':
        drawCheckerboard()
        drawCircle()
        drawSpectrum()
        