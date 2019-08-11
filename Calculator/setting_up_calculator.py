from tkinter import *
import numpy as np



class RefiEval():
    def __init__(self):
        window = Tk()
        window.title("Refinance Evaluator")

        Label(window, text="Loan Amount:", font='Helvetica 16').grid(row=1, column =1, sticky= W) #Sticky to West
        Label(window, text="Interest Rate:", font='Helvetica 16').grid(row=2, column =1, sticky= W) #Sticky to West
        Label(window, text="Term (years):", font='Helvetica 16').grid(row=3, column =1, sticky= W) #Sticky to West
        Label(window, text=None).grid(row=4, column =1, sticky= W) #Sticky to West

        #outputs
        Label(window, text="Payment:", font='Helvetica 16').grid(row=5, column=1, sticky=W)
        Label(window, text="Total Payements:", font='Helvetica 16').grid(row=6, column=1, sticky=W)

        #variables to store inputs
        self.pv = StringVar()
        self.interest_rate = StringVar()
        self.term = StringVar()

        #Variables payment output
        self.pmt = StringVar()
        self.total = StringVar()

        #declare entry widget
        Entry(window, textvariable = self.pv,
              justify=RIGHT).grid(row=1, column =2, padx = (0,5))
        Entry(window, textvariable = self.interest_rate,
              justify=RIGHT).grid(row=2,column =2, padx = (0,5))
        Entry(window, textvariable = self.term,
              justify=RIGHT).grid(row=3, column =2, padx = (0,5))

        Label(window, textvariable=self.pmt,
              font = "Helvetica 12 bold",
              justify=RIGHT).grid(row=5, column=2, sticky = E)

        Label(window, textvariable=self.total,
              font = "Helvetica 12 bold",
              justify=RIGHT).grid(row=6, column=2, sticky = E)

        Button(window, text="Calculate Payment",
               command = self.calcPayment,
               font="Helvetica 14", bg="green").grid(row=7, column=2, padx= (100,5), pady=5)

        #refinance variables
        self.old_pmt = StringVar()
        self.timeleft = StringVar()
        self.refi_cost = StringVar()

        Label(window, text = "Current Payment",
              font="helvetica 16").grid(row=8, column=1)
        Label(window, text = "Time left",
              font="helvetica 16").grid(row=9, column=1)
        Label(window, text = "Refi Cost",
              font="helvetica 16").grid(row=10, column=1)

        # evaluation entries
        Entry(window, textvariable=self.old_pmt,
              justify=RIGHT).grid(row=8, column=2, padx= (0,5))
        Entry(window, textvariable=self.timeleft,
              justify=RIGHT).grid(row=9, column=2, padx= (0,5))
        Entry(window, textvariable=self.refi_cost,
              justify=RIGHT).grid(row=10, column=2, padx= (0,5))

        #outputs variable for evaluation
        self.monthly_saving = StringVar()
        self.payback = StringVar()
        self.overall_savings = StringVar()

        Label(window, text = "Monthly Saving",
              font="helvetica 16").grid(row=11, column=1)
        Label(window, text = "Payback",
              font="helvetica 16").grid(row=12, column=1)
        Label(window, text = "Overall Savings",
              font="helvetica 16").grid(row=13, column=1)

        Button(window, text="Eval Refi",
               font="Helvetica 14", command=self.evalRefi).grid(row=14, column=2, padx= (100,5), pady=5)

        window.mainloop()

    def calcPayment(self):
        pv = float(self.pv.get())
        rate = float(self.interest_rate.get())
        term = int(self.term.get())

        pmt = np.pmt(rate / 1200, term * 12 , -pv, 0)
        total = pmt * 12 * term

        self.pmt.set("PLN" + format(pmt, "5,.2f"))
        self.total.set("PLN" + format(total, "8,.2f"))

    def evalRefi(self):
        pass



RefiEval()