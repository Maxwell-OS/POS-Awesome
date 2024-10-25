import frappe

def extract_token_number(doc, method):
    # Split the document name by '-' and extract the last part
    parts = doc.name.split('-')
    
    # Check if there are parts and extract the token after the last dash
    if parts:
        token = parts[-1].strip()  # Remove any unwanted spaces
        
        # Set the token value to the custom field `custom_token_no`
        doc.custom_token_no = token
        
        # Save the token number directly in the database to avoid triggering further events
        frappe.db.set_value("Sales Invoice", doc.name, "custom_token_no", token)

