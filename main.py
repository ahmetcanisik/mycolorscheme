import os
import json
from mytheme import MyTheme, runAll
from package import Package

def main():

    import argparse
    
    parser = argparse.ArgumentParser(description="Mycolorscheme\ntailwindcss offers an option where you can print color codes to a css file under the root variable and print them by compressing theme.")
    parser.add_argument('-g', '--generate', type=str, required=False, help="You can enter one parameters as 'mytheme'. If you enter any value other than these, you will receive an error. ex: --generate mytheme")
    parser.add_argument('-o', '--output', type=str, required=False, help="Extract the processed data to a file, ex: --output mytheme.css")
    parser.add_argument('-p', '--package', action="store_true", required=False, help="What do you want to pack for? There is currently only one option and that is npm. ex: --package npm")
    parser.add_argument('-a', '--all', action="store_true", required=False, help="It organizes the entire file configuration by running the main function under the Mytheme class.")
    parser.add_argument('-m', '--minify', action="store_true", required=False, help="If you enter this flag, it will shrink your data.")
    parser.add_argument('-v', '--version', action="store_true", required=False, help="--version is the parameter where you can find out the version of the project. ex: --version")
    args = parser.parse_args()

    if args.version:
        with open(os.path.abspath(os.path.join("manifest.json")), "r", encoding="utf-8") as file:
            package_info = json.load(file)
        print(f"{package_info["name"]} {package_info["version"]}")

    if args.generate:
        if args.generate == "mytheme":
            generator = MyTheme()
            
            if args.output:
                generator.save(file_name=args.output, minify=args.minify)
            else:
                generator.save(minify=args.minify)
        else:
            print(f"Invalid value for --generate: {args.generate}")
            
    if args.all:
        runAll()
    
    if args.package:
        try:
            package = Package()
            package.for_npm()
        except Exception as err:
            print("For --package you can only enter 'npm'. ex: --package npm\n", err)

if __name__ == "__main__":
    main()