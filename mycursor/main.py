import os
import shutil
class MyCursor:
    def __init__(self):
        self.dirPath = os.path.abspath(os.path.join("output", "mycursor"))
        self.cursors = ["default", "pointer", "not-allowed", "progress", "text", "wait"]

    # css kodlarımızı oluşturuyoruz.
    def __generateCSS__(self, minify=False):
        themes = ["light", "dark"]
        css = ""
        for i, mode in enumerate(themes):
            for j in range(len(themes)):
                if j == 0:
                    if mode == "light":
                        css += ":root {\n"
                    else:
                        css += "@media (prefers-color-scheme: dark) {\n:root {\n"
                else:
                    if mode == "light":
                        css += "[data-theme='light'] {\n"
                    else:
                        css += "[data-theme='dark'] {\n    color-scheme: dark;\n"

                for cursor in self.cursors:
                    css += f"   --cursor-{cursor}: url('cursor/{mode}/{cursor}.svg');\n"
                if mode == "light":
                    css += "}\n"
                else:
                    css += "}\n"
                    if j == 0:
                        css += "}\n"  # Close media query for dark mode
        return css.replace('\n', '').replace(' ', '') if minify else css


    # mycursor.css dosyası oluşturuluyor
    def __mycursorCSS__(self, minify=False, file_name="mycursor.css"):
        #create output>mycursor folders
        os.makedirs(self.dirPath, exist_ok=True)

        full_path = os.path.abspath(os.path.join(self.dirPath, file_name))
        with open(full_path, "w", encoding="utf-8") as file:
            file.write(self.__generateCSS__(minify=minify))
        print(f"saving successfully! {full_path}")

    
    def save(self, minify=False, file_name="mycursor.css"):
        self.__mycursorCSS__(minify=minify, file_name=file_name)

def main():
    cursor = MyCursor()
    cursor.save(file_name="mycursor.css")
    cursor.save(minify=True, file_name="mycursor.min.css")

if __name__ == "__main__":
    main()