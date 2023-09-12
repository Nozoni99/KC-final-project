import tkinter as tk
from tkinter import IntVar, Radiobutton 
import random

window= tk.Tk()
window.title("My story")
window.geometry("600x600")
window.configure(bg= 'Cornsilk')

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)


def  Input_user():
    window.destroy()
    Input_user= tk.Tk()
    Input_user.title("My story")
    Input_user.geometry("600x600")
    Input_user.configure(bg= 'Cornsilk') 


    first_sent = tk.Frame(relief='sunken', borderwidth=5 , bg='Cornsilk')
    first_sent.pack(padx=20 , pady=20)
    sent= tk.Label(Input_user , text="Please enter the following qestions :" , font=('Harrington', 20), bg='BlanchedAlmond')
    sent.pack(padx=20 , pady=20)

    inputs = tk.Frame(relief="raised", borderwidth=5 , bg='Cornsilk' )
    inputs.pack(padx=20 , pady=20)
    

    lbl_first_name = tk.Label(master=inputs, text="First character Name:"  ,font =("Andalus", 20),bg= 'Cornsilk' )
    global ent_first_name
    ent_first_name = tk.Entry(master=inputs, width=70 ,font=("Andalus" , 20) , )
    

    lbl_first_name.grid(row=0, column=0, padx=5 , pady=5 , )
    ent_first_name.grid(row=0, column=1)
    

    lbl_sec_name = tk.Label(master= inputs , text="Second character Name:", font=('Andalus', 20) ,bg= 'Cornsilk')
    global ent_sec_name
    ent_sec_name = tk.Entry(master= inputs , width=70, font =('Andalus', 20))

    lbl_sec_name.grid(row=1, column=0,padx=5 , pady=5)
    ent_sec_name.grid(row=1, column=1)


    lbl_additional1 = tk.Label(master= inputs, text="Additional character name:",font =('Andalus', 20) ,bg= 'Cornsilk')
    global ent_additional1
    ent_additional1 = tk.Entry(master= inputs, width=70 ,font =('Andalus', 20))

    lbl_additional1.grid(row=2, column=0,padx=5 , pady=5 )
    ent_additional1.grid(row=2, column=1)


    lbl_place = tk.Label(master= inputs , text="Main place of the story :" ,font =('Andalus', 20) ,bg= 'Cornsilk')
    global ent_place
    ent_place = tk.Entry(master= inputs , width=70,font =('Andalus', 20))

    lbl_place.grid(row=3, column=0,padx=5 , pady=5 )
    ent_place.grid(row=3, column=1)


    sent_nice = tk.Frame(relief='ridge', borderwidth=5 , bg='Cornsilk')
    sent_nice.pack(padx=20 , pady=20)
    nice= tk.Label(master=Input_user , text="Niiiiccceeee !!! " , font=('Harrington', 20), bg='BlanchedAlmond')
    nice.pack(padx=15 , pady=15)


    btn_next = tk.Button(Input_user , text=" Let's see waht is next !!" ,font=('Andalus', 18), width=30 , height=10 , bg='Wheat' , command=Story_type )
    btn_next.pack(padx=20 , pady= 50)


def Story_type():
    Story_type = tk.Tk()
    Story_type.title("My story")
    Story_type.geometry("900x900")
    Story_type.configure(bg='Cornsilk')

    sent2= tk.Label(master=Story_type, text='''Ohhh Ohhh , well , it is nice to see you
    excited for the story , now choose your story type and we will procced a starting sentence to give 
    you some ideas . ''' , font=('Harrington', 20), bg='BlanchedAlmond', width= 90 , height=5)
    sent2.grid(padx=20 , pady=20)

    first_btn = tk.Radiobutton(Story_type, text="Adventure",  font=('Harrington', 20), bg='Wheat',command=lambda:adven())
    first_btn.grid(padx=10, pady=10)
    
    second_btn = tk.Radiobutton(Story_type, text="Drama" , font=('Harrington', 20), bg='Wheat',command=lambda:drama())
    second_btn.grid(padx=10, pady=10)
    
    third_btn = tk.Radiobutton(Story_type,  text="Horror",   font=('Harrington', 20), bg='Wheat',command=lambda:horr())
    third_btn.grid(padx=10, pady=10)
    
    fourth_btn = tk.Radiobutton(Story_type , text="Comedey",  font=('Harrington', 20), bg='Wheat',command=lambda:come())
    fourth_btn.grid(padx=10, pady=10)

    label = tk.Label(Story_type)
    label.grid(padx=20 , pady=20 )


def Start_story():
    Start_story= tk.Tk()
    Start_story.title("My story")
    Start_story.geometry("900x900")
    Start_story.configure(bg= 'Cornsilk') 

    user = tk.Frame(master= Start_story , relief='ridge', borderwidth=5 , bg='Cornsilk')
    user.pack(padx=20 , pady=20)
    user_data= tk.Label(master= user , text="Start writting here :" , font=('Harrington', 20), bg='BlanchedAlmond')
    enter_data = tk.Text(Start_story, width=190 , height=90 , font=("Arial", 20 ))
    enter_data.pack(padx=10 , pady=10 )
    user_data.pack(padx=15 , pady=15)



