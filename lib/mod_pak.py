import os
import glob
import subprocess
import re
import uuid

print("[+] Renaming...")

wem_files = glob.glob('./Wem/*.*')

pattern = r"\.wav_[0-9A-F]+.wem$"
subst = ".wem"

for wem_file in wem_files:
    updated_name = re.sub(pattern, subst, wem_file)
    if wem_file != updated_name:
        os.rename(wem_file, updated_name)

print("[+] Renaming Complete")


# Copy Folder ./Mod_Folder/Sample
input_mod = input("Mod Name : ")
input_description = input("Mod Description : ")
print("[+] Copying...")
source_folder = '.\lib\Mod_Folder\SampleMod'
destination_folder = f'.\lib\Mod_Folder\{input_mod}'
subprocess.run(['xcopy', source_folder, destination_folder, '/e', '/i', '/h', '/y'])

wem_files = glob.glob('./Wem/*.*')
for wem_file in wem_files:
    os.rename(wem_file, f'./lib/Mod_Folder/{input_mod}/Mods/Gustav/Localization/English/Soundbanks/{os.path.basename(wem_file)}')
print("[+] Copying Complete")

import xml.etree.ElementTree as ET
tree = ET.parse(f'./lib/Mod_Folder/{input_mod}/Mods/SampleMod/meta.lsx')
root = tree.getroot()

for attribute in root.findall(".//attribute"):
    attribute_id = attribute.get("id")
    
    if attribute_id == "Name":
        attribute.set("value", input_mod)
    elif attribute_id == "Folder":
        attribute.set("value", input_mod)
    elif attribute_id == "Description":
        attribute.set("value", input_description)
    elif attribute_id == "UUID":
        uuid_str = str(uuid.uuid4())
        attribute.set("value", uuid_str)

tree.write(f'./lib/Mod_Folder/{input_mod}/Mods/SampleMod/meta.lsx')

with open(f'./lib/Mod_Folder/{input_mod}/Mods/SampleMod/meta.lsx', "r+") as f:
    content = f.read()
    f.seek(0, 0)
    f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" + content)

if not os.path.exists(f'./lib/Mod_Folder/{input_mod}/Mods/{input_mod}'):
    os.rename(f'./lib/Mod_Folder/{input_mod}/Mods/SampleMod', f'./lib/Mod_Folder/{input_mod}/Mods/{input_mod}')

print("[+] lsx Created.")
print("[+] Creating pak file...")
source_directory = os.path.join(os.getcwd(), 'lib\Mod_Folder', input_mod)
destination_directory = os.path.join(os.getcwd(), 'Mods', input_mod + '.pak')

subprocess.run(['.\lslib\Tools\divine.exe', '-g', 'bg3', '-s', source_directory, '-d', destination_directory, '-a', 'create-package', '-c', 'none'], shell=True)
with open(f'./Mods/{input_mod}.pak', 'rb+') as f:
  f.seek(0x15)
  f.write(int.to_bytes(25, 4, byteorder='little'))
print("[+] pak file Created.")