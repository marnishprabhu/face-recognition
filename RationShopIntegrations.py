
import tkinter as tk
from tkinter import *

from PIL import Image,ImageTk
import os
import json
import matplotlib.pyplot as plt
image_dir ='Images1'

current_name = ""
totalprice = 0
# id = []

ration_ = ''
listItems = []


borr_items = []

directory_ID = ""
# with open('rationID.json', 'r') as file:
#     id = json.load(file)
def get_image(name):
    for root, dirs, files in os.walk('Images1'):

        for dir in dirs:
                a = os.listdir('Images1/' + dir)
                for image in a:
                    if (image.lower().__eq__(name.lower())):

                        b = os.listdir('Images1/' + dir+'/'+image)
                        print(b)
                        for c in  b:
                            print(c)
                            return ('Images1/' + dir + '/' + image + '/' + c)
                            break




        break
# def main(name):
#     current_name = name
#
#     image = get_image(name)
#     # print(image)
#     #
#     # root = Tk()
#     #
#     # root.title('Ration Card Details')
#     # # img = 'C:\\Users\Marnish Prabhu\PycharmProjects\FaceRecogDummy\FullSetupTest\palani.jpg'
#     # image = Image.open(image)
#     # # image = image.resize((100, 100), Image.ANTIALIAS)
#     # im = ImageTk.PhotoImage(image)
#     #
#     # image = Label(root, image=im, height=500, width=500, padx=60)
#     # image.grid(row=1, column=1)
#     #
#     # img = 'C:\FaceRecognition\FaceRecognition\\rationcard\palani.jpg'
#     image = Image.open(image)
#     image = image.resize((200, 200), Image.ANTIALIAS)
#     im = ImageTk.PhotoImage(image)
#
#     image = Label(root, image=im)
#     image.grid(row=8, column=4)
#
#     root.mainloop()
def main(name,json_ration,directory_id,items):
    ration_ = json_ration
    directory_ID = directory_id

    borr_items = items
    # if len (borr_items)>0:
    #     for item in borr_items:


    totalPrice = 0


    current_name = name

    # root = Tk()

    root = Toplevel()
    select_all_var = IntVar()
    rice_var = IntVar()
    wheat_var = IntVar()
    oil_var = IntVar()
    sugar_var = IntVar()
    rr_var = IntVar()
    tp_var = IntVar()
    # totalPrice = StringVar()

    image12 = get_image(name)

    image13 = Image.open(image12)
    image = image13.resize((200, 200), Image.ANTIALIAS)
    im = ImageTk.PhotoImage(image)

    image1 = Label(root, image=im)
    image1.grid(row=8, column=4)
    with open('ration_materials.json', 'r') as file:
        materials = json.load(file)['materilas']


    def borrow(name):
        for item in borr_items:
            if name == item:
                return True
        return False
    def select():
        e = 'normal'
        d = 'disabled'
        _var = select_all_var.get()

        rice = rice_cb.cget("state")
        wheat = wheat_cb.cget("state")
        oil = oil_cb.cget("state")
        sugar = sugar_cb.cget("state")
        rr_c = rr_cb.cget("state")
        thuvaram_paruppu = tp_cb.cget("state")
        if _var == 1:
            if rice == e:
                rice_cb.select()
            if wheat == e:
                wheat_cb.select()
            if oil == e:
                oil_cb.select()
            if sugar == e:
                sugar_cb.select()
            if rr_c == e:
                rr_cb.select()
            if thuvaram_paruppu == e:
                tp_cb.select()


        else:
            wheat_cb.deselect()
            sugar_cb.deselect()
            oil_cb.deselect()
            rice_cb.deselect()
            rr_cb.deselect()
            tp_cb.deselect()

    def saveFile():
        bought = []

        with open('bought.json', 'r') as file:
            bought = json.load(file)

        bought['bought']['names'].append(current_name)

        with open('bought.json', 'w') as file:
            json.dump(bought, file)

    def buy():

        total = 0
        listItems = []

        # a = ["ration id"]
        #
        # a['id'] = "123"


        rv = rice_var.get()
        wv = wheat_var.get()
        ov = oil_var.get()
        sv = sugar_var.get()
        tpv = tp_var.get()

        rrv = rr_var.get()
        if (rv == 1):
            r = int(rp)
            total = total + r
            listItems.append("Rice")

        if (wv == 1):
            if (wp == 'FREE'):
                listItems.append("Wheat")
                pass
            else:

                w = int(wp)
                total = total + w
                listItems.append("Wheat")

        if (ov == 1):
            o = int(op)

            total = total + o
            listItems.append("Oil")


        if (sv == 1):
            s = int(sp)
            total = total + s
            listItems.append("Sugar")

        if rrv == 1:
            if rrp == 'FREE':
                listItems.append("Raw Rice")
                pass
            else:
                wi = int(rrp)

                total = total + wi
                listItems.append("Raw Rice")

        if tpv == 1:
            if tpp == 'FREE':
                listItems.append("Thuvaram Paruppu")
                pass
            else:
                tppr = int(tpp)
                total = total + tppr
                listItems.append("Thuvaram Paruppu")
        # val = ration_["ration id"]
        # print(directory_id)
        # print(len(listItems))
        before_val   = ''
        try:
            before_val = ration_["ration id"][directory_ID]

            for k in  before_val:
                if not listItems.__contains__(k):
                    listItems.append(k)

            ration_["ration id"][directory_ID] = listItems
        except:
            print('in the except block')
            ration_["ration id"][directory_ID] = listItems


        with open('rationID.json', 'w') as file:
             json.dump(ration_,file)

        totalP.config(text=total)
        saveFile()

    root.title('Ration Card Details')

    name_label = Label(root, text='Photo', font=('Verdana', 20))
    name_label.grid(row=7, column=4)

    ration_card_name = Label(root, text='Ration Materials', font=('Verdana', 20))
    ration_card_name.grid(row=0, column=4)

    selectall_cb = Checkbutton(root, variable=select_all_var, text='Select All Available'
                               , font=('Verdana', 20), command=select, pady=50)
    selectall_cb.grid(row=2, column=3)

    state = materials['rice']['available']
    isAlreadyBorrowed = borrow('Rice')
    print(state)

    if state == '1' and not isAlreadyBorrowed:
        rice_cb = Checkbutton(root, text='Rice', font=('Verdana', 20), variable=rice_var)
    else:
        rice_cb = Checkbutton(root, text='Rice', font=('Verdana', 20), state=DISABLED)

    rice_cb.grid(row=2, column=4)

    state = materials['wheat']['available']
    print(state)
    isAlreadyBorrowed = borrow('Wheat')
    if state == '1' and not isAlreadyBorrowed:
        wheat_cb = Checkbutton(root, text='Wheat', font=('Verdana', 20), variable=wheat_var)
    else:
        wheat_cb = Checkbutton(root, text='Wheat', font=('Verdana', 20), state=DISABLED)

    wheat_cb.grid(row=2, column=5)

    state = materials['sugar']['available']
    print(state)
    isAlreadyBorrowed = borrow('Sugar')

    if state == '1' and not isAlreadyBorrowed:
        sugar_cb = Checkbutton(root, text='Sugar', font=('Verdana', 20), variable=sugar_var)
    else:
        sugar_cb = Checkbutton(root, text='Sugar', font=('Verdana', 20), state=DISABLED)

    sugar_cb.grid(row=2, column=6)

    state = materials['oil']['available']
    print(state)
    isAlreadyBorrowed = borrow('Oil')


    if state == '1' and not isAlreadyBorrowed:
        print('aaa')
        oil_cb = Checkbutton(root, text='Oil', font=('Verdana', 20), variable=oil_var)
    else:
        print('bbb')
        oil_cb = Checkbutton(root, text='Oil', font=('Verdana', 20), state=DISABLED)
    oil_cb.grid(row=2, column=7)

    state = materials['raw rice']['available']

    isAlreadyBorrowed = borrow('Raw Rice')


    if state == '1' and not isAlreadyBorrowed:
        rr_cb = Checkbutton(root, text='Raw Rice', font=('Verdana', 20), variable=rr_var)
    else:
        rr_cb = Checkbutton(root, text='Raw Rice', font=('Verdana', 20), state=DISABLED)
    rr_cb.grid(row=2, column=8)

    buy_button = Button(root, text='Buy Materials', command=buy, font=('Verdana', 20)
                        , bg='blue', fg='white')
    buy_button.grid(row=8, column=3)
    state = materials['Thuvaram Paruppu']['available']

    isAlreadyBorrowed = borrow('Thuvaram Paruppu')

    if state == '1' and not isAlreadyBorrowed:
        tp_cb = Checkbutton(root, text='Thuvaram Paruppu', font=('Verdana', 20), variable=tp_var)
    else:
        tp_cb = Checkbutton(root, text='Thuvaram Paruppu', font=('Verdana', 20), state=DISABLED)
    tp_cb.grid(row=2, column=9)
    #### row 3

    # RiceP = StringVar()
    # WheatP = StringVar()
    # OilP = StringVar()
    # SugarP = StringVar()
    # DhalP = StringVar()

    sp = materials['sugar']['price']
    op = materials['oil']['price']
    rp = materials['rice']['price']
    wp = materials['wheat']['price']
    rrp = materials['raw rice']['price']
    tpp = materials['Thuvaram Paruppu']['price']

    riceLa = Label(root, text='Rice', font=('Verdana', 20), pady=15)
    riceLa.grid(row=3, column=2)
    ricePr = Label(root, text=rp, font=('Verdana', 20))
    ricePr.grid(row=3, column=3)

    riceLa = Label(root, text='WheaT', font=('Verdana', 20), pady=15)
    riceLa.grid(row=4, column=2)
    ricePr = Label(root, text=wp, font=('Verdana', 20))
    ricePr.grid(row=4, column=3)

    riceLa = Label(root, text='Oil', font=('Verdana', 20), pady=15)
    riceLa.grid(row=5, column=2)
    ricePr = Label(root, text=op, font=('Verdana', 20))
    ricePr.grid(row=5, column=3)

    riceLa = Label(root, text='Sugar', font=('Verdana', 20), pady=15)
    riceLa.grid(row=6, column=2)
    ricePr = Label(root, text=sp, font=('Verdana', 20))
    ricePr.grid(row=6, column=3)

    riceLa = Label(root, text='Raw Rice', font=('Verdana', 20), pady=15)
    riceLa.grid(row=7, column=2)
    ricePr = Label(root, text=rrp, font=('Verdana', 20))
    ricePr.grid(row=7, column=3)

    riceLa = Label(root, text='Thuvaram Paruppu', font=('Verdana', 20), pady=15)
    riceLa.grid(row=4, column=4)
    ricePr = Label(root, text=tpp, font=('Verdana', 20))
    ricePr.grid(row=4, column=5)

    totalL = Label(root, text='Total', font=('Verdana', 20), pady=15)
    totalL.grid(row=5, column=4)
    totalP = Label(root, text=totalPrice, font=('Verdana', 20))
    totalP.grid(row=5, column=5)

    root.mainloop()



