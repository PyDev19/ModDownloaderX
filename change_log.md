# Latest
- Removed single mod download feature, it was use less anyways
- Now you only need to specify the mod loader and minecraft version once at the begining of the file
- You can download the latest version of each mod by add `VERSION=latest` in the second line for the file, make sure that all the mods have the same latest version or you might run into some trouble for your modpack
- You can change the download folder that the mods are downloaded to, make sure it a absolute path
- Added documentation to both `main.py` and `mods.py` to make to easier for contributors to make changes to the code
- Added prompt to ask user weather they want to see the browser window while the mods are being downloaded