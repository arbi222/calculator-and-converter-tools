from tkinter import *
import math
from tkinter import messagebox

def run():

    root = Toplevel()
    root.title("Calculator")
    root.geometry('489x546+305+180')
    root.resizable(0,0)
    root.config(background = 'gray91')
    root.grid()



    ###################  THE CLASS WITH IT'S FUNCTIONS  #############################

    class Calc:
        def __init__(self):
            self.total = 0
            self.current = ''
            self.input_value = True
            self.check_sum = False
            self.op = ''
            self.result = False

        def display(self , value):
            txtDisplay.delete(0 , END)
            txtDisplay.insert(0 , value)

        def entering_numbers(self, num):
            self.result = False
            first_num = txtDisplay.get()
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

        def equals_to(self):
            self.result = True
            self.current = float(self.current)
            if self.check_sum == True:
                self.valid_function()
            else:
                self.total = float(txtDisplay.get())


        def valid_function(self):
            if self.op == 'Add':
                self.total += self.current
            elif self.op == 'Subtract':
                self.total -= self.current
            elif self.op == 'Multiply':
                self.total *= self.current
            elif self.op == 'Divide':
                self.total /= self.current
            self.input_value = True
            self.check_sum = False
            result = '{:,}'.format(self.total)
            self.display(result)

        def operation(self , op):
            self.current = float((str(self.current).replace(',' , '')))
            if self.check_sum:
                self.valid_function()
            elif not self.result:
                self.total = self.current
                self.input_value = True
            self.check_sum = True
            self.op = op
            self.result = False

        def clear_entry(self):
            self.result = False
            self.current = '0'
            self.display(0)
            self.input_value = True


        def remove_last(self):
            self.result = False
            def clearing():
                length = len(txtDisplay.get())
                txtDisplay.delete(length - 1 , 'end')
                the_number = str(txtDisplay.get()).replace(',' , '').split(' ')
                self.current = float(the_number[0])
            if txtDisplay.get() == '0':
                txtDisplay.insert(0 , '0')
            if len(txtDisplay.get()) == 1:
                txtDisplay.insert(0, '0')

            clearing()
            self.input_value = False

        def plusminus(self):
            self.result = False
            self.current = -(float(str(txtDisplay.get()).replace(',' , '')))
            result = '{:,}'.format(self.current)
            self.display(result)

        def squareroot(self):
            self.result = False
            self.current = math.sqrt(float(str(txtDisplay.get()).replace(',' , '')))
            result = '{:,}'.format(self.current)
            self.display(result)

        ######## scientific functions ########

        def pi(self):
            self.result = False
            self.current = math.pi
            self.display(self.current)

        def factorial(self):
            self.result = False
            try:
                self.current = math.factorial(int(txtDisplay.get()))
                self.display(self.current)
            except:
                messagebox.showwarning(title='Input Error', message='Please enter a Whole number!')
            finally:
                pass
                # self.display(self.current)

        def e(self):
            self.result = False
            self.current = math.e
            self.display(self.current)

        def log(self):
            self.result = False
            self.current = math.log10(float(str(txtDisplay.get()).replace(',' , '')))
            result = '{:,}'.format(self.current)
            self.display(result)

        def sin(self):
            self.result = False
            self.current = math.sin(math.radians(float(str(txtDisplay.get()).replace(',' , ''))))
            result = '{:,}'.format(self.current)
            self.display(result)

        def cos(self):
            self.result = False
            self.current = math.cos(math.radians(float(str(txtDisplay.get()).replace(',' , ''))))
            result = '{:,}'.format(self.current)
            self.display(result)

        def tan(self):
            self.result = False
            self.current = math.tan(math.radians(float(str(txtDisplay.get()).replace(',' , ''))))
            result = '{:,}'.format(self.current)
            self.display(result)

        def X2(self):
            self.result = False
            def square(a):
                s = a ** 2
                return s
            self.current = square(float(str(txtDisplay.get()).replace(',' , '')))
            result = '{:,}'.format(self.current)
            self.display(result)

        def X3(self):
            self.result = False
            def cub(a):
                k = a ** 3
                return k
            self.current = cub(float(str(txtDisplay.get()).replace(',' , '')))
            result = '{:,}'.format(self.current)
            self.display(result)

        def DevideByX(self):
            self.result = False
            def oneDivideX(x):
                y = 1 / x
                return y
            self.current = oneDivideX(float(str(txtDisplay.get()).replace(',' , '')))
            result = '{:,}'.format(self.current)
            self.display(result)

    #### Creating the object
    calculations = Calc()

    ########## The Entry Field #################################

    txtDisplay = Entry(root , font = ('arial',28,'bold') , bg = 'ivory4' , bd = 12 , width = 22, justify = RIGHT )
    txtDisplay.grid(row = 0 , column = 0 , columnspan = 4 , pady = 1)
    txtDisplay.insert(0 , '0')


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
        button[8].config(background = 'gray78')
        button[8].config(font=('arial', 21, 'bold'))

    def hover_out_eight(event):
        button[8].config(background='white')
        button[8].config(font=('arial', 20, 'bold'))

    numbers = '789456123'
    i = 0
    button = []
    for j in range(2,5):
        for k in range(3):
            button.append(Button(root , width = 6 , height = 2 , background = 'white' , activebackground = 'gray78' ,
                                 font = ('arial',20,'bold') , bd = 4 , text = numbers[i] ))
            button[i].grid(row = j , column = k , pady = 1)
            button[i]['command'] = lambda x = numbers[i] : calculations.entering_numbers(x)
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


    ############## Add , Subtract , Multiply , Divide ######################

    def hover_in_add(event):
        Add_button.config(background = 'gray78')
        Add_button.config(font=('arial', 21, 'bold'))

    def hover_out_add(event):
        Add_button.config(background = 'gray91')
        Add_button.config(font=('arial', 20, 'bold'))

    def hover_in_subtract(event):
        Subtract_button.config(background = 'gray78')
        Subtract_button.config(font=('arial', 21, 'bold'))

    def hover_out_subtract(event):
        Subtract_button.config(background = 'gray91')
        Subtract_button.config(font=('arial', 20, 'bold'))

    def hover_in_multiply(event):
        Multiply_button.config(background = 'gray78')
        Multiply_button.config(font=('arial', 21, 'bold'))

    def hover_out_multiply(event):
        Multiply_button.config(background = 'gray91')
        Multiply_button.config(font=('arial', 20, 'bold'))

    def hover_in_divide(event):
        Divide_button.config(background = 'gray78')
        Divide_button.config(font=('arial', 21, 'bold'))

    def hover_out_divide(event):
        Divide_button.config(background = 'gray91')
        Divide_button.config(font=('arial', 20, 'bold'))

    Add_button = Button(root, text='+', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                    bg="gray91" , activebackground = 'gray78' , command = lambda : calculations.operation('Add'))
    Add_button.grid(row=1, column=3, pady=1)
    Add_button.bind("<Enter>" , hover_in_add)
    Add_button.bind("<Leave>", hover_out_add)

    Subtract_button = Button(root, text='−', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                         bg="gray91" , activebackground = 'gray78' , command = lambda : calculations.operation('Subtract'))
    Subtract_button.grid(row=2, column=3,pady=1)
    Subtract_button.bind("<Enter>", hover_in_subtract)
    Subtract_button.bind("<Leave>", hover_out_subtract)

    Multiply_button = Button(root, text='x', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                         bg="gray91" , activebackground = 'gray78' , command = lambda : calculations.operation('Multiply'))
    Multiply_button.grid(row=3, column=3, pady=1)
    Multiply_button.bind("<Enter>", hover_in_multiply)
    Multiply_button.bind("<Leave>", hover_out_multiply)

    Divide_button = Button(root, text='÷', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                       bg="gray91" , activebackground = 'gray78' , command = lambda : calculations.operation('Divide'))
    Divide_button.grid(row=4, column=3, pady=1)
    Divide_button.bind("<Enter>", hover_in_divide)
    Divide_button.bind("<Leave>", hover_out_divide)



    ############## Other Buttons for Standard ######################

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

    def hover_in_squareroot(event):
        Sqareroot_button.config(background = 'gray78')
        Sqareroot_button.config(font=('arial', 21, 'bold'))

    def hover_out_squareroot(event):
        Sqareroot_button.config(background = 'gray91')
        Sqareroot_button.config(font=('arial', 20, 'bold'))


    Clear_last_button = Button(root, text='⌫', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                      bg="gray91" , activebackground = 'gray78' , command = calculations.remove_last)
    Clear_last_button.grid(row=1, column=1, pady=1)
    Clear_last_button.bind("<Enter>", hover_in_clear_last)
    Clear_last_button.bind("<Leave>", hover_out_clear_last)


    AllClear_button = Button(root, text=chr(67), width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                         bg="gray91" , activebackground = 'gray78' , command = calculations.clear_entry)
    AllClear_button.grid(row=1, column=0, pady=1)
    AllClear_button.bind("<Enter>", hover_in_all_clear)
    AllClear_button.bind("<Leave>", hover_out_all_clear)


    Sqareroot_button = Button(root, text='√¯', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                          bg="gray91" , activebackground = 'gray78' , command = calculations.squareroot)
    Sqareroot_button.grid(row=1, column=2, pady=1)
    Sqareroot_button.bind("<Enter>", hover_in_squareroot)
    Sqareroot_button.bind("<Leave>", hover_out_squareroot)


    ######################################################################################

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

    def hover_in_plus_minus(event):
        PlusMinus_button.config(background = 'gray78')
        PlusMinus_button.config(font=('arial', 21, 'bold'))

    def hover_out_plus_minus(event):
        PlusMinus_button.config(background = 'gray91')
        PlusMinus_button.config(font=('arial', 20, 'bold'))

    def hover_in_equal(event):
        Equal_button.config(background = 'SteelBlue2')
        Equal_button.config(font=('arial', 21, 'bold'))

    def hover_out_equal(event):
        Equal_button.config(background = 'SteelBlue1')
        Equal_button.config(font=('arial', 20, 'bold'))

    Zero_button = Button(root, text='0', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                     bg = 'white' , activebackground = 'gray78' , command = lambda: calculations.entering_numbers(0))
    Zero_button.grid(row=5, column=1, pady=1)
    Zero_button.bind("<Enter>", hover_in_zero)
    Zero_button.bind("<Leave>", hover_out_zero)


    Dot_button = Button(root, text='.', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                    bg="gray91" , activebackground = 'gray78', command = lambda: calculations.entering_numbers('.'))
    Dot_button.grid(row=5, column=0, pady=1)
    Dot_button.bind("<Enter>", hover_in_dot)
    Dot_button.bind("<Leave>", hover_out_dot)


    PlusMinus_button = Button(root, text=chr(177), width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                          bg="gray91" , activebackground = 'gray78' , command = calculations.plusminus)
    PlusMinus_button.grid(row=5, column=2, pady=1)
    PlusMinus_button.bind("<Enter>", hover_in_plus_minus)
    PlusMinus_button.bind("<Leave>", hover_out_plus_minus)


    Equal_button = Button(root, text='=', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                      bg="SteelBlue1" , activebackground = 'SteelBlue3' , command = calculations.equals_to)
    Equal_button.grid(row=5, column=3, pady=1)
    Equal_button.bind("<Enter>", hover_in_equal)
    Equal_button.bind("<Leave>", hover_out_equal)


    ################## SCIENTIFIC BUTTONS #####################################

    def hover_in_pi(event):
        Pi_button.config(background = 'gray78')
        Pi_button.config(font=('arial', 21, 'bold'))

    def hover_out_pi(event):
        Pi_button.config(background = 'gray91')
        Pi_button.config(font=('arial', 20, 'bold'))

    def hover_in_factiorial(event):
        factiorial_button.config(background = 'gray78')
        factiorial_button.config(font=('arial', 21, 'bold'))

    def hover_out_factiorial(event):
        factiorial_button.config(background = 'gray91')
        factiorial_button.config(font=('arial', 20, 'bold'))

    def hover_in_sin(event):
        Sin_button.config(background = 'gray78')
        Sin_button.config(font=('arial', 21, 'bold'))

    def hover_out_sin(event):
        Sin_button.config(background = 'gray91')
        Sin_button.config(font=('arial', 20, 'bold'))

    def hover_in_cos(event):
        Cos_button.config(background = 'gray78')
        Cos_button.config(font=('arial', 21, 'bold'))

    def hover_out_cos(event):
        Cos_button.config(background = 'gray91')
        Cos_button.config(font=('arial', 20, 'bold'))

    def hover_in_tan(event):
        Tan_button.config(background = 'gray78')
        Tan_button.config(font=('arial', 21, 'bold'))

    def hover_out_tan(event):
        Tan_button.config(background = 'gray91')
        Tan_button.config(font=('arial', 20, 'bold'))

    Pi_button = Button(root, text='π', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                   bg="gray91" , activebackground = 'gray78' , command = calculations.pi)
    Pi_button.grid(row=1, column=4, pady=1  , padx = 3)
    Pi_button.bind("<Enter>", hover_in_pi)
    Pi_button.bind("<Leave>", hover_out_pi)

    factiorial_button = Button(root, text='n!', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                    bg="gray91" , activebackground = 'gray78' , command = calculations.factorial)
    factiorial_button.grid(row=2, column=4, pady=1)
    factiorial_button.bind("<Enter>", hover_in_factiorial)
    factiorial_button.bind("<Leave>", hover_out_factiorial)

    Sin_button = Button(root, text='sin', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                    bg="gray91" , activebackground = 'gray78', command = calculations.sin)
    Sin_button.grid(row=3, column=4, pady=1)
    Sin_button.bind("<Enter>", hover_in_sin)
    Sin_button.bind("<Leave>", hover_out_sin)

    Cos_button = Button(root, text='cos', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                    bg="gray91" , activebackground = 'gray78' , command = calculations.cos)
    Cos_button.grid(row=4, column=4, pady=1)
    Cos_button.bind("<Enter>", hover_in_cos)
    Cos_button.bind("<Leave>", hover_out_cos)

    Tan_button = Button(root, text='tan', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                    bg="gray91" , activebackground = 'gray78' , command = calculations.tan)
    Tan_button.grid(row=5, column=4, pady=1)
    Tan_button.bind("<Enter>", hover_in_tan)
    Tan_button.bind("<Leave>", hover_out_tan)

    #################################################################

    def hover_in_PowerOf2(event):
        PowerOf2_button.config(background = 'gray78')
        PowerOf2_button.config(font=('arial', 21, 'bold'))

    def hover_out_PowerOf2(event):
        PowerOf2_button.config(background = 'gray91')
        PowerOf2_button.config(font=('arial', 20, 'bold'))

    def hover_in_PowerOf3(event):
        PowerOf3_button.config(background = 'gray78')
        PowerOf3_button.config(font=('arial', 21, 'bold'))

    def hover_out_PowerOf3(event):
        PowerOf3_button.config(background = 'gray91')
        PowerOf3_button.config(font=('arial', 20, 'bold'))

    def hover_in_dividebyX(event):
        DividedByX_button.config(background = 'gray78')
        DividedByX_button.config(font=('arial', 21, 'bold'))

    def hover_out_dividebyX(event):
        DividedByX_button.config(background = 'gray91')
        DividedByX_button.config(font=('arial', 20, 'bold'))

    def hover_in_e(event):
        e_button.config(background = 'gray78')
        e_button.config(font=('arial', 21, 'bold'))

    def hover_out_e(event):
        e_button.config(background = 'gray91')
        e_button.config(font=('arial', 20, 'bold'))

    def hover_in_log(event):
        log_button.config(background = 'gray78')
        log_button.config(font=('arial', 21, 'bold'))

    def hover_out_log(event):
        log_button.config(background = 'gray91')
        log_button.config(font=('arial', 20, 'bold'))


    PowerOf2_button = Button(root, text='x²', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                         bg="gray91" , activebackground = 'gray78' , command = calculations.X2)
    PowerOf2_button.grid(row=1, column=5, pady=1 , padx = 3)
    PowerOf2_button.bind("<Enter>", hover_in_PowerOf2)
    PowerOf2_button.bind("<Leave>", hover_out_PowerOf2)

    PowerOf3_button = Button(root, text='x³', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                         bg="gray91" , activebackground = 'gray78' , command = calculations.X3)
    PowerOf3_button.grid(row=2, column=5, pady=1)
    PowerOf3_button.bind("<Enter>", hover_in_PowerOf3)
    PowerOf3_button.bind("<Leave>", hover_out_PowerOf3)

    DividedByX_button = Button(root, text='1/x', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                            bg="gray91" , activebackground = 'gray78' , command = calculations.DevideByX)
    DividedByX_button.grid(row=3, column=5, pady=1)
    DividedByX_button.bind("<Enter>", hover_in_dividebyX)
    DividedByX_button.bind("<Leave>", hover_out_dividebyX)

    e_button = Button(root, text='e', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                  bg="gray91" , activebackground = 'gray78' , command = calculations.e)
    e_button.grid(row=4, column=5, pady=1)
    e_button.bind("<Enter>", hover_in_e)
    e_button.bind("<Leave>", hover_out_e)

    log_button = Button(root, text='log', width=6, height=2, font=('arial', 20, 'bold'), bd=4,
                    bg="gray91" , activebackground = 'gray78' , command = calculations.log)
    log_button.grid(row=5, column=5, pady=1)
    log_button.bind("<Enter>", hover_in_log)
    log_button.bind("<Leave>", hover_out_log)

    ############## Displaying Scientific
    nameDisplay = Label(root, text="Scientific", bg = 'gray91',  font=('arial', 32, 'bold'), justify=CENTER)
    nameDisplay.grid(row=0, column=4, columnspan=4)

    ########## File menu #################################

    def standard():
        root.resizable(0 , 0)
        root.geometry('489x546+305+180')

    def scientific():
        root.resizable(0 , 0)
        root.geometry('732x546+305+180')

    menubar = Menu(root)

    filemenu = Menu(menubar , tearoff = 0)
    menubar.add_cascade(label = 'File' , menu = filemenu)
    filemenu.add_command(label = 'Standard' , command = standard)
    filemenu.add_command(label = 'Scientific' , command = scientific)
    filemenu.add_separator()
    filemenu.add_command(label = 'Exit' , command = root.destroy)

    root.config(menu = menubar)

    root.mainloop()