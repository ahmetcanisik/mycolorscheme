import requests
from bs4 import BeautifulSoup
import json
import os


# tailwind renk kodlarını çekeceğim.
class websiteContent:
    def __init__(self):
        self.url = "https://tailwindcss.com/docs/customizing-colors"
        self.response = requests.get(self.url)

        if self.response.status_code == 200:
            self.soup = BeautifulSoup(self.response.content, "html.parser")
        else:
            print(f"Sunucu ile iletişimde bir sorun oluştu. {self.response.status_code}")

    def get(self):
        return self.soup


class tailwindColors:
    def __init__(self):
        self.content = websiteContent()
        self.soup = self.content.get()

        # content_wrapper
        self.content_wrapper = self.soup.find(id="content-wrapper")
        self.content_wrapper_child = self.content_wrapper.find(class_="grid grid-cols-[repeat(auto-fit,minmax(8rem,1fr))] gap-x-2 gap-y-8 sm:grid-cols-1")
        self.colors = self.content_wrapper_child.find_all(class_="2xl:contents")

    def get(self):
        result = []
        for parent in self.colors:
            # Başlığı çek
            title_element = parent.find()
            if title_element is None:
                continue
            title = title_element.contents[0]
            codes = []

            # 2xl:content yani parent'ın şu class'a sahip elemanına...
            color_parent = parent.find(class_="grid mt-3 grid-cols-1 sm:grid-cols-11 gap-y-3 gap-x-2 sm:mt-2 2xl:mt-0")
            if color_parent is None:
                continue

            color_parent_childs = color_parent.find_all(class_="relative flex")
            for color_parent_child in color_parent_childs:
                code_element = color_parent_child.find().find(class_="px-0.5").find(
                    class_="text-slate-500 text-xs font-mono lowercase dark:text-slate-400 sm:text-[0.625rem] md:text-xs lg:text-[0.625rem] 2xl:text-xs")
                if code_element is None:
                    continue
                codes.append(code_element.contents[0])

            result.append({
                "title": title,
                "colors": codes
            })

        return result


class MyTheme:
    def __init__(self):
        self.dirPath = os.path.abspath("package")
        if not os.path.exists(self.dirPath):
            os.makedirs(self.dirPath)
        self.twColors = tailwindColors().get()
        self.color_codes = ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"]

    
    def manifest(self):
        with open(os.path.abspath("manifest.json"), "r", encoding="utf-8") as file:
            info = json.load(file)
        css = f"""/*
* @name         : {info["name"]}
* @version      : {info["version"]}
* @description  : {info["description"]}
* @author       : {info["author"]}
* @license      : {info["license"]}
*/
"""
        return css


    def create_variables(self, mode, lang, minify=False):
        if lang == "css":
            css = ""
            for color in self.twColors:
                title = color["title"].lower()

                if minify == False:
                    css += f"\n/* {title} */\n"

                if mode == "dark":
                    for index, color_code in enumerate(reversed(color["colors"])):
                        css += f"--{title}-{str(self.color_codes[index])}: {color_code};\n"
                else:
                    for index, color_code in enumerate(color["colors"]):
                        css += f"--{title}-{str(self.color_codes[index])}: {color_code};\n"
            return css
        if lang == "json":
            color_list = {
                "light": {},
                "dark": {}
            }
            for color in self.twColors:
                title = color["title"].lower()
                for index, color_code in enumerate(reversed(color["colors"])):
                    color_list["dark"][f'{title}-{str(self.color_codes[index])}'] = color_code
                for index, color_code in enumerate(color["colors"]):
                    color_list["light"][f'{title}-{str(self.color_codes[index])}'] = color_code
            return color_list


    def theme(self, mode, minify = False):
        if mode == "dark":
            css = f"""
@media (prefers-color-scheme: dark) {{
    :root {{
        {self.create_variables(mode="dark", lang="css", minify=minify)}
    }}
}}
[data-theme='dark'] {{
    {self.create_variables(mode="dark", lang="css", minify=minify)}
}}
            """
        else:
            css = f"""
:root {{
    {self.create_variables(mode="light", lang="css", minify=minify)}
}}
[data-theme='light'] {{
    {self.create_variables(mode="light", lang="css", minify=minify)}
}}
            """
        return css.replace('\n', '').replace(' ', '') if minify else css


    def save(self, minify=False, file_name="mytheme.css"):
        full_path = os.path.abspath(os.path.join(self.dirPath, file_name))
        with open(full_path, "w", encoding="utf-8") as file:
            file.write(self.manifest() + self.theme(mode="light", minify=minify) + self.theme(mode="dark", minify=minify))
        with open("mycolorscheme.json", "w", encoding="utf-8") as jsonFile:
            json.dump(self.create_variables(lang="json", mode="light"), jsonFile, ensure_ascii=False, indent=2)
        print(f"saving succesfully! {full_path}")


def main():
    mytheme = MyTheme()
    mytheme.save()
    mytheme.save(file_name="mytheme.min.css", minify=True)

# tailwind renk kodlarını mytheme.css içerisine :root sınıfı içerisinde --slate-1,2,3 olarak kaydedeceğim.
if __name__ == "__main__":
    main()