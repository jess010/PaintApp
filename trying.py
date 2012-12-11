from Tkinter import *
import Image, ImageTk,ImageDraw
import os, sys
from tkFileDialog import askopenfilename
import tkFileDialog
from tkColorChooser import askcolor
import ImageFilter
import ImageEnhance
import ImageChops
import tkMessageBox

class Viewer:
    def __init__(self, master):
        self.index=0
        self.colors=[23,42,42]
        self.colors2=[23,23,32]
        self.xyz1=[4,0.33,0.33,0,0.33,4,0.33,0,0.33,0.33,4,0]
        self.xyz2=[0,0,0,0,0.33,0,0.33,0,0.33,0.33,0,0]
        self.xyz3=[4,4,0.33,0,4,4,0.33,0,4,0.33,4,0]
        self.xyz4=[4,0,0.33,0,0,4,0.33,0,0.33,0,4,0]
        self.xyz5=[4,4,4,0,0,4,0,0,0,4,4,0]
        self.xyz6=[4,1,2,0,2,4,2,0,1,4,4,0]
        self.xyz7=[0.5,0.5,0.5,0,0.5,0.5,0.5,0,0.5,0.5,0.5,0]
        self.call=[self.circle,self.circlef,self.rectangle,self.rectanglef,self.ellipse,self.ellipsef,self.square,self.squaref,self.pencil,self.crop,self.line,self.rubber,self.brush]
        self.call2=[self.circle2,self.circlef2,self.rectangle2,self.rectanglef2,self.ellipse2,self.ellipsef2,self.square2,self.squaref2,self.pencil2,self.crop2,self.line2,self.rubber2,self.brush2]
        self.call3=[self.circle3,self.circlef3,self.rectangle3,self.rectanglef3,self.ellipse3,self.ellipsef3,self.square3,self.squaref3,self.pencil3,self.crop3,self.line3,self.rubber3,self.brush3]
        self.sha=self.call[self.index]
        self.sha2=self.call2[self.index]
        self.sha3=self.call3[self.index]
        v=self.rectangle
        v1=self.rectangle2
        v2=self.rectangle3
        self.top = master
        self.index = 0
        self.btn='up'
        self.pt0=(0,0)
        self.size2=(1000,500)
        print 'sdjcnd'
        print self.size2
        #display first image
        self.im = Image.open('me.jpg')
        self.im0=self.im.copy()
        self.size = self.im.size
        self.im=self.im.resize((self.size2[0],self.size2[1]),Image.ANTIALIAS)
        self.tkimage = ImageTk.PhotoImage(self.im)
        self.lbl = Label(self.top, image=self.tkimage)
        self.rect=[0,0,self.size[0]/2,self.size[1]]
        self.lbl.pack(side='top')
        self.str1="#ffffff"
        self.str2="#ffffff"
        #menu
        self.menu=Menu(self.top)
        self.top.config(menu=self.menu)
        self.col0=(134,24,23)
        self.col1=(12,67,89)

                # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(self.menu, tearoff=0)
        filemenu.add_command(label="New File", command=lambda: self.newAsDlg())
        filemenu.add_command(label="Open File", command=lambda: self.openAsDlg())
        filemenu.add_command(label="Image 2", command=lambda: self.openAsDlg2())
        filemenu.add_command(label="Save File", command=lambda: self.SaveAsDlg())
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        self.menu.add_cascade(label="   File   ", menu=filemenu)

        filtermenu = Menu(self.menu, tearoff=0)
        filtermenu.add_command(label="Image Blur",command=self.fill1)
        filtermenu.add_command(label="Image Contour", command=self.fill2)
        filtermenu.add_command(label="Image Detail", command=self.fill3)
        filtermenu.add_command(label="Image Edge Enhance",command=self.fill4)
        filtermenu.add_command(label="More Edge Enhance", command=self.fill5)
        filtermenu.add_command(label="Image Emboss", command=self.fill6)
        filtermenu.add_command(label="Image Edges",command=self.fill7)
        filtermenu.add_command(label="Image Smooth", command=self.fill8)
        filtermenu.add_command(label="Image More Smooth", command=self.fill9)
        filtermenu.add_command(label="Image Sharpen", command=self.fill10)
        self.menu.add_cascade(label=" Filter Gallery ", menu=filtermenu)

        enhancemenu = Menu(self.menu, tearoff=0)
        enhancemenu.add_command(label="Color Balance", command=self.en1)
        enhancemenu.add_command(label="Brightness", command=self.en2)
        enhancemenu.add_command(label="Contrast",command=self.en3)
        enhancemenu.add_command(label="Sharpness", command=self.en4)
        enhancemenu.add_command(label="Color Adjustment", command=self.en5)
        enhancemenu.add_command(label="Grayscale", command=self.en6)
        self.menu.add_cascade(label="Image Enhance", menu=enhancemenu)

        trmenu = Menu(self.menu, tearoff=0)
        trmenu.add_command(label="Sample 1", command=self.tr1)
        trmenu.add_command(label="Sample 2", command=self.tr2)
        trmenu.add_command(label="Sample 3",command=self.tr3)
        trmenu.add_command(label="Sample 4", command=self.tr4)
        trmenu.add_command(label="Sample 5", command=self.tr5)
        trmenu.add_command(label="Sample 6", command=self.tr6)
        self.menu.add_cascade(label="Matrix Operations", menu=trmenu)
        
        mergemenu = Menu(self.menu, tearoff=0)
        mergemenu.add_command(label="Lightning", command=self.r1)
        mergemenu.add_command(label="Darkening", command=self.r2)
        mergemenu.add_command(label="Subtraction",command=self.r3)
        mergemenu.add_command(label="Multiply", command=self.r4)
        mergemenu.add_command(label="Superposition", command=self.r5)
        mergemenu.add_command(label="Adding", command=self.r6)
        mergemenu.add_command(label="Blending", command=self.r7)
        self.menu.add_cascade(label="Merging Images", menu=mergemenu)

        
        mergemenu = Menu(self.menu, tearoff=0)
        

        self.menu.add_cascade(label="Apply", command=self.tran)
        self.menu.add_cascade(label="Remove", command=self.rem)
                               
        # the button frame
        fr = Frame(master)
        fr.pack(side='top', expand=1, fill='x')

        photo1 = PhotoImage(file="b1.gif")
        self.b1= Button(fr, compound=TOP, width=25, height=25, image=photo1,command=lambda: self.fn(1),cursor="tcross")
        self.b1.grid(row=0, column=4, sticky="w", padx=2, pady=2)
        self.b1.image = photo1
        
        photo2 = PhotoImage(file="b2.gif")
        self.b2= Button(fr, compound=TOP, width=25, height=25, image=photo2,command=lambda: self.fn(2))
        self.b2.grid(row=0, column=5, sticky="w", padx=2, pady=2)
        self.b2.image = photo2

        photo3 = PhotoImage(file="b3.gif")
        self.b3= Button(fr, compound=TOP, width=25, height=25, image=photo3,command=lambda: self.fn(3))
        self.b3.grid(row=0, column=6, sticky="w", padx=2, pady=2)
        self.b3.image = photo3

        photo4 = PhotoImage(file="b14.gif")
        self.b4= Button(fr,text='Fill[]', compound=TOP, width=25, height=25, image=photo4,command=lambda: self.fn(4))
        self.b4.grid(row=0, column=7, sticky="w", padx=2, pady=2)
        self.b4.image = photo4

        photo5 = PhotoImage(file="b5.gif")
        self.b5= Button(fr, compound=TOP, width=25, height=25, image=photo5,command=lambda: self.fn(5))
        self.b5.grid(row=0, column=8, sticky="w", padx=2, pady=2)
        self.b5.image = photo5

        photo6 = PhotoImage(file="b6.gif")
        self.b6= Button(fr, compound=TOP, width=25, height=25, image=photo6,command=lambda: self.fn(6))
        self.b6.grid(row=0, column=9, sticky="w", padx=2, pady=2)
        self.b6.image = photo6

        photo7 = PhotoImage(file="b7.gif")
        self.b7= Button(fr, compound=TOP, width=25, height=25, image=photo7,command=lambda: self.fn(7))
        self.b7.grid(row=0, column=10, sticky="w", padx=2, pady=2)
        self.b7.image = photo7

        photo8 = PhotoImage(file="b8.gif")
        self.b8= Button(fr, compound=TOP, width=25, height=25, image=photo8,command=lambda: self.fn(8))
        self.b8.grid(row=0, column=11, sticky="w", padx=2, pady=2)
        self.b8.image = photo8

        photo9 = PhotoImage(file="b15.gif")
        self.b9= Button(fr,text='Pencil', compound=TOP, width=25, height=25, image=photo9,command=lambda: self.fn(9))
        self.b9.grid(row=0, column=12, sticky="w", padx=2, pady=2)
        self.b9.image = photo9

        photo10 = PhotoImage(file="b10.gif")
        self.b10= Button(fr, compound=TOP, width=25, height=25, image=photo10,command=lambda: self.fn(10))
        self.b10.grid(row=0, column=13, sticky="w", padx=2, pady=2)
        self.b10.image = photo10

        photo11 = PhotoImage(file="b11.gif")
        self.b11= Button(fr, compound=TOP, width=25, height=25, image=photo11,command=lambda: self.fn(11))
        self.b11.grid(row=0, column=14, sticky="w", padx=2, pady=2)
        self.b11.image = photo11

        photo12 = PhotoImage(file="b16.gif")
        self.b12= Button(fr,text='Rub', compound=TOP, width=25, height=25, image=photo12,command=lambda: self.fn(12))
        self.b12.grid(row=0, column=15, sticky="w", padx=2, pady=2)
        self.b12.image = photo12

        photo13 = PhotoImage(file="b17.gif")
        self.b13= Button(fr,text='Brush', compound=TOP, width=25, height=25, image=photo13,command=lambda: self.fn(13))
        self.b13.grid(row=0, column=16, sticky="w", padx=2, pady=2)
        self.b13.image = photo13

        photo14 = PhotoImage(file="b18.gif")
        self.push1=Button(fr,text='Boundary' ,compound=TOP,width=50, height=25,image=photo14, command=self.setBgColor1,borderwidth=4,highlightbackground='black',highlightcolor='red')
        self.push1.grid(row=1, column=4, sticky="w", padx=2, pady=2,columnspan=2)
        self.push1.image = photo14

        photo15 = PhotoImage(file="b19.gif")
        self.push2=Button(fr,text='Fill color', compound=TOP, width=50, height=25,image=photo15,command=self.setBgColor2,borderwidth=4,highlightbackground='black',highlightcolor='red')
        self.push2.grid(row=1, column=6, sticky="w", padx=2, pady=2,columnspan=2)
        self.push2.image = photo15

        self.var=IntVar()
        self.var2=IntVar()
        self.var3=IntVar()
        self.w = Scale(fr, from_=0, to=255,orient=HORIZONTAL,variable=self.var,label="Red",length=180)
        self.w.grid(row=0, column=0, sticky="e", padx=2, pady=2)

        self.w2 = Scale(fr, from_=0, to=255, orient=HORIZONTAL,variable=self.var2,label="blue",length=180)
        self.w2.grid(row=0, column=1, sticky="e", padx=2, pady=2)

        self.w3 = Scale(fr, from_=0, to=255, orient=HORIZONTAL,variable=self.var3,label="green",length=180)
        self.w3.grid(row=0, column=2, sticky="e", padx=2, pady=2)

        self.lbl.bind("<Motion>",self.sha)
        self.lbl.bind("<ButtonPress-1>",self.sha2)
        self.lbl.bind("<ButtonRelease-1>",self.sha3)
        

        
    def rectangle(self,event):
      if (self.btn=='down'):
        im2=self.im.copy()
        draw = ImageDraw.Draw(im2)
        a0=self.pt0[0]
        b0=event.x
        a1=self.pt0[1]
        b1=event.y
        if (event.x<self.pt0[0]):
            a0=event.x
            b0=self.pt0[0]
        if (event.y<self.pt0[1]):
            a1=event.y
            b1=self.pt0[1]
        draw.rectangle((a0,a1,b0,b1),outline=self.str1)
        self.tkimage.paste(im2)
    def rectangle2(self,event):
        self.btn='down'
        self.pt0=(event.x,event.y)
    def rectangle3(self,event):
      if(self.btn=='down'):
        im2=self.im
        draw = ImageDraw.Draw(im2)
        a0=self.pt0[0]
        b0=event.x
        a1=self.pt0[1]
        b1=event.y
        if (event.x<self.pt0[0]):
            a0=event.x
            b0=self.pt0[0]
        if (event.y<self.pt0[1]):
            a1=event.y
            b1=self.pt0[1]
        draw.rectangle((a0,a1,b0,b1),outline=self.str1)
        self.tkimage.paste(im2)
      self.btn='up'

    def rectanglef(self,event):
      if (self.btn=='down'):
        im2=self.im.copy()
        draw = ImageDraw.Draw(im2)
        a0=self.pt0[0]
        b0=event.x
        a1=self.pt0[1]
        b1=event.y
        if (event.x<self.pt0[0]):
            a0=event.x
            b0=self.pt0[0]
        if (event.y<self.pt0[1]):
            a1=event.y
            b1=self.pt0[1]
        draw.rectangle((a0,a1,b0,b1),outline=self.str1,fill=self.str2)
        self.tkimage.paste(im2)
    def rectanglef2(self,event):
        self.btn='down'
        self.pt0=(event.x,event.y)
    def rectanglef3(self,event):
      if(self.btn=='down'):
        im2=self.im
        draw = ImageDraw.Draw(im2)
        a0=self.pt0[0]
        b0=event.x
        a1=self.pt0[1]
        b1=event.y
        if (event.x<self.pt0[0]):
            a0=event.x
            b0=self.pt0[0]
        if (event.y<self.pt0[1]):
            a1=event.y
            b1=self.pt0[1]
        draw.rectangle((a0,a1,b0,b1),outline=self.str1,fill=self.str2)
        self.tkimage.paste(im2)
      self.btn='up'
      
    def ellipse(self,event):
      if (self.btn=='down'):
        im2=self.im.copy()
        draw = ImageDraw.Draw(im2)
        a0=self.pt0[0]
        b0=event.x
        a1=self.pt0[1]
        b1=event.y
        if (event.x<self.pt0[0]):
            a0=event.x
            b0=self.pt0[0]
        if (event.y<self.pt0[1]):
            a1=event.y
            b1=self.pt0[1]
        draw.ellipse((a0,a1,b0,b1),outline=self.str1)
        self.tkimage.paste(im2)
    def ellipse2(self,event):
        self.btn='down'
        self.pt0=(event.x,event.y)
    def ellipse3(self,event):
      if(self.btn=='down'):
        im2=self.im
        draw = ImageDraw.Draw(im2)
        a0=self.pt0[0]
        b0=event.x
        a1=self.pt0[1]
        b1=event.y
        if (event.x<self.pt0[0]):
            a0=event.x
            b0=self.pt0[0]
        if (event.y<self.pt0[1]):
            a1=event.y
            b1=self.pt0[1]
        draw.ellipse((a0,a1,b0,b1),outline=self.str1)
        self.tkimage.paste(im2)
      self.btn='up'

    def ellipsef(self,event):
      if (self.btn=='down'):
        im2=self.im.copy()
        draw = ImageDraw.Draw(im2)
        a0=self.pt0[0]
        b0=event.x
        a1=self.pt0[1]
        b1=event.y
        if (event.x<self.pt0[0]):
            a0=event.x
            b0=self.pt0[0]
        if (event.y<self.pt0[1]):
            a1=event.y
            b1=self.pt0[1]
        draw.ellipse((a0,a1,b0,b1),outline=self.str1)
        self.tkimage.paste(im2)
    def ellipsef2(self,event):
        self.btn='down'
        self.pt0=(event.x,event.y)
    def ellipsef3(self,event):
      if(self.btn=='down'):
        im2=self.im
        draw = ImageDraw.Draw(im2)
        a0=self.pt0[0]
        b0=event.x
        a1=self.pt0[1]
        b1=event.y
        if (event.x<self.pt0[0]):
            a0=event.x
            b0=self.pt0[0]
        if (event.y<self.pt0[1]):
            a1=event.y
            b1=self.pt0[1]
        draw.ellipse((a0,a1,b0,b1),outline=self.str1,fill=self.str2)
        self.tkimage.paste(im2)
      self.btn='up'

      
    def square(self,event):
      if (self.btn=='down'):
        im2=self.im.copy()
        draw = ImageDraw.Draw(im2)
        a0=self.pt0[0]
        b0=event.x
        a1=self.pt0[1]
        b1=event.y
        if (event.x<self.pt0[0]):
            a0=event.x
            b0=self.pt0[0]
        if (event.y<self.pt0[1]):
            a1=event.y
            b1=self.pt0[1]
        draw.rectangle((a0,a1,b0,a1+b0-a0),outline=self.str1)
        self.tkimage.paste(im2)
    def square2(self,event):
        self.btn='down'
        self.pt0=(event.x,event.y)
    def square3(self,event):
      if(self.btn=='down'):
        im2=self.im
        draw = ImageDraw.Draw(im2)
        a0=self.pt0[0]
        b0=event.x
        a1=self.pt0[1]
        b1=event.y
        if (event.x<self.pt0[0]):
            a0=event.x
            b0=self.pt0[0]
        if (event.y<self.pt0[1]):
            a1=event.y
            b1=self.pt0[1]
        draw.rectangle((a0,a1,b0,a1+b0-a0),outline=self.str1)
        self.tkimage.paste(im2)
      self.btn='up'

    def squaref(self,event):
      if (self.btn=='down'):
        im2=self.im.copy()
        draw = ImageDraw.Draw(im2)
        a0=self.pt0[0]
        b0=event.x
        a1=self.pt0[1]
        b1=event.y
        if (event.x<self.pt0[0]):
            a0=event.x
            b0=self.pt0[0]
        if (event.y<self.pt0[1]):
            a1=event.y
            b1=self.pt0[1]
        draw.rectangle((a0,a1,b0,a1+b0-a0),outline=self.str1)
        self.tkimage.paste(im2)
    def squaref2(self,event):
        self.btn='down'
        self.pt0=(event.x,event.y)
    def squaref3(self,event):
      if(self.btn=='down'):
        im2=self.im
        draw = ImageDraw.Draw(im2)
        a0=self.pt0[0]
        b0=event.x
        a1=self.pt0[1]
        b1=event.y
        if (event.x<self.pt0[0]):
            a0=event.x
            b0=self.pt0[0]
        if (event.y<self.pt0[1]):
            a1=event.y
            b1=self.pt0[1]
        draw.rectangle((a0,a1,b0,a1+b0-a0),outline=self.str1,fill=self.str2)
        self.tkimage.paste(im2)
      self.btn='up'
      
    def circle(self,event):
      self.index=2
      if (self.btn=='down'):
        im2=self.im.copy()
        draw = ImageDraw.Draw(im2)
        a0=self.pt0[0]
        b0=event.x
        a1=self.pt0[1]
        b1=event.y
        if (event.x<self.pt0[0]):
            a0=event.x
            b0=self.pt0[0]
        if (event.y<self.pt0[1]):
            a1=event.y
            b1=self.pt0[1]
        draw.ellipse((a0,a1,b0,a1+b0-a0),outline=self.str1)
        self.tkimage.paste(im2)
    def circle2(self,event):
        self.btn='down'
        self.pt0=(event.x,event.y)
    def circle3(self,event):
      if(self.btn=='down'):
        im2=self.im
        draw = ImageDraw.Draw(im2)
        a0=self.pt0[0]
        b0=event.x
        a1=self.pt0[1]
        b1=event.y
        if (event.x<self.pt0[0]):
            a0=event.x
            b0=self.pt0[0]
        if (event.y<self.pt0[1]):
            a1=event.y
            b1=self.pt0[1]
        draw.ellipse((a0,a1,b0,a1+b0-a0),outline=self.str1)
        self.tkimage.paste(im2)
      self.btn='up'
    
    def circlef(self,event):
      if (self.btn=='down'):
        im2=self.im.copy()
        draw = ImageDraw.Draw(im2)
        a0=self.pt0[0]
        b0=event.x
        a1=self.pt0[1]
        b1=event.y
        if (event.x<self.pt0[0]):
            a0=event.x
            b0=self.pt0[0]
        if (event.y<self.pt0[1]):
            a1=event.y
            b1=self.pt0[1]
        draw.ellipse((a0,a1,b0,a1+b0-a0),outline=self.str1)
        self.tkimage.paste(im2)
    def circlef2(self,event):
        self.btn='down'
        self.pt0=(event.x,event.y)
    def circlef3(self,event):
      if(self.btn=='down'):
        im2=self.im
        draw = ImageDraw.Draw(im2)
        a0=self.pt0[0]
        b0=event.x
        a1=self.pt0[1]
        b1=event.y
        if (event.x<self.pt0[0]):
            a0=event.x
            b0=self.pt0[0]
        if (event.y<self.pt0[1]):
            a1=event.y
            b1=self.pt0[1]
        draw.ellipse((a0,a1,b0,a1+b0-a0),outline=self.str1,fill=self.str2)
        self.tkimage.paste(im2)
      self.btn='up'
      
    def line(self,event):
      if (self.btn=='down'):
        im2=self.im.copy()
        draw = ImageDraw.Draw(im2)
        a0=self.pt0[0]
        b0=event.x
        a1=self.pt0[1]
        b1=event.y
        draw.line((a0,a1,b0,b1),fill=self.str2,width=4)
        self.tkimage.paste(im2)
    def line2(self,event):
        self.btn='down'
        self.pt0=(event.x,event.y)
    def line3(self,event):
      if(self.btn=='down'):
        im2=self.im
        draw = ImageDraw.Draw(im2)
        a0=self.pt0[0]
        b0=event.x
        a1=self.pt0[1]
        b1=event.y
        draw.line((a0,a1,b0,b1),fill=self.str2,width=4)
        self.tkimage.paste(im2)
      self.btn='up'

    def pencil(self,event):
      if (self.btn=='down'):
        draw = ImageDraw.Draw(self.im)
        a0=self.pt[0]
        b0=event.x
        a1=self.pt[1]
        b1=event.y
        draw.line((a0,a1,b0,b1),fill=self.str2,width=1)
        self.tkimage.paste(self.im)
        self.pt=(event.x,event.y)
    def pencil2(self,event):
        self.btn='down'
        self.pt=(event.x,event.y)
    def pencil3(self,event):
        self.btn='up'

    def rubber(self,event):
      if (self.btn=='down'):
        draw = ImageDraw.Draw(self.im)
        a0=self.pt[0]
        b0=event.x
        a1=self.pt[1]                                                            # specify the width in each 
        b1=event.y
        draw.line((a0,a1,b0,b1),fill=self.str2,width=4)
        self.tkimage.paste(self.im)
        self.pt=(event.x,event.y)
    def rubber2(self,event):
        self.btn='down'
        self.pt=(event.x,event.y)
    def rubber3(self,event):
        self.btn='up'

    def brush(self,event):
     if (self.btn=='down'):
        draw = ImageDraw.Draw(self.im)
        a0=self.pt[0]
        b0=event.x
        a1=self.pt[1]
        b1=event.y
        draw.line((a0,a1,b0,b1),fill=self.str2,width=4)
        self.tkimage.paste(self.im)
        self.pt=(event.x,event.y)
    def brush2(self,event):
        self.btn='down'
        self.pt=(event.x,event.y)
    def brush3(self,event):
        self.btn='up'

    def crop(self,event):
     if (self.btn=='down'):
        im2=self.im.copy()
        draw = ImageDraw.Draw(im2)
        a0=self.pt0[0]
        b0=event.x
        a1=self.pt0[1]
        b1=event.y
        if (event.x<self.pt0[0]):
            a0=event.x
            b0=self.pt0[0]
        if (event.y<self.pt0[1]):
            a1=event.y
            b1=self.pt0[1]
        draw.rectangle((a0,a1,b0,b1),outline=self.str1)
        self.tkimage.paste(im2)
    def crop2(self,event):
        self.btn='down'
        self.pt0=(event.x,event.y)
    def crop3(self,event):
       if(self.btn=='down'):
        a0=self.pt0[0]
        b0=event.x
        a1=self.pt0[1]
        b1=event.y
        if (event.x<self.pt0[0]):
            a0=event.x
            b0=self.pt0[0]
        if (event.y<self.pt0[1]):
            a1=event.y
            b1=self.pt0[1]
        box=(a0,a1,b0,b1)
        im2 = self.im.crop(box)
        im3=Image.open('me.jpg')
        im3=im3.resize((self.size2[0],self.size2[1]),Image.ANTIALIAS)
        im3.paste(im2,(0,0,b0-a0,b1-a1))
        self.tkimage.paste(im3)
        self.im=im3
       self.btn='up'

       
    def openAsDlg(self):
      if tkMessageBox.askokcancel('Quit','Open a new Image!!'): 
       k=self.main()
       if (k!=0):
        im = Image.open(k)
        self.size = im.size
        im=im.resize((self.size2[0],self.size2[1]),Image.ANTIALIAS)
        self.im=im
        self.tkimage.paste(im)

    def newAsDlg(self):
      if tkMessageBox.askokcancel('Quit','Want a New Image'):  
        k='me.jpg'
        im = Image.open(k)
        im=im.resize((self.size2[0],self.size2[1]),Image.ANTIALIAS)
        self.im=im
        self.tkimage.paste(im)

    def SaveAsDlg(self):
        filename = tkFileDialog.asksaveasfilename(filetypes=[("imagefiles","*.jpg")])
        if (filename!=''):
            self.im.save(filename+'.jpg')
            

    def fill1(self):
       if (self.rect[0]==0):
        im1 = self.im.filter(ImageFilter.BLUR)
        self.tkimage.paste(im1)
        self.im3=im1.copy()
        print 'mdkdvds'
       else:
        self.im3=self.im.copy()
        im2 = self.im.crop(self.rect)
        im2 = im2.filter(ImageFilter.BLUR)
        self.im3.paste(im2,self.rect)
        self.tkimage.paste(self.im3)

    def fill2(self):
       if (self.rect[0]==0):
        im1 = self.im.filter(ImageFilter.CONTOUR)
        self.tkimage.paste(im1)
        self.im3=im1.copy()
       else:  
        self.im3=self.im.copy()
        im2 = self.im.crop(self.rect)
        im2 = im2.filter(ImageFilter.BLUR)
        self.im3.paste(im2,self.rect)
        self.tkimage.paste(self.im3)

    def fill3(self):
       if (self.rect[0]==0):
        im1 = self.im.filter( ImageFilter.DETAIL)
        self.tkimage.paste(im1)
        self.im3=im1.copy()
       else:  
        self.im3=self.im.copy()
        im2 = self.im.crop(self.rect)
        im2 = im2.filter(ImageFilter.BLUR)
        self.im3.paste(im2,self.rect)
        self.tkimage.paste(self.im3)

    def fill4(self):
       if (self.rect[0]==0):
        im1 = self.im.filter(ImageFilter.EDGE_ENHANCE)
        self.tkimage.paste(im1)
        self.im3=im1.copy()
       else:  
        self.im3=self.im.copy()
        im2 = self.im.crop(self.rect)
        im2 = im2.filter(ImageFilter.BLUR)
        self.im3.paste(im2,self.rect)
        self.tkimage.paste(self.im3)

    def fill5(self):
       if (self.rect[0]==0):
        im1 = self.im.filter(ImageFilter.EDGE_ENHANCE_MORE)
        self.tkimage.paste(im1)
        self.im3=im1.copy()
       else:  
        self.im3=self.im.copy()
        im2 = self.im.crop(self.rect)
        im2 = im2.filter(ImageFilter.BLUR)
        self.im3.paste(im2,self.rect)
        self.tkimage.paste(self.im3)

    def fill6(self):
       if (self.rect[0]==0):
        im1 = self.im.filter(ImageFilter.EMBOSS)
        self.tkimage.paste(im1)
        self.im3=im1.copy()
       else:  
        self.im3=self.im.copy()
        im2 = self.im.crop(self.rect)
        im2 = im2.filter(ImageFilter.BLUR)
        self.im3.paste(im2,self.rect)
        self.tkimage.paste(self.im3)

    def fill7(self):
       if (self.rect[0]==0):
        im1 = self.im.filter(ImageFilter.FIND_EDGES)
        self.tkimage.paste(im1)
        self.im3=im1.copy()
       else:  
        self.im3=self.im.copy()
        im2 = self.im.crop(self.rect)
        im2 = im2.filter(ImageFilter.FIND_EDGES)
        self.im3.paste(im2,self.rect)
        self.tkimage.paste(self.im3)

    def fill8(self):
       if (self.rect[0]==0):
        im1 = self.im.filter(ImageFilter.SMOOTH)
        self.tkimage.paste(im1)
        self.im3=im1.copy()
       else:  
        self.im3=self.im.copy()
        im2 = self.im.crop(self.rect)
        im2 = im2.filter(ImageFilter.SMOOTH)
        self.im3.paste(im2,self.rect)
        self.tkimage.paste(self.im3)

    def fill9(self):
       if (self.rect[0]==0):
        im1 = self.im.filter(ImageFilter.SMOOTH_MORE)
        self.tkimage.paste(im1)
        self.im3=im1.copy()
       else:  
        self.im3=self.im.copy()
        im2 = self.im.crop(self.rect)
        im2 = im2.filter(ImageFilter.SMOOTH_MORE)
        self.im3.paste(im2,self.rect)
        self.tkimage.paste(self.im3)

    def fill10(self):
       if (self.rect[0]==0):
        im1 = self.im.filter(ImageFilter.SHARPEN)
        self.tkimage.paste(im1)
        self.im3=im1.copy()
       else:  
        self.im3=self.im.copy()
        im2 = self.im.crop(self.rect)
        im2 = im2.filter(ImageFilter.SHARPEN)
        self.im3.paste(im2,self.rect)
        self.tkimage.paste(self.im3)

    def en1(self):
      enhancer = ImageEnhance.Color(self.im)
      factor = float(self.var.get())
      
      if (factor<128):
        self.im3=enhancer.enhance(float(factor/128))
      if (factor>=128):
        self.im3=enhancer.enhance(factor-127)
      self.tkimage.paste(self.im3)

    def en2(self):
      enhancer = ImageEnhance.Brightness(self.im)
      factor = float(self.var.get())
      if (factor<128):
        print float(factor/128)
        self.im3=enhancer.enhance(float(factor/128))
      if (factor>=128):
        self.im3=enhancer.enhance(factor-127)  
      self.tkimage.paste(self.im3)

    def en3(self):
      enhancer = ImageEnhance.Contrast(self.im)
      factor = float(self.var.get())
      if (factor<128):
        print float(factor/128)
        self.im3=enhancer.enhance(float(factor/128))
      if (factor>=128):
        self.im3=enhancer.enhance(factor-127)  
      self.tkimage.paste(self.im3)

    def en4(self):
      enhancer = ImageEnhance.Sharpness(self.im)
      factor = float(self.var.get())
      if (factor<128):
        self.im3=enhancer.enhance(float(factor/128))
      if (factor>=128):
        self.im3=enhancer.enhance(factor-127)  
      self.tkimage.paste(self.im3)

    def en5(self):
        im=self.im.copy()
        source = im.split()
        factor= float(self.var.get())
        factor2= float(self.var2.get())
        factor3= float(self.var3.get())
        R, G, B = 0, 1, 2
        out = source[R].point(lambda i:i+factor)
        source[R].paste(out, None)
        out=source[G].point(lambda i:i+factor2)
        source[G].paste(out, None)
        out=source[B].point(lambda i:i+factor3)
        source[B].paste(out, None)
        self.im3 = Image.merge(im.mode, source)
        self.tkimage.paste(self.im3)
    
    def en6(self):
        factor= float(self.var.get())
        factor2= float(self.var2.get())
        factor3= float(self.var3.get())
        self.xyz7[0]=float(factor/50)
        self.xyz7[4]=float(factor/50)
        self.xyz7[8]=float(factor/50)
        self.xyz7[1]=float(factor2/50)
        self.xyz7[5]=float(factor2/50)
        self.xyz7[9]=float(factor2/50)
        self.xyz7[2]=float(factor3/50)
        self.xyz7[6]=float(factor3/50)
        self.xyz7[10]=float(factor3/50)
        im2=self.im.copy()
        self.im3=im2.convert("RGB",self.xyz7)
        self.tkimage.paste(self.im3)

    def tr1(self):
        factor= float(self.var.get())
        factor2= float(self.var2.get())
        factor3= float(self.var3.get())
        self.xyz1[0]=float(factor/50)
        self.xyz1[5]=float(factor2/50)
        self.xyz1[10]=float(factor3/50)
        im2=self.im.copy()
        self.im3=im2.convert("RGB",self.xyz1)
        self.tkimage.paste(self.im3)

    def tr2(self):
        factor= float(self.var.get())
        factor2= float(self.var2.get())
        factor3= float(self.var3.get())
        self.xyz2[0]=float(factor/50)
        self.xyz2[5]=float(factor2/50)
        self.xyz2[10]=float(factor3/50)
        im2=self.im.copy()
        self.im3=im2.convert("RGB",self.xyz2)
        self.tkimage.paste(self.im3)
        
    def tr3(self):
        factor= float(self.var.get())
        factor2= float(self.var2.get())
        factor3= float(self.var3.get())
        self.xyz3[0]=float(factor/50)
        self.xyz3[5]=float(factor2/50)
        self.xyz3[10]=float(factor3/50)
        im2=self.im.copy()
        self.im3=im2.convert("RGB",self.xyz3)
        self.tkimage.paste(self.im3)

    def tr4(self):
        factor= float(self.var.get())
        factor2= float(self.var2.get())
        factor3= float(self.var3.get())
        self.xyz4[0]=float(factor/50)
        self.xyz4[5]=float(factor2/50)
        self.xyz4[10]=float(factor3/50)
        im2=self.im.copy()
        self.im3=im2.convert("RGB",self.xyz4)
        self.tkimage.paste(self.im3)

    def tr5(self):
        factor= float(self.var.get())
        factor2= float(self.var2.get())
        factor3= float(self.var3.get())
        self.xyz5[0]=float(factor/50)
        self.xyz5[5]=float(factor2/50)
        self.xyz5[10]=float(factor3/50)
        im2=self.im.copy()
        self.im3=im2.convert("RGB",self.xyz5)
        self.tkimage.paste(self.im3)

    def tr6(self):
        factor= float(self.var.get())
        factor2= float(self.var2.get())
        factor3= float(self.var3.get())
        self.xyz6[0]=float(factor/50)
        self.xyz6[5]=float(factor2/50)
        self.xyz6[10]=float(factor3/50)
        im2=self.im.copy()
        self.im3=im2.convert("RGB",self.xyz6)
        self.tkimage.paste(self.im3)

    def r1(self):
        self.im3=ImageChops.lighter(self.im,self.im0)
        self.tkimage.paste(self.im3)

    def r2(self):
        self.im3=ImageChops.darker(self.im,self.im0)
        self.tkimage.paste(self.im3)

    def r3(self):
        self.im3=ImageChops.difference(self.im,self.im0)
        self.tkimage.paste(self.im3)
    
    def r4(self):
        self.im3=ImageChops.multiply(self.im,self.im0)
        self.tkimage.paste(self.im3)

    def r5(self):
        self.im3=ImageChops.screen(self.im,self.im0)
        self.tkimage.paste(self.im3)

    def r6(self):
        self.im3=ImageChops.add(self.im,self.im0,100,1)
        self.tkimage.paste(self.im3)

    def r7(self):
        alpha=float(self.var.get())
        self.im3=ImageChops.blend(self.im,self.im0,float(alpha/255))
        self.tkimage.paste(self.im3)
    def rotate(self):
        print self.size2
        im2=self.im.rotate(90)
        self.im=im2
        print im2.size
        self.tkimage.paste(im2)
            
    def hello(self):
        print 'dnckjndk'

    def openAsDlg2(self):
      if tkMessageBox.askokcancel('Quit','It would override the previous image2'): 
       k=self.main()
       if (k!=0):
        im = Image.open(k)
        self.size = im.size
        im=im.resize((self.size2[0],self.size2[1]),Image.ANTIALIAS)
        self.im0=im

    def fn(self,i):
        self.index=i-1
        self.sha=self.call[self.index]
        self.sha2=self.call2[self.index]
        self.sha3=self.call3[self.index]
        self.lbl.bind("<Motion>",self.sha)
        self.lbl.bind("<ButtonPress-1>",self.sha2)
        self.lbl.bind("<ButtonRelease-1>",self.sha3)
            
    
    def tran(self):
        self.im=self.im3.copy()
        self.tkimage.paste(self.im)

    def setBgColor1(self):
     (triple, hexstr) = askcolor()
     if hexstr:
        print hexstr
        self.str1=hexstr
        self.push1.config(bg=hexstr)

    def setBgColor2(self):
     (triple, hexstr) = askcolor()
     if hexstr:
        print hexstr
        self.str2=hexstr
        self.push2.config(bg=hexstr)

    def wr(self,i):
        self.listbox=i
       
    def c2(self):
        print float(self.var2.get())
        self.colors2[0]=self.var.get()
        self.colors2[1]=self.var2.get()
        self.colors2[2]=self.var3.get()
    
    def rem(self):
        self.tkimage.paste(self.im)
        
    def main(self):
        filename = askopenfilename(filetypes=[("allfiles","*"),("imagefiles","*.jpg")])
        if not os.path.exists(filename):
            filename =int(0)
        return filename

root = Tk()
app = Viewer(root)
root.mainloop()
