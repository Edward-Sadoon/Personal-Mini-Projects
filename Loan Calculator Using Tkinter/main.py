from tkinter import *


class LoanCalculator:

    def __init__(self):
        # create a window
        window = Tk()
        # set the title
        window.title('Loan Calculator')
        window.geometry('275x150+50+50')

        # create all the labels
        l1 = Label(window, text='Annual Interest Rate')
        l1.grid(row=1, column=1, sticky=W)

        l2 = Label(window, text='Number of Years')
        l2.grid(row=2, column=1, sticky=W)

        l3 = Label(window, text='Loan Amount')
        l3.grid(row=3, column=1, sticky=W)

        l4 = Label(window, text='Monthly Payment')
        l4.grid(row=4, column=1, sticky=W)

        l5 = Label(window, text='Total Payment')
        l5.grid(row=5, column=1, sticky=W)

        # create the user entry boxes
        self.annual_interest_rate_var = StringVar()
        e1 = Entry(
            window, textvariable=self.annual_interest_rate_var, justify=RIGHT)
        e1.grid(row=1, column=2)

        self.number_of_years_var = StringVar()
        e2 = Entry(window, textvariable=self.number_of_years_var, justify=RIGHT)
        e2.grid(row=2, column=2)

        self.loan_amount_var = StringVar()
        e3 = Entry(window, textvariable=self.loan_amount_var, justify=RIGHT)
        e3.grid(row=3, column=2)

        # display the calculated values
        self.monthly_payment_var = StringVar()
        v1 = Label(window, textvariable=self.monthly_payment_var)
        v1.grid(row=4, column=2, sticky=E)

        self.total_payment_var = StringVar()
        v2 = Label(window, textvariable=self.total_payment_var)
        v2.grid(row=5, column=2, sticky=E)

        # create the execution button
        button = Button(window, text='Calculate Payment',
                        command=self.calculatePayment)
        button.grid(row=6, column=2, sticky=E)

        # create loop to keep window open
        window.mainloop()

    def calculatePayment(self):
        # calculate the monthly payment
        monthly_payment = self.getMonthlyPayment(float(self.loan_amount_var.get()),
                                                 float(
            self.annual_interest_rate_var.get()) / 1200,
            int(self.number_of_years_var.get()))

        self.monthly_payment_var.set(format(monthly_payment, '10.2f'))
        total_payment = float(self.monthly_payment_var.get()) * \
            12 * int(self.number_of_years_var.get())
        self.total_payment_var.set(format(total_payment, '10.2f'))

    def getMonthlyPayment(self, loan_amount, monthly_interest_rate, number_of_years):
        monthly_payment = loan_amount * monthly_interest_rate / \
            (1 - 1 / (1 + monthly_interest_rate) ** (number_of_years * 12))
        return monthly_payment
        root = Tk()  # create the widget


# call the class to run the program
LoanCalculator()
