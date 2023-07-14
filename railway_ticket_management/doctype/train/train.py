# Copyright (c) 2023, madhu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Train(Document):
#Validation Hooks
	def validate(self):
		self.validate_available_seats()
		self.validate_fare()




	def validate_available_seats(self):
		if self.available_seats < 0:
			frappe.throw("Available Seats must be a positive value.")

	def validate_fare(self):
		if self.fare <= 0:
			frappe.throw("Fare must be a positive value.")
	
	


    # logic
	def check_seat_availability(train_name):
		train = frappe.get_doc("Train", train_name)
		return train.available_seats
		pass
	def calculate_fare(train_name):
		train = frappe.get_doc("Train", train_name)
		return train.fare
	
