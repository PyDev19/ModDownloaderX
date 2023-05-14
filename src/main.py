from src.mods import download_mod
from src.drivers import set_driver_options
from selenium import webdriver

# Mod loader ids for curseforge url
MOD_LOADERS = {
    'forge': '1',
    'fabric': '4',
    'quilt': '5'
}

print('What browser do you want to use (make sure it is installed):\n1. Chrome\n2. Chromium')
browser = input('').lower()

service, options, download_dir = set_driver_options(browser)

print('\n')

# Prints instructions to tell users what to do
print('INSTRUCTIONS:')
print('1. Create a text file called "mods.txt" in the same folder as this program.')
print('2. In the first line of the file write "LOADER=" and the loader you want (forge, fabric, quilt) after the equal sign.')
print('3. In the second line of the file write "VERSION=" and the Minecraft version of the mods you want. If you want the latest version, just write "VERSION=latest", but make sure every mod you want has the same latest version.')
print('4. After that, in each line, write the name of the mod you want. Make sure it is accurate. ONE MOD NAME PER LINE.')
print('5. Repeat step 4 for each mod you want to download.')
print('6. Press Enter to start the download process.')

input('')

with open('mods.txt', 'r') as file:
    lines = file.readlines() # gets all the lines of the file

    # Create the driver instance
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window() # starts the web driver at maximized window

    for i, line in enumerate(lines):
        if i == 0:
            # Read the loader from the first line
            loader = line.strip().split("=")[1].lower()
            loader_id = MOD_LOADERS.get(loader.lower()) # gets the loader id for the url of the webpage
        if i == 1:
            # Read the version from the second line
            version = line.strip().split("=")[1]

            # Checks if the version is set to latest
            if version == 'latest':
                version = 0 # sets version to 0 if the version is set to latest
        if i >= 2:
            # Download each mod from line 3 onwards
            name = line.strip() # get the name of mod

            # Checks if the version is set to latest (i.e. 0)
            if version == 0:
                # If version is latest then print this
                print(f"Downloading {loader} {name} mod for the latest Minecraft version")
            else:
                print(f'Downloading {loader} {name} mod for Minecraft version {version}')
            
            name = name.replace(' ', '+') # Replace white spaces with a plus for the url of the web page

            # Checks if the line is the last line of the file
            if i == len(lines) - 1:
                # If line is the last line, then make the browser wait 15 seconds to ensure that all files are done downloading before exiting
                download_mod(name, version, loader, loader_id, driver)
            else:
                # If line is not the last line then the browser only waits for 5 seconds to ensure that the file starts downloading before going to the next one
                download_mod(name, version, loader, loader_id, driver, wait=False)

            # Checks if the version is set to latest (i.e. 0)
            if version == 0:
                # If version is latest then print this
                print(f'Done downloading {name.replace("+", " ")} {loader} for the latest Minecraft version')
                print('\n')
            else:
                # If version is not the latest then print this
                print(f'Done downloading {name.replace("+", " ")} {loader} for Minecraft version {version}')
                print('\n')

print(f'Done downloading all the mods. They are available in the {download_dir} folder.')
