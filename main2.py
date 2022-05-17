from tkinter import *
from tkinter.ttk import Frame, Button, Entry, Style
import tkinter as tk
from PIL import Image, ImageTk
import heapq

class Koszyk(Frame):
    def __init__(self):
        super().__init__()
        self.shoppinglist = []
        self.listazakupow = []
        self.kolejnosc = []
        self.adding = True
        self.initUI()

    def initUI(self):
        def press():
            sc.delete("1.0", tk.END)
            sc.insert(tk.END, getList(self))

        def press2():
            sc2.delete("1.0", tk.END)
            sc2.insert(tk.END, getZakupy(self))

        def addpress():
            self.adding=not self.adding
            if self.adding==True:
                ar['text'] = "Click to \r remove"
                press()
            else:
                ar['text']="Click to \r add"
                press()

        def shop(s):
            if(self.adding==True):
                self.shoppinglist.append(s)
            else:
                if s in self.shoppinglist:
                    self.shoppinglist.remove(s)

        def robieliste(s):
            if(self.adding==True):
                self.listazakupow.append(s)
            else:
                if s in self.listazakupow:
                    self.listazakupow.remove(s)

        def zmien():
            self.kolejnosc.clear()
            self.listazakupow.clear()
            self.shoppinglist.clear()
            sc.delete("1.0", tk.END)
            sc2.delete("1.0", tk.END)
            self.sc3.delete("1.0", tk.END)

        def blok():
            trasa["state"]="disabled"

        def odblok():
            trasa["state"]="normal"

        self.master.title("sklyp")

        # Trasa button dla PageRoute master.switch_frame(PageRoute)    .pack()
        trasa = tk.Button(self, text="Wyświetl \r Kolejność \r Zakupów", bg="red", fg="white", font='Arial 19 bold', width=11,
                          height=10, command=lambda: [kolejnosc(self), blok()])
        trasa.grid(row=2, column=6, rowspan=3)

        ar = tk.Button(self, text="Remove \r Item", bg="green", fg="white", font='Arial 19 bold', width=11,
                       height=10, command=lambda: [addpress()])
        ar.grid(row=6, column=6, rowspan=3)

        exit = tk.Button(self, text="Exit", fg="white", bg="blue", font='Arial 19 bold',
                         command=self.master.destroy, width=11, height=10)
        exit.grid(row=6, column=10, rowspan=4)

        zmiana = tk.Button(self, command=lambda: [zmien(), odblok()], text = "Zmień \r Listę \r Zakupów", width=15, height=4, font='Arial 14')
        zmiana.grid(row=5, column=6)

        woda = tk.Button(self, command=lambda: [shop("Woda"), press(), robieliste('1'), press2()])
        image = Image.open('woda.jpg')
        image = image.resize((100, 100))
        myimage = ImageTk.PhotoImage(image)
        woda.config(image=myimage, width=100, height=100, bg="green")
        woda.image = myimage
        woda.grid(row=2, column=1)

        napgaz = tk.Button(self, command=lambda:[shop("Napoje gazowane"),press(), robieliste('2'), press2()])
        myimage = Image.open('napgaz.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        napgaz.config(image=image, width=100, height=100, bg="green")
        napgaz.image = image
        napgaz.grid(row=2, column=2)

        napowo = tk.Button(self, command=lambda: [shop("Napoje owocowe"),press(), robieliste('3'), press2()])
        myimage = Image.open('napowo.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        napowo.config(image=image, width=100, height=100, bg="green")
        napowo.image = image
        napowo.grid(row=2, column=3)

        alko = tk.Button(self, command=lambda:[shop("Alkohole mocne"),press(), robieliste('4'), press2()])
        myimage = Image.open('alko.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        alko.config(image=image, width=100, height=100, bg="green")
        alko.image = image
        alko.grid(row=2, column=4)

        piwa = tk.Button(self, command=lambda: [shop("Piwa"), press(), robieliste('5'), press2()])
        myimage = Image.open('piwa.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        piwa.config(image=image, width=100, height=100, bg="green")
        piwa.image = image
        piwa.grid(row=2, column=5)

        sery = tk.Button(self, command=lambda: [shop("Sery "), press(), robieliste('6'), press2()])
        myimage = Image.open('sery.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        sery.config(image=image, width=100, height=100, bg="green")
        sery.image = image
        sery.grid(row=3, column=1)

        jogurty = tk.Button(self, command=lambda: [shop("Jogurty"), press(), robieliste('7'), press2()])
        myimage = Image.open('jogurty.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        jogurty.config(image=image, width=100, height=100, bg="green")
        jogurty.image = image
        jogurty.grid(row=3, column=2)

        smietany = tk.Button(self, command=lambda: [shop("Śmietany"), press(), robieliste('8'), press2()])
        myimage = Image.open('smietany.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        smietany.config(image=image, width=100, height=100, bg="green")
        smietany.image = image
        smietany.grid(row=3, column=3)

        mleka = tk.Button(self, command=lambda: [shop("Mleka"), press(), robieliste('9'), press2()])
        myimage = Image.open('mleka.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        mleka.config(image=image, width=100, height=100, bg="green")
        mleka.image = image
        mleka.grid(row=3, column=4)

        jajka = tk.Button(self, command=lambda: [shop("Jajka"), press(), robieliste('10'), press2()])
        myimage = Image.open('jajka.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        jajka.config(image=image, width=100, height=100, bg="green")
        jajka.image = image
        jajka.grid(row=3, column=5)

        mieso = tk.Button(self, command=lambda: [shop("Mięso"), press(), robieliste('11'), press2()])
        myimage = Image.open('miesa.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        mieso.config(image=image, width=100, height=100, bg="green")
        mieso.image = image
        mieso.grid(row=4, column=1)

        przyprawy = tk.Button(self, command=lambda: [shop("przyprawy"), press(), robieliste('12'), press2()])
        myimage = Image.open('przyprawy.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        przyprawy.config(image=image, width=100, height=100, bg="green")
        przyprawy.image = image
        przyprawy.grid(row=4, column=2)

        artcuk = tk.Button(self, command=lambda:[shop("Artykuły cukiernicze"),press(), robieliste('13'), press2()])
        myimage = Image.open('artcuk.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        artcuk.config(image=image, width=100, height=100, bg="green")
        artcuk.image = image
        artcuk.grid(row=4, column=3)

        ryze = tk.Button(self, command=lambda:[shop("Ryże"),press(), robieliste('14'), press2()])
        myimage = Image.open('ryze.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        ryze.config(image=image, width=100, height=100, bg="green")
        ryze.image = image
        ryze.grid(row=4, column=4)

        kasze = tk.Button(self, command=lambda: [shop("Kasze"),press(), robieliste('15'), press2()])
        myimage = Image.open('kasze.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        kasze.config(image=image, width=100, height=100, bg="green")
        kasze.image = image
        kasze.grid(row=4, column=5)

        ciastka = tk.Button(self, command=lambda:[shop("Ciastka"),press(), robieliste('16'), press2()])
        myimage = Image.open('ciastka.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        ciastka.config(image=image, width=100, height=100, bg="green")
        ciastka.image = image
        ciastka.grid(row=5, column=1)

        czipery = tk.Button(self, command=lambda: [shop("Chipsy"), press(), robieliste('17'), press2()])
        myimage = Image.open('czipsy.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        czipery.config(image=image, width=100, height=100, bg="green")
        czipery.image = image
        czipery.grid(row=5, column=2)

        makarony = tk.Button(self, command=lambda: [shop("Makarony"), press(), robieliste('18'), press2()])
        myimage = Image.open('makarony.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        makarony.config(image=image, width=100, height=100, bg="green")
        makarony.image = image
        makarony.grid(row=5, column=3)

        konserwy = tk.Button(self, command=lambda: [shop("Konserwy"), press(), robieliste('19'), press2()])
        myimage = Image.open('konserwy.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        konserwy.config(image=image, width=100, height=100, bg="green")
        konserwy.image = image
        konserwy.grid(row=5, column=4)

        platki = tk.Button(self, command=lambda: [shop("Płatki śniadaniowe"), press(), robieliste('20'), press2()])
        myimage = Image.open('platki.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        platki.config(image=image, width=100, height=100, bg="green")
        platki.image = image
        platki.grid(row=5, column=5)

        owoce = tk.Button(self, command=lambda: [shop("Owoce"), press(), robieliste('21'), press2()])
        myimage = Image.open('owoce.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        owoce.config(image=image, width=100, height=100, bg="green")
        owoce.image = image
        owoce.grid(row=6, column=1)

        warzywa = tk.Button(self, command=lambda: [shop("Warzywa"), press(), robieliste('22'), press2()])
        myimage = Image.open('warzywa.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        warzywa.config(image=image, width=100, height=100, bg="green")
        warzywa.image = image
        warzywa.grid(row=6, column=2)

        pieczywo = tk.Button(self, command=lambda: [shop("Pieczywo"), press(), robieliste('23'), press2()])
        myimage = Image.open('pieczywo.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        pieczywo.config(image=image, width=100, height=100, bg="green")
        pieczywo.image = image
        pieczywo.grid(row=6, column=3)

        ubrania = tk.Button(self, command=lambda: [shop("Ubrania"), press(), robieliste('24'), press2()])
        myimage = Image.open('ubrania.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        ubrania.config(image=image, width=100, height=100, bg="green")
        ubrania.image = image
        ubrania.grid(row=6, column=4)

        rtv = tk.Button(self, command=lambda: [shop("RTV"),press(), robieliste('25'), press2()])
        myimage = Image.open('rtv.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        rtv.config(image=image, width=100, height=100, bg="green")
        rtv.image = image
        rtv.grid(row=6, column=5)

        agd = tk.Button(self, command=lambda:[shop("AGD"),press(), robieliste('26'), press2()])
        myimage = Image.open('agd.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        agd.config(image=image, width=100, height=100, bg="green")
        agd.image = image
        agd.grid(row=7, column=1)

        artnapr = tk.Button(self, command=lambda: [shop("Narzędzia"), press(), robieliste('27'), press2()])
        myimage = Image.open('narzedzia.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        artnapr.config(image=image, width=100, height=100, bg="green")
        artnapr.image = image
        artnapr.grid(row=7, column=2)

        artrosl = tk.Button(self, command=lambda: [shop("Art. Do uprawy roślin"), press(), robieliste('28'), press2()])
        myimage = Image.open('artros.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        artrosl.config(image=image, width=100, height=100, bg="green")
        artrosl.image = image
        artrosl.grid(row=7, column=3)

        srczyst = tk.Button(self, command=lambda: [shop("Środki czystości"), press(), robieliste('29'), press2()])
        myimage = Image.open('srczys.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        srczyst.config(image=image, width=100, height=100, bg="green")
        srczyst.image = image
        srczyst.grid(row=7, column=4)

        kosmetyki = tk.Button(self, command=lambda: [shop("Kosmetyki"), press(), robieliste('30'), press2()])
        myimage = Image.open('kosmetyki.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        kosmetyki.config(image=image, width=100, height=100, bg="green")
        kosmetyki.image = image
        kosmetyki.grid(row=7, column=5)

        artszk = tk.Button(self, command=lambda: [shop("Art. Szkolne"), press(), robieliste('31'), press2()])
        myimage = Image.open('artszk.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        artszk.config(image=image, width=100, height=100, bg="green")
        artszk.image = image
        artszk.grid(row=8, column=1)

        zabawki = tk.Button(self, command=lambda: [shop("Zabawki"), press(), robieliste('32'), press2()])
        myimage = Image.open('zabawki.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        zabawki.config(image=image, width=100, height=100, bg="green")
        zabawki.image = image
        zabawki.grid(row=8, column=2)

        artzoo = tk.Button(self, command=lambda: [shop("Art. Zoologiczne"), press(), robieliste('33'), press2()])
        myimage = Image.open('artzoo.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        artzoo.config(image=image, width=100, height=100, bg="green")
        artzoo.image = image
        artzoo.grid(row=8, column=3)

        artkuch = tk.Button(self, command=lambda: [shop("Art. Kuchenne"), press(), robieliste('34'), press2()])
        myimage = Image.open('artkuch.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        artkuch.config(image=image, width=100, height=100, bg="green")
        artkuch.image = image
        artkuch.grid(row=8, column=4)

        promocje = tk.Button(self, command=lambda: [shop("Promocje"), press(), robieliste('35'), press2()])
        myimage = Image.open('promocje.jpg')
        myimage = myimage.resize((100,100))
        image = ImageTk.PhotoImage(myimage)
        promocje.config(image=image, width=100, height=100, bg="green")
        promocje.image = image
        promocje.grid(row=8, column=5)

        sklepp = tk.Button(self, command=lambda: [kolejnosc(self)])
        myimage = Image.open('sklepgraf.jpg')
        myimage = myimage.resize((720,421))
        image = ImageTk.PhotoImage(myimage)
        sklepp.config(image=image, width=720, height=421, bg="green")
        sklepp.image = image
        sklepp.grid(row=2, column=7,columnspan=4, rowspan=4)

        sc = tk.Text(self, height=14, width=18, font='Calibri 14 bold')
        sc.insert(tk.END, getList(self))
        sc.grid(row=6, column=7, rowspan=3)

        sc2 = tk.Text(self, height=14, width=18, font='Calibri 14 bold')
        sc2.insert(tk.END, getZakupy(self))
        sc2.grid(row=6, column=8, rowspan=3)

        self.sc3 = tk.Text(self, height=14, width=18, font='Calibri 14 bold')
        #self.sc3.insert(tk.END, getKolejnosc(self))
        self.sc3.grid(row=6, column=9, rowspan=3)

        self.pack()

graph = {'1':{'2':1,'3':2,'4':8,'5':9,'6':2,'7':3,'8':4,'9':2,'10':3,'11':5,'12':10,'13':11,'14':2,'15':3,'16':12,'17':13,'18':9,'19':8,'20':15,'21':7,'22':8,'23':9,'24':6,'25':18,'26':19,'27':7,'28':6,'29':6,'30':7,'31':7,'32':8,'33':12,'34':8,'35':7},
        '2':{'1':1,'3':2,'4':8,'5':9,'6':3,'7':3,'8':5,'9':3,'10':4,'11':5,'12':11,'13':12,'14':3,'15':4,'16':13,'17':14,'18':12,'19':11,'20':16,'21':6,'22':7,'23':8,'24':7,'25':18,'26':19,'27':7,'28':6,'29':6,'30':7,'31':7,'32':8,'33':12,'34':8,'35':7},
        '3':{'1':1,'2':1,'4':5,'5':6,'6':2,'7':3,'8':4,'9':2,'10':3,'11':4,'12':7,'13':8,'14':2,'15':3,'16':9,'17':10,'18':6,'19':5,'20':11,'21':5,'22':6,'23':7,'24':6,'25':13,'26':14,'27':7,'28':6,'29':6,'30':7,'31':7,'32':8,'33':12,'34':8,'35':7},
        '4':{'2':5,'3':5,'1':5,'5':1,'6':5,'7':7,'8':8,'9':4,'10':4,'11':4,'12':14,'13':14,'14':7,'15':7,'16':13,'17':13,'18':16,'19':17,'20':17,'21':3,'22':2,'23':2,'24':10,'25':18,'26':18,'27':4,'28':6,'29':6,'30':7,'31':9,'32':8,'33':16,'34':9,'35':2},
        '5':{'2':5,'3':5,'1':5,'4':1,'6':5,'7':7,'8':8,'9':4,'10':4,'11':4,'12':14,'13':14,'14':7,'15':7,'16':13,'17':13,'18':16,'19':17,'20':17,'21':3,'22':2,'23':2,'24':10,'25':18,'26':18,'27':4,'28':6,'29':6,'30':7,'31':9,'32':8,'33':16,'34':9,'35':2},
        '6':{'2':1,'3':1,'4':5,'5':6,'1':2,'7':3,'8':4,'9':2,'10':3,'11':4,'12':7,'13':8,'14':2,'15':3,'16':9,'17':10,'18':6,'19':5,'20':11,'21':5,'22':6,'23':7,'24':6,'25':13,'26':14,'27':7,'28':6,'29':6,'30':7,'31':7,'32':8,'33':12,'34':8,'35':7},
        '7':{'2':1,'3':1,'4':5,'5':6,'6':2,'1':3,'8':4,'9':2,'10':3,'11':4,'12':7,'13':8,'14':2,'15':3,'16':9,'17':10,'18':6,'19':5,'20':11,'21':5,'22':6,'23':7,'24':6,'25':13,'26':14,'27':7,'28':6,'29':6,'30':7,'31':7,'32':8,'33':12,'34':8,'35':7},
        '8':{'2':1,'3':1,'4':5,'5':6,'6':2,'7':3,'1':4,'9':2,'10':3,'11':4,'12':7,'13':8,'14':2,'15':3,'16':9,'17':10,'18':6,'19':5,'20':11,'21':5,'22':6,'23':7,'24':6,'25':13,'26':14,'27':7,'28':6,'29':6,'30':7,'31':7,'32':8,'33':12,'34':8,'35':7},
        '9':{'2':1,'3':1,'4':5,'5':6,'6':2,'7':3,'8':4,'1':2,'10':3,'11':4,'12':7,'13':8,'14':2,'15':3,'16':9,'17':10,'18':6,'19':5,'20':11,'21':5,'22':6,'23':7,'24':6,'25':13,'26':14,'27':7,'28':6,'29':6,'30':7,'31':7,'32':8,'33':12,'34':8,'35':7},
        '10':{'2':1,'3':1,'4':5,'5':6,'6':2,'7':3,'8':4,'9':2,'1':3,'11':4,'12':7,'13':8,'14':2,'15':3,'16':9,'17':10,'18':6,'19':5,'20':11,'21':5,'22':6,'23':7,'24':6,'25':13,'26':14,'27':7,'28':6,'29':6,'30':7,'31':7,'32':8,'33':12,'34':8,'35':7},
        '11':{'2':4,'3':4,'4':5,'5':6,'6':2,'7':3,'8':4,'9':3,'10':3,'1':4,'12':7,'13':8,'14':2,'15':3,'16':9,'17':10,'18':6,'19':5,'20':11,'21':5,'22':6,'23':7,'24':6,'25':13,'26':14,'27':7,'28':6,'29':6,'30':7,'31':7,'32':8,'33':12,'34':8,'35':7},
        '12':{'2':7,'3':7,'4':15,'5':16,'6':8,'7':5,'8':4,'9':8,'10':8,'11':10,'1':7,'13':1,'14':6,'15':6,'16':3,'17':4,'18':1,'19':2,'20':5,'21':15,'22':14,'23':16,'24':4,'25':6,'26':6,'27':10,'28':9,'29':9,'30':8,'31':2,'32':4,'33':4,'34':3,'35':11},
        '13':{'2':7,'3':7,'4':15,'5':16,'6':8,'7':5,'8':4,'9':8,'10':8,'11':10,'12':1,'1':7,'14':6,'15':6,'16':3,'17':4,'18':1,'19':2,'20':5,'21':15,'22':14,'23':16,'24':4,'25':6,'26':6,'27':10,'28':9,'29':9,'30':8,'31':2,'32':4,'33':4,'34':3,'35':11},
        '14':{'2':1,'3':1,'4':5,'5':6,'6':2,'7':3,'8':4,'9':2,'10':3,'11':4,'12':7,'13':8,'1':2,'15':3,'16':9,'17':10,'18':6,'19':5,'20':11,'21':5,'22':6,'23':7,'24':6,'25':13,'26':14,'27':7,'28':6,'29':6,'30':7,'31':7,'32':8,'33':12,'34':8,'35':7},
        '15':{'2':1,'3':1,'4':5,'5':6,'6':2,'7':3,'8':4,'9':2,'10':3,'11':4,'12':7,'13':8,'14':2,'1':3,'16':9,'17':10,'18':6,'19':5,'20':11,'21':5,'22':6,'23':7,'24':6,'25':13,'26':14,'27':7,'28':6,'29':6,'30':7,'31':7,'32':8,'33':12,'34':8,'35':7},
        '16':{'2':7,'3':7,'4':15,'5':16,'6':8,'7':5,'8':4,'9':8,'10':8,'11':10,'12':2,'13':1,'14':6,'15':6,'1':9,'17':4,'18':1,'19':2,'20':5,'21':15,'22':14,'23':16,'24':4,'25':6,'26':6,'27':10,'28':9,'29':9,'30':8,'31':2,'32':4,'33':4,'34':3,'35':11},
        '17':{'2':7,'3':7,'4':15,'5':16,'6':8,'7':5,'8':4,'9':8,'10':8,'11':10,'1':7,'13':1,'14':6,'15':6,'16':3,'12':4,'18':1,'19':2,'20':5,'21':15,'22':14,'23':16,'24':4,'25':6,'26':6,'27':10,'28':9,'29':9,'30':8,'31':2,'32':4,'33':4,'34':3,'35':11},
        '18':{'2':7,'3':7,'4':15,'5':16,'6':8,'7':5,'8':4,'9':8,'10':8,'11':10,'1':7,'13':1,'14':6,'15':6,'16':3,'17':4,'12':1,'19':2,'20':5,'21':15,'22':14,'23':16,'24':4,'25':6,'26':6,'27':10,'28':9,'29':9,'30':8,'31':2,'32':4,'33':4,'34':3,'35':11},
        '19':{'2':7,'3':7,'4':15,'5':16,'6':8,'7':5,'8':4,'9':8,'10':8,'11':10,'1':7,'13':1,'14':6,'15':6,'16':3,'17':4,'18':1,'12':2,'20':5,'21':15,'22':14,'23':16,'24':4,'25':6,'26':6,'27':10,'28':9,'29':9,'30':8,'31':2,'32':4,'33':4,'34':3,'35':11},
        '20':{'2':7,'3':7,'4':15,'5':16,'6':8,'7':5,'8':4,'9':8,'10':8,'11':10,'1':7,'13':1,'14':6,'15':6,'16':3,'17':4,'18':1,'19':2,'12':5,'21':15,'22':14,'23':16,'24':4,'25':6,'26':6,'27':10,'28':9,'29':9,'30':8,'31':2,'32':4,'33':4,'34':3,'35':11},
        '21':{'2':4,'3':4,'4':4,'5':5,'6':2,'7':3,'8':4,'9':2,'1':3,'11':4,'12':7,'13':8,'14':2,'15':3,'16':9,'17':10,'18':6,'19':5,'20':11,'10':5,'22':1,'23':1,'24':6,'25':13,'26':14,'27':7,'28':6,'29':6,'30':7,'31':7,'32':8,'33':12,'34':8,'35':7},
        '22':{'2':4,'3':4,'4':3,'5':4,'6':3,'7':5,'8':6,'9':4,'10':3,'11':1,'12':7,'13':8,'14':2,'15':3,'16':9,'17':10,'18':6,'19':5,'20':11,'21':1,'1':6,'23':7,'24':6,'25':13,'26':14,'27':7,'28':6,'29':6,'30':7,'31':7,'32':8,'33':12,'34':8,'35':2},
        '23':{'2':4,'3':4,'4':3,'5':4,'6':3,'7':5,'8':6,'9':4,'10':3,'11':1,'12':7,'13':8,'14':2,'15':3,'16':9,'17':10,'18':6,'19':5,'20':11,'21':1,'1':6,'22':1,'24':6,'25':13,'26':14,'27':7,'28':6,'29':6,'30':7,'31':7,'32':8,'33':12,'34':8,'35':2},
        '24':{'2':4,'3':4,'4':9,'5':10,'6':5,'7':3,'8':2,'9':5,'10':5,'11':7,'12':1,'13':2,'14':3,'15':2,'16':3,'17':4,'18':1,'19':2,'20':4,'21':9,'22':10,'23':11,'1':6,'25':6,'26':6,'27':7,'28':6,'29':6,'30':7,'31':1,'32':8,'33':12,'34':3,'35':8},
        '25':{'2':13,'3':13,'4':15,'5':16,'6':14,'7':12,'8':11,'9':14,'10':14,'11':15,'12':7,'13':8,'14':2,'15':3,'16':9,'17':10,'18':6,'19':5,'20':11,'21':5,'22':6,'23':7,'24':6,'1':13,'26':1,'27':7,'28':6,'29':6,'30':5,'31':7,'32':4,'33':1,'34':2,'35':7},
        '26':{'2':13,'3':13,'4':15,'5':16,'6':14,'7':12,'8':11,'9':14,'10':14,'11':15,'12':7,'13':8,'14':2,'15':3,'16':9,'17':10,'18':6,'19':5,'20':11,'21':5,'22':6,'23':7,'24':6,'1':13,'25':1,'27':7,'28':6,'29':6,'30':5,'31':7,'32':4,'33':1,'34':2,'35':7},
        '27':{'2':4,'3':4,'4':6,'5':7,'6':2,'7':3,'8':4,'9':5,'10':5,'11':6,'12':7,'13':8,'14':2,'1':3,'16':9,'17':10,'18':6,'19':5,'20':11,'21':5,'22':6,'23':7,'24':6,'25':4,'26':4,'32':4,'28':3,'29':3,'30':2,'31':7,'33':3,'15':3,'34':1,'35':7},
        '28':{'2':4,'3':4,'4':6,'5':7,'6':2,'7':3,'8':4,'9':5,'10':5,'11':6,'12':7,'13':8,'14':2,'1':3,'16':9,'17':10,'18':6,'19':5,'20':11,'21':5,'22':6,'23':7,'24':6,'25':4,'26':4,'27':4,'32':3,'29':3,'30':2,'31':7,'33':3,'15':3,'34':1,'35':7},
        '29':{'2':4,'3':4,'4':6,'5':7,'6':2,'7':3,'8':4,'9':5,'10':5,'11':6,'12':7,'13':8,'14':2,'1':3,'16':9,'17':10,'18':6,'19':5,'20':11,'21':5,'22':6,'23':7,'24':6,'25':4,'26':4,'27':4,'28':3,'32':3,'30':2,'31':7,'33':3,'15':3,'34':1,'35':7},
        '30':{'2':4,'3':4,'4':6,'5':7,'6':2,'7':3,'8':4,'9':5,'10':5,'11':6,'12':7,'13':8,'14':2,'1':3,'16':9,'17':10,'18':6,'19':5,'20':11,'21':5,'22':6,'23':7,'24':6,'25':4,'26':4,'27':4,'28':3,'29':3,'32':2,'31':7,'33':3,'15':3,'34':1,'35':7},
        '31':{'2':4,'3':4,'4':9,'5':10,'6':5,'7':3,'8':2,'9':5,'10':5,'11':7,'12':1,'13':2,'14':3,'15':2,'16':3,'17':4,'18':1,'19':2,'20':4,'21':9,'22':10,'23':11,'1':6,'25':6,'26':6,'27':7,'28':6,'29':6,'30':7,'24':1,'32':8,'33':12,'34':3,'35':8},
        '32':{'2':4,'3':4,'4':6,'5':7,'6':2,'7':3,'8':4,'9':5,'10':5,'11':6,'12':7,'13':8,'14':2,'1':3,'16':9,'17':10,'18':6,'19':5,'20':11,'21':5,'22':6,'23':7,'24':6,'25':4,'26':4,'27':4,'28':3,'29':3,'30':2,'31':7,'33':3,'15':3,'34':1,'35':7},
        '33':{'2':13,'3':13,'4':15,'5':16,'6':14,'7':12,'8':11,'9':14,'10':14,'11':15,'12':7,'13':8,'14':2,'15':3,'16':9,'17':10,'18':6,'19':5,'20':11,'21':5,'22':6,'23':7,'24':6,'1':13,'26':1,'27':7,'28':6,'29':6,'30':5,'31':7,'32':4,'25':1,'34':2,'35':7},
        '34':{'2':13,'3':13,'4':15,'5':16,'6':14,'7':12,'8':11,'9':14,'10':14,'11':15,'12':7,'13':8,'14':2,'15':3,'16':9,'17':10,'18':6,'19':5,'20':11,'21':5,'22':6,'23':7,'24':6,'1':13,'26':1,'27':7,'28':6,'29':6,'30':5,'31':7,'32':4,'33':1,'25':2,'35':7},
        '35':{'2':3,'3':3,'4':2,'5':3,'6':3,'7':4,'8':5,'9':2,'1':3,'11':4,'12':7,'13':8,'14':2,'15':3,'16':9,'17':10,'18':6,'19':5,'20':11,'21':5,'22':6,'23':7,'24':6,'25':13,'26':14,'27':7,'28':6,'29':6,'30':7,'31':7,'32':8,'33':12,'34':8,'10':2},
        '0':{'26':1,'2':13,'3':14,'4':19,'5':20,'6':16,'7':15,'8':15,'9':16,'10':15,'11':18,'12':12,'13':10,'14':14,'15':14,'16':7,'17':5,'18':14,'19':16,'20':5,'21':17,'22':16,'23':19,'24':12,'1':14,'25':3,'27':10,'28':8,'29':7,'30':6,'31':9,'32':6,'33':2,'34':4,'35':15},}


def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def kolejnosc(self):

    self.kolejnosc.clear()
    print(self.shoppinglist)
    print(self.listazakupow)
    print(self.kolejnosc)

    temp = calculate_distances(graph,'0')[self.listazakupow[0]]
    tempStart = self.listazakupow[0]
    for x in range(len(self.listazakupow)):
        if calculate_distances(graph,'0')[self.listazakupow[x]] < temp:
            temp = calculate_distances(graph,'0')[self.listazakupow[x]]
            tempStart = self.listazakupow[x]

    self.kolejnosc.append(tempStart)

    dlugosc = len(self.listazakupow)

    self.listazakupow.remove(tempStart)
    temp = self.listazakupow[0]
    for i in range(len(self.listazakupow)):
        if len(self.kolejnosc) == dlugosc:
            break
        x=0
        while x <= len(self.listazakupow):
            if len(self.listazakupow) == 1:
                temp = self.listazakupow[0]
                self.kolejnosc.append(temp)
                self.listazakupow.remove(temp)
                break
            elif calculate_distances(graph, tempStart)[self.listazakupow[x+1]] < calculate_distances(graph, tempStart)[self.listazakupow[x]]:
                temp = self.listazakupow[x+1]
                self.kolejnosc.append(temp)

            else:
                temp = self.listazakupow[x]
                self.kolejnosc.append(temp)

            self.listazakupow.remove(temp)
    print(self.kolejnosc)
    self.sc3.delete("1.0", tk.END)
    self.sc3.insert(tk.END, getKolejnosc(self))


def getKolejnosc(self):
    print(self.kolejnosc)
    items ='Kolejność: \n'
    for item in self.kolejnosc:
        items += item + "\n"
    return items

def getZakupy(self):
    items='Dodane ID: \n'
    for item in self.listazakupow:
        items+= item + "\n"
    return items

def getList(self):
    items='Koszyk: \n'
    for item in self.shoppinglist:
        items+= item + "\n"
    return items

def main():
    root = Tk()
    app = Koszyk()
    root.configure(background="green")
    root.mainloop()

if __name__ == '__main__':
    main()
