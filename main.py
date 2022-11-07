from tkinter import *
import webbrowser


# Creating the main window
main_window = Tk()
main_window.title("Calculator and Converter tools")
main_window.config(background = 'gray79')
main_window.resizable(0 , 0)
main_window.geometry('610x420+20+45')
main_window.grid()

#########################   Calculator   ################################################
def open_calculator():
    import Calculator
    Calculator.run()

def hover_in_calc(event):
    Calculator.config(background = 'gray')
    Calculator.config(font = ('arial',21,'bold'))

def hover_out_calc(event):
    Calculator.config(background = 'white')
    Calculator.config(font=('arial', 20, 'bold'))

Calculator = Button(main_window , text = 'Calculator' , background = 'white' , activebackground = 'gray' ,
                    width = 10 , height = 1 , font = ('arial',20,'bold') , bd = 4 , relief= 'solid' , command = open_calculator)
Calculator.grid(row = 0 , column = 0 , padx = 60 , pady = 5)
Calculator.bind("<Enter>" , hover_in_calc)
Calculator.bind("<Leave>" , hover_out_calc)


################################# Temperature ###############################################

def open_temperature():
    import Temperature
    Temperature.run()

def hover_in_length(event):
    Temperature.config(background = 'gray')
    Temperature.config(font = ('arial',21,'bold'))

def hover_out_length(event):
    Temperature.config(background = 'white')
    Temperature.config(font=('arial', 20, 'bold'))

Temperature = Button(main_window , text = 'Temperature' , background = 'white' , activebackground = 'gray' ,
                    width = 10 , height = 1 , font = ('arial',20,'bold') , bd = 4 , relief= 'solid' , command = open_temperature)
Temperature.grid(row = 0 , column = 1 , padx = 60 , pady = 5)
Temperature.bind("<Enter>" , hover_in_length)
Temperature.bind("<Leave>" , hover_out_length)

#####################################  Length   ###########################################
def open_length():
    import Length
    Length.run()

def hover_in_length(event):
    Length.config(background = 'gray')
    Length.config(font = ('arial',21,'bold'))

def hover_out_length(event):
    Length.config(background = 'white')
    Length.config(font=('arial', 20, 'bold'))

Length = Button(main_window , text = 'Length' , background = 'white' , activebackground = 'gray' ,
                    width = 10 , height = 1 , font = ('arial',20,'bold') , bd = 4 , relief= 'solid' , command = open_length)
Length.grid(row = 1 , column = 0 , padx = 60 , pady = 5)
Length.bind("<Enter>" , hover_in_length)
Length.bind("<Leave>" , hover_out_length)



#################################### Weight  ############################################

def open_weight():
    import Weight
    Weight.run()

def hover_in_weight(event):
    Weight.config(background = 'gray')
    Weight.config(font = ('arial',21,'bold'))

def hover_out_weight(event):
    Weight.config(background = 'white')
    Weight.config(font=('arial', 20, 'bold'))

Weight = Button(main_window , text = 'Weight' , background = 'white' , activebackground = 'gray' ,
                    width = 10 , height = 1 , font = ('arial',20,'bold') , bd = 4 , relief= 'solid' , command = open_weight)
Weight.grid(row = 1 , column = 1 , padx = 60 , pady = 5)
Weight.bind("<Enter>" , hover_in_weight)
Weight.bind("<Leave>" , hover_out_weight)



##################################  Volume ##############################################

def open_volume():
    import Volume
    Volume.run()

def hover_in_volume(event):
    Volume.config(background = 'gray')
    Volume.config(font = ('arial',21,'bold'))

def hover_out_volume(event):
    Volume.config(background = 'white')
    Volume.config(font=('arial', 20, 'bold'))

Volume = Button(main_window , text = 'Volume' , background = 'white' , activebackground = 'gray' ,
                    width = 10 , height = 1 , font = ('arial',20,'bold') , bd = 4 , relief= 'solid' , command = open_volume)
Volume.grid(row = 2 , column = 0 , padx = 60 , pady = 5)
Volume.bind("<Enter>" , hover_in_volume)
Volume.bind("<Leave>" , hover_out_volume)


#####################################  Area  ###########################################
def open_area():
    import Area
    Area.run()

def hover_in_area(event):
    Area.config(background = 'gray')
    Area.config(font = ('arial',21,'bold'))

def hover_out_area(event):
    Area.config(background = 'white')
    Area.config(font=('arial', 20, 'bold'))

Area = Button(main_window , text = 'Area' , background = 'white' , activebackground = 'gray' ,
                    width = 10 , height = 1 , font = ('arial',20,'bold') , bd = 4 , relief= 'solid' , command = open_area)
Area.grid(row = 2 , column = 1 , padx = 60 , pady = 5)
Area.bind("<Enter>" , hover_in_area)
Area.bind("<Leave>" , hover_out_area)



##################################  Angle  ##############################################

def open_angle():
    import Angle
    Angle.run()

def hover_in_angle(event):
    Angle.config(background = 'gray')
    Angle.config(font = ('arial',21,'bold'))

def hover_out_angle(event):
    Angle.config(background = 'white')
    Angle.config(font=('arial', 20, 'bold'))

Angle = Button(main_window , text = 'Angle' , background = 'white' , activebackground = 'gray' ,
                    width = 10 , height = 1 , font = ('arial',20,'bold') , bd = 4 , relief= 'solid' , command = open_angle)
