from tkinter import *
from tkinter import ttk
from PyPDF2 import PdfFileReader,PdfFileWriter
import sys,time


class pdfmerger:

    def __init__(self):


        self.root=Tk()
        self.root.rowconfigure(0,weight=1)
        self.root.columnconfigure(0,weight=1)
        self.root.geometry('450x250')
        self.root.title('PDF MERGER')
        self.root.resizable(height=FALSE,width=FALSE)



        f=ttk.Frame(self.root,height=500,width=400,relief=RAISED,borderwidth=5)
        f.grid(row=0,column=0,sticky='nsew')


        l=ttk.Label(f,text='PDF MERGER',font=('helvitica',15,'bold'))
        l.grid(row=2,column=2,columnspan=4)

        l1=ttk.Label(f,text='PDF1',font=('helvitica',10,'bold'))
        l1.grid(row=4,column=2,sticky='nsew')

        self.e1=ttk.Entry(f)
        self.e1.grid(row=4,column=4,sticky='nsew')

        b1=ttk.Button(f,text='Browse',command=self.openpdf1)
        b1.grid(row=4,column=6,sticky='nsew')

        l2=ttk.Label(f,text='PDF2',font=('helvitica',10,'bold'))
        l2.grid(row=6,column=2,sticky='nsew')

        self.e2=ttk.Entry(f,width=50)
        self.e2.grid(row=6,column=4,sticky='nsew')

        b2=ttk.Button(f,text='Browse',command=self.openpdf2)
        b2.grid(row=6,column=6,sticky='nsew')

        l3=ttk.Label(f,text='OUTPUT',font=('helvitica',10,'bold'))
        l3.grid(row=8,column=2,sticky='nsew')
        
        self.e3=ttk.Entry(f,width=50)
        self.e3.grid(row=8,column=4,sticky='nsew')

        b3=ttk.Button(f,text='Browse',command=self.saveoutput)
        b3.grid(row=8,column=6,sticky='nsew')


        b4=ttk.Button(f,text='MERGE',command=self.merging,)
        b4.grid(row=10,column=4)


        b5=ttk.Button(f,text="QUIT",command=self.quitapp)
        b5.grid(row=10,column=6)

        self.f1=None
        self.f2=None
        self.f3=None

        self.output=None
        self.pdf1=None
        self.pdf2=None
        

        self.root.mainloop()
        
    def quitapp(self):

        self.root.destroy()
        

    def openpdf1(self):

        self.f1=filedialog.askopenfilename()
        self.e1.delete(0,END)
        self.e1.insert(0,self.f1)
        self.pdf1= PdfFileReader(open(self.f1, "rb"))

    def openpdf2(self):

        self.f2=filedialog.askopenfilename()
        self.e2.delete(0,END)
        self.e2.insert(0,self.f2)
        self.pdf2 = PdfFileReader(open(self.f2, "rb"))

    def saveoutput(self):
        
        self.f3=filedialog.asksaveasfilename(defaultextension='.pdf')
        self.e3.delete(0,END)
        self.e3.insert(0,self.f3)

    def merging(self):

        self.output = PdfFileWriter()
        
        npages1=self.pdf1.numPages
        
        npages2=self.pdf2.numPages
      

        for i in range(npages1):

            self.output.addPage(self.pdf1.getPage(i))

        for i in range(npages2):

            self.output.addPage(self.pdf2.getPage(i))

            
        os = open(self.f3,"wb")
        self.output.write(os)
        time.sleep(2)
        os.close()

        messagebox.showinfo('pdfmerger','completed')

        
           
app=pdfmerger()
