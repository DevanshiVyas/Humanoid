#Name:Devanshi Vyas
#ID no.201101141
#This program generates a number of new images using blending,
#different filters and various effects and saves them as .jpg & saves them in the same folder.
#The program also creates an image by writing pixel by pixel
#P.S: while running this program,images 22,13 and 21 must be in the same folder as the program.
#Also as the images are big,it msy take a while. Please be patient.
# This is statement is required by the build system to query build info
if __name__ == '__build__':
	raise Exception
#import libraries
import sys
from PIL import Image
from PIL import ImageChops
from PIL import ImageFilter

ALPHA=0.5
im1 = Image.open("image22.jpg")
im2 = Image.open("image13.jpg")

im3 = Image.open("image21.jpg")
#Blending the images
Imt = Image.blend(im1,im2,ALPHA)
Im = Image.blend(Imt,im3,0.3)


# Original Blended Images
Im.save("Blended_Original.jpg","JPEG")

#Creating a new image by writing pixel to pixel
#size chosen to match the dimensions of the other image
img = Image.new( 'RGB', (1920,1200), "black")
pixels=img.load()
#for every pixel
for i in range(img.size[0]):   
    for j in range(img.size[1]):
        pixels[i,j] = (i,j,100)

#creating a random image then blending it with various other images  

piximg=Image.blend(Im,img,0.4)
piximg.save("Pixelimg.jpg","JPEG")


# Convert to black & white
ImBW = Im.convert('1')
ImBW.save('Blended_B&W.jpg',"JPEG")

# Use min filter
ImMin = Im.filter(ImageFilter.MinFilter(3))
ImMin.save('Blended_Min.jpg',"JPEG")

# Use max filter
ImMax = Im.filter(ImageFilter.MaxFilter(3))
ImMax.save('Blended_Max.jpg',"JPEG")

# Use median filter
ImMedian = Im.filter(ImageFilter.MedianFilter(size=3))
ImMedian.save('Blended_Median.jpg',"JPEG")

# Use mode filter
ImMode = Im.filter(ImageFilter.ModeFilter(size=3))
ImMode.save('Blended_Mode.jpg',"JPEG")

# Invert image (obtain negative)
ImInv = ImageChops.invert(Im)
ImInv.save('Blended_Inv.jpg',"JPEG")
 
# apply BLUR filter
ImBlur = Im.filter(ImageFilter.BLUR)
ImBlur.save('Blended_Blur.jpg',"JPEG")
 
# apply Gaussian BLUR filter
ImGBlur = Im.filter(ImageFilter.GaussianBlur(radius = 20))
ImGBlur.save('Blended_GaussianBlur.jpg',"JPEG")

# apply CONTOUR filter
ImContour = Im.filter(ImageFilter.CONTOUR)
ImContour.save('Blended_Contour.jpg',"JPEG")
 
# apply DETAIL filter
ImDetail = Im.filter(ImageFilter.DETAIL)
ImDetail.save('Blended_Detail.jpg',"JPEG")
 
# apply EDGE_ENHANCE filter
ImEH = Im.filter(ImageFilter.EDGE_ENHANCE)
ImEH.save('Blended_EdgeEnhance.jpg',"JPEG")
 
# apply EDGE_ENHANCE_MORE filter
ImEHM = Im.filter(ImageFilter.EDGE_ENHANCE_MORE)
ImEHM.save('Blended_EEM.jpg',"JPEG")
 
# apply EMBOSS filter
ImEmb = Im.filter(ImageFilter.EMBOSS)
ImEmb.save('Blended_Emboss.jpg',"JPEG")
 
# apply FIND_EDGES filter
ImEdges = Im.filter(ImageFilter.FIND_EDGES)
ImEdges = ImEdges.save('Blended_Find_Edges.jpg',"JPEG")
 
# apply SMOOTH filter
ImSmooth = Im.filter(ImageFilter.SMOOTH)
ImSmooth = ImSmooth.save('Blended_Smooth.jpg',"JPEG")
 
# apply SMOOTH_MORE filter
ImSmoothMore = Im.filter(ImageFilter.SMOOTH_MORE)
ImSmoothMore = ImSmoothMore.save('Blended_Smooth_More.jpg',"JPEG")
 
# apply SHARPEN filter
ImSharp = Im.filter(ImageFilter.SHARPEN)
ImSharp = ImSharp.save('Blended_Sharpen.jpg',"JPEG")
