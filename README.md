[![CodeQL](https://github.com/kggx/HGToolkit/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/kggx/HGToolkit/actions/workflows/codeql-analysis.yml)
[![buildOPLibs](https://github.com/kggx/HGToolkit/actions/workflows/build_oplibraries.yml/badge.svg)](https://github.com/kggx/HGToolkit/actions/workflows/build_oplibraries.yml)

# Houdini Games Toolkit
![alt text](https://github.com/kggx/HGToolkit/blob/master/DeveloperTools/image/HGT_LOGO.png?raw=true)


This is a library contianing various quality of life tools aswell as some Houdini Engine specific tools & generators.

---

## Setup
- Clone (or download & unzip) this repository into a permanent location.
  - Master is the most stable branch
  - Develop contains the newest features and fixes but may be instable.
- Run the installer.bat 
  - The installer will find **all** Houdini Versions in User Documents and place a pre configured HGToolkit.json file in the packages folders. 
- To uninstall the toolkit just run the uninstaller.bat
  - This will remove all remove **all** HGToolkit.json files from the package folders.

---

## Contributing
Feel free to contribute and follow the given guide how to create and name tools. 

1. Create a feature in git-flow based on the latest develop branch.
2. Create your tool in the _HGToolkit/ToolGroup/_ folder. (See below.)
3. Please minimize the use of external HDAs.
4. Once you're finished: Open a pull request and the tool will be reviewed. 

We do the review process to ensure quality, performance, usability of the tools and keep the library tidy.

---

### Variables for the naming
|Variable|Description|
|:---|:----|
|ToolIdentifier|Unique Identifier for the tool. Only letters and underscores are allowed.|
|ToolDisplayName|This will be shown to the user|
|ToolIcon|Use a appropiate icon to visualize the tools function. A full list can be found here.|
|ToolVersion|This is the major version of the tool.
|HoudiniLicense|This indicates the version the tool was created in. (FC = Full, LC = Limited & NC = NonCommerial)|
|ToolGroup|This indicates the tool use case. f.E: PGD, Geometry, Houdini Engine|

---

### Release Versions
If a tool drastically changes in behavior, a new version must be created on file level. 

{ToolVersion} would change from 1 -> 2 for the new release and so does all of the naming. 

**Example**: hgt_TestTemplate_1_FC.hda --> hgt_TestTemplate_2_FC.hda
---

### Tool Groups

Please use the following groups. We can add more but this requires changes to the HGToolkit.template!

|Group|Description|
|:---|:---|
|Geometry|All tools that modify geometry|
|UVs|All tools that modify uvs|
|PDG|All tools that were created for use in PDG|
|Utilities|All tools that are more utility base.|
|Generators|All tools that generate something|
|...|More can be added if needed...|

---

### File Naming
All tools follow the following naming pattern.
```
hgt_{ToolIdentifier}_{ToolVersion}_{HoudiniLicense}.hda
```

**Example**: hgt_TestTemplate_1_LC.hda

---

### HDA Requirements
In the "Interactive -> Shelf Tools -> Options" section the hda must feature the following:
- Name: hgt_{ToolIdentifier}
- Label: {ToolDisplayName} ({ToolVersion} | {HoudiniLicense})
- Icon: {ToolIcon}
- Keywords: hgt houdini game toolkit {ToolIdentifier} {ToolVersion} {HoudiniLicense} 

In the "Interactive -> Shelf Tools -> Context" section the hda must feature the following:
- TAB Submenu Path: "HGT/{ToolGroup}"

---

## Feature requests & Issues
Please open a issue with the appropiated template. Thank you!  

---

## Maintainers

[Kilian Braun](https://3d-kb.com/) (@kggx) - [hello@3d-kb.com](mailto:hello@3d-kb.com?subject=Hello.%20Let's%20work%20together%20on%3A%20your%20Project) 

---

## FAQ
```
Can I use this in a (commercial) production? 
```
Yes you can. This is complete open source library. However you need pay attention to the Houdini License version (LC, NC). Additionally we do not take responsibility if you lose your work due to a crash.