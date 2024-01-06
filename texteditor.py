#importing packages
from tkinter import *
from tkinter.ttk import*
from tkinter import font,filedialog,messagebox
import os

#functionality
def toolbarFunc():
    if show_toolbar.get()==False:
        tool_bar.pack_forget()
    if show_toolbar.get()==True:
        textarea.pack_forget()
        tool_bar.pack(fill=X)
        textarea.pack(fill=BOTH,expand=1)
        
def statusbarFunc():
    if show_statusbar.get()==False:
        status_bar.pack_forget()
    else:
        status_bar.pack()
url=''
def new_file():
    global url
    textarea.delete(0.0,END)
    
def open_file():
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd,title='Select File',filetype=(('Text File','txt'),('All Files','*.*')))  
    if url!='':
        print(url)
        data=open(url,'r')
        textarea.insert(0.0,data.read())
    root.title(os.path.basename(url))
    
def save_file():
    if url=='':
        save_url=filedialog.asksaveasfile (mode='w',defaultextension='.txt',filetypes=(('Text File','txt'),('All Files','*.*')))
        content=textarea.get(0.0,END)
        save_url.write(content)
        save_url.close()
    else:
        content=textarea.get(0.0,END)
        file=open(url,'w')
        file.write(content)
def saveas_file():
    save_url=filedialog.asksaveasfile (mode='w',defaultextension='.txt',filetypes=(('Text File','txt'),('All Files','*.*')))
    content=textarea.get(0.0,END)
    save_url.write(content)
    save_url.close()
    if url!='':
        os.remove(url)
def exit():
    if textarea.edit_modified():
        result=messagebox.askyesnocancel('Warning','Do you want to save the file?')
        if result is True:
            if url=='':
                content=textarea.get(0.0,END)
                file=open(url,'w')
                file.write(content)
                root.destroy()
            else:
                content=textarea.get(0.0,'END')
                save_url=filedialog.asksaveasfile (mode='w',defaultextension='.txt',filetypes=(('Text File','txt'),('All Files','*.*')))
                save_url.write(content)
                save_url.close()
                root.destroy
        elif result is False:
            root.destroy()
        else:
            pass
    else:
        root.destroy()               
def statusBarFunction(event):
    if textarea.edit_modified():
        Words=textarea.get(0.0,END).split()
        characters=len(textarea.get(0.0,'end=1c'.replace(' ',' ')))
        status_bar.config(text=f'Characters: {characters} Words: {Words}')
        
    textarea.edit_modified(False)      
fontSize=12
fontStyle='arial'
def font_style(event):
    global fontStyle
    fontStyle=font_family_variable.get()
    textarea.config(font=(fontStyle,fontSize))
    
def font_size(event):
    global fontSize
    fontSize=size_variable.get()
    textarea.config(font=(fontStyle,fontSize))
    
def bold_text():
    text_property=font.Font(font=textarea['font']).actual()
    if text_property['weight']=='normal':
        textarea.config(font=(fontStyle,fontSize,'bold'))
    if text_property['weight']=='bold':
        textarea.config(font=(fontStyle,fontSize,'normal'))
    
def italic_text():
    text_property=font.Font(font=textarea['font']).actual()
    if text_property['slant']=='roman':
        textarea.config(font=(fontStyle,fontSize,'italic'))
    if text_property['slant']=='italic':
        textarea.config(font=(fontStyle,fontSize,'roman'))
        
def underline_text():
    text_property=font.Font(font=textarea['font']).actual()
    if text_property['underline']==0:
        textarea.config(font=(fontStyle,fontSize,'underline'))
    if text_property['underline']==1:
        textarea.config(font=(fontStyle,fontSize,'underline'))
        
def align_right():
    data=textarea.get(0.0,END)
    textarea.tag_config('right',justify=RIGHT)
    textarea.delete(0.0,END)
    textarea.insert(INSERT,data,'right')
    
def align_left():
    data=textarea.get(0.0,END)
    textarea.tag_config('left',justify=LEFT)
    textarea.delete(0.0,END)
    textarea.insert(INSERT,data,'left')
    
def align_center():
    data=textarea.get(0.0,END)
    textarea.tag_config('center',justify=CENTER)
    textarea.delete(0.0,END)
    textarea.insert(INSERT,data,'center')
    
root = Tk()
root.title("Text Editor")
root.geometry('1200x620+10+10')
root.resizable(False,False)
menubar=Menu(root)
root.config(menu=menubar)
#File
filemenu=Menu(menubar,tearoff=False)
menubar.add_cascade(label='File',menu=filemenu)
newImage=PhotoImage(file='new.png')
openImage=PhotoImage(file='open.png')
saveImage=PhotoImage(file='save.png')
saveasImage=PhotoImage(file='save_as.png')
exitImage=PhotoImage(file='exit.png')

