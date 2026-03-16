import os
import requests
import json

# This tells the robot where your Google Sheet lives
# (We set this up in your GitHub Secrets)
GOOGLE_SCRIPT_URL = os.environ.get('GOOGLE_SCRIPT_URL')

# The list of websites you provided
TARGET_URLS = [
    "https://baycare.org/events",
    "https://aa-intergroup.org/meetings/",
    "https://growtherapy.com/find/florida/cash?treatmentMethods[0]=Group%20Therapy",
    "https://www.limecounseling.com/services/groups"
]

def scan_for_groups():
    print(f"🤖 Research Bot starting monthly scan of {len(TARGET_URLS)} sites...")
    
    # In a real scenario, this would use 'BeautifulSoup' or 'Playwright' 
    # to scrape the actual HTML. For this setup, we're building the 
    # connection to your Google Sheet first.
    
    new_finds = [
        {
            "groupName": "NEW: BayCare Caregiver Support",
            "therapist": "BayCare Staff",
            "county": "Pinellas/Hillsborough",
            "modality": "In-Person",
            "type": "Open",
            "email": "events@baycare.org",
            "cost": "Free",
            "schedule": "Check Site for Dates",
            "keywords": "caregiver, memory, dementia",
            "language": "English",
            "status": "Pending"
        }
    ]

    for group in new_finds:
        try:
            print(f"📤 Sending '{group['groupName']}' to Google Sheets...")
            response = requests.post(
                GOOGLE_SCRIPT_URL, 
                data=json.dumps({"action": "add", "data": group})
            )
            print(f"✅ Response: {response.text}")
        except Exception as e:
            print(f"❌ Error sending data: {e}")

if __name__ == "__main__":
    scan_for_groups()
