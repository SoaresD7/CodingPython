tamanho_arquivo = float(input("Digite o tamanho do arquivo para download (em MB): "))

velocidade_link = float(input("Digite a velocidade do link de internet (em Mbps): "))

velocidade_link_MBps = velocidade_link / 8

tempo_download_segundos = tamanho_arquivo / velocidade_link_MBps

tempo_download_minutos = tempo_download_segundos / 60

print(f"O tempo aproximado de download do arquivo é de {tempo_download_minutos:.2f} minutos.")
