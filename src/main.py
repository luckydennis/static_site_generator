# python
import os
import shutil

from copystatic import copy_files_recursive
from gen_content import generate_page, generate_pages_recursive 

DIR_STATIC = "static"
DIR_PUBLIC = "public"
DIR_CONTENT = "content"
TEMPLATE = "template.html"

def main():
    print("Deleting public directory...")
    if os.path.exists(DIR_PUBLIC):
        shutil.rmtree(DIR_PUBLIC)

    print("Copying static files to public directory...")
    copy_files_recursive(DIR_STATIC, DIR_PUBLIC)

    print("Generating page...")
    generate_pages_recursive(DIR_CONTENT, TEMPLATE, DIR_PUBLIC)

if __name__ == "__main__":
    main()