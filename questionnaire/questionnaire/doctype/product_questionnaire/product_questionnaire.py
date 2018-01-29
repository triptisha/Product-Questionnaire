# -*- coding: utf-8 -*-
# Copyright (c) 2018, trip and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ProductQuestionnaire(Document):

	def on_submit(doc,method=None):
		if doc.product_type == "Rack":
			rack_doc = frappe.new_doc("Rack")
			rack_doc.rack_types = doc.rack_types
			rack_doc.racks_required = doc.racks_required
			rack_doc.physical_dimensions = doc.physical_dimensions
			rack_doc.roller_tracks = doc.roller_track
			rack_doc.casters_required = doc.casters_required
			rack_doc.levelers = doc.levelers
			rack_doc.powder_coated = doc.powder_coated
			rack_doc.cable_manager = doc.cable_manager
			rack_doc.sliding_tray = doc.sliding_tray
			rack_doc.fans = doc.fans
			rack_doc.blanking_plate = doc.blanking_plate
			rack_doc.door = doc.door
			rack_doc.require_pdu = doc.require_pdu
			rack_doc.parent = doc.name
			rack_doc.parentfield =doc.product_type
			rack_doc.save() 
			rack_email_template(doc)




		if doc.product_type == "Server":
			server_doc = frappe.new_doc("Server")
			server_doc.os_vendor = doc.os_vendor
			server_doc.virtualization = doc.virtualization
			server_doc.server_type = doc.server_type
			server_doc.application = doc.application
			server_doc.network_connectivity = doc.network_connectivity
			server_doc.disk_types = doc.disk_types
			server_doc.storage_type = doc.storage_type
			server_doc.usable_size = doc.usable_size
			server_doc.cache = doc.cache
			server_doc.warranty = doc.warranty
			server_doc.no_of_server = doc.no_of_server
			server_doc.budget = doc.budget
			server_doc.parent = doc.name
			server_doc.parentfield = doc.product_type
			server_doc.save()
			server_email_template(doc)
         




		if doc.product_type == "PDU":
			pdu_doc = frappe.new_doc("PDU")
			pdu_doc.pdu = doc.pdu
			pdu_doc.single_dual_pdu = doc.single_dual_pdu
			pdu_doc.voltage_current = doc.voltage_current
			pdu_doc.output_power_socket = doc.output_power_socket
			pdu_doc.input_power_plug = doc.input_power_plug
			pdu_doc.c13_c19 = doc.c13_c19
			pdu_doc.input_power_cord = doc.input_power_cord
			pdu_doc.parent = doc.name
			pdu_doc.parentfield = doc.product_type
			pdu_doc.save()
			pdu_email_template(doc)    
		




def rack_email_template(doc,method=None):
	user_email = doc.email_id
	try:
		frappe.sendmail(
			#recipients=["david.newman@emiuae.ae","rachitsaharia@emiuae.ae"],
			recipients=[user_email],
			expose_recipients="header",
			# sender=frappe.session.user,
			# reply_to=None,
			subject="Rack Questions & Answers",
			content=None,
			reference_doctype=None,
			reference_name=None,
			message = frappe.render_template("templates/email/rack_email_template.html", {"rack_types":doc.rack_types,"racks_required":doc.racks_required,"physical_dimensions":doc.physical_dimensions,"roller_track":doc.roller_track,"casters_required":doc.casters_required,"levelers":doc.levelers,"powder_coated":doc.powder_coated,"cable_manager":doc.cable_manager,"sliding_tray":doc.sliding_tray,"fans":doc.fans,"blanking_plate":doc.blanking_plate,"door":doc.door,"require_pdu":doc.require_pdu}),
			message_id=None,
			unsubscribe_message=None,
			delayed=False,
			communication=None
		)
	except Exception,e:
		frappe.throw(("Mail has not been Sent. Kindly Contact to Administrator"))





def server_email_template(doc,method=None):
	user_email = doc.email_id
	try:
		frappe.sendmail(
			#recipients=["david.newman@emiuae.ae","rachitsaharia@emiuae.ae"],
			recipients=[user_email],
			expose_recipients="header",
			# sender=frappe.session.user,
			# reply_to=None,
			subject="Server Questions & Answers",
			content=None,
			reference_doctype=None,
			reference_name=None,
			message = frappe.render_template("templates/email/server_email_template.html", {"os_vendor":doc.os_vendor,"virtualization":doc.virtualization,"server_type":doc.server_type,"application":doc.application,"network_connectivity":doc.network_connectivity,"disk_types":doc.disk_types,"storage_type":doc.storage_type,"usable_size":doc.usable_size,"cache":doc.cache,"warranty":doc.warranty,"no_of_server":doc.no_of_server,"budget":doc.budget}),
			message_id=None,
			unsubscribe_message=None,
			delayed=False,
			communication=None
		)
	except Exception,e:
		frappe.throw(("Mail has not been Sent. Kindly Contact to Administrator"))







def pdu_email_template(doc,method=None):
	user_email = doc.email_id
	try:
		frappe.sendmail(
			#recipients=["david.newman@emiuae.ae","rachitsaharia@emiuae.ae"],
			recipients=[user_email],
			expose_recipients="header",
			# sender=frappe.session.user,
			# reply_to=None,
			subject="PDU Questions & Answers",
			content=None,
			reference_doctype=None,
			reference_name=None,
			message = frappe.render_template("templates/email/pdu_email_template.html", {"pdu":doc.pdu,"single_dual_pdu":doc.single_dual_pdu,"voltage_current":doc.voltage_current,"output_power_socket":doc.output_power_socket,"input_power_plug":doc.input_power_plug,"c13_c19":doc.c13_c19,"input_power_cord":doc.input_power_cord}),
			message_id=None,
			unsubscribe_message=None,
			delayed=False,
			communication=None
		)
	except Exception,e:
		frappe.throw(("Mail has not been Sent. Kindly Contact to Administrator"))

