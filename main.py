import whisper
import warnings
from tqdm import tqdm
from colorama import Fore, Style
from pydub import AudioSegment

def decouper_audio(fichier_audio, segment_duree):
    audio = AudioSegment.from_file(fichier_audio)
    duree_audio = len(audio)
    segments = []
    for start in range(0, duree_audio, segment_duree):
        end = min(start + segment_duree, duree_audio)
        segments.append(audio[start:end])
    return segments, duree_audio / 1000

def odt(fichier_audio, segment_duree=30 * 1000):
    print(f"{Fore.BLUE}Début de la transcription... (dev by Tawren){Style.RESET_ALL}")
    modele = whisper.load_model("base")
    segments, duree_totale = decouper_audio(fichier_audio, segment_duree)
    texte_complet = ""
    with tqdm(total=duree_totale, bar_format="{l_bar}{bar} {percentage:3.0f}%", colour="blue", unit="s") as barre:
        for segment in segments:
            segment.export("temp_segment.wav", format="wav")
            resultat = modele.transcribe("temp_segment.wav", language="fr")
            texte_complet += resultat["text"] + " "
            barre.update(len(segment) / 1000)
    return texte_complet.strip()

warnings.filterwarnings("ignore")

fichier_mp3 = "yourfile.mp3"

import os
if not os.path.exists(fichier_mp3):
    print(f"{Fore.RED}Le fichier audio '{fichier_mp3}' n'existe pas ! Vérifiez le chemin et réessayez. (dev by Tawren){Style.RESET_ALL}")
    exit()

texte_transcrit = odt(fichier_mp3)

with open("transcription.txt", "w", encoding="utf-8") as fichier:
    fichier.write(texte_transcrit)
    
print(f"{Fore.GREEN}Transcription terminée ! (dev by Tawren){Style.RESET_ALL}")
print(f"{Fore.GREEN}Le texte a été sauvegardé dans 'transcription.txt'. (dev by Tawren){Style.RESET_ALL}")