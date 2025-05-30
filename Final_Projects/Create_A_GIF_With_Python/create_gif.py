import imageio.v3 as iio # we are importin version 3 of the imageio pacage and nicknamed it as iio

filenames = [ 'Beagle-bark0.png','Beagle-bark1.png','Beagle-bark2.png','Beagle-bark3.png','Beagle-bark4.png'] #name of the images / images need to be on the same folder as the Python program file 
images = [] #Empty list to store actual image t¿data from these files

for filename in filenames:
    images.append(iio.imread(filename)) #The .imread() method loads an image based on the file path. So now, our images variable has all the images!

iio.imwrite('Beagle_bark.gif',images,duration=100, loop=0) #let’s use the .imwrite() method to turn the images into a GIF

#This takes in four arguments:
#'Beagle_bark.gif': This is the name you want to give to your new GIF file.
#images: The list containing the image data.
#duration = 500: How long each picture should show in the GIF, in milliseconds.
#loop = 0: How many times the GIF should repeat (0 means it keeps looping forever).