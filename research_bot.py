import os
import requests
import json

# This looks for the secret you just saved in GitHub Settings
GOOGLE_SCRIPT_URL = os.environ.get('GOOGLE_SCRIPT_URL')

def scan_for_groups():
    if not GOOGLE_SCRIPT_URL:
        print("❌ ERROR: GOOGLE_SCRIPT_URL is missing! Check your GitHub Secrets.")
        return

    print(f"🤖 Research Bot starting scan...")
    
    # This is a test group to make sure the connection works
    new_finds = [
        {
            "groupName": "NEW: BayCare Caregiver Support",
            "therapist": "BayCare Staff",
            "county": "Pinellas",
            "modality": "In-Person",
            "type": "Open",
            "email": "events@baycare.org",
            "cost": "Free",
            "schedule": "Monthly",
            "keywords": "caregiver, memory",
            "language": "English",
            "status": "Pending"
        }
    ]

    for group in new_finds:
        try:
            print(f"📤 Sending '{group['groupName']}' to Google Sheets...")
            # We use a timeout to make sure it doesn't hang forever
            response = requests.post(
                GOOGLE_SCRIPT_URL, 
                data=json.dumps({"action": "add", "data": group}),
                timeout=30 
            )
            print(f"✅ Response: {response.text}")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    scan_for_groups()
