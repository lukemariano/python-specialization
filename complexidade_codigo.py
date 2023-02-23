"""

CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim) (quanto mais afastado da margem pior)

"""

velocidade = 61  # velocidade atual do carro
local_carro = 99  # local que o carro está na estrada

RADAR_1 = 60  # velocidade máxima no radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # distância onde o radar pega

# tornando o código mais clean
velocidade_carro_passou_radar1 = velocidade > RADAR_1
carro_passou_no_radar1 = (-(RADAR_RANGE) <= local_carro - LOCAL_1 <= +(RADAR_RANGE))
carro_multado_radar1 = carro_passou_no_radar1 and velocidade_carro_passou_radar1

# carro passou da velocidade do radar 1
if velocidade_carro_passou_radar1:
    print('Passou da velocidade máxima do Radar 1')

# o carro passou no radar 1?
if carro_passou_no_radar1:
    print('O carro passou no radar 1')

# o carro foi multado no radar 1?
if carro_multado_radar1:
    print('Foi multado!')
    print(f'Local carro: {local_carro} e velocidade {velocidade} no radar 1')
else:
    print('Não foi multado!')