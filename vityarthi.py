# insert data
def insertdata():
    import mysql.connector as mp
    con=mp.connect(host='localhost', user='root', password='',      db='konkona')
    cursor=con.cursor()
    sno=int(input("enter serial no"))
    novel=input("enter novel")
    author=input("enter name of author")
    genre=input("enter genre")
    quantity=int(input("enter amt of copies"))
    rating=int(input("enter rating"))
    query="insert into library values({},'{}','{}','{}',{},{})".format(sno, novel, author, genre, quantity,rating)
    cursor.execute(query)
    con.commit()
    print("data inserted")
    c=input("do you want to insert more data? yes/no")
    if (c=='yes'):
        insertdata()
    else:
        menu()
# UDATING OLD DATA
def updatedata():
    


    def updatenovel():
        import mysql.connector as mp
        conn=mp.connect(host='localhost',user='root',password='',db='konkona')
        cursor=conn.cursor()
        sno=int(input('Enter sno of book where details has to be updated'))
        novel=input('Enter updated novel')
        query="update library set novel ='{}' where sno ={}".format(novel,sno)
        cursor.execute(query)
        conn.commit()
        print("data updated successfully")
        k=input("do you want to update again? yes/no")
        if k=='yes':
            updatemenu()
        else:
                menu()
    def updateauthor():
        import mysql.connector as mp
        conn=mp.connect(host='localhost',user='root',password='',db='konkona')
        cursor=conn.cursor()
        sno=int(input('Enter sno of book where details has to be updated'))
        author=input('Enter updated author')
        query="update library set author ='{}' where sno ={}".format(author,sno)
        cursor.execute(query)
        conn.commit()
        print("data updated successfully")
        k=input("do you want to update again? yes/no")
        if k=='yes':
            updatemenu()
        else:
                menu()

    def updategenre():
        import mysql.connector as mp
        conn=mp.connect(host='localhost',user='root',password='',db='konkona')
        cursor=conn.cursor()
        sno=int(input('Enter sno of book where details has to be updated'))
        genre=input('Enter updated genre')
        query="update library set genre ='{}' where sno ={}".format(genre,sno)
        cursor.execute(query)
        conn.commit()
        print("data updated successfully")
        k=input("do you want to update again? yes/no")
        if k=='yes':
            updatemenu()
        else:
                menu()
    def updatequantity():
        import mysql.connector as mp
        conn=mp.connect(host='localhost',user='root',password='',db='konkona')
        cursor=conn.cursor()
        sno=int(input('Enter sno of book where details has to be updated'))
        quantity=input('Enter updated copies')
        query="update library set quantity ='{}' where sno ={}".format(quantity,sno)
        cursor.execute(query)
        conn.commit()
        print("data updated successfully")
        k=input("do you want to update again? yes/no")
        if k=='yes':
            updatemenu()
        else:
                menu()

  

    def updatemenu():
        print("press t to update novel")
        print("press a to update authorname")
        print("press g to update genre")
        print("press c to update no of copies")
        choice=input("enter what you wish to update")
        if choice=='t':
            updatenovel()
        
        elif  choice=='a':
                updateauthor()
        elif choice=='g':
            updategenre()
        elif choice=='c':
            updatequantity()
        else:
            print("no value updated")
    updatemenu()

    print('data updated successfully')
   
#DISPLAY DATA 

def displaydata():
    import mysql.connector as mp
    conn=mp.connect(host='localhost',user='root',password='',db='konkona')
    cursor=conn.cursor()

    query="select * from library"
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
        print(row)
    print('data displayed successfully')
    c=input("do you want to display again? yes/no")
    if c=='yes':
        displaydata()
    else:
        menu()
#DELETE DATA 
def deletedata():
    import mysql.connector as mp
    conn=mp.connect(host='localhost',user='root',password='',db='konkona')
    cursor=conn.cursor()

    sno=int(input('Enter sno of book where details has to be deleted'))

    query="delete from library where sno ={}".format(sno)
    cursor.execute(query)
    conn.commit()
    print('data deleted successfully')
    c=input("do you want to delete more data?")
    if c=='yes':
        deletedata()
    else:
        menu()


# plotting data
    
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
d = pd.read_csv(r"E:\vityarthi\students.csv")
# Strip any leading/trailing spaces in column names
d.columns = d.columns.str.strip()

