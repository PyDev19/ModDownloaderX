# ModDownloaderX
ModDownloaderX is a Python program that allows users to download Minecraft mods from CurseForge by reading a list of mods in a text file. The program uses the Selenium library to automate web browsing and simulate user interactions, allowing for easy and efficient mod downloads.

# Features
- Download a single mod by name, loader, and version
- Download multiple mods from a list in a text file
- Supports Forge, Fabric, and Quilt mod loaders
- Automatically detects the latest version of each mod
- Downloads mods directly to the downloads folder

# Getting Started
To use ModDownloaderX, follow these steps:
- Clone the repository to your local machine using git clone `https://github.com/PyDev19/ModDownloaderX.git`
- Install the required Python libraries using `pip install -r requirements.txt`
- Install the appropriate browser driver for your browser (currently only supports Edge) and add it to your `PATH`
- Create a text file called mods.txt in the same folder as mod_downloader.py
- In each line of the text file, enter the name of a mod, the mod loader (Forge, Fabric, or Quilt), and the game version (e.g. 1.16.5), example: JEI,Forge,1.19.2
- Run mod_downloader.py using python mod_downloader.py
- Follow the prompts to download your mods

# Contributing
Contributions to ModDownloaderX are always welcome! If you'd like to contribute, please follow these steps:

- Fork the repository
- Create a new branch (git checkout -b my-new-feature)
- Make your changes and commit them (git commit -am 'Add some feature')
- Push your changes to your forked repository (git push origin my-new-feature)
- Create a new Pull Request

# License
ModDownloaderX is licensed under the `MIT` License. See `LICENSE` for more information.