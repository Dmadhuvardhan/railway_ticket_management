# Copyright (c) 2023, madhu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Passenger(Document):
#Validation Hooks
	def validate(self):
		self.validate_age()
		self.validate_gender()
		self.validate_contact_number()
		self.validate_email_address()
		self.validate_passenger_name()

	def validate_passenger_name(self):
		if not self.passenger_name:
			frappe.throw(("Passenger Name is required."))
			
	def validate_age(self):
		if not self.age:
			frappe.throw(("Age is required."))
		if self.age < 0:
			frappe.throw(("Age cannot be negative."))

	def validate_gender(self):
		if not self.gender:
			frappe.throw(("Gender is required."))


	def validate_contact_number(self):
		if not self.contact_number:
			frappe.throw(("Contact Number is required."))
		if len(self.contact_number) < 10:
			frappe.throw(("Contact Number should be at least 10 digits long."))

			
	def validate_email_address(self):
		if not self.email_address:
			frappe.throw(("Email Address is required."))
		if not frappe.utils.validate_email_address(self.email_address):
			frappe.throw(("Invalid Email Address."))	


# Logic
	def create_passenger(passenger_name, age, gender, contact_number, email_address):
		passenger = frappe.new_doc("Passenger")
		passenger.passenger_name = passenger_name
		passenger.age = age
		passenger.gender = gender
		passenger.contact_number = contact_number
		passenger.email_address = email_address
		passenger.save()
		frappe.msgprint("Passenger created successfully!")

# API method to fetch passenger data
	@frappe.whitelist()
	def get_passenger_data():
		passenger = frappe.get_doc('Passenger',passenger)
		if passenger:
			return {
				'passenger_name': passenger.passenger_name,
				'age': passenger.age,
				'gender': passenger.gender,
				'contact_number': passenger.contact_number,
				'email_address': passenger.email_address
			}
		else:
			frappe.throw('Passenger data not found for the current user.')




	
