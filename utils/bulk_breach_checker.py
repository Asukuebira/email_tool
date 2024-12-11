
def check_breaches(emails):
    breached_emails = []
    for email in emails.split(","):
        if "breached" in email:
            breached_emails.append(email)
    return {"breached": breached_emails}
