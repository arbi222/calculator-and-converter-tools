from tkinter import *
from tkinter import ttk


def run():


    root = Toplevel()
    root.title("Weight")
    root.geometry('510x451+305+180')
    root.resizable(0, 0)
    root.config(background='gray91')
    root.grid()




    # getting input
    txtDisplay_get = Entry(root, font=('arial', 28, 'bold'), bg='ivory4', bd=12, width=15, justify=RIGHT)
    txtDisplay_get.grid(row=0, column=0, columnspan=2, pady=1)
    txtDisplay_get.insert(0, '0')

    options = [
        'Carats',
        'Milligrams',
        'Centigrams',
        'Decigrams',
        'Grams',
        'Dekagrams',
        'Hectograms',
        'Kilograms',
        'Quintal',
        'Tonnes'
    ]

    style = ttk.Style()
    style.configure('my.TMenubutton', font=('Calibri', 10, 'bold'), width=10)

    choosing_get = StringVar()

    paddings = {'ipadx': 31, 'ipady': 22}

    drop_get = ttk.OptionMenu(root, choosing_get, options[7], *options, style='my.TMenubutton')
    drop_get.grid(row=0, column=2, **paddings)

    ##### displaying results
    txtDisplay = Label(root, text='0', font=('arial', 24, 'bold'), bg='gray91', bd=12, width=16, anchor=E)
    txtDisplay.grid(row=1, column=1, columnspan=2, pady=1)

    display_info = StringVar()

    drop_display = ttk.OptionMenu(root, display_info, options[4], *options, style='my.TMenubutton')
    drop_display.grid(row=1, column=0, **paddings)


    ############## CREATE THE CLASS #######################

    class Weight():
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

            def function_multiply(first, second, multiplyer):

                if choosing_get.get() == first and display_info.get() == second:
                    result = float(txtDisplay_get.get()) * multiplyer
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:,}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:,}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)


            def function_divide(first, second, divider):

                if choosing_get.get() == first and display_info.get() == second:
                    result = float(txtDisplay_get.get()) / divider
                    if str(result)[-2:] == '.0':
                        fixed_result = str(result)[:-2]
                        formated_result = '{:,}'.format(int(fixed_result))
                        txtDisplay['text'] = str(formated_result)
                    else:
                        formated_result = '{:,}'.format(float(result))
                        txtDisplay['text'] = str(formated_result)


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

            #  Carats
            function_same('Carats')

            function_divide('Milligrams' , 'Carats' , 200)

            function_divide('Centigrams', 'Carats', 20)

            function_divide('Decigrams', 'Carats', 2)

            function_multiply('Grams' , 'Carats' , 5)

            function_multiply('Dekagrams', 'Carats', 50)

            function_multiply('Hectograms', 'Carats', 500)

            function_multiply('Kilograms', 'Carats', 5_000)

            function_multiply('Quintal', 'Carats', 500_000)

            function_multiply('Tonnes', 'Carats', 5_000_000)

            # Milligrams
            function_multiply('Carats', 'Milligrams', 200)

            function_same('Milligrams')

            function_multiply('Centigrams', 'Milligrams', 10)

            function_multiply('Decigrams', 'Milligrams', 100)

            function_multiply('Grams', 'Milligrams', 1000)

            function_multiply('Dekagrams', 'Milligrams', 10_000)

            function_multiply('Hectograms', 'Milligrams', 100_000)

            function_multiply('Kilograms', 'Milligrams', 1_000_000)

            function_multiply('Quintal', 'Milligrams', 100_000_000)

            function_multiply('Tonnes', 'Milligrams', 1_000_000_000)


            # Centigrams
            function_multiply('Carats', 'Centigrams', 20)

            function_divide('Milligrams' , 'Centigrams' , 10)

            function_same('Centigrams')

            function_multiply('Decigrams', 'Centigrams', 10)

            function_multiply('Grams', 'Centigrams', 100)

            function_multiply('Dekagrams', 'Centigrams', 1_000)

            function_multiply('Hectograms', 'Centigrams', 10_000)

            function_multiply('Kilograms', 'Centigrams', 100_000)

            function_multiply('Quintal', 'Centigrams', 10_000_000)

            function_multiply('Tonnes', 'Centigrams', 100_000_000)


            # Decigrams
            function_multiply('Carats' , 'Decigrams' , 2)

            function_divide('Milligrams', 'Decigrams', 100)

            function_divide('Centigrams', 'Decigrams', 10)

            function_same('Decigrams')

            function_multiply('Grams', 'Decigrams', 10)

            function_multiply('Dekagrams', 'Decigrams', 100)

            function_multiply('Hectograms', 'Decigrams', 1_000)

            function_multiply('Kilograms', 'Decigrams', 10_000)

            function_multiply('Quintal', 'Decigrams', 1_000_000)

            function_multiply('Tonnes', 'Decigrams', 10_000_000)


            # Grams
            function_divide('Carats', 'Grams', 5)

            function_divide('Milligrams', 'Grams', 1_000)

            function_divide('Centigrams', 'Grams', 100)

            function_divide('Decigrams', 'Grams', 10)

            function_same('Grams')

            function_multiply('Dekagrams', 'Grams', 10)

            function_multiply('Hectograms', 'Grams', 100)

            function_multiply('Kilograms', 'Grams', 1_000)

            function_multiply('Quintal', 'Grams', 100_000)

            function_multiply('Tonnes', 'Grams', 1_000_000)


            # Dekagrams
            function_divide('Carats', 'Dekagrams', 50)

            function_divide('Milligrams', 'Dekagrams', 10_000)

            function_divide('Centigrams', 'Dekagrams', 1_000)

            function_divide('Decigrams', 'Dekagrams', 100)

            function_divide('Grams', 'Dekagrams', 10)

            function_same('Dekagrams')

            function_multiply('Hectograms', 'Dekagrams', 10)

            function_multiply('Kilograms', 'Dekagrams', 100)

            function_multiply('Quintal', 'Dekagrams', 10_000)

            function_multiply('Tonnes', 'Dekagrams', 100_000)


            # Hectograms
            function_divide('Carats', 'Hectograms', 500)

            if choosing_get.get() == 'Milligrams' and display_info.get() == 'Hectograms':
                result = float(txtDisplay_get.get()) / 100_000
                if str(result)[-2:] == '.0':
                    fixed_result = str(result)[:-2]
                    formated_result = '{:.5f}'.format(int(fixed_result))
                    txtDisplay['text'] = str(formated_result)
                else:
                    formated_result = '{:.5f}'.format(float(result))
                    txtDisplay['text'] = str(formated_result)

            function_divide('Centigrams', 'Hectograms', 10_000)

            function_divide('Decigrams', 'Hectograms', 1_000)

            function_divide('Grams', 'Hectograms', 100)

            function_divide('Dekagrams', 'Hectograms', 10)

            function_same('Hectograms')

            function_multiply('Kilograms', 'Hectograms', 10)

            function_multiply('Quintal', 'Hectograms', 1_000)

            function_multiply('Tonnes', 'Hectograms', 10_000)


            # Kilograms
            function_divide('Carats', 'Kilograms', 5000)

            if choosing_get.get() == 'Milligrams' and display_info.get() == 'Kilograms':
                result = float(txtDisplay_get.get()) / 1_000_000
                if str(result)[-2:] == '.0':
                    fixed_result = str(result)[:-2]
                    formated_result = '{:.6f}'.format(int(fixed_result))
                    txtDisplay['text'] = str(formated_result)
                else:
                    formated_result = '{:.6f}'.format(float(result))
                    txtDisplay['text'] = str(formated_result)

            if choosing_get.get() == 'Centigrams' and display_info.get() == 'Kilograms':
                result = float(txtDisplay_get.get()) / 100_000
                if str(result)[-2:] == '.0':
                    fixed_result = str(result)[:-2]
                    formated_result = '{:.5f}'.format(int(fixed_result))
                    txtDisplay['text'] = str(formated_result)
                else:
                    formated_result = '{:.5f}'.format(float(result))
                    txtDisplay['text'] = str(formated_result)

            function_divide('Decigrams', 'Kilograms', 10_000)

            function_divide('Grams', 'Kilograms', 1_000)

            function_divide('Dekagrams', 'Kilograms', 100)

            function_divide('Hectograms', 'Kilograms', 10)

            function_same('Kilograms')

            function_multiply('Quintal', 'Kilograms', 100)

            function_multiply('Tonnes', 'Kilograms', 1_000)


            # Quintals
            if choosing_get.get() == 'Carats' and display_info.get() == 'Quintal':
                result = float(txtDisplay_get.get()) / 500_000
                if str(result)[-2:] == '.0':
                    fixed_result = str(result)[:-2]
                    formated_result = '{:.6f}'.format(int(fixed_result))
                    txtDisplay['text'] = str(formated_result)
                else:
                    formated_result = '{:.6f}'.format(float(result))
                    txtDisplay['text'] = str(formated_result)

            if choosing_get.get() == 'Milligrams' and display_info.get() == 'Quintal':
                result = float(txtDisplay_get.get()) / 100_000_000
                if str(result)[-2:] == '.0':
                    fixed_result = str(result)[:-2]
                    formated_result = '{:.8f}'.format(int(fixed_result))
                    txtDisplay['text'] = str(formated_result)
                else:
                    formated_result = '{:.8f}'.format(float(result))
                    txtDisplay['text'] = str(formated_result)


            if choosing_get.get() == 'Centigrams' and display_info.get() == 'Quintal':
                result = float(txtDisplay_get.get()) / 10_000_000
                if str(result)[-2:] == '.0':
                    fixed_result = str(result)[:-2]
                    formated_result = '{:.7f}'.format(int(fixed_result))
                    txtDisplay['text'] = str(formated_result)
                else:
                    formated_result = '{:.7f}'.format(float(result))
                    txtDisplay['text'] = str(formated_result)

            if choosing_get.get() == 'Decigrams' and display_info.get() == 'Quintal':
                result = float(txtDisplay_get.get()) / 1_000_000
                if str(result)[-2:] == '.0':
                    fixed_result = str(result)[:-2]
                    formated_result = '{:.6f}'.format(int(fixed_result))
                    txtDisplay['text'] = str(formated_result)
                else:
                    formated_result = '{:.6f}'.format(float(result))
                    txtDisplay['text'] = str(formated_result)

            if choosing_get.get() == 'Grams' and display_info.get() == 'Quintal':
                result = float(txtDisplay_get.get()) / 100_000
                if str(result)[-2:] == '.0':
                    fixed_result = str(result)[:-2]
                    formated_result = '{:.5f}'.format(int(fixed_result))
                    txtDisplay['text'] = str(formated_result)
                else:
                    formated_result = '{:.5f}'.format(float(result))
                    txtDisplay['text'] = str(formated_result)

            function_divide('Dekagrams', 'Quintal', 10_000)

            function_divide('Hectograms', 'Quintal', 1_000)

            function_divide('Kilograms', 'Quintal', 100)

            function_same('Quintal')

            function_multiply('Tonnes', 'Quintal', 10)


            # Tonnes
            if choosing_get.get() == 'Carats' and display_info.get() == 'Tonnes':
                result = float(txtDisplay_get.get()) / 5_000_000
                if str(result)[-2:] == '.0':
                    fixed_result = str(result)[:-2]
                    formated_result = '{:.7f}'.format(int(fixed_result))
                    txtDisplay['text'] = str(formated_result)
                else:
                    formated_result = '{:.7f}'.format(float(result))
                    txtDisplay['text'] = str(formated_result)


            if choosing_get.get() == 'Milligrams' and display_info.get() == 'Tonnes':
                result = float(txtDisplay_get.get()) / 1_000_000_000
                if str(result)[-2:] == '.0':
                    fixed_result = str(result)[:-2]
                    formated_result = '{:.9f}'.format(int(fixed_result))
                    txtDisplay['text'] = str(formated_result)
                else:
                    formated_result = '{:.9f}'.format(float(result))
                    txtDisplay['text'] = str(formated_result)


            if choosing_get.get() == 'Centigrams' and display_info.get() == 'Tonnes':
                result = float(txtDisplay_get.get()) / 100_000_000
                if str(result)[-2:] == '.0':
                    fixed_result = str(result)[:-2]
                    formated_result = '{:.8f}'.format(int(fixed_result))
                    txtDisplay['text'] = str(formated_result)
                else:
                    formated_result = '{:.8f}'.format(float(result))
                    txtDisplay['text'] = str(formated_result)


            if choosing_get.get() == 'Decigrams' and display_info.get() == 'Tonnes':
                result = float(txtDisplay_get.get()) / 10_000_000
                if str(result)[-2:] == '.0':
                    fixed_result = str(result)[:-2]
                    formated_result = '{:.7f}'.format(int(fixed_result))
                    txtDisplay['text'] = str(formated_result)
                else:
                    formated_result = '{:.7f}'.format(float(result))
                    txtDisplay['text'] = str(formated_result)


            if choosing_get.get() == 'Grams' and display_info.get() == 'Tonnes':
                result = float(txtDisplay_get.get()) / 1_000_000
                if str(result)[-2:] == '.0':
                    fixed_result = str(result)[:-2]
                    formated_result = '{:.6f}'.format(int(fixed_result))
                    txtDisplay['text'] = str(formated_result)
                else:
                    formated_result = '{:.6f}'.format(float(result))
                    txtDisplay['text'] = str(formated_result)

            if choosing_get.get() == 'Dekagrams' and display_info.get() == 'Tonnes':
                result = float(txtDisplay_get.get()) / 100_000
                if str(result)[-2:] == '.0':
                    fixed_result = str(result)[:-2]
                    formated_result = '{:.5f}'.format(int(fixed_result))
                    txtDisplay['text'] = str(formated_result)
                else:
                    formated_result = '{:.5f}'.format(float(result))
                    txtDisplay['text'] = str(formated_result)

            function_divide('Hectograms', 'Tonnes', 10_000)

            function_divide('Kilograms', 'Tonnes', 1_000)

            function_divide('Quintal', 'Tonnes', 10)

            function_same('Tonnes')


    Weight_calculations = Weight()


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
            button[i]['command'] = lambda x=numbers[i]: Weight_calculations.entering_numbers(x)
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
                         bg='white', activebackground='gray78' , command = lambda : Weight_calculations.entering_numbers(0))
    Zero_button.grid(row=7, column=1, pady=1)
    Zero_button.bind("<Enter>", hover_in_zero)
    Zero_button.bind("<Leave>", hover_out_zero)

    Dot_button = Button(root, text='.', width=9, height=1, font=('arial', 20, 'bold'), bd=4,
                         bg='gray91', activebackground='gray78' , command = lambda : Weight_calculations.entering_numbers('.'))
    Dot_button.grid(row=7, column=0, pady=1)
    Dot_button.bind("<Enter>", hover_in_dot)
    Dot_button.bind("<Leave>", hover_out_dot)

    #empty_label1 = Label(root, width=22, height=3, bd=6, bg='gray80', state='disabled')
    #empty_label1.grid(row=2, column=0, pady=1)

    Result_button = Button(root , text = 'Calculate' , font=('arial', 20, 'bold') ,  width=9, height=1 , bd=4 ,
                           bg="SteelBlue1" , activebackground = 'SteelBlue3' , command = Weight_calculations.calculate)
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
                               bg="gray91", activebackground='gray78' , command = Weight_calculations.remove_last)
    Clear_last_button.grid(row=2, column=1, pady=1)
    Clear_last_button.bind("<Enter>", hover_in_clear_last)
    Clear_last_button.bind("<Leave>", hover_out_clear_last)

    AllClear_button = Button(root, text=chr(67), width=9, height=1, font=('arial', 20, 'bold'), bd=4,
                             bg="gray91", activebackground='gray78' , command = Weight_calculations.clear_entry)
    AllClear_button.grid(row=2, column=2, pady=1)
    AllClear_button.bind("<Enter>", hover_in_all_clear)
    AllClear_button.bind("<Leave>", hover_out_all_clear)



    root.mainloop()