# Copyright (c) 2023, madhu and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class TrainStation(Document):

	def validate(self):
		self.validate_departure_station()
		self.validate_arrival_station()


	def validate_departure_station(self):
		if not self.departure_station:
			frappe.throw(("Departure Station is required."))

	def validate_arrival_station(self):
		if not self.arrival_station:
			frappe.throw(("Arrival Station is required."))

		if self.arrival_station == self.departure_station:
			frappe.throw(("arrival station cannot be the same as departure station."))
	pass
