# Houdini Games Toolkit

**Logo**

This is a library contianing various quality of life aswell as some Houdini Engine specific tools.

---

## Setup
- Clone this repository
  - Master is the most stable branch
  - Develop contains the newest features and fixes but may be instable.
- Run the installer.bat 
  - The installer will find **all** Houdini Versions in User Documents and place a package.json file. 
- To uninstall the toolkit just run the uninstaller.bat
  - This will remove all remove **all** HGToolkit.json files from the package folders.

---

## Naming & HDA Informations

### Variables
|Variable|Description|
|:---|:----|
|ToolIdentifier|Unique Identifier for the tool. Only letters and underscores are allowed.|
|ToolDisplayName|This will be shown to the user|
|ToolIcon|Use a appropiate icon to visualize the tools function. A full list can be found here.|
|ToolVersion|This is the major version of the tool.
|HoudiniLicense|This indicates the version the tool was created in.|
|ToolGroup|This indicates the tool use case. f.E: PGD, Geometry, Houdini Engine|

---

### Release Versions
If a tool drastically changes in behavior, a new version must be created on file level. 

{ToolVersion} would change from 1 -> 2 for the new release and so does all of the naming. 

---

### Tool Groups

|Group|Description|
|:---|:---|
|Geometry|All tools that modify geometry|
|UVs|All tools that modify uvs|
|PDG|All tools that were created for use in PDG|
|Utilities|All tools that are more utility base.|
|Generators|All tools that generate something|
|TBD|More if needed...|

---

### File Naming
All tools follow the following naming pattern.
```
hgt_{ToolIdentifier}_{ToolVersion}_{HoudiniLicense}.hda
```

**Example**: hgt_TestTemplate_1_lc.hda

---

### HDA Requirements
In the "Interactive -> Shelf Tools -> Options" section the hda must feature the following:
- Name: hgt_{ToolIdentifier}
- Label: {ToolDisplayName} ({ToolVersion} | {HoudiniLicense})
- Icon: {ToolIcon}

In the "Interactive -> Shelf Tools -> Context" section the hda must feature the following:
- TAB Submenu Path: "HGT/{ToolGroup}"

---

## Contributing
Feel free to contribute and follow the given guide how to create and name tools. 

1. Create a feature in git-flow based on the latest develop branch.
2. Please minimize the use of external HDAs.
3. Once you're finished: Open a pull request and the tool will be reviewed. 

We do the review process to ensure quality, performance, usability of the tools and keep the library tidy.

---

## Feature requests & Issues
Please open a issue with the appropiated tag and describe you're desire.  

---

## Maintainers

[Kilian Braun](https://3d-kb.com/) (@kggx) - [hello@3d-kb.com](mailto:hello@3d-kb.com?subject=Hello.%20Let's%20work%20together%20on%3A%20your%20Project) 

---

## FAQ
```
Can I use this in a (commercial) production? 
```
Yes you can. This is complete open source library. However we do not take responsibility if you lose your work due to a crash.