"""
CONSTANTE = "Variáveis" que não vão mudar
MUITAS condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 61 # Velocidade máxima do radar 1
local_carro = 100 # Local em que o carro está na estrada

RADAR_1 = 60 # Velocidade máxima do radar 1
LOCAL_1 = 100 # Local do o radar 1 está
RADAR_RANGE = 1 #A distância onde o radar pega

carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= LOCAL_1 - RADAR_RANGE and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and carro_pass_radar_1

if carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar 1')

if carro_multado_radar_1:
    print('Carro foi multado no radar 1')
