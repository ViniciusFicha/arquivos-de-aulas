import os
import shutil

caminho_origem = r"C:\Users\vinie\Downloads\teste"

mapa_pastas = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Vídeos": [".mov", ".mp4", ".avi", ".webm"],
    "Músicas": [".mp3", ".wav", ".flac"],
    "Arquivos Comprimidos": [".zip", ".rar", ".7z"],    
}

print("--- Iniciando Organização 2.0 ---")

for nome_do_item in os.listdir(caminho_origem):
    caminho_completo = os.path.join(caminho_origem, nome_do_item)

    if os.path.isfile(caminho_completo):
        nome, extensao = os.path.splitext(nome_do_item)
        extensao_minuscula = extensao.lower()

        for nome_da_pasta, extensoes in mapa_pastas.items():
            if extensao_minuscula in extensoes:
                caminho_destino = os.path.join(caminho_origem, nome_da_pasta)
                if not os.path.exists(caminho_destino):
                    os.mkdir(caminho_destino)
                shutil.move(caminho_completo, caminho_destino)
                print(f"Movendo arquivo: {nome_do_item} para a pasta: {nome_da_pasta}")
                break
            
print("--- Organização Concluída ---")
