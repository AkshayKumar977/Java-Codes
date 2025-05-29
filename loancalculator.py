from tkinter import *
class LoanCalculator:
    def __init__(self):
        window = Tk()
        window.title("Loan Calculator")
        Label(window,text = "Annual Interest Rate: ").grid(row=1,column = 1,sticky = W)
        Label(window,text = "Number of Years: ").grid(row = 2,column = 1,sticky = W)
        Label(window,text = "Loan Amount: ").grid(row = 3,column = 1,sticky = W)
        Label(window,text = "Monthly Payment: ").grid(row = 4,column = 1,sticky = W)
        Label(window,text = "Total Payment: ").grid(row = 5,column = 1,sticky = W)
        self.annualInterestRateVar = StringVar()
        Entry(window,textvariable = self.annualInterestRateVar,justify = RIGHT).grid(row = 1,column = 2)
        self.numberofYears = StringVar()
        Entry(window,textvariable = self.numberofYears,justify = RIGHT).grid(row=2,column=2)
        self.loanamount = StringVar()
        Entry(window,textvariable = self.loanamount,justify=RIGHT).grid(row=3,column= 2)
        self.monthlypayment = StringVar()
        lblmonthlypayment = Label(window,textvariable = self.monthlypayment).grid(row=4,column = 2,sticky = E)
        self.totalpayment = StringVar()
        lblTotalPayment = Label(window,textvariable = self.totalpayment).grid(row=5,column = 2,sticky = E)
        btComputebutton = Button(window,text = "Compute Payment",command = self.computepayment).grid(row=6,column=2,sticky = E)
        window.mainloop()
    def computepayment(self):
        monthlypayment = self.getMonthlypayment(
            float(self.loanamount.get()),
            float(self.annualInterestRateVar.get())/1200,
            int(self.numberofYears.get()))
        self.monthlypayment.set(format(monthlypayment,"10.2f"))
        totalpayment = float(self.monthlypayment.get()) *12 * int(self.numberofYears.get())
        self.totalpayment.set(format(totalpayment,"10.2f"))
    def getMonthlypayment(self,loanamount,monthlyinterestRate,numberofYears):
        monthlypayment = loanamount * monthlyinterestRate / (1-1/(1+monthlyinterestRate)**(numberofYears*12))
        return monthlypayment
LoanCalculator()