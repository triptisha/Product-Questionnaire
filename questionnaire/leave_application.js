frappe.ui.form.on("Leave Application",{
	validate:function(frm){
		role = frappe.user_role
		console.log("__________________",frm.total_leave_days)
		console.log("__________________",role)

	},


});
