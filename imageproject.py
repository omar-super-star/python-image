import zipfile

from PIL import Image,ImageDraw,ImageFont
import pytesseract 
import cv2 as cv
import numpy as np
with zipfile.ZipFile('small_img.zip', 'r') as myzip:
    pageslist=myzip.namelist()
    myzip.extractall()
print(pageslist)
# loading the face detection classifier
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\User\Desktop\myproject\New folder (2)\tesseract.exe'
face_cascade = cv.CascadeClassifier(cv.data.haarcascades +'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('readonly/haarcascade_eye.xml')
faces_photo=[]
n=input()
using_image={}
contact_sheet_list=[]
for i in pageslist:
    image=Image.open(i)
    image_cv=cv.imread(i)
    text=pytesseract.image_to_string(image)
    if n in text:
        using_image[i]=using_image.get(i,[]).append(image)
        using_image_cv=image_cv
        gray = cv.cvtColor(using_image_cv, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3,5)
        for j in faces:
            pil_img=Image.fromarray(gray,mode="L")
            faces_photo.append(pil_img.crop((j[0],j[1],j[0]+j[2],j[1]+j[3])))
        locationx=0
        locationy=190
        under=1
        contact_sheet=Image.new(pil_img.mode,(150*5,pil_img.height))
        
        for b in faces_photo:
            b=b.resize((150,900))
            contact_sheet.paste(b, (locationx, locationy))
            locationx+=150
            if locationx>=150*5:
                locationx=0
                locationy+=900
                under+=1
        contact_sheet=contact_sheet.resize((150*5,locationy+900))
        contact_sheet=contact_sheet.crop((0,0,150*5,270*under+100))
        d=ImageDraw.Draw(contact_sheet)
        font = ImageFont.truetype("arial.ttf",55)
        d.rectangle((0,0,150*5,100),fill="white")
        d.text((0,0),f"result found in file {i}.",font=font)
        contact_sheet_list.append(contact_sheet)
standard_height=contact_sheet_list[0].height
finial_sheet=Image.new(pil_img.mode,(150*5,3*standard_height))
current=0
for i in contact_sheet_list:
    finial_sheet.paste(i,(0,current))
    current+=standard_height