Angle.grid(row = 3 , column = 0 , padx = 60 , pady = 5)
Angle.bind("<Enter>" , hover_in_angle)
Angle.bind("<Leave>" , hover_out_angle)


#####################################  Power   ###########################################
def open_power():
    import Power
    Power.run()

def hover_in_power(event):
    Power.config(background = 'gray')
    Power.config(font = ('arial',21,'bold'))

def hover_out_power(event):
    Power.config(background = 'white')
    Power.config(font=('arial', 20, 'bold'))

Power = Button(main_window , text = 'Power' , background = 'white' , activebackground = 'gray' ,
                    width = 10 , height = 1 , font = ('arial',20,'bold') , bd = 4 , relief= 'solid' , command = open_power)
Power.grid(row = 3 , column = 1 , padx = 60 , pady = 5)
Power.bind("<Enter>" , hover_in_power)
Power.bind("<Leave>" , hover_out_power)



#####################################  Time   ###########################################
def open_time():
    import Time
    Time.run()

def hover_in_time(event):
    Time.config(background = 'gray')
    Time.config(font = ('arial',21,'bold'))

def hover_out_time(event):
    Time.config(background = 'white')
    Time.config(font=('arial', 20, 'bold'))

Time = Button(main_window , text = 'Time' , background = 'white' , activebackground = 'gray' ,
                    width = 10 , height = 1 , font = ('arial',20,'bold') , bd = 4 , relief= 'solid' , command = open_time)
Time.grid(row = 4 , column = 0 , padx = 60 , pady = 5)
Time.bind("<Enter>" , hover_in_time)
Time.bind("<Leave>" , hover_out_time)



#####################################  Speed   ###########################################
def open_speed():
    import Speed
    Speed.run()

def hover_in_speed(event):
    Speed.config(background = 'gray')
    Speed.config(font = ('arial',21,'bold'))

def hover_out_speed(event):
    Speed.config(background = 'white')
    Speed.config(font=('arial', 20, 'bold'))

Speed = Button(main_window , text = 'Speed' , background = 'white' , activebackground = 'gray' ,
                    width = 10 , height = 1 , font = ('arial',20,'bold') , bd = 4 , relief= 'solid' , command = open_speed)
Speed.grid(row = 4 , column = 1 , padx = 60 , pady = 5)
Speed.bind("<Enter>" , hover_in_speed)
Speed.bind("<Leave>" , hover_out_speed)



#####################################  Pressure  ###########################################
def open_pressure():
    import Pressure
    Pressure.run()

def hover_in_pressure(event):
    Pressure.config(background = 'gray')
    Pressure.config(font = ('arial',21,'bold'))

def hover_out_pressure(event):
    Pressure.config(background = 'white')
    Pressure.config(font=('arial', 20, 'bold'))

Pressure = Button(main_window , text = 'Pressure' , background = 'white' , activebackground = 'gray' ,
                    width = 10 , height = 1 , font = ('arial',20,'bold') , bd = 4 , relief= 'solid' , command = open_pressure)
Pressure.grid(row = 5 , column = 0 , padx = 60 , pady = 5)
Pressure.bind("<Enter>" , hover_in_pressure)
Pressure.bind("<Leave>" , hover_out_pressure)


#####################################  Energy  ###########################################
def open_energy():
    import Energy
    Energy.run()

def hover_in_energy(event):
    Energy.config(background = 'gray')
    Energy.config(font = ('arial',21,'bold'))

def hover_out_energy(event):
    Energy.config(background = 'white')
    Energy.config(font=('arial', 20, 'bold'))

Energy = Button(main_window , text = 'Energy' , background = 'white' , activebackground = 'gray' ,
                    width = 10 , height = 1 , font = ('arial',20,'bold') , bd = 4 , relief= 'solid' , command = open_energy)
Energy.grid(row = 5 , column = 1 , padx = 60 , pady = 5)
Energy.bind("<Enter>" , hover_in_energy)
Energy.bind("<Leave>" , hover_out_energy)




############# Menubar and it's files #############################

menubar = Menu(main_window)

def darkmode():
    main_window.config(background = 'black')

def lightmode():
    main_window.config(background = 'gray79')

filemenu = Menu(menubar , tearoff = 0)
menubar.add_cascade(label = 'File' , menu = filemenu)
filemenu.add_command(label = "Dark Mode" , command = darkmode)
filemenu.add_command(label = "Light Mode" , command = lightmode)
filemenu.add_separator()
filemenu.add_command(label = "Exit" , command = main_window.destroy)

def Facebook():
    webbrowser.open('https://www.facebook.com/Arbi.hamolli2/')

def Instagram():
    webbrowser.open('https://www.instagram.com/arbi.hamolli/')

def Linkedin():
    webbrowser.open('https://www.linkedin.com/in/arbi-hamolli-1ab33a215/')


filemenu2 = Menu(menubar , tearoff = 0)
menubar.add_cascade(label = 'Contact' , menu = filemenu2)
filemenu2.add_command(label = "Facebook" , command = Facebook)
filemenu2.add_command(label = "Instagram" , command = Instagram)
filemenu2.add_command(label = "Linkedin" , command = Linkedin)


main_window.config(menu = menubar)

main_window.mainloop()