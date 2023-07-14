# Copyright (c) 2023, madhu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class TrainSchedule(Document):

	# Validation Hooks
	def validate(self):
		self.validate_departure_and_arrival()
		self.validate_departure_time()
		self.validate_arrival_time()
		self.validate_train_stations()

	def validate_departure_and_arrival(self):
		if self.departure_station == self.arrival_station:
			frappe.throw(("Departure station cannot be the same as arrival station."))

	def validate_departure_time(self):
		if self.departure_time >= self.arrival_time:
			frappe.throw(("Departure time should be earlier than arrival time."))

	def validate_arrival_time(self):
		if self.arrival_time <= self.departure_time:
			frappe.throw(("Arrival time should be later than departure time."))
	

	def validate_train_stations(self):
		if self.departure_station and not frappe.db.exists("Train Station", self.departure_station):
			frappe.throw(("Invalid Departure Station."))

		if self.arrival_station and not frappe.db.exists("Train Station", self.arrival_station):
			frappe.throw(("Invalid Arrival Station."))
	pass