# Now  accessing the 'novel' and 'quantity' columns 

'''x =d['novel'].tolist()
y = d['quantity'].tolist()
z=d['rating'].tolist()

    # Create the plot
   
plt.xlabel('Novel')
plt.ylabel('Quantity')

def line_chart():
    
    w=input("do you want to see quantity graph or ratings graph? Press q or r respectively")
    if w=='q':
        plt.xlabel('Novel')
        plt.ylabel('Quantity')
        plt.plot(x, y)
        plt.show()
    elif w=='r':
        plt.xlabel('Novel')
        plt.zlabel('Rating')
        plt.plot(x, z)
        plt.show()
    else:
        graphmenu()
    e=input("do you wish to review? press yes or no")
    if e=='yes':
        line_chart()
    else:
        graphmenu()
    
def horizontal_bar():
    
    plt.xlabel('Novel')
    plt.ylabel('Quantity')
    plt.barh(x, y)
    plt.show()
    e=input("do you wish to review? press yes or no")
    if e=='yes':
        horizontal_bar()
    else:
        graphmenu()
    
def vertical_bar():
    
    plt.xlabel('Novel')
    plt.ylabel('Quantity')
    plt.bar(x, y)
    plt.show()
    e=input("do you wish to review? press yes or no")
    if e=='yes':
        vertical_bar()
    else:
        graphmenu()
def piechart():
    plt.pie(y, labels=x)
    plt.show()
    e=input("do you wish to review? press yes or no")
    if e=='yes':
        piechart()
    else:
        graphmenu()
        
def graphmenu():
    print("press l to plot line chart")
    print("press h to plot horizontal bar")
    print("press v to plot vertical bar")
    
    print("press p to plot pie chart")
    choice=input("enter what you wish to see")
    if choice=='l':
        line_chart()
        
    elif  choice=='h':
             horizontal_bar()
    elif choice=='v':
        vertical_bar()
    elif choice=='p':
        piechart()
    else:
        print("no graph available")'''

#MENU
    
def menu():
    print("welcome to menu")
    print("press 1 for inserting data")
    print("press 2 for updating data")
    print("press 3 for display data")
    print("press 4 for deleteing data")
    print("press 5 for displaying graphing data")
    cho=int(input("enter your choice"))
    if cho==1:
        insertdata()
    elif cho==2:
        updatedata()
    elif cho==3:
        displaydata()
    elif cho==4:
        deletedata()
    elif cho==5:
        graphmenu()
        
    else:
        print("wrong choice")
        choi=input("if you still wish to continue press y")
        if choi=='y':
            menu()
        else:
            print("thank you for visiting")            
# insert data
def insertdatas():
    import mysql.connector as mp
    con=mp.connect(host='localhost', user='root', password='', db='konkona')
    cursor=con.cursor()
    sn=int(input("enter serial no"))
    name=input("enter name")
    book=input("enter name of book")
    grade=input("enter grade")
    
    query="insert into students values({},'{}','{}','{}')".format(sn,name,book, grade )
    cursor.execute(query)
    con.commit()
    print("data inserted")
    c=input("do you want to insert more data? yes/no")
    if (c=='yes'):
        insertdatas()
    else:
        smenu()

def updatedatas():
    


    def updatenames():
        import mysql.connector as mp
        conn=mp.connect(host='localhost',user='root',password='',db='konkona')
        cursor=conn.cursor()
        sn=int(input('Enter sno of book where details has to be updated'))
        name=input('Enter updated name')
        query="update students set name ='{}' where sn ={}".format(name,sn)
        cursor.execute(query)
        conn.commit()
        q=input("do you want to update again? press yes or no")
        if q=='yes':
            updatesmenu()
        else:
            smenu()
    def updatebooks():
        import mysql.connector as mp
        conn=mp.connect(host='localhost',user='root',password='',db='konkona')
        cursor=conn.cursor()
        sn=int(input('Enter sno of book where details has to be updated'))
        book=input('Enter updated book')
        query="update students set book ='{}' where sn ={}".format(book,sn)
        cursor.execute(query)
        conn.commit()
        q=input("do you want to update again? press yes or no")
        if q=='yes':
            updatesmenu()
        else:
            smenu()

    def grades():
        import mysql.connector as mp
        conn=mp.connect(host='localhost',user='root',password='',db='konkona')
        cursor=conn.cursor()
        sn=int(input('Enter sno of book where details has to be updated'))
        grade=input('Enter updated grade')
        query="update students set grade ={} where sn ={}".format(grade, sn)
        cursor.execute(query)
        conn.commit()
        q=input("do you want to update again? press yes or no")
        if q=='yes':
            updatesmenu()
        else:
            smenu()
  

    def updatesmenu():
        print("press n to update name")
        print("press b to update book")
        print("press g to update grade")
        
        choice=input("enter what you wish to update")
        if choice=='n':
            updatenames()
        
        elif  choice=='b':
                updatebooks()
        elif choice=='g':
            grades()
        
        else:
            print("no value updated")
    updatesmenu()

    print('data updated successfully')


