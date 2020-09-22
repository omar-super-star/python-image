import PIL
from PIL import Image
from PIL import ImageEnhance,ImageDraw,ImageFont
#that is a project change the colors of the image, creating variations based on a single photo

# use a bitmap font
font = ImageFont.truetype("readonly/fanwood-webfont.ttf", 75)
# read image and convert to RGB
image=Image.open("your photo")
image=image.convert('RGB')
l=[0.1,0.5,0.9]
r,g,b=image.split()
i1=0.1
i2=0.1
i3=0.1
c1=0
c2=0
c3=0
images=[]
# build a list of 9 images which have different brightnesses
n=0.1
for i in l:
    v=r.point(lambda x: x*i)
    
    display(r)
    images.append(Image.merge("RGB",(v,g,b)))
for i in l:
    v=g.point(lambda x: x*i)
    
    display(r)
    images.append(Image.merge("RGB",(r,v,b)))
for i in l:
    v=b.point(lambda x: x*i)
    
    images.append(Image.merge("RGB",(r,g,v)))
# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0
r=1
for img in images:
    # Lets paste the current image into the contact sheet
    
    if r<=3:
        draw = ImageDraw.Draw(img)
        draw.rectangle((0,400,800,450),fill="black")
        draw.text((0, 400), "channel {} intensity {}".format(c1,i1), font=font)
        c2+=1
        i2+=0.4
    elif r<=6:
        draw = ImageDraw.Draw(img)
        draw.rectangle((0,400,800,450),fill="black")
        draw.text((0, 400), "channel {} intensity {}".format(c1,i1), font=font)
        c3+=1
        i3+=0.4 
    elif r<=9:
        draw = ImageDraw.Draw(img)
        draw.rectangle((0,400,800,450),fill="black")
        draw.text((0, 400), "channel {} intensity {}".format(c1,i1), font=font)
        c1+=1
        i1+=0.4
    contact_sheet.paste(img, (x, y))    
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width
    r+=1   
# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
