import os
import glob
import subprocess

CHARACTER_VOICE_SWITCH = {
    "Shadowheart": "v3ed74f063c6042dc83f6f034cb47c679",
    "Astarion": "vc7c13742bacd460a8f65f864fe41f255"
}

print("Choose Character to change voice. (1: Shadowheart, 2: Astarion)")
selected_character = int(input("Input Number: "))

if selected_character == 1:
    input_character = CHARACTER_VOICE_SWITCH["Shadowheart"]
elif selected_character == 2:
    input_character = CHARACTER_VOICE_SWITCH["Astarion"]
else:
    print("[-] Wrong Input.")
    exit()

print("[+] Start to convert... It may take a few minutes.")
wem_files = glob.glob('./Voice/Mods/Gustav/Localization/English/SoundBanks/*.wem')
output_folder = './Mangio-RVC-v23.7.0/audios'
for wem_file in wem_files:
    if os.path.basename(wem_file).startswith(input_character):
        output_wav_file = os.path.join(output_folder, os.path.splitext(os.path.basename(wem_file))[0] + '.wav')
        subprocess.run(['./lib/vgmstream/vgmstream-cli.exe', '-o', output_wav_file, wem_file], stdout=subprocess.PIPE)

print("[+] Converting Complete.")