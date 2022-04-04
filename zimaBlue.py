# -*- coding: utf-8 -*-

import numpy as np
import cv2 as cv


ZimaBlue = (255,127,0)
imagem = np.zeros((1000,800,3),dtype=np.uint8)

imagemAssinatura = np.zeros((1000,800,3),dtype=np.uint8)

cy0 , cx0 = imagem.shape[:2] 


video = cv.VideoWriter('./ZimaBlue.mp4',cv.VideoWriter.fourcc(*'mp4v'),15,(cx0,cy0))

cx0 , cy0 = int(cx0/2) , int(cy0/2)

cx1,cy1 = (cx0+50,cy0+100)


cv.putText(imagemAssinatura,
           'Zima Blue',
           (cx0-50,cy0+50),
           cv.FONT_HERSHEY_SIMPLEX,
           1,
           ZimaBlue,
           1,
           cv.LINE_AA)

def retangulo(imageParam,pt1,pt2,cor):
    
    cv.rectangle(imageParam,
                 pt1,
                 pt2,
                 cor,
                 cv.FILLED)

def preenche(imageParam,pt1,pt2):
    cv.rectangle(imageParam,
             pt1,
             pt2,
             (0,0,0),
             3,
             cv.LINE_AA)
    
def circulo(imageParam,pt1,cor):
    cv.circle(imageParam,
              (pt1),
              4,
              cor,
              -1)
def linha(imageParam,pt1,pt2,cor):
    cv.line(imageParam,
            pt1,
            pt2,
            cor,
            1,
            cv.LINE_8)

video.write(imagem)
retangulo(imagem,(cx0,cy0),(cx1,cy1),ZimaBlue)
cv.imshow('ZimaBlue',imagem)

for i in range(100):

    video.write(imagem)
    cv.waitKey(300)

for i in range(0,25): 
    video.write(imagem)
    preenche(imagem,(cx0+i,cy0+i),(cx1-i,cy1-i))
    cv.imshow('ZimaBlue',imagem)
    cv.waitKey(45)


circulo(imagem, (cx0+25, cy0+50),ZimaBlue)
video.write(imagem)
for i in range(0,60):
    video.write(imagem)
    linha(imagem,((cx0+25)-i,cy1-50),((cx0+25)+i,cy1-50),ZimaBlue)
    cv.imshow('ZimaBlue',imagem)
    cv.waitKey(60)

circulo(imagem, (cx0+25, cy0+50),(0,0,0))
video.write(imagem)
for i in range(0,60): 
    video.write(imagem)
    linha(imagem,((cx0+25)-i,cy1-50),((cx0+25)+i,cy1-50),(0,0,0))
    cv.imshow('ZimaBlue',imagem)
    cv.waitKey(60)

for i in np.arange(0.00,1.00,0.01):
    
    added_image = cv.addWeighted(imagemAssinatura,i,imagemAssinatura,i,0)
    video.write(added_image)
    cv.imshow('ZimaBlue',added_image)
    cv.waitKey(300)
video.release()
cv.waitKey()
cv.destroyAllWindows()
