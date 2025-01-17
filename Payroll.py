from tkinter import *

    
PayrollWin=Tk()
PayrollWin.title("Payroll")
PayrollWin.geometry("300x500")

GrossPay=IntVar()
Tax=DoubleVar()
Tax.set('0.0')
NatIns=DoubleVar()
NatIns.set('0.0')
Pension=DoubleVar()
Pension.set('0.0')
Deducts=DoubleVar()
Deducts.set('0.0')
NetPay=DoubleVar()
NetPay.set('0.0')
Repayment=DoubleVar()
Repayment.set('0.0')
NetLoanD=DoubleVar()
NetLoanD.set('0.0')

def CalcPay():

    Gross = float(GrossPay.get())
    Tax.set(Gross * 0.22)       # Tax value adjusted from 20% (0.2) to 22% (0.22)
    NatIns.set(Gross * 0.085)   # National Insurance value adjusted from 14% (0.14) to 8.5% (0.085)
    Pension.set(Gross * 0.08)
    Deducts.set(Gross * 0.2 + Gross * 0.14 + Gross * 0.08)
    NetPay.set(Gross - (Gross * 0.2 + Gross * 0.14 + Gross * 0.08))
    
def CalcLoan():
    Gross = float(GrossPay.get())
    Repayment.set(Gross * 0.1)
    NetPay.set(Gross - (Gross * 0.2 + Gross * 0.14 + Gross * 0.08))
    NetLoanD.set(NetPay.get() - Repayment.get())
        
   
GrossPayLabel=Label(PayrollWin, text="Gross Pay").grid(row=3, column=0, sticky=W)
GrossPayEntry= Entry(PayrollWin, textvariable=GrossPay)
GrossPayEntry.grid(row=3,column=1)


b1= Button(PayrollWin, text=" Calculate ", command=CalcPay).grid(row=4)
 

TaxLabelText=Label(PayrollWin, text="Tax: ").grid(row=5, column=0, sticky=W)
TaxLabelValue=Label(PayrollWin, textvariable=Tax).grid(row=5, column=1, sticky=W)
NatInsLabelText =Label(PayrollWin, text="National Insurance: ").grid(row=6, column=0, sticky=W)
NatInsLabelValue=Label(PayrollWin, textvariable=NatIns).grid(row=6, column=1, sticky=W)
PensionLabeltext=Label(PayrollWin, text="Pension Contribution: " ).grid(row=7, column=0, sticky=W)
PensionLabelValue=Label(PayrollWin, textvariable=Pension).grid(row=7, column=1, sticky=W)
DeductsLabelText=Label(PayrollWin, text="Deductions: " ).grid(row=8, column=0, sticky=W)
DeductsLabelValue=Label(PayrollWin, textvariable=Deducts).grid(row=8, column=1, sticky=W)
NetPayLabelText=Label(PayrollWin, text="Net Pay: ").grid(row=9, column=0, sticky=W)
NetPayLabelValue=Label(PayrollWin, textvariable=NetPay).grid(row=9, column=1, sticky=W)

b2= Button(PayrollWin, text=" Student Loan - Calculate ", command=CalcLoan).grid(row=12)

TaxLabelText=Label(PayrollWin, text="Student loan repayment: ").grid(row=10, column=0, sticky=W)
TaxLabelValue=Label(PayrollWin, textvariable=Repayment).grid(row=10, column=1, sticky=W)
NetPayLabelText=Label(PayrollWin, text="Net Pay - Loan deducted: ").grid(row=11, column=0, sticky=W)
NetPayLabelValue=Label(PayrollWin, textvariable=NetLoanD).grid(row=11, column=1, sticky=W)


b3= Button(PayrollWin, text=" Back ", command=PayrollWin.destroy).grid(row=13)
   
    
PayrollWin.mainloop()
