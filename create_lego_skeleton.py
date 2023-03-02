import os

all_files = []
# Parent Directory path as Input
parent_dir = "/Users/shlokabhalgat/Awesome-CloudOps-Automation"
# Connector Name
connector_name = "AWS"
final_path = parent_dir +"/"+ connector_name +"/legos"
# create a new directory/folder
lego_name = "test_my_folder"
path = os.path.join(final_path, lego_name)
if not os.path.exists(lego_name):
    try: 
        os.makedirs(path)
        print(f"Created folder '{lego_name}'")
    except OSError as error: 
        print(error) 
python_file = f"{lego_name}/{lego_name}.py"
json_file = f"{lego_name}/{lego_name}.json"
init_file = f"{lego_name}/__init__.py"
readme_file = f"{lego_name}/README.md"
all_files = [python_file,json_file,init_file,readme_file]
for file in all_files:
    with open(os.path.join(final_path, file), "w") as fp:
        print(f"Created file '{file}'")
        print()
        if file==f"{lego_name}/{lego_name}.py":
            fp.write(f"##\n# Copyright (c) 2021 unSkript, Inc\n#  All rights reserved.\n##\nfrom pydantic import BaseModel, Field\nfrom typing import List, Dict, Tuple, Optional\nimport pprint\n\n\nclass InputSchema(BaseModel):\n\ndef {lego_name}_printer(output):\n\tif output is None:\n\t\treturn\npprint.pprint(output)\n\ndef {lego_name}() -> RETURN_TYPE:\n\n")
        if file==f"{lego_name}/{lego_name}.json":
            lego_title = lego_name.replace('_', ' ')
            action_title = lego_title.title()
            action_type = "LEGO_TYPE"+"_"+connector_name
            fp.write(f"{{\n\t\"action_title\": \"{action_title}\",\n\t\"action_description\": \" \",\n\t\"action_type\": \"{action_type}\",\n\t\"action_version\": \"1.0.0\",\n\t\"action_entry_function\": \"{lego_name}\",\n\t\"action_needs_credential\": \"true\",\n\t\"action_supports_poll\": \" \",\n\t\"action_supports_iteration\": \" \",\n\t\"action_output_type\": \"ACTION_OUTPUT_TYPE_\"\n}} ")