import os
import shutil

caminho = r"C:/Desenvolvimento/projeto_automacao_py"

arquivos = os.listdir(caminho)

pasta_videos = caminho + "/Videos"
pasta_imagens = caminho + "/Imagens"
pasta_outros = caminho + "/Outros"

if not os.path.exists(pasta_videos):
    os.mkdir(pasta_videos)

if not os.path.exists(pasta_imagens):
    os.mkdir(pasta_imagens)

if not os.path.exists(pasta_outros):
    os.mkdir(pasta_outros)

for item in arquivos:

    origem = caminho + "/" + item

    if os.path.isfile(origem):

        if item.endswith(".mp4"):
            shutil.move(origem, pasta_videos)
            print(f"{item} movido para Videos")

        elif item.endswith((".jpg", ".png")):
            shutil.move(origem, pasta_imagens)
            print(f"{item} movido para Imagens")

        else:
            shutil.move(origem, pasta_outros)
            print(f"{item} movido para Outros")


# Forma mais "suja" do arquivo

# import os
# import shutil

# caminho = r"C:/Desenvolvimento/projeto_automacao_py"

# arquivos = os.listdir(caminho)


# for item in arquivo:
#     print(item)

#     if item.endswith(".mp4"):
#         print("Esse arquivo é um video")
#     elif item.endswith((".jpg", ".png")):
#         print("Esse arquivo é uma imagem")
#     else:
#         print('É um arquivo de outro tipo')

# pasta_videos = caminho + "/Videos"

# if not os.path.exists(pasta_videos):
#     os.mkdir(pasta_videos)

# pasta_imagens = caminho + "/Imagens"

# if not os.path.exists(pasta_imagens):
#     os.mkdir(pasta_imagens)

# pasta_outros = caminho + "/Outros"
# if not os.path.exists(pasta_outros):
#     os.mkdir(pasta_outros)



# for item in arquivo:

#     origem = caminho + "/" + item
    
#     if os.path.isfile(origem):

#         if item.endswith(".mp4"):
#             shutil.move(origem, pasta_videos)

#         elif item.endswith((".jpg", ".png")):
#             shutil.move(origem, pasta_imagens)

#         else:
#             shutil.move(origem, pasta_outros)