from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def download_mod(name: str, version: str, loader: str, loader_id: str, driver: webdriver.Edge, wait: bool = True) -> None:
    """
    Download a mod from CurseForge.

    Args:
        name (str): The name of the mod.
        version (str): The version of the Minecraft game.
        loader (str): The mod loader (forge, fabric, quilt).
        loader_id (str): The ID corresponding to the mod loader.
        driver (webdriver.Edge): The Edge WebDriver instance.
        wait (bool, optional): Whether to wait for the download to complete (default is True).
    """
    
    # Construct the search URL for CurseForge using the mod name and version
    url = f'https://www.curseforge.com/minecraft/search?search={name}&page=1&class=mc-mods&gameFlavorsIds={loader_id}&sortType=1&pageSize=20'

    # Navigate to the search URL and wait for the page to load
    driver.get(url)
    driver.implicitly_wait(10)  # Wait up to 10 seconds for page elements to load

    # Extract the HTML content and parse it with BeautifulSoup
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Find the `body` element
    body = soup.find('body')

    # Find the `main` element within the `body`
    main = body.find('main')

    # Find the `div` element with class 'results-container' within the `main`
    results_container = main.find('div', class_='results-container')

    # Find the first mod with the given name and navigate to its files page for the desired version
    mod = results_container.find('div', class_='project-card')
    mod_link = mod.find('a')['href']
    if version == 0:
        driver.get(f'https://www.curseforge.com{mod_link}/files')
    else:
        driver.get(f'https://www.curseforge.com{mod_link}/files?version={version}')
    driver.implicitly_wait(10)

    loaders_list = driver.find_element(By.CSS_SELECTOR, 'ul[class="dropdown-list"]')
    loaders_list = loaders_list.find_elements(By.TAG_NAME, 'li')

    for loaders in loaders_list:
        if loaders.text.lower() == loader:
            loaders.click()

    # Find the file card with the desired version and download the mod file
    file_cards = driver.find_elements(By.CLASS_NAME, 'file-row')
    mod_file = None
    found = False

    if version != 0:
        for file_card in file_cards:
            # Find the `game-version` element within the file card
            game_version = file_card.find_element(By.CSS_SELECTOR, 'div[data-testid^="game-version"]')
            game_version = game_version.find_element(By.TAG_NAME, 'span').text

            if version in game_version:
                # If the file card matches the desired version, click on it and download the mod file
                mod_file = file_card
                mod_file.click()
                found = True

                mod_file = (driver.current_url).replace('files','download')
                break
    else:
        for file_card in file_cards:
            mod_file = file_card
            mod_file.click()
            found = True

            mod_file = (driver.current_url).replace('files','download')
            break

    if not found:
        # If the desired version is not available, print an error message
        if version == 0:
            print(f'{name.replace("+", " ")} is not available for the latest Minecraft version')
        else:
            print(f'{name.replace("+", " ")} is not available for Minecraft version {version}')
    else:
        # Otherwise, navigate to the mod file download page and wait for the download to start
        driver.get(mod_file)
        
        if wait == True:
            # Wait for the file to download
            time.sleep(15)
        else:
            time.sleep(5)