def displaydatas():
    import mysql.connector as mp
    conn=mp.connect(host='localhost',user='root',password='',db='konkona')
    cursor=conn.cursor()

    query="select * from students"
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
        print(row)
    print('data displayed successfully')
    c=input("do you want to display again? yes/no")
    if c=='yes':
        displaydatas()
    else:
        smenu()

def deletedatas():
    import mysql.connector as mp
    conn=mp.connect(host='localhost',user='root',password='',db='konkona')
    cursor=conn.cursor()

    sn=int(input('Enter sno of book where details has to be deleted'))

    query="delete from students where sn ={}".format(sn)
    cursor.execute(query)
    conn.commit()
    print('data deleted successfully')
    c=input("do you want to delete more data?")
    if c=='yes':
        deletedatas()
    else:
        smenu()


# plotting data
    
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
d = pd.read_csv(r"E:\vityarthi\students.csv")
# Strip any leading/trailing spaces in column names
d.columns = d.columns.str.strip()

# Now  accessing the 'novel' and 'quantity' columns 

x = d['name'].tolist()
y = d['grade'].tolist()


    # Create the plot
   
plt.xlabel('Name')
plt.ylabel('Grade')

def line_charts():
    
   
    plt.xlabel('Name')
    plt.ylabel('Grade')
    plt.plot(x, y)
    plt.show()
   
    e=input("do you wish to review? press yes or no")
    if e=='yes':
        line_charts()
    else:
        graphsmenu()
    
def horizontal_bars():
    
     plt.xlabel('Name')
     plt.ylabel('Grade')
     plt.barh(x, y)
     plt.show()
     e=input("do you wish to review? press yes or no")
     if e=='yes':
         horizontal_bars()
     else:
         graphsmenu()
    
def vertical_bars():
    
     plt.xlabel('Name')
     plt.ylabel('Grade')
     plt.bar(x, y)
     plt.show()
     e=input("do you wish to review? press yes or no")
     if e=='yes':
         vertical_bars()
     else:
         graphsmenu()
def piecharts():
     
     plt.pie(y, labels=x)
     plt.show()
   
     e=input("do you wish to review? press yes or no")
     if e=='yes':
         piecharts()
     else:
         graphsmenu()
        
def graphsmenu():
    print("press l to plot line chart")
    print("press h to plot horizontal bar")
    print("press v to plot vertical bar")
    
    print("press p to plot pie chart")
    choice=input("enter what you wish to see")
    if choice=='l':
        line_charts()
        
    elif  choice=='h':
             horizontal_bars()
    elif choice=='v':
        vertical_bars()
    elif choice=='p':
        piecharts()
    else:
        print("no graph available")


    
    

    
def smenu():
    print("welcome to menu")
    print("press 1 for inserting data")
    print("press 2 for updating data")
    print("press 3 for display data")
    print("press 4 for deleteing data")
    print("press 5 for displaying graphs")
    cho=int(input("enter your choice"))
    if cho==1:
        insertdatas()
    elif cho==2:
        updatedatas()
    elif cho==3:
        displaydatas()
    elif cho==4:
        deletedatas()
    elif cho==5:
        graphsmenu()
    else:
        print("wrong choice")
        choi=input("if you still wish to continue press y")
        if choi=='y':
            smenu()
        else:
            print("thank you for visiting")            

        

# Main program
print("Welcome to the Library management")
print("This Application helps you keep track of books delivering from the publisher and issued by students")

choic=input("do you want to acess the library books or student system?, press b or s")
if choic=='b':
    menu()
elif choic=='s':
    smenu()
    
else:
    print("have a nice day")
    print("We hope you visit soon")
