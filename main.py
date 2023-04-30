from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from mods import download_mod

mod_loaders = {
    'forge': '1',
    'fabric': '4',
    'quilt': '5'
}

print('What mode would you like to use: ')
print('1. Download a single mod')
print('2. Download mods from a list')

mode = input('Enter the number of mod you want to use: ')

if mode == '1':
    print('INSTRUCTIONS: ')
    print('1. Type the name of the mod accurately enough so that it shows up as the first result')
    print('2. Type the mod loader of that mod')
    print('3. Type the minecraft version that the mod is available in, ex: 1.19.2 or 1.16.5')

    print('\n')

    # Prompt user for the name and version of the Minecraft mod they want to download
    mod_name = input('Enter the name of the Minecraft mod to search for: ')
    loader = input('Enter the mod loader supporter by the mod: ')
    version = input('Enter the version of the mod you want: ')

    loader_id = mod_loaders.get(loader, None)

    mod_name = mod_name.replace(' ', '+')

    # Set up the Edge driver with options to enable JavaScript and cookies
    edge_options = Options()
    edge_options.add_argument('--enable-javascript')
    edge_options.add_argument('--enable-cookies')
    edge_service = Service(executable_path='./msedgedriver')
    driver = webdriver.Edge(options=edge_options)
    driver.maximize_window()

    download_mod(mod_name, version, loader, loader_id, driver)
    print(f'Done downloading {mod_name.replace("+", " ")} {loader} for {version}, it is located in the downloads folder')

if mode == '2':
    print('INSTRUCTIONS: ')
    print('1. Create a text file called "mods.txt" in the same folder as this program')
    print('2. In each line follow this format to add a mod to download: mod name,loader,game version')
    print('3. Do that for every mod you want to download, make sure each mod is in a different')
    print('4. After you are done that press enter in this program')
    print('WARNING: Mod name should be accurate enough that it shows up as the first result in the search bar on curseforge')
    print('WARNING: Make sure the mod loader is availbe for the mod you want')
    print('WARNING: Make sure the game version is just the number, ex: 1.19.2 or 1.16.5')

    print('\n')

    input('')

    # Set up the Edge driver with options to enable JavaScript and cookies
    edge_options = Options()
    edge_options.add_argument('--enable-javascript')
    edge_options.add_argument('--enable-cookies')
    edge_service = Service(executable_path='./msedgedriver')
    driver = webdriver.Edge(options=edge_options)
    driver.maximize_window()

    with open('mods.txt', 'r') as file:
        lines = file.readlines()

        for i, line in enumerate(lines):
            name, loader, version = line.strip().split(',')
            # Do something with the data, e.g. print it
            print(f"Downloading {loader} {name} mod for minecraft {version}")

            name = name.replace(' ', '+')

            loader_id = mod_loaders.get(loader, None)


            if i == len(lines) - 1:
                download_mod(name, version, loader, loader_id, driver)
            else:
                download_mod(name, version, loader, loader_id, driver, wait=False)

            print(f'Done downloading {name.replace("+", " ")} {loader} for {version}')

        print('Done downloading all the mods, they are available in downloads folder')