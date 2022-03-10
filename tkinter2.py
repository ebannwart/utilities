from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Bannwart')
root.geometry("500x600")

style = ttk.Style()
style.theme_use('default')
style.configure('Treeview',
                background='#D3D3D3',
                foreground='black',
                rowheight=25,
                fieldbackground='#D3D3D3')
style.map('Treeview',
          background=[('selected','blue')])

my_tree = ttk.Treeview(root)
my_tree['columns'] = ('Name','ID','Favorite')
my_tree.column('#0',width=0,stretch=NO)
my_tree.column('Name',anchor=W,width=140)
my_tree.column('ID',anchor=CENTER,width=100)
my_tree.column('Favorite',anchor=W,width=120)

my_tree.heading('#0',text='',anchor=W)
my_tree.heading('Name',text='Name',anchor=W)
my_tree.heading('ID',text='ID',anchor=CENTER)
my_tree.heading('Favorite',text='Favorite',anchor=W)

data = [
        ['John',0,'Toscana'],
        ['Mary',1,'Marguerita'],
        ['Mcdonald',2,'Caipira'],
        ['Iris',3,'Pepperoni'],
        ['Jess',4,'4Queijos'],
        ['Billy',5,'Toscana']     
        ]

my_tree.tag_configure('oddrow',background='white')
my_tree.tag_configure('evenrow',background='lightblue')



global count
count = 0
for record in data:
    if count %2 == 0:  
        my_tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2]),tags=('evenrow',))
    else:
        my_tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2]),tags=('oddrow',))
    count += 1
    
    
my_tree.pack(pady=20)

add_frame = Frame(root)
add_frame.pack(pady=20)

nl = Label(add_frame,text='Name')
nl.grid(row=0,column=0)

il = Label(add_frame,text='ID')
il.grid(row=0,column=1)

tl = Label(add_frame,text='Topping')
tl.grid(row=0,column=2)


name_box = Entry(add_frame)
name_box.grid(row=1,column=0)

id_box = Entry(add_frame)
id_box.grid(row=1,column=1)

toping_box = Entry(add_frame)
toping_box.grid(row=1,column=2)




def add_record():
    global count    
    if count %2 == 0:  
        my_tree.insert(parent='',index='end',iid=count,text='',values=(name_box.get(),id_box.get(),toping_box.get()),tags=('evenrow',))
    else:
        my_tree.insert(parent='',index='end',iid=count,text='',values=(name_box.get(),id_box.get(),toping_box.get()),tags=('oddrow',))
        
    count += 1
    
    name_box.delete(0,END)
    id_box.delete(0,END)
    toping_box.delete(0,END)
    
    
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)
        
def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)

add_record = Button(root,text='Add record',command=add_record)
add_record.pack(pady=20)

remove_all = Button(root,text='Remove All Recordos',command=remove_all)
remove_all.pack(pady=20)

remove_one = Button(root,text='Remove One Selected',command=remove_one)
remove_one.pack(pady=20)






root.mainloop()












































        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    