def adven():
    name1= ent_first_name.get()
    name2= ent_sec_name.get()
    name3= ent_additional1.get()
    main_place= ent_place.get()
    adven = tk.Tk()
    adven.title("My story")
    adven.geometry("800x800")
    adven.configure(bg='Cornsilk')

    sent_starter=["Once upon a time ","One day ","One full moon night ","At the sunset,near the sea ","A long time ago "]
    names=[name1 ,name2 ,name3 ]
    plots=[" knew something is wrong with"," discovered the secret of "," saw an unexpected person, "," woken up in a strange place with "]
    places=[" at the hill "," in the cave "," under the water "," in woods "," in the station ",]
    actions=[" run till reached"," jumped away "," fighted hard in "," then stole the map from "," then drove crazy to "," then blocked the train of "," then ride the horse to "]
    sec_place=[" the house ","the mountain "," the chamber "," the cave "," the forest "]
    times=[" in the evening ","in the moring "," at the sunset ","in the middle of the night "," at 5:30 ","when the sun rised "]
    
    frm= tk.Frame(master=adven , bg='Bisque' , width=100 , height=5)
    frm.pack(padx=10 , pady=10)
    text_adve = tk.Label(master=frm , font=('Arial', 18), bg='Bisque',width=100 , height=5, wraplength=800,
    text = ( random.choice(sent_starter)+(f"in the {main_place} ")+random.choice(names)+
          random.choice(plots)+ random.choice(names)+random.choice(places)+
          random.choice(names)+random.choice(actions)
          +random.choice(sec_place)+random.choice(times)))               
    text_adve.pack(padx=20 , pady=20)


    your_turn = tk.Frame(relief='ridge', borderwidth=5 , bg='Cornsilk')
    your_turn.pack(padx=20 , pady=20)
    nice= tk.Label(master=adven , text="Here you go , now it is your turn !" , font=('Harrington', 20), bg='BlanchedAlmond')
    nice.pack(padx=15 , pady=15)


    btn_next = tk.Button(adven, text=" Let's see waht is next !!" ,font=('Andalus', 18), width=30 , height=10 , bg='Wheat' , command=Start_story )
    btn_next.pack(padx=20 , pady= 50)
            

def drama():
    name1= ent_first_name.get()
    name2= ent_sec_name.get()
    name3= ent_additional1.get()
    main_place= ent_place.get()
    drama = tk.Tk()
    drama.title("My story")
    drama.geometry("800x800")
    drama.configure(bg='Cornsilk')

    sent_starter=["Once upon a time ","One day ","At the sunset,near the sea ","A long time ago "]
    names=[name1,name2,name3]
    plots=[" knew something is wrong "," discovered the secret..... "," saw an unexpected person, "]
    support=["it was his.....son!","Hanaa is died ! ",(random.choice(names)+" betrayed us and revealed everything to the army")]
    actions=[ "he couldn't believe "," she cried alot "," then he fighted with him "," then drove crazy"]
    sec_place=[" the house was quiet "," the chamber was quiet "," the place was quiet only hearing the sound of cry, "]
    times=[" in the evening "," at the sunset ","in the middle of the night ", "when the sun rised "]
        
    frm= tk.Frame(master=drama , bg='Bisque' , width=100 , height=5)
    frm.pack(padx=10 , pady=10)
    text_drama = tk.Label(master=frm , font=('Arial', 18), bg='Bisque', width=100 , height=5 ,wraplength=800,
    text=(random.choice(sent_starter)+(f"in the {main_place}")+
        random.choice(names)+random.choice(plots)+random.choice(support)+
        random.choice(actions)+random.choice(sec_place)+random.choice(times)+"then everything was over." ))
    text_drama.pack(padx=20 , pady=20)

    your_turn = tk.Frame(master=drama , relief='ridge', borderwidth=5 , bg='Cornsilk')
    your_turn.pack(padx=20 , pady=20)
    nice = tk.Label(master=your_turn , text="Here you go , now it is your turn !" , font=('Harrington', 20), bg='BlanchedAlmond')
    nice.pack(padx=15 , pady=15)


    btn_next = tk.Button(drama, text=" Let's see waht is next !!" ,font=('Andalus', 18), width=30 , height=10 , bg='Wheat' , command=Start_story )
    btn_next.pack(padx=20 , pady= 50)
            

