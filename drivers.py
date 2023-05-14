import requests
import zipfile
import io
import subprocess

def get_browser_version(browser_name):
    browser_name = browser_name.lower()
    browser_name = browser_name + "-browser"

    try:
        version_output = subprocess.check_output([browser_name, '--version'])
        browser_name = browser_name.split('-')[0]
        version_string = version_output.decode().strip()
        if browser_name == 'chromium':
            version = version_string.split()[1]
        else:
            version = version_string.split()[2]

        return browser_name, version
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    
def get_browser_driver(browser_name):
    browser_name, browser_version = get_browser_version(browser_name)
    
    if browser_name == 'chromium' or browser_name == 'chrome':
        driver_url = f'https://chromedriver.storage.googleapis.com/{browser_version}/chromedriver_linux64.zip'

    # Directory to extract the contents
    extract_directory = 'drivers/'

    # Download the zip file
    response = requests.get(driver_url)
    
    print(f'Downloading {browser_name} driver')

    # Check if the request was successful
    if response.status_code == 200:
        # Create a ZipFile object from the downloaded content
        zip_file = zipfile.ZipFile(io.BytesIO(response.content))
        
        # Extract the contents of the zip file to the specified directory
        zip_file.extractall(extract_directory)
        
        # Close the ZipFile object
        zip_file.close()
        
        print(f'Done downloading {browser_name} driver')
        return True
    else:
        print(f'Failed to download {browser_name} driver')
        return False
