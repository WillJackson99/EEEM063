import os
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img


def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles
#imName = '/home/will/Documents/imageProc/data/downloads/Formula1/Mercedes w10/173.minichamps-118-mercedes-w10-hamilton-winner-shanghai-2019-.jpg'
datagen = ImageDataGenerator(
        rotation_range=15,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.1,
        zoom_range = 0.05,
        horizontal_flip=True,
        fill_mode='nearest')


#dirName = '/home/will/Documents/imageProc/data/downloads/Formula1_Aug/Mercedes w10' 
#dirName = '/home/will/Documents/imageProc/data/downloads/Formula1_Aug/Ferrari F2004'
#dirName = '/home/will/Documents/imageProc/data/downloads/Formula1_Aug/Williams FW18'
#dirName = '/home/will/Documents/imageProc/data/downloads/Formula1_Aug/Mclaren MP4_4'
#dirName = '/home/will/Documents/imageProc/data/downloads/Formula1_Aug/Ferrari 312T'

Directories = ['/home/will/Documents/imageProc/data/downloads/Formula1_Aug/Mercedes w10',
                '/home/will/Documents/imageProc/data/downloads/Formula1_Aug/Ferrari F2004',
                '/home/will/Documents/imageProc/data/downloads/Formula1_Aug/Williams FW18',
                '/home/will/Documents/imageProc/data/downloads/Formula1_Aug/Mclaren MP4_4',
                '/home/will/Documents/imageProc/data/downloads/Formula1_Aug/Ferrari 312T']

for dirName in Directories:

    listOfFiles = getListOfFiles(dirName)

    size = len(listOfFiles)/2
    print(len(listOfFiles))
    z = 0

    for imName in listOfFiles:

        img = load_img(imName)
        x = img_to_array(img)
        x = x.reshape((1,) + x.shape)

        i = 0
        for batch in datagen.flow(x, batch_size=1,save_to_dir=dirName, 
                save_prefix='aug', save_format='jpeg'):
            i += 1
            if i > 0:
                break
        z += 1
        if z > size:
            break