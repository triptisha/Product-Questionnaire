from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

def validate(doc,method=None):
	doc.total = doc.first + doc.second
	print "tripti"