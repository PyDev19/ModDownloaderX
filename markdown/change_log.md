# Change Log

## Latest
- Removed edge browser support
- You can now use chrome or chrominum browser
- You will be prompted which browser you want to use, make sure they are installed on your system

## 5/7/2023
- Removed the single mod download feature as it was not useful.
- Now you only need to specify the mod loader and Minecraft version once at the beginning of the `mods.txt` file.
- Added support for downloading the latest version of each mod. To do this, add `VERSION=latest` in the second line of the `mods.txt` file. Please ensure that all the mods have the same latest version to avoid issues with your modpack.
- Added the ability to specify a custom download folder for the downloaded mods. Ensure that you provide an absolute path.
- Documented `main.py` and `mods.py` to facilitate easier code contributions from other contributors.
- Added a prompt to ask users whether they want to see the browser window while the mods are being downloaded.