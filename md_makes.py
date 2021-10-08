import os, shutil
from datetime import datetime
import re



def convert_obsidian_to_md(in_file):    
    file_name = os.path.basename(in_file)
    yaml_data = {
        "title": file_name.replace("-", " ").capitalize()[:-3],
        "date": datetime.today().strftime('%Y-%m-%d'),
        "tags": [],
        "draft": "false",
        "summary": ""
    } 

    print(f"File : {file_name}")
    if os.path.exists(in_file):
        data = open(in_file, "r", encoding="utf-8").read()
    else:
        print(f"File not exist")
        return 

    # Set front matter 
    if not data.startswith("---"): 
        mod_data = data[:].lower()
        start = mod_data.index("tags:")
        # end = mod_data.index("related:")
        tags = data[start:]
        matches = re.findall("#[^\s]*", tags)
        yaml_data["tags"] = [ x.replace("#", "") for x in matches ]

        front_matter =  "\n".join([ f"{k}: {v}" for k,v in yaml_data.items() ])
        front_matter = "---\n" + front_matter + "\n---\n"
        data = front_matter + data
        print(" Front formatter set")
    
    # Convert image urls from obsidian to md 
    obsidian_links = re.findall("!\[\[[^\]\]]*]]", data)        
    for x in obsidian_links:
        url = x[:].replace('![[','').replace(']]','')
        if str(url).startswith("static"): url = "/"+url
        md_link = f"\n![{url}]({url})\n"
        data = data.replace(x, md_link)
    if len(obsidian_links): print(" Links  updated")

    # final data         
    with open(in_file, "w", encoding="utf-8") as f:
        f.write(data)

if __name__ == "__main__":
    in_path = r"E:\Studies\obsidian\nextjs_blog\tailwind-nextjs-starter-blog\data\blog\papers"

    if os.path.isdir(in_path):
        for in_file in os.listdir(in_path):
            convert_obsidian_to_md(os.path.join(in_path,in_file))
    



