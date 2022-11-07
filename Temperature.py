from tkinter import *
from tkinter import ttk


def run():


    root = Toplevel()
    root.title("Temperature")
    root.geometry('510x451+305+180')
    root.resizable(0, 0)
    root.config(background='gray91')
    root.grid()




    # getting input
    txtDisplay_get = Entry(root, font=('arial', 28, 'bold'), bg='ivory4', bd=12, width=15, justify=RIGHT)
    txtDisplay_get.grid(row=0, column=0, columnspan=2, pady=1)
    txtDisplay_get.insert(0, '0')

    options = [
        'Celcius',
        'Fahrenheit',
        'Kelvin'
    ]

    style = ttk.Style()
    style.configure('my.TMenubutton', font=('Calibri', 10, 'bold'), width=10)

    choosing_get = StringVar()

    paddings = {'ipadx': 31, 'ipady': 22}

    drop_get = ttk.OptionMenu(root, choosing_get, options[0], *options, style='my.TMenubutton')
    drop_get.grid(row=0, column=2, **paddings)

    ##### displaying results
    txtDisplay = Label(root, text='0', font=('arial', 24, 'bold'), bg='gray91', bd=12, width=16, anchor=E)
    txtDisplay.grid(row=1, column=1, columnspan=2, pady=1)

    display_info = StringVar()

    drop_display = ttk.OptionMenu(root, display_info, options[1], *options, style='my.TMenubutton')
    drop_display.grid(row=1, column=0, **paddings)


    ############## CREATE THE CLASS #######################

    class Temperature():
        def __init__(self):
            self.current = ''
            self.input_value = True

        def display(self , value):
            txtDisplay_get.delete(0 , END)
            txtDisplay_get.insert(0 , value)

        def entering_numbers(self, num):

            first_num = txtDisplay_get.get()
            second_num = str(num)
            if self.input_value:
                self.current = second_num
                self.input_value = False
            else:
                if second_num == '.':
                    if second_num in first_num:
                        return
                self.current = first_num + second_num
            self.display(self.current)


        def clear_entry(self):

            self.current = '0'
            self.display(0)
            txtDisplay['text'] = '0'
            self.input_value = True

        def remove_last(self):

            def clearing():
                length = len(txtDisplay_get.get())
                txtDisplay_get.delete(length - 1 , 'end')
                the_number = str(txtDisplay_get.get()).replace(',' , '').split(' ')
                self.current = float(the_number[0])
            if txtDisplay_get.get() == '0':
                txtDisplay_get.insert(0 , '0')
            if len(txtDisplay_get.get()) == 1:
                txtDisplay_get.insert(0, '0')

            clearing()
            self.input_value = False


        def plusminus(self):

            self.current = -(float(str(txtDisplay_get.get())))
            if str(self.current)[-2:] == '.0':
                fixed_result = str(self.current)[:-2]
                self.display(fixed_result)
            else:
                self.display(self.current)


        def calculate(self):

            def celcius_to_celcius():
                if choosing_get.get() == 'Celcius' and display_info.get() == 'Celcius':
                    result = float(txtDisplay_get.get())
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:,}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:,}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)

            celcius_to_celcius()


            def celcius_to_fahrenheit():
                if choosing_get.get() == 'Celcius' and display_info.get() == 'Fahrenheit':
                    result = (float(txtDisplay_get.get()) * (9/5)) + 32
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:,}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        rounded_result = round(result , 5)
                        formated_result = '{:,}'.format(float(rounded_result))
                        txtDisplay['text'] = str(formated_result)

            celcius_to_fahrenheit()


            def celcius_to_kelvin():
                if choosing_get.get() == 'Celcius' and display_info.get() == 'Kelvin':
                    result = float(txtDisplay_get.get()) + 273.15
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:,}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        rounded_result = round(result, 5)
                        formated_result = '{:,}'.format(float(rounded_result))
                        txtDisplay['text'] = str(formated_result)

            celcius_to_kelvin()


            def fahrenheit_to_celcius():
                if choosing_get.get() == 'Fahrenheit' and display_info.get() == 'Celcius':
                    result = (float(txtDisplay_get.get()) - 32) * (5/9)
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:,}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        rounded_result = round(result, 5)
                        formated_result = '{:,}'.format(float(rounded_result))
                        txtDisplay['text'] = str(formated_result)

            fahrenheit_to_celcius()


            def fahrenheit_to_fahrenheit():
                if choosing_get.get() == 'Fahrenheit' and display_info.get() == 'Fahrenheit':
                    result = float(txtDisplay_get.get())
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:,}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:,}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)

            fahrenheit_to_fahrenheit()


            def fahrenheit_to_kelvin():
                if choosing_get.get() == 'Fahrenheit' and display_info.get() == 'Kelvin':
                    result = ((float(txtDisplay_get.get()) - 32) * (5/9)) + 273.15
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:,}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        rounded_result = round(result, 5)
                        formated_result = '{:,}'.format(float(rounded_result))
                        txtDisplay['text'] = str(formated_result)

            fahrenheit_to_kelvin()


            def kelvin_to_celcius():
                if choosing_get.get() == 'Kelvin' and display_info.get() == 'Celcius':
                    result = float(txtDisplay_get.get()) - 273.15
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:,}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        rounded_result = round(result, 5)
                        formated_result = '{:,}'.format(float(rounded_result))
                        txtDisplay['text'] = str(formated_result)

            kelvin_to_celcius()


            def kelvin_to_fahrenheit():
                if choosing_get.get() == 'Kelvin' and display_info.get() == 'Fahrenheit':
                    result = ((float(txtDisplay_get.get()) - 273.15) * (9/5)) + 32
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:,}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:,}'.format(float(result))
                        formated_result = round(float(formated_result) , 5)
                        txtDisplay['text'] = str(formated_result)

            kelvin_to_fahrenheit()


            def kelvin_to_kelvin():
                if choosing_get.get() == 'Kelvin' and display_info.get() == 'Kelvin':
                    result = float(txtDisplay_get.get())
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:,}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:,}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)

            kelvin_to_kelvin()



    Temperature_calculations = Temperature()


    ########## Numbers ###########################################
    def hover_in_zero(event):
        button[0].config(background='gray78')
        button[0].config(font=('arial', 21, 'bold'))

    def hover_out_zero(event):
        button[0].config(background='white')
        button[0].config(font=('arial', 20, 'bold'))

    def hover_in_one(event):
        button[1].config(background='gray78')
        button[1].config(font=('arial', 21, 'bold'))

    def hover_out_one(event):
        button[1].config(background='white')
        button[1].config(font=('arial', 20, 'bold'))

    def hover_in_two(event):
        button[2].config(background='gray78')
        button[2].config(font=('arial', 21, 'bold'))

    def hover_out_two(event):
        button[2].config(background='white')
        button[2].config(font=('arial', 20, 'bold'))

    def hover_in_three(event):
        button[3].config(background='gray78')
        button[3].config(font=('arial', 21, 'bold'))

    def hover_out_three(event):
        button[3].config(background='white')
        button[3].config(font=('arial', 20, 'bold'))

    def hover_in_four(event):
        button[4].config(background='gray78')
        button[4].config(font=('arial', 21, 'bold'))

    def hover_out_four(event):
        button[4].config(background='white')
        button[4].config(font=('arial', 20, 'bold'))

    def hover_in_five(event):
        button[5].config(background='gray78')
        button[5].config(font=('arial', 21, 'bold'))

    def hover_out_five(event):
        button[5].config(background='white')
        button[5].config(font=('arial', 20, 'bold'))

    def hover_in_six(event):
        button[6].config(background='gray78')
        button[6].config(font=('arial', 21, 'bold'))

    def hover_out_six(event):
        button[6].config(background='white')
        button[6].config(font=('arial', 20, 'bold'))

    def hover_in_seven(event):
        button[7].config(background='gray78')
        button[7].config(font=('arial', 21, 'bold'))

    def hover_out_seven(event):
        button[7].config(background='white')
        button[7].config(font=('arial', 20, 'bold'))

    def hover_in_eight(event):
        button[8].config(background='gray78')
        button[8].config(font=('arial', 21, 'bold'))

    def hover_out_eight(event):
        button[8].config(background='white')
        button[8].config(font=('arial', 20, 'bold'))

    numbers = '789456123'
    i = 0
    button = []
    for j in range(4, 7):
        for k in range(3):
            button.append(Button(root, width=9, height=1, background='white', activebackground='gray78',
                                 font=('arial', 20, 'bold'), bd=4, text=numbers[i]))
            button[i].grid(row=j, column=k, pady=1)
            button[i]['command'] = lambda x=numbers[i]: Temperature_calculations.entering_numbers(x)
            i += 1

    button[0].bind("<Enter>", hover_in_zero)
    button[0].bind("<Leave>", hover_out_zero)

    button[1].bind("<Enter>", hover_in_one)
    button[1].bind("<Leave>", hover_out_one)

    button[2].bind("<Enter>", hover_in_two)
    button[2].bind("<Leave>", hover_out_two)

    button[3].bind("<Enter>", hover_in_three)
    button[3].bind("<Leave>", hover_out_three)

    button[4].bind("<Enter>", hover_in_four)
    button[4].bind("<Leave>", hover_out_four)

    button[5].bind("<Enter>", hover_in_five)
    button[5].bind("<Leave>", hover_out_five)

    button[6].bind("<Enter>", hover_in_six)
    button[6].bind("<Leave>", hover_out_six)

    button[7].bind("<Enter>", hover_in_seven)
    button[7].bind("<Leave>", hover_out_seven)

    button[8].bind("<Enter>", hover_in_eight)
    button[8].bind("<Leave>", hover_out_eight)




    def hover_in_zero(event):
        Zero_button.config(background = 'gray78')
        Zero_button.config(font=('arial', 21, 'bold'))

    def hover_out_zero(event):
        Zero_button.config(background = 'white')
        Zero_button.config(font=('arial', 20, 'bold'))

    def hover_in_dot(event):
        Dot_button.config(background = 'gray78')
        Dot_button.config(font=('arial', 21, 'bold'))

    def hover_out_dot(event):
        Dot_button.config(background = 'gray91')
        Dot_button.config(font=('arial', 20, 'bold'))

    def hover_in_result(event):
        Result_button.config(background = 'SteelBlue2')
        Result_button.config(font=('arial', 21, 'bold'))

    def hover_out_result(event):
        Result_button.config(background = 'SteelBlue1')
        Result_button.config(font=('arial', 20, 'bold'))

    def hover_in_pm(event):
        Plus_minus_button.config(background = 'gray78')
        Plus_minus_button.config(font=('arial', 21, 'bold'))

    def hover_out_pm(event):
        Plus_minus_button.config(background = 'gray91')
        Plus_minus_button.config(font=('arial', 20, 'bold'))


    Zero_button = Button(root, text='0', width=9, height=1, font=('arial', 20, 'bold'), bd=4,
                         bg='white', activebackground='gray78' , command = lambda : Temperature_calculations.entering_numbers(0))
    Zero_button.grid(row=7, column=1, pady=1)
    Zero_button.bind("<Enter>", hover_in_zero)
    Zero_button.bind("<Leave>", hover_out_zero)

    Dot_button = Button(root, text='.', width=9, height=1, font=('arial', 20, 'bold'), bd=4,
                         bg='gray91', activebackground='gray78' , command = lambda : Temperature_calculations.entering_numbers('.'))
    Dot_button.grid(row=7, column=0, pady=1)
    Dot_button.bind("<Enter>", hover_in_dot)
    Dot_button.bind("<Leave>", hover_out_dot)

    Result_button = Button(root , text = 'Calculate' , font=('arial', 20, 'bold') ,  width=9, height=1 , bd=4 ,
                           bg="SteelBlue1" , activebackground = 'SteelBlue3' , command = Temperature_calculations.calculate)
    Result_button.grid(row=7, column=2, pady=1)
    Result_button.bind("<Enter>", hover_in_result)
    Result_button.bind("<Leave>", hover_out_result)

    Plus_minus_button = Button(root, text=chr(177), font=('arial', 20, 'bold'), width=9, height=1, bd=4,
                           bg="gray91", activebackground='gray78' , command = Temperature_calculations.plusminus)
    Plus_minus_button.grid(row=2, column=0, pady=1)
    Plus_minus_button.bind("<Enter>", hover_in_pm)
    Plus_minus_button.bind("<Leave>", hover_out_pm)


    def hover_in_clear_last(event):
        Clear_last_button.config(background = 'gray78')
        Clear_last_button.config(font=('arial', 21, 'bold'))

    def hover_out_clear_last(event):
        Clear_last_button.config(background = 'gray91')
        Clear_last_button.config(font=('arial', 20, 'bold'))

    def hover_in_all_clear(event):
        AllClear_button.config(background = 'gray78')
        AllClear_button.config(font=('arial', 21, 'bold'))

    def hover_out_all_clear(event):
        AllClear_button.config(background = 'gray91')
        AllClear_button.config(font=('arial', 20, 'bold'))



    Clear_last_button = Button(root, text='⌫', width=9, height=1, font=('arial', 20, 'bold'), bd=4,
                               bg="gray91", activebackground='gray78' , command = Temperature_calculations.remove_last)
    Clear_last_button.grid(row=2, column=1, pady=1)
    Clear_last_button.bind("<Enter>", hover_in_clear_last)
    Clear_last_button.bind("<Leave>", hover_out_clear_last)

    AllClear_button = Button(root, text=chr(67), width=9, height=1, font=('arial', 20, 'bold'), bd=4,
                             bg="gray91", activebackground='gray78' , command = Temperature_calculations.clear_entry)
    AllClear_button.grid(row=2, column=2, pady=1)
    AllClear_button.bind("<Enter>", hover_in_all_clear)
    AllClear_button.bind("<Leave>", hover_out_all_clear)



    root.mainloop()