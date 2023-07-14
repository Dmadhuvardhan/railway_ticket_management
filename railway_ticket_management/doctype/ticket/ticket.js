// Copyright (c) 2023, madhu and contributors
// For license information, please see license.txt

frappe.ui.form.on('Ticket', {
    onload: function(frm) {
        frappe.call({
            method: 'railway_ticket_management.railway_ticket_management.doctype.passenger.passenger.get_passenger_data',
            callback: function(response) {
                var data = response.message;

                // Update the passenger field in the ticket form
                frm.set_value('passenger', data.name);
                frm.refresh_field('passenger');
            }
        });
    }
});