def come():
    name1= ent_first_name.get()
    name2= ent_sec_name.get()
    name3= ent_additional1.get()
    main_place= ent_place.get()
    come = tk.Tk()
    come.title("My story")
    come.geometry("800x800")
    come.configure(bg='Cornsilk')

    sent_starter=["Once upon a time ","One day ","At the sunset, ","A long time ago "]
    names=[ name1 , name2 , name3 ]
    plots=[" was walking "," was playing "," was reading "," was talking to the cat "," was actually dreaming "]
    places=[" in the room. "," near the beach. "," in woods. "," in the school. "," in the house. "]
    actions=[" The bird started talking "," A rabbit suddenly apeared and asked :'hey you human, give me food! '"," I missed the bus "," I forgot the key "," Ops! I ate the berries! "]
    sec_place=[" The house "," The room "," The cave "," The forest "]
    times=[" in the evening ","in the moring "," at the sunset "," at 5:30 ","when the sun rised "]

    frm= tk.Frame(master= come , bg='Bisque' , width=100 , height=5)
    frm.pack(padx=10 , pady=10)
    text_come = tk.Label(master=frm , font=('Arial', 18), bg='Bisque', width=100 , height=5 ,wraplength=800,
    text=(  random.choice(sent_starter)+(f"in the {main_place} ")+random.choice(names)+
            random.choice(plots)+random.choice(places)+random.choice(actions)+
            " said "+random.choice(names)+". "+"but the "+random.choice(sec_place)+"was all in a miss !"))
    text_come.pack(padx=20 , pady=20 )

    your_turn = tk.Frame(master=come,relief='ridge', borderwidth=5 , bg='Cornsilk')
    your_turn.pack(padx=20 , pady=20)
    nice= tk.Label(master=your_turn , text="Here you go , now it is your turn !" , font=('Harrington', 20), bg='BlanchedAlmond')
    nice.pack(padx=15 , pady=15)


    btn_next = tk.Button(come , text=" Let's see waht is next !!" ,font=('Andalus', 18), width=30 , height=10 , bg='Wheat' , command=Start_story )
    btn_next.pack(padx=20 , pady= 50)
            

def horr():
    name1= ent_first_name.get()
    name2= ent_sec_name.get()
    name3= ent_additional1.get()
    main_place= ent_place.get()
    horr = tk.Tk()
    horr.title("My story")
    horr.geometry("800x800")
    horr.configure(bg='Cornsilk')
    
    sent_starter=["One full moon night , ","One night ","At the sunset, near the sea ","A long time ago "]
    names=[name1 ,name2 ,name3 ]
    plots=[" heard a sound ","siad that :' the black creature was runing after me and.... '"," saw a shadow...... "]
    support=[" it was a kind of ........ deadly scream !"," it was with no head !!? "," but was it just a dream...?"]
    actions=[" panicked out  "," cried a lot "," shivered with fear "," shocked and.... went crazy "]
    sec_place=[" the house was quiet "," the room was quiet "," the place was quiet","only hearing the sound of cry,"]
    times=[" In the evening ","It was at the sunset ","In the middle of the night ", "When the sun rised "]
        
    frm= tk.Frame(master=horr ,bg='Bisque' , width=100 , height=5)
    frm.pack(padx=10 , pady=10)
    text_horror = tk.Label(master=frm , font=('Arial', 18), bg='Bisque', width=100 , height=5 ,wraplength=800,
    text=(    random.choice(sent_starter)+(f"in the {main_place}" )+
              random.choice(names)+random.choice(plots)+random.choice(support)+
              random.choice(times)+random.choice(names)+random.choice(actions)+"then"+random.choice(sec_place)))
    text_horror.pack(padx=20 , pady=20)

    your_turn = tk.Frame(master = horr , relief='ridge', borderwidth=5 , bg='Cornsilk')
    your_turn.pack(padx=20 , pady=20)
    nice= tk.Label(master=your_turn , text="Here you go , now it is your turn !" , font=('Harrington', 20), bg='BlanchedAlmond')
    nice.pack(padx=15 , pady=15)


    btn_next = tk.Button(horr, text=" Let's see waht is next !!" ,font=('Andalus', 18), width=30 , height=10 , bg='Wheat' , command=Start_story )
    btn_next.pack(padx=20 , pady= 50)
            

frame_page = tk.Frame(master=window, relief="sunken", borderwidth=3 , bg='BlanchedAlmond')
frame_page.pack(padx=20 , pady=20)
label= tk.Label(master = frame_page, text="Welcome to My story" , font=('Harrington', 20), bg='BlanchedAlmond')
label.pack(padx=20, pady=20)


frm_wlcome = tk.Frame(master=window, relief="sunken", borderwidth=3 , width=50 ,height=15 )
frm_wlcome.pack(padx=3 , pady=3)
lbl_welcome = tk.Label(master= frm_wlcome, text='''Welcome our great writer to My story. Each one 
of us has his own story, written by his own words,
but we pretty shy about writing them seriously !
Here we will encourage you to give yourself a try
and help you to write your own story.''' , 
font=("Andalus", 18) , bg='BlanchedAlmond', width=50 , height=10)
lbl_welcome.pack()

btn_go = tk.Button(window , text=" Let's go !" , width=30 , height=10 , bg='Wheat' , command=Input_user )
btn_go.pack(padx=20 , pady= 50)


window.mainloop()


####### THE END #######
#  الود ودي احط صور حلوه بدل ما شكله سادة كده بس معرفتش انا سو ساد والله#