import requests
import zipfile
import io
import subprocess

def get_browser_version(browser_name):
    """
    Get the version of the specified browser.

    Args:
        browser_name (str): Name of the browser (e.g., 'chrome', 'firefox').

    Returns:
        tuple: A tuple containing the browser name and version (browser_name, version),
               or None if the browser is not found.

    Raises:
        subprocess.CalledProcessError: If the subprocess call fails.
        FileNotFoundError: If the browser executable is not found.
    """
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
    
def download_browser_driver(browser_name):
    """
    Download the appropriate browser driver for the specified browser and extract it.

    Args:
        browser_name (str): Name of the browser (e.g., 'chrome', 'firefox').

    Returns:
        bool: True if the download and extraction were successful, False otherwise.
    """
    browser_name, browser_version = get_browser_version(browser_name)

    if browser_name not in ['chromium', 'chrome']:
        print(f'Unsupported browser: {browser_name}')
        return False

    driver_url = f'https://chromedriver.storage.googleapis.com/{browser_version}/chromedriver_linux64.zip'
    extract_directory = 'drivers/'

    try:
        response = requests.get(driver_url)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        print(f'Downloading {browser_name} driver')

        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
            zip_file.extractall(extract_directory)

        print(f'Done downloading {browser_name} driver')
        return True
    except (requests.RequestException, zipfile.BadZipFile) as e:
        print(f'Error occurred while downloading {browser_name} driver: {str(e)}')
        return False

def set_driver_options(browser):
    """
    Set up the driver options for the specified browser.

    Args:
        browser (str): Selection of the browser (1 for Chrome, 2 for Chromium).

    Returns:
        tuple: A tuple containing the WebDriver instance and the download directory.
               If the browser selection is unsupported, returns (None, None).
    """
    download_dir = input('Enter the download directory you want to download to (leave empty for default): ')
    headless = input('Do you want to see the browser window? (y/n): ')

    options = None
    service = None

    if browser in ['1', 'chrome']:
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service

        if download_browser_driver('chrome'):
            # Set up the Chrome driver with options to enable JavaScript and cookies
            options = Options()
            options.add_argument('--enable-javascript')
            options.add_argument('--enable-cookies')
            service = Service(executable_path='drivers/chromedriver')

    elif browser in ['2', 'chromium']:
        from selenium.webdriver.chromium.options import ChromiumOptions
        from selenium.webdriver.chromium.service import ChromiumService

        if download_browser_driver('chromium'):
            # Set up the Chromium driver with options to enable JavaScript and cookies
            options = ChromiumOptions()
            options.add_argument('--enable-javascript')
            options.add_argument('--enable-cookies')
            service = ChromiumService(executable_path='drivers/chromedriver')

    if options is None or service is None:
        print('Unsupported browser selection')
        return None, None

    if download_dir:
        # Set the download directory preference if provided
        prefs = {
            'download.default_directory': download_dir,
            'download.prompt_for_download': False,
            'safebrowsing.enabled': False,  # Disable the safe browsing warning
            'profile.default_content_settings.popups': 0
        }
        options.add_experimental_option('prefs', prefs)
        options.add_argument('--safebrowsing-disable-download-protection')

    if headless == 'n':
        # Set the user agent to mimic a specific web browser (Chrome in this case)
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
        options.add_argument(f'user-agent={user_agent}')
        options.add_argument('--headless')

    

    return service, options, download_dir
