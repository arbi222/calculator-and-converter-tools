from tkinter import *
from tkinter import ttk


def run():


    root = Toplevel()
    root.title("Length")
    root.geometry('510x451+305+180')
    root.resizable(0, 0)
    root.config(background='gray91')
    root.grid()




    # getting input
    txtDisplay_get = Entry(root, font=('arial', 28, 'bold'), bg='ivory4', bd=12, width=15, justify=RIGHT)
    txtDisplay_get.grid(row=0, column=0, columnspan=2, pady=1)
    txtDisplay_get.insert(0, '0')

    options = [
        'Nanometers',
        'Micrometers',
        'Milimeters',
        'Centimeters',
        'Meters',
        'Kilometers',
        'Inches',
        'Feet',
        'Yards',
        'Miles'
    ]

    style = ttk.Style()
    style.configure('my.TMenubutton', font=('Calibri', 10, 'bold'), width=10)

    choosing_get = StringVar()

    paddings = {'ipadx': 31, 'ipady': 22}

    drop_get = ttk.OptionMenu(root, choosing_get, options[4], *options, style='my.TMenubutton')
    drop_get.grid(row=0, column=2, **paddings)

    ##### displaying results
    txtDisplay = Label(root, text='0', font=('arial', 24, 'bold'), bg='gray91', bd=12, width=16, anchor=E)
    txtDisplay.grid(row=1, column=1, columnspan=2, pady=1)

    display_info = StringVar()

    drop_display = ttk.OptionMenu(root, display_info, options[3], *options, style='my.TMenubutton')
    drop_display.grid(row=1, column=0, **paddings)


    ############## CREATE THE CLASS #######################

    class Length():
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


        def calculate(self):


            def function_same(first):
                if choosing_get.get() == first and display_info.get() == first:
                    result = float(txtDisplay_get.get())
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:,}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:,}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)

            def function_multiply(first , second , multiplyer):
                if choosing_get.get() == first and display_info.get() == second:
                    result = float(txtDisplay_get.get()) * multiplyer
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:,}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:,}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)


            def function_divide(first , second , divider):
                if choosing_get.get() == first and display_info.get() == second:
                    result = float(txtDisplay_get.get()) / divider
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:,}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:,}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)

            # Nanometers
            function_same('Nanometers')
            function_multiply('Micrometers', 'Nanometers', 1_000)
            function_multiply('Milimeters', 'Nanometers', 1_000_000)
            function_multiply('Centimeters', 'Nanometers', 10_000_000)
            function_multiply('Meters', 'Nanometers', 1_000_000_000)
            function_multiply('Kilometers', 'Nanometers', 1_000_000_000_000)
            function_multiply('Inches', 'Nanometers', 25_400_000)
            function_multiply('Feet', 'Nanometers', 304_800_000)
            function_multiply('Yards', 'Nanometers', 914_400_000)
            function_multiply('Miles', 'Nanometers', 1_609_344_000_000)

            # Micrometers
            function_divide('Nanometers', 'Micrometers', 1_000)
            function_same('Micrometers')
            function_multiply('Milimeters', 'Micrometers', 1_000)
            function_multiply('Centimeters', 'Micrometers', 10_000)
            function_multiply('Meters', 'Micrometers', 1_000_000)
            function_multiply('Kilometers', 'Micrometers', 1_000_000_000)
            function_multiply('Inches', 'Micrometers', 25400)
            function_multiply('Feet', 'Micrometers', 304800)
            function_multiply('Yards', 'Micrometers', 914400)
            function_multiply('Miles', 'Micrometers', 1_609_344_000)

            # Milimeters
            def nano_to_mili():
                if choosing_get.get() == 'Nanometers' and display_info.get() == 'Milimeters':
                    result = float(txtDisplay_get.get()) / 1000000
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:.6f}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:.6f}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)
            nano_to_mili()

            function_divide('Micrometers', 'Milimeters', 1_000)
            function_same('Milimeters')
            function_multiply('Centimeters', 'Milimeters', 10)
            function_multiply('Meters', 'Milimeters', 1_000)
            function_multiply('Kilometers', 'Milimeters', 1_000_000)
            function_multiply('Inches', 'Milimeters', 25.4)
            function_multiply('Feet', 'Milimeters', 304.8)
            function_multiply('Yards', 'Milimeters', 914.4)
            function_multiply('Miles', 'Milimeters', 1_609_344)

            # Centimeters
            def nano_to_centi():
                if choosing_get.get() == 'Nanometers' and display_info.get() == 'Centimeters':
                    result = float(txtDisplay_get.get()) / 10000000
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:.7f}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:.7f}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)
            nano_to_centi()

            function_divide('Micrometers', 'Centimeters', 10_000)
            function_divide('Milimeters', 'Centimeters', 10)
            function_same('Centimeters')
            function_multiply('Meters', 'Centimeters', 100)
            function_multiply('Kilometers', 'Centimeters', 100_000)
            function_multiply('Inches', 'Centimeters', 2.54)
            function_multiply('Feet', 'Centimeters', 30.48)
            function_multiply('Yards', 'Centimeters', 91.44)
            function_multiply('Miles', 'Centimeters', 160_934.4)

            # Meter
            def nano_to_meter():
                if choosing_get.get() == 'Nanometers' and display_info.get() == 'Meters':
                    result = float(txtDisplay_get.get()) / 1_000_000_000
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:.9f}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:.9f}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)
            nano_to_meter()

            def micro_to_meter():
                if choosing_get.get() == 'Micrometers' and display_info.get() == 'Meters':
                    result = float(txtDisplay_get.get()) / 1_000_000
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:.6f}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:.6f}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)
            micro_to_meter()

            function_divide('Milimeters', 'Meters', 1_000)
            function_divide('Centimeters', 'Meters', 100)
            function_same('Meters')
            function_multiply('Kilometers' , 'Meters' , 1_000)
            function_multiply('Inches', 'Meters', 0.0254)
            function_multiply('Feet', 'Meters', 0.3048)
            function_multiply('Yards', 'Meters', 0.9144)
            function_multiply('Miles', 'Meters', 1_609.344)


            # Kilometer
            def nano_to_kilometer():
                if choosing_get.get() == 'Nanometers' and display_info.get() == 'Kilometers':
                    result = float(txtDisplay_get.get()) / 1_000_000_000_000
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:.12f}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:.12f}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)
            nano_to_kilometer()

            def micro_to_kilometer():
                if choosing_get.get() == 'Micrometers' and display_info.get() == 'Kilometers':
                    result = float(txtDisplay_get.get()) / 1_000_000_000
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:.9f}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:.9f}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)
            micro_to_kilometer()

            def mili_to_kilometer():
                if choosing_get.get() == 'Milimeters' and display_info.get() == 'Kilometers':
                    result = float(txtDisplay_get.get()) / 1_000_000
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:.6f}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:.6f}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)
            mili_to_kilometer()

            def cm_to_kilometer():
                if choosing_get.get() == 'Centimeters' and display_info.get() == 'Kilometers':
                    result = float(txtDisplay_get.get()) / 100000
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:.5f}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:.5f}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)
            cm_to_kilometer()

            function_divide('Meters' , 'Kilometers' , 1_000)
            function_same('Kilometers')

            def inches_to_kilometer():
                if choosing_get.get() == 'Inches' and display_info.get() == 'Kilometers':
                    result = float(txtDisplay_get.get()) * 0.000025
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:.6f}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:.6f}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)
            inches_to_kilometer()

            def feet_to_kilometer():
                if choosing_get.get() == 'Feet' and display_info.get() == 'Kilometers':
                    result = float(txtDisplay_get.get()) * 0.000305
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:.6f}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:.6f}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)
            feet_to_kilometer()

            def yards_to_kilometer():
                if choosing_get.get() == 'Yards' and display_info.get() == 'Kilometers':
                    result = float(txtDisplay_get.get()) * 0.000914
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:.6f}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:.6f}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)
            yards_to_kilometer()

            function_multiply('Miles' , 'Kilometers' , 1.609344)


            # Inches
            def nano_to_inches():
                if choosing_get.get() == 'Nanometers' and display_info.get() == 'Inches':
                    result = float(txtDisplay_get.get()) * 0.000000039370079
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:.15f}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:.15f}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)
            nano_to_inches()

            def micro_to_inches():
                if choosing_get.get() == 'Micrometers' and display_info.get() == 'Inches':
                    result = float(txtDisplay_get.get()) * 0.000039
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:.6f}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:.6f}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)
            micro_to_inches()

            function_multiply('Milimeters' , 'Inches' , 0.03937)
            function_multiply('Centimeters', 'Inches', 0.393701)
            function_multiply('Meters', 'Inches', 39.37008)
            function_multiply('Kilometers', 'Inches', 39_370.08)
            function_same('Inches')
            function_multiply('Feet', 'Inches', 12)
            function_multiply('Yards', 'Inches', 36)
            function_multiply('Miles', 'Inches', 63_360)


            # Feet
            def nano_to_feet():
                if choosing_get.get() == 'Nanometers' and display_info.get() == 'Feet':
                    result = float(txtDisplay_get.get()) * 0.000_000_003_280_84
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:.14f}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:.14f}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)
            nano_to_feet()

            def micro_to_feet():
                if choosing_get.get() == 'Micrometers' and display_info.get() == 'Feet':
                    result = float(txtDisplay_get.get()) * 0.000003
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:.6f}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:.6f}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)
            micro_to_feet()

            function_multiply('Milimeters' , 'Feet' , 0.003281)
            function_multiply('Centimeters', 'Feet', 0.032808)
            function_multiply('Meters', 'Feet', 3.28084)
            function_multiply('Kilometers', 'Feet', 3280.84)
            function_multiply('Inches', 'Feet', 0.083333)
            function_same('Feet')
            function_multiply('Yards', 'Feet', 3)
            function_multiply('Miles', 'Feet', 5280)


            # Yards
            def nano_to_yards():
                if choosing_get.get() == 'Nanometers' and display_info.get() == 'Yards':
                    result = float(txtDisplay_get.get()) * 0.000_000_001_093_613
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:.15f}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:.15f}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)
            nano_to_yards()

            def micro_to_yards():
                if choosing_get.get() == 'Micrometers' and display_info.get() == 'Yards':
                    result = float(txtDisplay_get.get()) * 0.000_001
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:.6f}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:.6f}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)
            micro_to_yards()

            function_multiply('Milimeters' , 'Yards' , 0.001094)
            function_multiply('Centimeters', 'Yards', 0.010936)
            function_multiply('Meters', 'Yards', 1.093613)
            function_multiply('Kilometers', 'Yards', 1_093.613)
            function_multiply('Inches', 'Yards', 0.027778)
            function_multiply('Feet', 'Yards', 0.333333)
            function_same('Yards')
            function_multiply('Miles', 'Yards', 1760)


            # Miles
            def nano_to_miles():
                if choosing_get.get() == 'Nanometers' and display_info.get() == 'Miles':
                    result = float(txtDisplay_get.get()) * 0.000_000_000_000_621
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:.15f}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:.15f}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)
            nano_to_miles()

            def micro_to_miles():
                if choosing_get.get() == 'Micrometers' and display_info.get() == 'Miles':
                    result = float(txtDisplay_get.get()) * 0.000_000_000_621_371
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:.15f}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:.15f}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)
            micro_to_miles()

            def mili_to_miles():
                if choosing_get.get() == 'Milimeters' and display_info.get() == 'Miles':
                    result = float(txtDisplay_get.get()) * 0.000_000_621_371_192
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:.15f}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:.15f}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)
            mili_to_miles()

            def cm_to_miles():
                if choosing_get.get() == 'Centimeters' and display_info.get() == 'Miles':
                    result = float(txtDisplay_get.get()) * 0.000006
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:.6f}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:.6f}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)
            cm_to_miles()

            function_multiply('Meters' , 'Miles' , 0.000621)
            function_multiply('Kilometers', 'Miles', 0.621371)

            def inches_to_miles():
                if choosing_get.get() == 'Inches' and display_info.get() == 'Miles':
                    result = float(txtDisplay_get.get()) * 0.000016
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:.6f}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:.6f}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)
            inches_to_miles()

            function_multiply('Feet', 'Miles', 0.000189)
            function_multiply('Yards', 'Miles', 0.000568)
            function_same('Miles')


    Length_calculations = Length()


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
            button[i]['command'] = lambda x=numbers[i]: Length_calculations.entering_numbers(x)
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

    Zero_button = Button(root, text='0', width=9, height=1, font=('arial', 20, 'bold'), bd=4,
                         bg='white', activebackground='gray78' , command = lambda : Length_calculations.entering_numbers(0))
    Zero_button.grid(row=7, column=1, pady=1)
    Zero_button.bind("<Enter>", hover_in_zero)
    Zero_button.bind("<Leave>", hover_out_zero)

    Dot_button = Button(root, text='.', width=9, height=1, font=('arial', 20, 'bold'), bd=4,
                         bg='gray91', activebackground='gray78' , command = lambda : Length_calculations.entering_numbers('.'))
    Dot_button.grid(row=7, column=0, pady=1)
    Dot_button.bind("<Enter>", hover_in_dot)
    Dot_button.bind("<Leave>", hover_out_dot)

    #empty_label1 = Label(root, width=22, height=3, bd=6, bg='gray80', state='disabled')
    #empty_label1.grid(row=2, column=0, pady=1)

    Result_button = Button(root , text = 'Calculate' , font=('arial', 20, 'bold') ,  width=9, height=1 , bd=4 ,
                           bg="SteelBlue1" , activebackground = 'SteelBlue3' , command = Length_calculations.calculate)
    Result_button.grid(row=7, column=2, pady=1)
    Result_button.bind("<Enter>", hover_in_result)
    Result_button.bind("<Leave>", hover_out_result)


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
                               bg="gray91", activebackground='gray78' , command = Length_calculations.remove_last)
    Clear_last_button.grid(row=2, column=1, pady=1)
    Clear_last_button.bind("<Enter>", hover_in_clear_last)
    Clear_last_button.bind("<Leave>", hover_out_clear_last)

    AllClear_button = Button(root, text=chr(67), width=9, height=1, font=('arial', 20, 'bold'), bd=4,
                             bg="gray91", activebackground='gray78' , command = Length_calculations.clear_entry)
    AllClear_button.grid(row=2, column=2, pady=1)
    AllClear_button.bind("<Enter>", hover_in_all_clear)
    AllClear_button.bind("<Leave>", hover_out_all_clear)



    root.mainloop()