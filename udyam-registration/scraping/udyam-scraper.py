import requests
from bs4 import BeautifulSoup
import json

def scrape_udyam_form():
    url = "https://udyamregistration.gov.in/UdyamRegistration.aspx"
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/115.0.0.0 Safari/537.36"
            ),
            "Accept-Language": "en-US,en;q=0.9",
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract form fields from Step 1 (Aadhaar verification)
        step1_fields = []
        aadhaar_div = soup.find('div', {'id': 'divAadhaar'})
        if aadhaar_div:
            inputs = aadhaar_div.find_all('input')
            for input_tag in inputs:
                field = {
                    'id': input_tag.get('id', ''),
                    'name': input_tag.get('name', ''),
                    'type': input_tag.get('type', ''),
                    'required': 'required' in input_tag.attrs,
                    'placeholder': input_tag.get('placeholder', '')
                }
                step1_fields.append(field)
        
        # Extract form fields from Step 2 (PAN verification)
        step2_fields = []
        pan_div = soup.find('div', {'id': 'divPAN'})
        if pan_div:
            inputs = pan_div.find_all('input')
            for input_tag in inputs:
                field = {
                    'id': input_tag.get('id', ''),
                    'name': input_tag.get('name', ''),
                    'type': input_tag.get('type', ''),
                    'required': 'required' in input_tag.attrs,
                    'placeholder': input_tag.get('placeholder', '')
                }
                step2_fields.append(field)
        
        # Save the scraped data
        form_structure = {
            'step1': step1_fields,
            'step2': step2_fields
        }
        
        with open('udyam_form_structure.json', 'w') as f:
            json.dump(form_structure, f, indent=2)
            
        print("Scraping completed successfully. Data saved to udyam_form_structure.json")
        
    except Exception as e:
        print(f"Error during scraping: {str(e)}")

if __name__ == "__main__":
    scrape_udyam_form()