filemenu.add_command(label='New',accelerator='Ctrl+N',image=newImage,compound=LEFT,command=new_file)
filemenu.add_command(label='Open',accelerator='Ctrl+O',image=openImage,compoun=LEFT,command=open_file)
filemenu.add_command(label='Save',accelerator='Ctrl+S',image=saveImage,compound=LEFT,command=save_file)
filemenu.add_command(label='Save As',accelerator='Ctrl+Alt+S',image=saveasImage,compoun=LEFT,command=saveas_file)
filemenu.add_separator()
filemenu.add_command(label='Exit',accelerator='Ctrl+Q',image=exitImage,compoun=LEFT,command=exit)
#Edit
cutImage=PhotoImage(file='cut.png')
copyImage=PhotoImage(file='copy.png')
pasteImage=PhotoImage(file='paste.png')
clearImage=PhotoImage(file='clear_all.png')

editmenu=Menu(menubar,tearoff=False)
editmenu.add_command(label='Cut',accelerator='Ctrl+X',image=cutImage,compound=LEFT,command=lambda:textarea.event_generate('<Control x>'))
editmenu.add_command(label='Copy',accelerator='Ctrl+C',image=copyImage,compound=LEFT,command=lambda:textarea.event_generate('<Control c>'))
editmenu.add_command(label='Paste',accelerator='Ctrl+V',image=pasteImage,compound=LEFT,command=lambda:textarea.event_generate('<Control v>'))
editmenu.add_command(label='Clear',accelerator='Ctrl+Alt+V',image=clearImage,compound=LEFT,command=lambda:textarea.delete(0.0,END))          
menubar.add_cascade(label='Edit',menu=editmenu)
#View
show_toolbar=BooleanVar()
show_statusbar=BooleanVar()
statusbarImage=PhotoImage(file='status_bar.png')
toolbarImage=PhotoImage(file='tool_bar.png')
viewmenu=Menu(menubar,tearoff=False)
viewmenu.add_checkbutton(label='Tool Bar',variable=show_toolbar,onvalue=True,offvalue=False,image=toolbarImage,compound=LEFT,command=toolbarFunc)
show_toolbar.set(True)
viewmenu.add_checkbutton(label='Status Bar',variable=show_statusbar,onvalue=True,offvalue=False,image=statusbarImage,compound=LEFT,command=statusbarFunc)
show_statusbar.set(True)
menubar.add_cascade(label='view',menu=viewmenu)

tool_bar=Label(root)
tool_bar.pack(side=TOP,fill=X)
font_families=font.families()
font_family_variable=StringVar()
fontfamily_Combobox=Combobox(tool_bar,width=30,values=font_families,state='readonly',textvariable=font_family_variable)
fontfamily_Combobox.current(font_families.index('Arial'))
fontfamily_Combobox.grid(row=0,column=0,padx=5)
size_variable=IntVar()
font_size_Combobox=Combobox(tool_bar,width=14,textvariable=size_variable,state='readonly',values=tuple(range(8,100)))
font_size_Combobox.current(4)
font_size_Combobox.grid(row=0,column=1,padx=5)

fontfamily_Combobox.bind('<<ComboboxSelected>>',font_style)
font_size_Combobox.bind('<<ComboboxSelected>> ',font_size)
#Bold
boldImage=PhotoImage(file='bold.png')
boldButton=Button(tool_bar,image=boldImage,command=bold_text)
boldButton.grid(row=0,column=2,padx=5)
#Italic
italicImage=PhotoImage(file='italic.png')
italicButton=Button(tool_bar,image=italicImage,command=italic_text)
italicButton.grid(row=0,column=3,padx=5)
#Underline
underlineImage=PhotoImage(file='underline.png')
underlineButton=Button(tool_bar,image=underlineImage,command=underline_text)
underlineButton.grid(row=0,column=4,padx=5)
#Alignments
leftAlignImage=PhotoImage(file='Left.png')
leftAlignButton=Button(tool_bar,image=leftAlignImage,command=align_left)
leftAlignButton.grid(row=0,column=5,padx=5)

rightAlignImage=PhotoImage(file='right.png')
rightAlignButton=Button(tool_bar,image=rightAlignImage,command=align_right)
rightAlignButton.grid(row=0,column=6,padx=5)

centerAlignImage=PhotoImage(file='center.png')
centerAlignButton=Button(tool_bar,image=centerAlignImage,command=align_center)
centerAlignButton.grid(row=0,column=7,padx=5)
#Scrollbar
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(root,yscrollcommand=scrollbar.set,font=('arial',12))
textarea.pack(fill=BOTH,expand=True)
scrollbar.config(command=textarea.yview)

status_bar=Label(root,text='Status Bar')
status_bar.pack(side=BOTTOM)
textarea.bind('<<Modfied>>',statusBarFunction)
root.mainloop()