from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

def validate(doc,method=None):
	doc.total = doc.first + doc.second
	print "_________________",doc
	print "_________________",doc.name
	print "tripti"