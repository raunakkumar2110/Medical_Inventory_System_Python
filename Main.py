from tkinter import *;
from tkinter import ttk;
from PIL import Image,ImageTk;
import mysql.connector;
import numpy as np;
import datetime as dt;
import smtplib;
from email.mime.text import MIMEText;
from email.mime.multipart import MIMEMultipart;
from email.mime.base import MIMEBase;
from email import encoders;
import re;
#-----------------------------------------------------------------------------#
def LoginFrame1():
    global uname;
    global passw;
    global main_frame;
    main_frame = Tk();
    main_frame.geometry("700x330");
    main_frame.iconbitmap("ic1.ico");
    main_frame.title("Login Form");
    m = Menu(main_frame);
    m1 = Menu(m,tearoff = 0);
    m.add_cascade(label = "File",menu = m1);
    m1.add_command(label = "Register",command = regtologmenu);
    main_frame.config(menu = m);
    Label(main_frame,text = "Admin Login",justify = "center",font = ("Ink free",35,"bold"),fg = "Red",bg = "Black",width = 300).pack();
    bg = Image.open("l.jpg");
    img = ImageTk.PhotoImage(bg,master = main_frame);
    lbl = Label(main_frame,image = img).pack(pady = 0.5 );
    username_label = Label(main_frame,text = "UserName - ",font = ("helvetica",20,"bold"),bg = "Black",fg = "Blue").place(x = 40,y =90);
    password_label = Label(main_frame,text = "Password - ",font = ("helvetica",20,"bold"),bg = "Black",fg = "Blue").place(x = 40,y =140);
    uname = Entry(main_frame,width = 50,borderwidth = 3,font = ("Times New Roman",12,"bold"));
    uname.place(x = 275,y = 100);
    passw = Entry(main_frame,width = 50,borderwidth = 3,show = "*",font = ("Times New Roman",12,"bold"));
    passw.place(x = 275,y = 150);
    loginButt = Button(main_frame,text = "Login",font = ("Ink Free",15,"bold"),command = CredentialCheck,fg = "Red",bg = "Black",width = 10).place(x = 40,y = 214);
    clearButt = Button(main_frame,text = "Clear",font = ("Ink Free",15,"bold"),command = Clear_F1,fg = "Red",bg = "Black",width = 10).place(x = 188 ,y = 214);
    exitButt =  Button(main_frame, text = "Exit",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",command = main_frame.destroy,width = 10).place(x = 335,y = 214);
    forgotpButt =  Button(main_frame, text = "Forgot Password",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",width = 16,command = forgotpass).place(x = 482,y = 214);
    main_frame.mainloop();


global max_att;
max_att = 3;
global att ;
att = [];
def CredentialCheck():
    
    userna = uname.get();
    pas = passw.get();
    if userna == "" or pas == "":
        messagebox.showinfo("Alert","Please Fill the Username and Password");
    else:
        mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
        mycur=mydb.cursor()
        mycur.execute("CREATE TABLE IF NOT EXISTS credentials_login_registration(First_Name char(30), Last_Name char(30), Email_ID varchar(40), UserName varchar(40),Password varchar(100),Security_Que_Ans date)");
        sql = ("select * from credentials_login_registration where USERNAME =%s and PASSWORD =%s ");
        val = (userna,pas);
        mycur.execute(sql, val);
        result = mycur.fetchall()

        if result:
            messagebox.showinfo("","Welcome To Medical Inventory System 🎉 ");
            main_frame.destroy();
            MDPFrame2();
        else:
            att.append(1);
            if sum(att) >= max_att:
                messagebox.showinfo("","Access Denied!! Destroying Window");
                main_frame.destroy();
            else:
                messagebox.showinfo("","Credential's are Wrong Please Try Again");
                
            
            
def forgotpass():
    try:
        us = simpledialog.askstring(title="Input",prompt="Enter Your userame:");
        dob =  simpledialog.askstring(title="Input",prompt="Who is your special one (S/Q) :");
        mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
        mycur=mydb.cursor();
        mycur.execute("CREATE TABLE IF NOT EXISTS credentials_login_registration(First_Name char(30), Last_Name char(30), Email_ID varchar(40), UserName varchar(40),Password varchar(100),Security_Que_Ans date)");
        sql = ("select * from credentials_login_registration where USERNAME =%s and SECURITY_QUE_ANS =%s ");
        val = (us,dob);
        mycur.execute(sql, val);
        result = mycur.fetchall()
    except mysql.connector.errors.DatabaseError:
        messagebox.showinfo("","Please Enter The date correctly");
    if result:
        mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
        mycur=mydb.cursor();
        mycur.execute("select password from credentials_login_registration where username='" + us + "'");
        result = mycur.fetchone();
        b = list(result);
        c  = b[0];
        messagebox.showinfo("","Your Password is :- "+c);    
    else:
        messagebox.showinfo("","Error Value doesn't Matched : !");
    
    
        
            
         
            
                
            

def Clear_F1():
   uname.delete(0, END);
   passw.delete(0,END);

def RegisterForm():
    global fentry1;
    global lentry2;
    global emailentry3;
    global uentry4;
    global pentry5;
    global cpentry6;
    global forgotentry6;
    global rframe;
    rframe =  Tk();
    rframe.title("Registration Form");
    rframe.geometry("700x660");
    rframe.iconbitmap("ic1.ico");
    Label(rframe,text = "Registration Form",justify = "center",font = ("Ink Free",35,"bold"),fg = "Red",bg = "Black",width = 300).pack();
    bg = Image.open("l.jpg").resize((700,660));
    img = ImageTk.PhotoImage(bg,master  = rframe);
    lbl = Label(rframe,image = img).pack(pady = 0.5 );
    fname = Label(rframe,text = "FirstName",font = ("helvetica",17,"bold"),bg = "Black",fg = "Orange").place(x = 160,y =95);
    lname = Label(rframe,text = "LastName",font = ("helvetica",20,"bold"),bg = "Black",fg = "Orange").place(x = 400,y =90);
    fentry1 =Entry(rframe,width = 20,borderwidth = 3,font = ("Times New Roman",12,"bold"));
    fentry1.place(x = 144,y = 140);
    lentry2 =Entry(rframe,width = 20,borderwidth = 3,font = ("Times New Roman",12,"bold"));
    lentry2.place(x = 387,y = 140);
    Email = Label(rframe,text = "Email ID",font = ("helvetica",17,"bold"),bg = "Black",fg = "Orange").place(x = 160,y =180);
    sq = Label(rframe,text = "Who is Your Special One (S/Q)",font = ("helvetica",16,"bold"),bg = "Black",fg = "Orange").place(x = 160,y =510);
    emailentry3 = Entry(rframe,width = 51,borderwidth = 3,font = ("Times New Roman",12,"bold"));
    emailentry3.place(x = 140,y = 230);
    uname = Label(rframe,text = "Username",font = ("helvetica",17,"bold"),bg = "Black",fg = "Orange").place(x = 160,y =270);
    uentry4 = Entry(rframe,width = 51,borderwidth = 3,font = ("Times New Roman",12,"bold"));
    uentry4.place(x = 140,y = 310);
    p = Label(rframe,text = "Password",font = ("helvetica",17,"bold"),bg = "Black",fg = "Orange").place(x = 160,y =350);
    pentry5 = Entry(rframe,width = 51,borderwidth = 3,show = "*",font = ("Times New Roman",12,"bold"));
    pentry5.place(x = 140,y = 390);
    cp = Label(rframe,text = "Confirm Password",font = ("helvetica",17,"bold"),bg = "Black",fg = "Orange").place(x = 160,y =430);
    cpentry6 = Entry(rframe,width = 51,borderwidth = 3,show = "*",font = ("Times New Roman",12,"bold"));
    cpentry6.place(x = 140,y = 470);
    forgotentry6 = Entry(rframe,width = 51,borderwidth = 3,font = ("Times New Roman",12,"bold"));
    forgotentry6.place(x = 140,y = 550);
    registerButt = Button(rframe,text = "Register",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",width = 10,command = Register).place(x = 60,y = 600);
    clearButt = Button(rframe,text = "Clear",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",width = 10,command = ClearRegForm).place(x = 205 ,y = 600);
    backButt = Button(rframe,text = "Back",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",width = 10,command =  backRegForm).place(x = 350 ,y = 600);
    exitButt =  Button(rframe, text = "Exit",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",command = rframe.destroy,width = 10).place(x = 495,y = 600);
    rframe.mainloop();
    
    
def regtologmenu():
    main_frame.destroy();
    RegisterForm();
    
def  ClearRegForm():
    fentry1.delete(0,END);
    lentry2.delete(0,END);
    emailentry3.delete(0,END);
    uentry4.delete(0,END);
    pentry5.delete(0,END);
    cpentry6.delete(0,END);
    forgotentry6.delete(0,END);
 
def backRegForm():
    rframe.destroy();
    LoginFrame1();
    
  


def Register():
    fn = fentry1.get();
    ln = lentry2.get();
    ei = emailentry3.get();
    un = uentry4.get();
    p = pentry5.get();
    cp = cpentry6.get();
    fp = forgotentry6.get();

    if p != cp:
        messagebox.showinfo("","Password doesn't match");
        
    else:
        mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
        mycur = mydb.cursor();
        mycur.execute("CREATE TABLE IF NOT EXISTS credentials_login_registration(First_Name char(30), Last_Name char(30), Email_ID varchar(40), UserName varchar(40),Password varchar(100),Security_Que_Ans varchar(100))");
        val= [(fn,ln,ei,un,cp,fp)];
        sql="INSERT INTO credentials_login_registration(First_Name,Last_Name,Email_ID,UserName,Password,Security_Que_Ans)VALUES (%s,%s,%s,%s,%s,%s)";
        mycur.executemany(sql,val);
        mydb.commit();
        messagebox.showinfo("","You have been successfully Registered , Thank you ");
        ClearRegForm()
        
#-----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#             
def MDPFrame2():
    global Combo1;
    global Combo2;
    global medid;
    global medname;
    global meddesc;
    global stockavail;
    global exp;
    global price;
    global f2;
    f2 = Tk()
    f2.geometry("800x600");
    f2.iconbitmap("ic1.ico");
    f2.title("Medical Inventory System");
    Label(f2,text = "Medical Inventory System",justify = "center",font = ("Ink Free",35,"bold"),fg = "Red",bg = "Black",width = 300).pack();
    bg = Image.open("img2.jpg").resize((800,600));
    img = ImageTk.PhotoImage(bg,master = f2);
    lbl = Label(f2,image = img).pack();
    m = Menu(f2);
    m1 = Menu(m,tearoff = 0);
    m.add_cascade(label = "File",menu = m1);
    m1.add_command(label = "Inventory",command = inventory);
    m1.add_command(label = "Billing",command = billing);
    m1.add_command(label = "View Registered Members",command = vrm);
    m1.add_command(label = "Exit" ,command = f2.destroy);
    m2 = Menu(m,tearoff = 0);
    m.add_cascade(label = "Help",menu = m2);
    m2.add_command(label = "Feedback" , command = Feedback);
    m2.add_command(label = "About",command = About);
    f2.config(menu = m);
    MedIDLabel1 = Label(f2,text = "MedicineID -",font = ("Times New Roman",20,"bold"),fg = "Green").place(x = 40,y =100);
    MedNameLabel2 = Label(f2,text = "MedicineName -",font = ("Times New Roman",20,"bold"),fg = "Green").place(x = 40,y =150);
    DesLabel3 = Label(f2,text = "Description -",font = ("Times New Roman",20,"bold"),fg = "Green").place(x = 40,y =200);
    StavLabel4 = Label(f2,text = "StockAvalablity -",font = ("Times New Roman",20,"bold"),fg = "Green").place(x = 40,y =250);
    LocLabel5 = Label(f2,text = "Location -",font = ("Times New Roman",20,"bold"),fg = "Green").place(x = 40,y =300);
    PrioLabel6 = Label(f2,text = "Priority -",font = ("Times New Roman",20,"bold"),fg = "Green").place(x = 40,y =350);
    ExpLabel5 = Label(f2,text = "Expiry -",font = ("Times New Roman",20,"bold"),fg = "Green").place(x = 40,y =400);
    medid = Entry(f2,width = 50,borderwidth = 3,font = ("Times New Roman",12,"bold"), highlightthickness=2);
    medid.place(x = 275,y = 110);
    medname = Entry(f2,width = 50,borderwidth = 3,font = ("Times New Roman",12,"bold"));
    medname.place(x = 275,y = 160);
    meddesc = Entry(f2,width = 50,borderwidth = 3,font = ("Times New Roman",12,"bold"));
    meddesc.place(x = 275,y = 210);
    stockavail = Entry(f2,width = 50,borderwidth = 3,font = ("Times New Roman",12,"bold"));
    stockavail.place(x = 275,y = 260);
    optlist1 = ["Room No - 1","Room No - 2","Room No - 3"];
    Combo1 = ttk.Combobox(f2,values = optlist1,width = 48,font = ("Times New Roman",12,"bold"));
    Combo1.set("Select Location - ");
    Combo1.place(x = 275,y = 310);
    optlist2 = ["High","Medium","Low"]
    Combo2 = ttk.Combobox(f2,values = optlist2,width = 48,font = ("Times New Roman",12,"bold"));
    Combo2.set("Select Priority -");
    Combo2.place(x = 275,y = 360)
    exp = Entry(f2,width = 50,borderwidth = 3,font = ("Times New Roman",12,"bold"));
    exp.insert(0,"YYYY-MM-DD");
    #exp.config();
    exp.place(x = 275,y = 410);
    priceLabel5 = Label(f2,text = "Price -",font = ("Times New Roman",20,"bold"),fg = "Green").place(x = 40,y =450);
    price = Entry(f2,width = 50,borderwidth = 3,font = ("Times New Roman",12,"bold"));
    price.place(x = 275,y = 460);
    addtoinvent = Button(f2,text = "Add To Inventory",font = ("Ink Free",15,"bold"),command = add_to_invent,fg = "Red",bg = "Black",width = 20).place(x = 20,y = 510);
    clearbtn = Button(f2,text = "Clear",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",width = 10,command = clear_F2).place(x = 280,y = 510);
    Exitbtn = Button(f2,text = "Exit",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",width = 10,command = f2.destroy).place(x = 420,y = 510);
    logoutbtn = Button(f2,text = "Log Out",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",width = 15,command = logout).place(x = 560,y = 510);
    f2.mainloop();     

def logout():
    f2.destroy();
    LoginFrame1();




def vrm():
    
    user = simpledialog.askstring(title="Input",prompt="Enter Your userame:");
    password = simpledialog.askstring(title="Input",prompt="Enter Your Password:",show = "*");
    f2.destroy();
    if user != "admin" and password != "admin":  
        messagebox.showinfo("","Incorrect Username or Password");
        
    else:
        f8 = Tk();
        f8.title("Registered Member's");
        f8.iconbitmap("ic1.ico");
        f8.geometry("890x400");
        Label(f8,text = "Registered Member's",justify = "center",font = ("Ink Free",35,"bold"),fg = "Red",bg = "Black",width = 300).pack();
        mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
        mycur = mydb.cursor();
        mycur.execute("SELECT * FROM  credentials_login_registration");
        tree = ttk.Treeview(f8);
        tree["show"] = "headings";
        s = ttk.Style(f8);
        s.configure(".",font = ("Helvetica",9));
        s.configure("Treeview.Heading",foreground = "Red",font = ("Helvetica",9,"bold"));
        tree["columns"] = ("First_Name","Last_Name","Email_ID","UserName","Password","Security_Que_Ans");
        tree.column("First_Name",width = 120,minwidth = 50,anchor = CENTER);
        tree.column("Last_Name",width = 120,minwidth = 50,anchor = CENTER);
        tree.column("Email_ID",width = 170,minwidth = 50,anchor = CENTER);
        tree.column("UserName",width = 150,minwidth = 50,anchor = CENTER);
        tree.column("Password",width = 150,minwidth = 50,anchor = CENTER);
        tree.column("Security_Que_Ans",width = 150,minwidth = 50,anchor = CENTER);
    
        tree.heading("First_Name",text = "First_Name",anchor = CENTER);
        tree.heading("Last_Name",text = "Last_Name",anchor = CENTER);
        tree.heading("Email_ID",text = "Email_ID",anchor = CENTER);
        tree.heading("UserName",text = "UserName",anchor = CENTER);
        tree.heading("Password",text = "Password",anchor = CENTER);
        tree.heading("Security_Que_Ans",text = "Security_Que_Ans",anchor = CENTER);
        i = 0;
        for ro in mycur:
            tree.insert("", i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5]),tags=("even",));
            i = i+1;
        tree.place(x = 10,y =100);
        f8.mainloop();
   
    

def billing():
    f2.destroy();
    global f6,ne1,ne2,ne3,ne4,ne5,ne6,ne7,ne8,ne9,ne10,ne11,format_date;
    f6 = Tk();
    f6.geometry("1200x700");
    Label(f6,text = "Billing",justify = "center",font = ("Ink Free",35,"bold"),fg = "Red",bg = "Black",width = 300).pack();
    f6.title("BMS");
    f6.config(bg= "#fac898");
    m = Menu(f6);
    m1 = Menu(m,tearoff = 0);
    m.add_cascade(label = "File",menu = m1);
    m1.add_command(label = "View Purchase History",command = vph);
    f6.config(menu = m);
    l1 = Label(f6,text = "Name of The Customer",font = ("Helvetica",15),bg = "#fac898",fg = "Black").place(x = 60,y =100);
    ne1 = Entry(f6,width = 27,borderwidth = 2,font = ("Times New Roman",12));
    ne1.place(x = 54,y = 135);
    l2 = Label(f6,text = "Phone",font = ("Helvetica",15),bg = "#fac898",fg = "Black").place(x = 394,y =100);
    ne2 = Entry(f6,width = 27,borderwidth = 2,font = ("Times New Roman",12));
    ne2.place(x = 320,y = 135);
    l3 = Label(f6,text = "Email ID",font = ("Helvetica",15),bg = "#fac898",fg = "Black").place(x = 654,y =100);
    ne3 = Entry(f6,width = 27,borderwidth = 2,font = ("Times New Roman",12));
    ne3.place(x = 590,y = 135); 
    l4 = Label(f6,text = "Age",font = ("Helvetica",15),bg = "#fac898",fg = "Black").place(x = 940,y =100);
    ne4 = Entry(f6,width = 27,borderwidth = 2,font = ("Times New Roman",12));
    ne4.place(x = 850,y = 135);
    vmbtn = Button(f6,text = "View Medicine's Available",font = ("Ink free",15,"bold"),fg = "red",bg = "black",width = 25,borderwidth=1,command = vma).place(x = 120,y = 210);
    l5 = Label(f6,text = "Medicine Name",font = ("Helvetica",15),bg = "#fac898",fg = "Black").place(x = 634,y =200);
    ne5 = Entry(f6,width = 27,borderwidth = 2,font = ("Times New Roman",12));
    ne5.place(x = 600,y = 240);
    l6 = Label(f6,text = "Quantity",font = ("Helvetica",15),bg = "#fac898",fg = "Black").place(x = 667,y =300);
    ne6 = Entry(f6,width = 27,borderwidth = 2,font = ("Times New Roman",12));
    ne6.place(x = 600,y = 340);
    l7 = Label(f6,text = "Purchase Date",font = ("Helvetica",15),bg = "#fac898",fg = "Black").place(x = 635,y =400);
    ne7 = Entry(f6,width = 27,borderwidth = 2,font = ("Times New Roman",12));
    date=dt.datetime.now();
    format_date=f"{date:%a, %d %b %Y}";
    ne7.insert(0,format_date);
    ne7.place(x = 600,y = 440);
    ne7.config(state = DISABLED);
    l8 = Label(f6,text = "Total Amount (Rs.)",font = ("Helvetica",15),bg = "#fac898",fg = "Black").place(x = 65,y =550);
    ne8 = Entry(f6,width = 27,borderwidth = 2,font = ("Times New Roman",12));
  
    ne8.place(x = 40,y = 590);
    l8 = Label(f6,text = "GST Applicable (%)",font = ("Helvetica",15),bg = "#fac898",fg = "Black").place(x = 372,y =550);
    ne9 = Entry(f6,width = 27,borderwidth = 2,font = ("Times New Roman",12,"bold"));
    ne9.insert(0,"18");
    ne9.config(state = DISABLED);
    ne9.place(x = 350,y = 590);
    l10 = Label(f6,text = "Discount (%)",font = ("Helvetica",15),bg = "#fac898",fg = "Black").place(x = 713,y =550);
    ne10 = Entry(f6,width = 27,borderwidth = 2,font = ("Times New Roman",12));
    ne10.insert(0,"10");
    ne10.place(x = 660,y = 590);
    l11 = Label(f6,text = "Net Amount (Rs.)",font = ("Helvetica",15),bg = "#fac898",fg = "Black").place(x = 980,y =550);
    ne11 = Entry(f6,width = 27,borderwidth = 2,font = ("Times New Roman",12));
    ne11.place(x = 950,y = 590);
    addbtn =  Button(f6, text = "Add",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",width = 20,command = addbill).place(x = 900,y = 240);
    calbtn =  Button(f6, text = "Calculate",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",width = 20,command = valemail).place(x = 900,y = 300);
    clrbtn =  Button(f6, text = "Clear",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",width = 20,command = clrbill).place(x = 900,y = 360);
    extbtn =  Button(f6, text = "Exit",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",width = 20,command = f6.destroy).place(x = 900,y = 420);
     
    f6.mainloop();



def vph():
    global sentry,tree,f7;
    f7 = Tk();
    f7.title("Purchase History");
    f7.geometry("1200x700");
    f7.config(bg= "#fac898");
    Label(f7,text = "Purchase History",justify = "center",font = ("Ink Free",35,"bold"),fg = "Red",bg = "Black",width = 300).pack();
    mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
    mycur = mydb.cursor();
    mycur.execute("CREATE TABLE IF NOT EXISTS purchase_record(Name_of_The_Customer varchar(200),Purchase_Date varchar(100),Phone bigint,Email_ID varchar(100),Age int,Quantity int, Total_Amount_Rs float,GST_Applicable float, Discount float,Net_Amount_Rs float)");
    mycur.execute("SELECT Name_of_The_Customer,Purchase_Date,Phone,Email_ID,Age,Total_Amount_Rs,GST_Applicable,Discount,Net_Amount_Rs FROM purchase_record");
    searchlabel = Label(f7,text = "Enter Name to Search",font = ("Helvetica",15,"bold"),bg = "#fac898",fg = "green").place(x = 40,y =100);
    sentry = Entry(f7,width = 27,borderwidth = 2,font = ("Times New Roman",14));
    sentry.place(x = 260,y = 100);
    Button(f7, text = "Search",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",width = 8,command = searchdata).place(x = 550,y = 92);
    Button(f7, text = "Refresh",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",width = 8,command = refresh).place(x = 680,y = 92);
    clrbtn =  Button(f7, text = "Clear",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",width = 8,command = searchclear).place(x = 810,y = 92);
    extbtn =  Button(f7, text = "Exit",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",width = 8,command = f7.destroy).place(x = 940,y = 92);
    backbtn =  Button(f7, text = "Back",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",width = 8,command = backtobilling).place(x = 1070,y = 92);
    tree = ttk.Treeview(f7,selectmode = BROWSE);
    vsb = ttk.Scrollbar(f7, orient="vertical", command=tree.yview)
    vsb.place(x=1145, y=242, height=422)

    tree["show"] = "headings";
    s = ttk.Style(f7);
    s.configure(".",font = ("Helvetica",9),rowheight=40);
    s.configure("Treeview.Heading",foreground = "Red",font = ("Helvetica",9,"bold"));
    tree["columns"] = ("Name_of_The_Customer","Purchase_Date","Phone","Email_ID","Age","Total_Amount_Rs" ,"GST_Applicable","Discount","Net_Amount_Rs");
    tree.column("Name_of_The_Customer",width = 160,minwidth = 50,anchor = CENTER);
    tree.column("Purchase_Date",width = 150,minwidth = 50,anchor = CENTER);
    tree.column("Phone",width = 120,minwidth = 50,anchor = CENTER);
    tree.column("Email_ID",width = 210,minwidth = 50,anchor = CENTER);
    tree.column("Age",width = 60,minwidth = 50,anchor = CENTER);
    tree.column("Total_Amount_Rs",width = 120,minwidth = 50,anchor = CENTER);
    tree.column("GST_Applicable",width = 120,minwidth = 50,anchor = CENTER);
    tree.column("Discount",width = 70,minwidth = 50,anchor = CENTER);
    tree.column("Net_Amount_Rs",width = 140,minwidth = 50,anchor = CENTER);
    
    tree.heading("Name_of_The_Customer",text = "Name_of_The_Customer",anchor = CENTER);
    tree.heading("Purchase_Date",text = "Purchase_Date",anchor = CENTER);
    tree.heading("Phone",text = "Phone",anchor = CENTER);
    tree.heading("Email_ID",text = "Email_ID",anchor = CENTER);
    tree.heading("Age",text = "Age",anchor = CENTER);
    tree.heading("Total_Amount_Rs",text = "Total_Amount_Rs",anchor = CENTER);
    tree.heading("GST_Applicable",text = "GST_Applicable",anchor = CENTER);
    tree.heading("Discount",text = "Discount",anchor = CENTER);
    tree.heading("Net_Amount_Rs",text = "Net_Amount_Rs",anchor = CENTER);
    
    i = 0;
    for ro in mycur:   #For each row in mycur
            tree.insert("", i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8]),tags=("even",));
            i = i+1;
            
   
    tree.place(x = 10,y =240);  
    
    f7.mainloop();
    
def backtobilling():
    f7.destroy();
    billing();
    
def refresh():
    f7.destroy();
    vph();
    
    
def searchclear():
    sentry.delete(0,END);
    
def searchdata():
    se = sentry.get();
    for data in tree.get_children():
        tree.delete(data);
    mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
    mycur = mydb.cursor();
    mycur.execute("SELECT Name_of_The_Customer,Purchase_Date,Phone,Email_ID,Age,Total_Amount_Rs,GST_Applicable,Discount,Net_Amount_Rs FROM purchase_record where Name_of_The_Customer LIKE '"+se+"%'" );
    i = 0;
    for ro in mycur:   #For each row in mycur
            tree.insert("", i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8]),tags=("even",));
            i = i+1;
    if i == 0:
        messagebox.showinfo("","No RECORD Found!!!!");
    else:
        messagebox.showinfo("","Total : "+str(i)+" Records Found");


def vma():
    mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
    mycur = mydb.cursor();
    mycur.execute("CREATE TABLE IF NOT EXISTS mis_store( Medicine_ID varchar(40),Medicine_Name varchar(80), Description varchar(100), Stock_Availability int, Location varchar(30),Priority varchar(30),Expiry_Date date, Price decimal(10,2))");
    mycur.execute("SELECT Medicine_Name,Stock_Availability,Expiry_Date,Price FROM mis_store");
    tree = ttk.Treeview(f6);
    tree["show"] = "headings";
    s = ttk.Style(f6);
    s.configure(".",font = ("Helvetica",9));
    s.configure("Treeview.Heading",foreground = "Red",font = ("Helvetica",9,"bold"));
    tree["columns"] = ("Medicine_Name","Stock_Availability","Expiry_Date","Price");
    
    tree.column("Medicine_Name",width = 120,minwidth = 50,anchor = CENTER);

    tree.column("Stock_Availability",width = 150,minwidth = 50,anchor = CENTER);
   
    tree.column("Expiry_Date",width = 120,minwidth = 50,anchor = CENTER);
    tree.column("Price",width = 120,minwidth = 50,anchor = CENTER);
    
  
    tree.heading("Medicine_Name",text = "Medicine_Name",anchor = CENTER);
    
    tree.heading("Stock_Availability",text = "Stock_Availability",anchor = CENTER);
 
    tree.heading("Expiry_Date",text = "Expiry_Date",anchor = CENTER);
    tree.heading("Price",text = "Price",anchor = CENTER);
    
    i = 0;
    for ro in mycur:   #For each row in mycur
            tree.insert("", i, text="",values=(ro[0],ro[1],ro[2],ro[3]),tags=("odd",));
            i = i+1;
            
   
    tree.place(x = 30,y =280);
    
    
    
def addbill():
    ne11.config(state = NORMAL);
    ne11.delete(0,END);
    ne11.config(state = DISABLED);
    global s,n_e1,n_e2,n_e3,n_e4,n_e5,n_e6,n_e7;
    n_e1 = ne1.get();
    n_e2 = ne2.get();
    n_e3 = ne3.get();
    n_e4 = ne4.get();            
    n_e5 = ne5.get();
    n_e6 = ne6.get();
    if n_e1 == "" or n_e2 == "" or n_e3 == "" or n_e4 == "" or n_e5 == "" or n_e6 == "":
        messagebox.showinfo("","Every Field is Important , Please dont leave Empty");
    elif not n_e2.isdigit():
        messagebox.showinfo("","Please Enter The Phone Number  Correctly : - ");
    elif not n_e4.isdigit():
        messagebox.showinfo("","Please Enter The AGE Correctly : - ");
    elif not n_e6.isdigit():
        messagebox.showinfo("","Please Enter The Quantity  Correctly : - ");

    else:
        mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
        mycursor = mydb.cursor();
        mycursor.execute("select Medicine_Name from mis_store");
        result = mycursor.fetchall();   #fetch in the form of list
        a = np.array(result);           #2d array
        medarray = a.flatten();         #converting it to 1d for checking
        if n_e5 not in medarray:
            messagebox.showinfo("","Medicine Not Found !!");
        else:   
            try:
                mycursor.execute("CREATE TABLE IF NOT EXISTS cust(Medicine_Name VARCHAR(200),Quantity INT,Price FLOAT)");
                mycursor.execute("select Price from mis_store where Medicine_Name ='" + n_e5 + "'");
                result = mycursor.fetchone();
                b = list(result);
                c  = b[0];
                val= [(n_e5,n_e6,c)];
                sql="INSERT INTO cust(Medicine_Name,Quantity,Price)VALUES (%s,%s,%s)";
                mycursor.executemany(sql,val);
                mydb.commit();
                mycursor.execute("SELECT SUM(Quantity * Price)FROM cust");
                s = mycursor.fetchall();
                ne8.config(state = NORMAL);
                ne8.delete(0,END);
                ne8.insert(0,s);
                ne8.config(state = DISABLED);
            except mysql.connector.errors.DatabaseError:
                messagebox.showinfo("","Please Enter the Price Correctly");
                    
        
def valemail():
    nemail = ne3.get();
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$';
    if(re.search(regex,nemail)):
        calculation();
    else:
        messagebox.showinfo("","Email is not valid , pLease Enter a valid Email");
    

def calculation():
    ne8.config(state = NORMAL);
    n_e8 = float(ne8.get());
    n_e10 = float(ne10.get());
    b = (18 * n_e8)/100;
    c = b + n_e8;
    dis = (n_e10 * c)/100;
    netamt = c - dis;
    ne11.config(state = NORMAL);
    ne11.delete(0,END);
    ne11.insert(0,netamt);
    ne11.config(state = DISABLED);
    ne8.config(state = NORMAL);
    ne9.config(state = NORMAL);
    ne11.config(state = NORMAL);
    mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
    mycursor = mydb.cursor()
    n_e9 = float(ne9.get());
    n_e11 = float(ne11.get());
    mycursor.execute("CREATE TABLE IF NOT EXISTS purchase_record(Name_of_The_Customer VARCHAR(200),Purchase_Date varchar(100),Phone BIGINT,Email_ID VARCHAR(100),Age INT,Quantity INT,Total_Amount_Rs FLOAT,GST_Applicable FLOAT,Discount FLOAT,Net_Amount_Rs FLOAT )");
    val= [(n_e1,format_date,n_e2,n_e3,n_e4,n_e6,n_e8,n_e9,n_e10,n_e11)];
    sql="INSERT INTO purchase_record(Name_of_The_Customer,Purchase_Date,Phone,Email_ID,Age ,Quantity,Total_Amount_Rs ,GST_Applicable,Discount,Net_Amount_Rs)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)";
    mycursor.executemany(sql,val);
    mydb.commit();
    billgenerate();
    mycursor.execute("DROP table IF EXISTS cust");
    mydb.commit();
    mydb.close();
    ne8.config(state = DISABLED);
    ne9.config(state = DISABLED);
    ne11.config(state = DISABLED);
    
def billgenerate():
    n_e10 = ne10.get();
    mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
    mycursor = mydb.cursor();
    mycursor.execute("select count(Medicine_Name) from cust");
    result1 = mycursor.fetchone();
    b = list(result1);
    c  = b[0];
    mycursor.execute("select Medicine_Name from cust");
    result2 = mycursor.fetchall();
    a1 = np.array(result2);
    namemed = a1.flatten();
    mycursor.execute("select Quantity from cust");
    result3 = mycursor.fetchall();
    a2 = np.array(result3);
    quan = a2.flatten();
    mycursor.execute("select Price from cust");
    result4 = mycursor.fetchall();
    a3 = np.array(result4);
    pri = a3.flatten();
    myFile = open("bill.txt","w");
    myFile.write("---------------------------------------------------------------------------------------------------------------------\n\n");
    myFile.write("--------------------------------------------------------------------------------------------------------------------\n");
    myFile.write("NAME : "+str(n_e1)+" | PHONE : "+str(n_e2)+" | EMAIL_ID : "+str(n_e3)+" | AGE : "+str(n_e4)+" | DATE : "+str(format_date)+"\n");
    myFile.write("--------------------------------------------------------------------------------------------------------------------\n\n")
    myFile.write("---------------------------------------------------------------------------------------------------------------------\n");
    myFile.write("ITEM\t\t\tQUANTITY\t\tPRICE\n");
    myFile.write("---------------------------------------------------------------------------------------------------------------------\n");
    for i in range(0,c):
        myFile.write(str(namemed[i])+"\t\t\t");
        myFile.write(str(quan[i])+"\t\t\t");
        myFile.write(str(pri[i])+"\n");
    myFile.write("---------------------------------------------------------------------------------------------------------------------\n");
    ne11.config(state = NORMAL);
    ne8.config(state = NORMAL);
    n_e11 = float(ne11.get());
    n_e8 = float(ne8.get());
    myFile.write("GST(%) : 18 DISCOUNT(%) : "+str(n_e10)+" TOTAL : "+str(n_e8)+" NET PAYABLE AMT (Rs.) : "+str(n_e11)+"\n");
    ne11.config(state = DISABLED);
    ne8.config(state = DISABLED);
    myFile.write("---------------------------------------------------------------------------------------------------------------------\n");
    myFile.close();
    emailbill();
    
    
def emailbill():
    passwrd = simpledialog.askstring(title="Input",prompt="Enter Your G-Mail Passsword to Mail Invoice:",show = "*");
    from_user = "raunakkumar2110@gmail.com";
    to_user = ne3.get();
    subject = "Invoice";
    msg = MIMEMultipart();
    msg["From"] = from_user;
    msg["To"] = to_user;
    msg["Subject"] = subject;
    body = "Hi, Find The Below Attachment for INVOICE!!\nThank You , Visit Again ";
    msg.attach(MIMEText(body,"plain"));
    file = "bill.txt";
    attach = open(file,"rb");
    p = MIMEBase("application","octet-stream");
    p.set_payload((attach).read());        #changing into encoded form
    encoders.encode_base64(p);
    p.add_header('content-Disposition',"attachment; filename = "+file);
    msg.attach(p);
    text = msg.as_string();
    server = smtplib.SMTP('smtp.gmail.com',587);             
    server.starttls();
    server.login(from_user,passwrd);
    server.sendmail(from_user,to_user,text);
    c = server.quit();
    if c:
        messagebox.showinfo("","Invoice has been Successfully mailed");
    else:
        messagebox.showinfo("","Srry please check the Email again or other glitches");
    
   
    
def clrbill():
    ne1.delete(0,END);
    ne2.delete(0,END);
    ne3.delete(0,END);
    ne4.delete(0,END);
    ne5.delete(0,END);
    ne6.delete(0,END);
    ne7.delete(0,END);
    ne8.config(state = NORMAL);
    ne8.delete(0,END);
    ne9.delete(0,END);
    ne11.config(state = NORMAL);
    ne11.delete(0,END);
    ne11.config(state = DISABLED);
def add_to_invent():
    c1 = Combo1.get();
    c2 = Combo2.get();
    mi = medid.get();
    mn = medname.get();
    md = meddesc.get();
    sa = stockavail.get();
    p = price.get();
    e = exp.get();
    
    if mi == "" or mn == "" or md == "" or sa == "" or c1 == "Select Location - " or c2 == "Select Priority -" or e == "YYYY-MM-DD" or p == "" :
        messagebox.showinfo("","Every Field is Important Please Enter Accordingly: ");
    elif not sa.isdigit():
        messagebox.showinfo("","Please Enter the Stock Availability in the integer Format");

    else:
        try:
            mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
            mycur = mydb.cursor();
            val= [(mi,mn,md,sa,c1,c2,e,p)];
            sql="INSERT INTO mis_store(Medicine_ID,Medicine_Name,Description,Stock_Availability,Location,Priority,Expiry_Date,Price)VALUES (%s,%s,%s,%s,%s,%s,%s,%s)";
            mycur.executemany(sql,val);
            mydb.commit();
            messagebox.showinfo("","Medicine Details has been succesfully Added to inventory , Thank you ");
            clear_F2()
        except mysql.connector.errors.IntegrityError:
            messagebox.showinfo("","Medicine_ID Already Exists , Please Do Not Enter Duplicate Entry for the Medicine_ID Thank You" );
        except mysql.connector.errors.DataError:
            messagebox.showinfo("","Please Enter the date correctly");
        except mysql.connector.errors.DatabaseError:
            messagebox.showinfo("","Please Enter the Price in  Number Format(1,1.0,22.33)");
def clear_F2():
    medid.delete(0,END);
    medname.delete(0,END);
    meddesc.delete(0,END);
    stockavail.delete(0,END);
    Combo1.set("Select Location - ");
    Combo2.set("Select Priority -");
    exp.delete(0,END);
    exp.insert(0,"YYYY-MM-DD");
    price.delete(0,END);

def About():
    f3 = Tk();
    f3.geometry("350x170");
    f3.title("About");
    f3.iconbitmap("ic1.ico");
    bg = Image.open("black.jpg").resize((350,170));
    img = ImageTk.PhotoImage(bg,master = f3);
    lbl = Label(f3,image = img).place(x = 0,y = 0);
    lb1 = Label(f3,text = "Medical Inventory Sytem 1.0.0",font = ("Arial",12,"bold"),fg = "green",bg = "black").place(x = 10,y  =20);
    lb2 = Label(f3,text = "copyright ©️ 2021 by",font = ("Arial",12,"bold"),fg = "Green",bg = "black").place(x = 10,y  =40);
    lb3 = Label(f3,text = "Raunak Kumar",font = ("Arial",15,"bold"),fg = "green",bg = "black").place(x = 10,y  =60);
    exitButt =  Button(f3, text = "Exit",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",command = f3.destroy,width = 4).place(x = 10,y = 100);
    f3.mainloop();

def Feedback():
    f2.destroy();
    global e1;
    global e2;
    global e3;
    global sc;
    global tb;
    global f4;
    global var;
    f4 = Tk();
    f4.iconbitmap("ic1.ico");
    f4.title("Feedback");
    f4.geometry("800x750");
    Label(f4,text = "Feedback",justify = "center",font = ("Ink Free",35,"bold"),fg = "Red",bg = "Black",width = 300).pack();
    bg = Image.open("black.jpg").resize((800,750));
    img = ImageTk.PhotoImage(bg);
    lbl = Label(f4,image = img).place(x = 0,y = 63.3);
    Label(f4,text = "Name",font = ("Ink free",18,"bold"),bg = "Black",fg = "Green").pack(pady = 1);
    e1 = Entry(f4,width = 50,borderwidth = 0,font = ("Times New Roman",12,"bold"), highlightthickness=2);
    e1.config(highlightbackground = "Green", highlightcolor= "Green");
    e1.pack();
    Label(f4,text = "Email_ID",font = ("Ink free",18,"bold"),bg = "Black",fg = "Green").pack(pady = 10);
    e2 = Entry(f4,width = 50,borderwidth = 0,font = ("Times New Roman",12,"bold"), highlightthickness=2);
    e2.config(highlightbackground = "Green", highlightcolor= "Green");
    e2.pack();
    Label(f4,text = "Phone",font = ("Ink free",18,"bold"),bg = "Black",fg = "Green").pack(pady = 10);
    e3 = Entry(f4,width = 50,borderwidth = 0,font = ("Times New Roman",12,"bold"), highlightthickness=2);
    e3.config(highlightbackground = "Green", highlightcolor= "Green");
    e3.pack();
    Label(f4,text = "Rate",font = ("Ink free",18,"bold"),bg = "Black",fg = "Green").pack(pady = 10);
    i = Label(f4,text = "[1 - Poor, 2 - Fairy Poor, 3 - Good, 4 - Very Good, 5 - Excellent] ",font = ("Times New Roman",10,"bold"),bg = "Black",fg = "Red").pack(pady = 10);
    var=IntVar();
    sc=Scale(f4,variable=var,from_=1, to_=5,orient=HORIZONTAL,length = 150,highlightcolor = "Green");
    sc.config(highlightbackground = "Green");
    sc.pack();
    Label(f4,text = "Desrciption",font = ("Ink free",27,"bold"),bg = "Black",fg = "Green").pack(pady = 10);
    tb = Text(f4,width = 50,height = 8,highlightthickness=2,font = ("Times New Roman",12,"bold"));
    tb.config(highlightbackground = "Green", highlightcolor= "Green");
    tb.insert("1.0","Enter Some Text Here.....");
    tb.pack();
    submit = Button(f4,text = "Submit",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",width = 10,command = feedregister).place(x = 90,y = 680);
    clearButt = Button(f4,text = "Clear",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",width = 10,command = clear_f4).place(x = 250 ,y = 680);
    backButt = Button(f4,text = "Back",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",width = 10,command = backbttn_f4).place(x = 410 ,y = 680);
    exitButt =  Button(f4, text = "Exit",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",command = f4.destroy,width = 10).place(x = 570,y = 680);
    
    f4.mainloop();
  
def feedregister():
    e_1 = e1.get();
    e_2 = e2.get();
    e_3 = e3.get();
    v = var.get();
    t_b = tb.get("1.0","end-1c");
    if e_1 == "" or e_2 == "" or e_3 == "" or t_b == "Enter Some Text Here.....":
        messagebox.showinfo("","Every Field is Important so Fill Accordingly");
    elif not e_1.isalpha():
        messagebox.showinfo("","Please Use Characters only in Name Field");
    else:
        try:
            mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
            mycur = mydb.cursor();
            mycur.execute("CREATE TABLE IF NOT EXISTS feedback(Name char(40), Email_ID varchar(50), Phone bigint,Rate int, Description varchar(1000))");
            val= [(e_1,e_2,e_3,v,t_b)];
            sql="INSERT INTO feedback(Name,Email_ID,phone,Rate,Description)VALUES (%s,%s,%s,%s,%s)";
            mycur.executemany(sql,val);
            mydb.commit();
            messagebox.showinfo("","Thank For Your FeedBack");
            clear_f4();
        except mysql.connector.errors.DatabaseError:
            messagebox.showinfo("","Please Enter the Phone Number correctly without characters");
        

def clear_f4():
    e1.delete(0,END);
    e2.delete(0,END);
    e3.delete(0,END);
    tb.delete("1.0",END);
    tb.insert("1.0","Enter Some Text Here.....");
    var.set(0);
def backbttn_f4():
    f4.destroy();
    MDPFrame2();
def vmi():
    mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
    mycur = mydb.cursor();
    mycur.execute("SELECT * FROM mis_store");
    tree = ttk.Treeview(f5);
    tree["show"] = "headings";
    s = ttk.Style(f5);
    s.configure(".",font = ("Helvetica",9));
    s.configure("Treeview.Heading",foreground = "Red",font = ("Helvetica",9,"bold"));
    tree["columns"] = ("Medicine_ID","Medicine_Name","Description","Stock_Availability","Location","Priority","Expiry_Date","Price");
    tree.column("Medicine_ID",width = 120,minwidth = 50,anchor = CENTER);
    tree.column("Medicine_Name",width = 120,minwidth = 50,anchor = CENTER);
    tree.column("Description",width = 120,minwidth = 50,anchor = CENTER);
    tree.column("Stock_Availability",width = 150,minwidth = 50,anchor = CENTER);
    tree.column("Location",width = 150,minwidth = 50,anchor = CENTER);
    tree.column("Priority",width = 150,minwidth = 50,anchor = CENTER);
    tree.column("Expiry_Date",width = 120,minwidth = 50,anchor = CENTER);
    tree.column("Price",width = 120,minwidth = 50,anchor = CENTER);
    
    tree.heading("Medicine_ID",text = "Medicine_ID",anchor = CENTER);
    tree.heading("Medicine_Name",text = "Medicine_Name",anchor = CENTER);
    tree.heading("Description",text = "Description",anchor = CENTER);
    tree.heading("Stock_Availability",text = "Stock_Availability",anchor = CENTER);
    tree.heading("Location",text = "Location",anchor = CENTER);
    tree.heading("Priority",text = "Priority",anchor = CENTER);
    tree.heading("Expiry_Date",text = "Expiry_Date",anchor = CENTER);
    tree.heading("Price",text = "Price",anchor = CENTER);
    
    i = 0;
    for ro in mycur:   #For each row in mycur
            tree.insert("", i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7]),tags=("even",));
            i = i+1;
            
   
    tree.place(x = 10,y =100);
    
def dmi():
    var = StringVar();
    
    
    mydb1 = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
    mycur1 = mydb1.cursor();
    sql1 = """SELECT count(*) FROM mis_store""";
    mycur1.execute(sql1);
    result = mycur1.fetchone();
    mydb1.close();
    if 0 in result:
        messagebox.showinfo("","Table Is empty ,No records Present");
    else:
        var = simpledialog.askstring(title="Input",prompt="Enter The Medicine_Id to delete the Record:");
        if var == "":
                messagebox.showinfo("","Cant Leave Empty");
                
        else:
            mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
            mycur=mydb.cursor();
            sql = """select Medicine_ID from mis_store""";
            mycur.execute(sql);
            result = mycur.fetchall();
            a = np.array(result);
            medarray = a.flatten();
            if var in medarray:
                mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
                mycur = mydb.cursor();
                sql = "delete from mis_store where Medicine_ID ='%s'" %(var);
                mycur.execute(sql);
                mydb.commit();
                messagebox.showinfo("Information","Record has been DELETED Successfully");
            else:
                messagebox.showinfo("","Medicine_ID Not FOUND");

def umi():
    messagebox.showinfo("","Please write according to the option provided here for Location: - Room No - 1, Room No - 2,Room No - 3");
    messagebox.showinfo("","Please write according to the option provided here for Priority: - High, Medium, Low");
    val1 = simpledialog.askstring(title="Input",prompt="Please Specify the column name:");
    val2 = simpledialog.askstring(title="Input",prompt="Please Specify the new value for the column:");
    val3 = simpledialog.askstring(title="Input",prompt="Please Specify the old value for the column:");
    if val1 == "":
        messagebox.showinfo("","Cant Leave Empty");
    elif val2 == "":
        messagebox.showinfo("","Cant Leave Empty");
    elif val3 == "":
        messagebox.showinfo("","Cant Leave Empty");
    else:
        if val1 == "Medicine_ID":
            mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
            mycur=mydb.cursor();
            sql = "UPDATE mis_store SET Medicine_ID = '%s' where Medicine_ID = '%s'" %(val2,val3);
            mycur.execute(sql);
            mydb.commit();
            if mycur:
                messagebox.showinfo("Information","Information has been UPDATED Successfully");
        elif val1 == "Medicine_Name":
            mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
            mycur=mydb.cursor();
            sql = "UPDATE mis_store SET Medicine_Name = '%s' where Medicine_Name = '%s'" %(val2,val3);
            mycur.execute(sql);
            mydb.commit();
            if mycur:
               messagebox.showinfo("Information","Information has been UPDATED Successfully");
        elif val1 == "Description":
            mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
            mycur=mydb.cursor();
            sql = "UPDATE mis_store SET Description = '%s' where Description = '%s'" %(val2,val3);
            mycur.execute(sql);
            mydb.commit();
            if mycur:
               messagebox.showinfo("Information","Information has been UPDATED Successfully");
        elif val1 == "Stock_Availability":
            mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
            mycur=mydb.cursor();
            sql = "UPDATE mis_store SET Stock_Availability = '%s' where Stock_Availability = '%s'" %(val2,val3);
            mycur.execute(sql);
            mydb.commit();
            if mycur:
               messagebox.showinfo("Information","Information has been UPDATED Successfully");
        elif val1 == "Location":
            
            mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
            mycur=mydb.cursor();
            sql = "UPDATE mis_store SET Location = '%s' where Location = '%s'" %(val2,val3);
            mycur.execute(sql);
            mydb.commit();
            if mycur:
               messagebox.showinfo("Information","Information has been UPDATED Successfully");
        elif val1 == "Priority":
           
            mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
            mycur=mydb.cursor();
            sql = "UPDATE mis_store SET Priority = '%s' where Priority = '%s'" %(val2,val3);
            mycur.execute(sql);
            mydb.commit();
            if mycur:
               messagebox.showinfo("Information","Information has been UPDATED Successfully");
        elif val1 == "Expiry_Date":
            mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
            mycur=mydb.cursor();
            sql = "UPDATE mis_store SET Expiry_Date = '%s' where Expiry_Date = '%s'" %(val2,val3);
            mycur.execute(sql);
            mydb.commit();
            if mycur:
               messagebox.showinfo("Information","Information has been UPDATED Successfully");
        elif val1 == "Price":
            mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
            mycur=mydb.cursor();
            sql = "UPDATE mis_store SET Price = '%s' where Price = '%s'" %(val2,val3);
            mycur.execute(sql);
            mydb.commit();
            if mycur:
               messagebox.showinfo("Information","Information has been UPDATED Successfully");
        else:
            messagebox.showinfo("","Please Enter the Valid data");
        
def viewfb():
    mydb = mysql.connector.connect(host = "localhost",user = "root",password = "admin",database = "medical_inventory_system_python");
    mycur = mydb.cursor();
    mycur.execute("SELECT * FROM feedback");
    tree = ttk.Treeview(f5);
    tree["show"] = "headings";
    s = ttk.Style(f5);
    s.configure(".",font = ("Helvetica",9));
    s.configure("Treeview.Heading",foreground = "Red",font = ("Helvetica",9,"bold"));
    tree["columns"] = ("Name","Email_ID","Phone","Rate","Description");
    tree.column("Name",width = 170,minwidth = 50,anchor = CENTER);
    tree.column("Email_ID",width = 300,minwidth = 50,anchor = CENTER);
    tree.column("Phone",width = 170,minwidth = 50,anchor = CENTER);
    tree.column("Rate",width = 50,minwidth = 50,anchor = CENTER);
    tree.column("Description",width = 360,minwidth = 50,anchor = CENTER);
    
    tree.heading("Name",text = "Name",anchor = CENTER);
    tree.heading("Email_ID",text = "Email_ID",anchor = CENTER);
    tree.heading("Phone",text = "Phone",anchor = CENTER);
    tree.heading("Rate",text = "Rate",anchor = CENTER);
    tree.heading("Description",text = "Description",anchor = CENTER);
    
    
    i = 0;
    for ro in mycur:   #For each row in mycur
            tree.insert("", i, text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4]),tags=("even",));
            i = i+1;
            
   
    tree.place(x = 10,y =100);
                
def inventory():
    f2.destroy();
    global f5;
    f5 = Tk();
    f5.title("Inventory");
    f5.iconbitmap("ic1.ico");
    f5.geometry("1070x500");
    bg = Image.open("f5.jpg").resize((1070,500));
    m = Menu(f5);
    m1 = Menu(m,tearoff = 0);
    m.add_cascade(label = "File",menu = m1);
    m1.add_command(label = "View Feddback's",command = viewfb);
    m1.add_command(label = "Exit",command = f5.destroy);
    f5.config(menu = m);
    img = ImageTk.PhotoImage(bg,master = f5);
    lbl = Label(f5,image = img).place(x = 0,y = 63.3);
    Label(f5,text = "Inventory",justify = "center",font = ("Ink Free",35,"bold"),fg = "Red",bg = "Black",width = 300).pack();
    viewmi = Button(f5,text = "View Medicine Inventory",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",width = 25,command = vmi).place(x = 40,y = 400);
    delfinvent = Button(f5,text = "Delete from Inventory",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",width = 25,command = dmi).place(x = 380,y = 400);
    updateinvent = Button(f5,text = "Update Inventory",font = ("Ink Free",15,"bold"),fg = "Red",bg = "Black",width = 25,command = umi).place(x = 720,y = 400);
    f5.mainloop();
    
    

#-----------------------------------------------------------------------------#
LoginFrame1();
#MDPFrame2();
#About();
#Feedback();
#RegisterForm();
#inventory();
#billing();
#vph();
