# WARNING: THIS BRANCH IS FOR LINUX ONLY, PROBABLY WON'T RUN ON WINDOWS (YET)

# ModDownloaderX
ModDownloaderX is a Python program that allows users to download Minecraft mods from CurseForge by reading a list of mods in a text file. The program uses the Selenium library to automate web browsing and simulate user interactions, enabling easy and efficient mod downloads.

## Table of Contents
- [Change Log](#change-log)
- [Features](#features)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## Change Log
The latest change log can be found in [`change_logs.md`](https://github.com/PyDev19/ModDownloaderX/blob/main/change_log.md#latest).

## Features
- Download multiple mods from a list specified in a text file
- Supports Forge, Fabric, and Quilt mod loaders
- Automatically detects the latest version of each mod
- Downloads mods directly to the default downloads folder or a folder of your choice

## Getting Started
To use ModDownloaderX, follow these steps:

1. Clone the repository to your local machine using the command:
    ```shell
    git clone https://github.com/PyDev19/ModDownloaderX.git
    ```
2. Install the required Python libraries using:
    ```shell
    pip install -r requirements.txt
    ```
3. Install the appropriate browser driver for your browser (currently only supports Edge) and add it to your PATH.
4. Create a text file called `mods.txt` in the same folder as `main.py`.
5. In the first line add `LOADER=` followed by the mod loader you want, then in the second line add `VERSION=` followed by the minecraft version you want, or just added `latest` after it to get the latest version of the mods, lastly ever line after you should type the name of the mod accurately. For an example checkout [`example.md`](https://github.com/PyDev19/ModDownloaderX/blob/main/example.md)
6. Run the main.py script using:
    ```shell
    python main.py
    ```

# Contributing
Contributions to ModDownloaderX are always welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch: git checkout -b my-new-feature.
3. Make your changes and commit them: git commit -am 'Add some feature'.
4. Push your changes to your forked repository: git push origin my-new-feature.
5. Create a new Pull Request.

# License
ModDownloaderX is licensed under the MIT License. See the LICENSE file for more information.