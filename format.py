import json 
import os
from utils.utils import indent_file, update_matched

for file in os.listdir("./json/bics"):
    indent_file(f"./json/bics/{file}")
    update_matched(f"./json/bics/{file}")