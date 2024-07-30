import json
import shutil
import os

class Package:
    def __init__(self):
        # create package folder
        self.dirPath = os.path.abspath(os.path.join("package"))
        os.makedirs(self.dirPath, exist_ok=True)

        
        # The contents of the files that will be included in the npm package are kept in this object.
        self.files = {
            ".npmignore": """.vscode
.idea
.__pycache__

.gitignore
.gitattribiutes

main.py
setup.py
mytheme.py
mycursor.py
__init__.py
__main__.py""",

            "index.js": """function mycolorscheme() {
    console.log("this is not a function!")
}
module.exports = mycolorscheme;""",
        }
    

    # We create our .npmignore file.
    def __npmignore__(self):
        with open(os.path.abspath(os.path.join(self.dirPath, ".npmignore")), "w", encoding="utf-8") as file:
            file.write(self.files[".npmignore"])

    
    # We create our index.js file.
    def __index_js__(self):
        with open(os.path.abspath(os.path.join(self.dirPath, "index.js")), "w", encoding="utf-8") as file:
            file.write(self.files["index.js"])
    
    
    # We create our package.json file.
    def __package_json__(self):
        shutil.copy(os.path.abspath(os.path.join("manifest.json")), os.path.abspath(os.path.join(self.dirPath, "package.json")))
    
    
    # We also copy our README.md file, which is located in a higher directory and prepared for github, into this directory.
    def __readme_md__(self):
        shutil.copy(os.path.abspath(os.path.join(".", "README.md")), os.path.abspath(os.path.join(self.dirPath, "README.md")))
    

    def for_npm(self):
        self.__npmignore__()
        self.__index_js__()
        self.__package_json__()
        self.__readme_md__()
        print(f"successfully packaged for npm!\npackage folder : {self.dirPath}")


def main():
    package = Package()
    package.for_npm()


if __name__ == "__main__":
    main()