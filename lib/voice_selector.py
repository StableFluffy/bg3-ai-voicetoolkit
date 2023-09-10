import os
import glob
import subprocess

CHARACTER_VOICE_SWITCH = {
    1: {
        "name": "Lae'zel",
        "id": "v58a6933340bf83581d17fff240d7fb12"
    },
    2: {
        "name": "Shadowheart",
        "id": "v3ed74f063c6042dc83f6f034cb47c679"
    },
    3: {
        "name": "Gale",
        "id": "vad9af97d75da406aae137071c563f604"
    },
    4: {
        "name": "Astarion",
        "id": "vc7c13742bacd460a8f65f864fe41f255"
    },
    5: {
        "name": "Wyll",
        "id": "vc774d7644a1748dcb47032ace9ce447d"
    },
    6: {
        "name": "The Emperor",
        "id": "v73d49dc58b8b45dca98c927bb4e3169b"
    },
    7: {
        "name": "Raphael",
        "id": "vf65becd65cd74c88b85e6dd06b60f7b8"
    },
    8: {
        "name": "Nightwarden Minthara",
        "id": "v257213130c15493581769f134385451b"
    },
    9: {
        "name": "Nightsong",
        "id": "v6c55edb0901b4ba4b9e83475a8392d9b"
    },
    10: {
        "name": "Minsc",
        "id": "v0de603c542e248119dadf652de080eba"
    },
    11: {
        "name": "Karlach",
        "id": "v2c76687d93a2477b8b188a14b549304c"
    },
    12: {
        "name": "Jaheira",
        "id": "v91b6b2007d004d628dc999e8339dfa1a"
    },
    13: {
        "name": "Isobel",
        "id": "v263bfbfc616046f4a9e11089cdb5c211"
    },
    14: {
        "name": "Halsin",
        "id": "v7628bc0e52b842a7856a13a6fd413323"
    },
    15: {
        "name": "Narrator",
        "id": "vNARRATOR"
    },
}

def select_character():
    print("Select the character you want to edit the voice")
    for num, values in CHARACTER_VOICE_SWITCH.items():
        print(f'{num}: {values["name"]}')
    selected_number = int(input("Enter Number: "))

    if selected_number in CHARACTER_VOICE_SWITCH:
        return CHARACTER_VOICE_SWITCH[selected_number]["id"]
    else:
        print("You've entered the wrong number.")
        exit()

def convert_voice(input_character):
    print("[+] Starting voice conversion. It may take more than 10 minutes depending on your specifications.")
    wem_files = glob.glob('./Voice/Mods/Gustav/Localization/English/SoundBanks/*.wem')
    output_folder = './Mangio-RVC-v23.7.0/audios'
    for wem_file in wem_files:
        if os.path.basename(wem_file).startswith(input_character):
            output_wav_file = os.path.join(output_folder, os.path.splitext(os.path.basename(wem_file))[0] + '.wav')
            subprocess.run(['./lib/vgmstream/vgmstream-cli.exe', '-o', output_wav_file, wem_file], stdout=subprocess.PIPE)
    print("[+] Voice conversion complete")

def main():
    selected_character = select_character()
    convert_voice(selected_character)

if __name__ == '__main__':
    main()