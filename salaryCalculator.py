"""
Program: salaryCalculator.py
Chapter 8 practice project
1/25/2024

**NOTE: The module breezypythongui.py MUST be in the same directory as this file for the app to run correctly!!!

GUI-based version of the Salary Calculator app which calculates an employee's weekky earnings.
"""

from breezypythongui import EasyFrame
from tkinter.font import Font
# Other imports go here

#Class header (class name will change project to project)
class SalaryCalculator(EasyFrame):

	# Defintion of our classes' constructor method
	def __init__(self):
		# Call to the Easy Frame class constructor
		EasyFrame.__init__(self, title = "Salary Calculator", width = 420, height = 300, resizable = False, background = "seashell3")

		# Add various components to the window 
		self.addLabel(text = "Salary Calculator", row = 0, column = 0, sticky = "NSEW", columnspan = 2, background = "seashell3", foreground = "seashell4", font = Font(family = "Elephant", size = 20))


		# Lable and entry field for the input
		self.addLabel(text = "Hourly Wage", row = 1, column = 0, background = "seashell3", foreground = "seashell4", font = "Georgia")
		self.addLabel(text = "No. of Hours Worked", row = 2, column = 0, background = "seashell3", foreground = "seashell4", font = "Georgia")
		self.wageField = self.addFloatField(value = 0.0, row = 1, column = 1)
		self.hoursField = self.addIntegerField(value = 0, row = 2, column = 1)

		# Label and entry field for the output 
		self.hoursField.bind ("<Return>", lambda event: self.compute())
		
		self.computeButton = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)
		self.computeButton["background"] = "seashell4"
		self.computeButton["foreground"] = "seashell2"
		self.computeButton["width"] = 8
		self.computeButton["height"] = 1
		self.computeButton["font"] = "elephant"
		self.salaryLabel = self.addLabel(text = "The employee's salary is: ", row = 4, column = 0, columnspan = 2, background = "seashell3", foreground = "seashell4", font = "Georgia")

	def compute(self):
		hourly_wage = self.wageField.getNumber()
		hours_worked = self.hoursField.getNumber()

		# Calcultion (hourly wage * hours worked)
		salary = hourly_wage * hours_worked

		# Display result in label 
		self.salaryLabel["text"] = f"The emplpoyees's salary is: $ {salary: .2f}"

# Global definition of the main() method 
def main():
	# Instantiate an object from the class into mainloop()
	SalaryCalculator().mainloop()

# Global call to main() for program entry 
if __name__ == '__main__':
	main()