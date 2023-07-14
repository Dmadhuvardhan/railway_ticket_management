# Copyright (c) 2023, madhu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Ticket(Document):

#Validation hooks
	def validate(self):
		self.validate_passenger_link()
		self.validate_train_link()
		self.validate_booking_date()
		self.generate_ticket_id()
		self.on_submit()



	
	def validate_passenger_link(self):
		if self.passenger:
			passenger = frappe.get_doc("Passenger", self.passenger)

	def generate_ticket_id(self):
		if not self.ticket_id:
			self.ticket_id = frappe.generate_hash(length=10)  # Auto-generate ticket ID


	def validate_train_link(self):
		if self.train:
			train = frappe.get_doc("Train", self.train)
			if not train:
				frappe.throw(("Invalid train selected."))
		else:
			frappe.throw(("Train is required."))

	def validate_booking_date(self):
		if self.booking_date and self.booking_date < frappe.utils.nowdate():
			frappe.throw(("Booking date cannot be in the past."))

	def on_submit(self):
		#super(Ticket, self).on_submit()
		train = frappe.get_doc("Train", self.train)
		if train:
			train.available_seats -= 1
			train.save()
			frappe.msgprint("Ticket submitted successfully. Available seats updated.")


    
#logic

	def book_ticket(passenger_name, train_name, seat_number, booking_date):
		train = frappe.get_doc("Train", train_name)
		if train.available_seats > 0:
			ticket = frappe.new_doc("Ticket")
			ticket.passenger = passenger_name
			ticket.train = train_name
			ticket.seat_number = seat_number
			ticket.ticket_id = frappe.generate_hash(length=10)  # Auto-generate ticket ID
			ticket.booking_date = booking_date
			ticket.insert()
		else:
			frappe.throw("No seats available for the selected train.")
			
			# Update the available seats count in the Train document
			#train.available_seats -= 1
			#train.save()
			#frappe.msgprint("Ticket booked successfully!")
		#else:
			#frappe.throw("No seats available for the selected train.")
		

	@staticmethod
	def cancel_ticket(ticket_id):
		ticket = frappe.get_doc("Ticket", ticket_id)
		train = frappe.get_doc("Train", ticket.train)
		# Delete the Ticket document
		frappe.delete_doc("Ticket", ticket_id)
		# Update the available seats count in the Train document
		train.available_seats += 1
		train.save()
		return "Ticket cancelled successfully."
	




