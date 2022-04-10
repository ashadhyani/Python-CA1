class Employee:
        def __init__(self, StaffID, LastName, FirstName, RegHours, HourlyRate, OTMultiple, TaxCredit, StandardBand):
            self.StaffID=StaffID
            self.LastName=LastName
            self.FirstName=FirstName
            self.RegHours=RegHours
            self.HourlyRate=HourlyRate
            self.OTMultiple=OTMultiple
            self.TaxCredit=TaxCredit
            self.StandardBand=StandardBand
        # create function for create a compute payment
        def computePayment(self, count_no, date_value):
            over_time_rate=self.HourlyRate * self.OTMultiple
            Regular_Pay=self.RegHours * self.HourlyRate
            Overtime_Pay=(count_no-self.RegHours)*over_time_rate
            Gross_Pay=Regular_Pay+Overtime_Pay
            Standard_Rate_Pay=self.StandardBand
            Higher_Rate_Pay=Gross_Pay-Standard_Rate_Pay
            Higher_Tax=0
            std_rate=round(Gross_Pay*20/100)
            if Gross_Pay>self.StandardBand:
                Higher_Tax=(Higher_Rate_Pay*40)/100
            else:
                Higher_Tax=(Higher_Rate_Pay*20)/100
            prsi=(Gross_Pay*4.0)/100
            total_txt=std_rate+Higher_Tax
            Net_Tax=(std_rate-self.TaxCredit)+Higher_Tax
            Net_Deductions=prsi+Net_Tax
            Net_Deductions=Gross_Pay-Net_Deductions
            return_val={
                'name': self.LastName +' '+ self.FirstName, 
                'Date':date_value, 
                'Regular Hours Worked':self.RegHours,
                'Overtime Hours Worked':self.OTMultiple,
                'Regular Rate':self.HourlyRate,
                'Overtime Rate':over_time_rate, 
                'Regular Pay':Regular_Pay,
                'Overtime Pay':Overtime_Pay,
                'Gross Pay':Gross_Pay, 
                'Standard Rate Pay':Standard_Rate_Pay,
                'Higher Rate Pay':Higher_Rate_Pay, 
                'Standard Tax':std_rate,
                'Higher Tax':Higher_Tax,
                'Total Tax':total_txt,
                'Tax Credit':self.TaxCredit, 
                'Net Tax':Net_Tax, 
                'PRSI': prsi,
                'Net Deductions':Net_Deductions, 
                'Net Pay': Net_Deductions
                }

            return return_val

emp = Employee(12345,'Green','Joe', 37, 16, 1.5, 72, 710)
return_value= emp.computePayment(42, '31/10/2021')
print(return_value)