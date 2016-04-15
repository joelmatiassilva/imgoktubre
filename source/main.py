import libImg
import os
import glob
#print glob.glob("../img/*.jpg")

for jpg in glob.glob("../img/*.jpg"):        # Second Example
   libImg.resize_and_crop(jpg, '../newImg/'+os.path.basename(jpg), (150,150))
   
print 'TERMINO'