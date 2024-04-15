    from  tkinter import*def thread_fun():
   label.config(text="You can Click the button or Wait")
   time.sleep(5)
   label.config(text= "5 seconds Up!")
 
label= Label(win)
label.pack(pady=20)
#Create button
b1= Button(win,text= "Start", command=threading.Thread(target=thread_fun).start())
b1.pack(pady=20)