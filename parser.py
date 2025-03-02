from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import os
import sys
import traceback

def download_disclosure_pdf(well_url):
    driver = None
    try:
        print("Setting up Firefox options...")
        options = Options()
        
        # Set download behavior
        options.set_preference("browser.download.folderList", 2)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        download_dir = os.path.join(os.getcwd(), "downloads")
        os.makedirs(download_dir, exist_ok=True)
        options.set_preference("browser.download.dir", download_dir)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
        
        # Try to find Firefox automatically if path is incorrect
        if not os.path.exists("/usr/bin/firefox"):
            print("Firefox not found at specified path, trying alternatives...")
            if os.path.exists("/usr/bin/firefox-esr"):
                options.binary_location = "/usr/bin/firefox-esr"
            else:
                options.binary_location = ""  # Let Selenium try to find Firefox
        else:
            options.binary_location = "/usr/bin/firefox"
        
        print(f"Firefox binary set to: {options.binary_location or 'auto-detect'}")
        
        # Try to find geckodriver automatically
        gecko_path = "/usr/local/bin/geckodriver"
        if not os.path.exists(gecko_path):
            print("GeckoDriver not found at specified path, trying alternatives...")
            gecko_path = "geckodriver"  # Try to find in PATH
        
        print(f"Using GeckoDriver at: {gecko_path}")
        
        service = Service(executable_path=gecko_path)
        service.log_path = "geckodriver.log"
        
        print("Initializing Firefox webdriver...")
        driver = webdriver.Firefox(service=service, options=options)
        
        print(f"Navigating to {well_url}...")
        driver.get(well_url)
        
        # Give the page some time to load
        driver.implicitly_wait(10)
        
        print("Page loaded, looking for PDF download link...")
        # This is a placeholder - you'll need to inspect the page to find the correct selector
        # Example: Find a link with text containing "PDF"
        pdf_links = driver.find_elements_by_xpath("//a[contains(text(), 'PDF') or contains(@href, '.pdf')]")
        
        if pdf_links:
            print(f"Found {len(pdf_links)} potential PDF links")
            pdf_links[0].click()
            print("Clicked on PDF link, waiting for download...")
            
            # Wait for download to complete
            import time
            time.sleep(5)  # Adjust as needed
            
            # Find the most recently downloaded file
            files = os.listdir(download_dir)
            if files:
                newest_file = max([os.path.join(download_dir, f) for f in files], 
                                  key=os.path.getctime)
                return newest_file
            else:
                print("No files found in download directory")
                return None
        else:
            print("No PDF links found on page")
            return None
        
    except Exception as e:
        print(f"Error details: {str(e)}")
        print("Exception type:", type(e).__name__)
        print("Traceback:")
        traceback.print_exc()
        return None
    
    finally:
        # Make sure to close the browser
        try:
            if driver:
                driver.quit()
                print("Browser closed successfully")
        except Exception as cleanup_error:
            print(f"Error closing browser: {str(cleanup_error)}")

def main():
    well_url = "https://fracfocus.org/wells/42105353880000"
    
    print(f"Python version: {sys.version}")
    print(f"Attempting to download PDF Disclosure Form from {well_url}")
    
    downloaded_file = download_disclosure_pdf(well_url)
    
    if downloaded_file:
        print(f"Successfully downloaded PDF to {downloaded_file}")
    else:
        print("Failed to download PDF")

if __name__ == "__main__":
    main()