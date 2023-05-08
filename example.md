# Example of `mods.txt` File

## Latest Minecraft Version

To download mods for the latest version of Minecraft, use the following format:

```txt
LOADER=fabric   # Any Minecraft mod loader supported by the mods you want to download
VERSION=latest  # Specify "latest" to download the latest version of each mod

# List of mods
Mod Name 1    # Enter the accurate name of the mod
Mod Name 2
Mod Name 3
Mod Name 4
Mod Name 5
...
```

## Specific Minecraft Version
To download mods for a specific version of Minecraft, use the following format:

```txt
LOADER=fabric   # Any Minecraft mod loader supported by the mods you want to download
VERSION=1.19.4  # Enter the Minecraft version compatible with the mods

# List of mods
Mod Name 1    # Enter the accurate name of the mod
Mod Name 2
Mod Name 3
Mod Name 4
Mod Name 5
...
```
## Notes:

- In the LOADER field, specify the mod loader (e.g., fabric) that is supported by the mods you want to download.
- In the VERSION field, enter either "latest" or a specific Minecraft version that is compatible with the mods.
- In the list of mods, enter each mod's accurate name on a separate line.
- Ensure that the mods.txt file is located in the same folder as the main.py file.
