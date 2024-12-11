
def perform_osint(data):
    results = {}
    if "email" in data:
        email = data["email"]
        results["email"] = f"Performed OSINT lookup for {email}"
    if "phone" in data:
        phone = data["phone"]
        results["phone"] = f"Performed OSINT lookup for {phone}"
    return results
