import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# t (s) - Eixo X
t = np.array([
    0.049999942857208164, 0.06666592381037278, 0.08333290476239458, 0.0,
    0.01666598095316462, 0.033332961905186365, 0.09999988571441638, 0.11666586666758094,
    0.13333284761960262, 0.14999982857162442, 0.1666658095247891, 0.18333279047681092,
    0.21666575238199726, 0.23333273333401908, 0.24999971428604087, 0.1999997714288326,
    0.2666656952392054, 0.2833326761912272, 0.3166656380964136, 0.2999996571432489,
    0.33333261904843536, 0.34999960000045716, 0.3666655809536218, 0.39999954285766526,
    0.38333256190564347, 0.41666552381082994, 0.43333250476285173, 0.4499994857148734,
    0.4666654666680381, 0.4833324476200598, 0.4999994285720817, 0.5333323904772681,
    0.5166654095252462, 0.5499993714292898, 0.5666653523824543, 0.5833323333344763
])

# v_y (m/s) - Eixo Y
v_y = np.array([
    -0.5605464567236017, -0.8719611549033808, -0.8719349965918988, np.nan,
    -0.24913175854381686, -0.5916701762587829, -1.121092913447198, -1.1210929134472023,
    -1.4947457084432532, -1.5259320210809058, -1.806205249442698, -1.8061510643689258,
    -2.086478477804507, -2.428961776220276, -2.3978931759842905, -2.1176199476224937,
    -2.771590813800024, -2.8026482033310995, -3.1452884516157376, -3.145288451615743,
    -3.518880521960152, -3.518986089431482, -3.861542257429257, -4.297522834880912,
    -3.861426413478411, -4.297522834880918, -4.453096589737191, -4.484371653788799,
    -5.044918110512399, -4.920204623625692, -5.32519133887419, -5.698718013439883,
    -5.387474278510146, -5.667747506871983, -6.166011023959568, -6.228107118513534
])

# Remover valores inválidos (NaN) para regressão
mask = ~np.isnan(v_y)
t = t[mask]
v_y = v_y[mask]

# Regressão Linear
# A equação é v_y = a*t + b (ou g*t + v0)
# 'slope' (a) será o valor de 'g'
# 'stderr' será a incerteza 'delta_a'
resultado = stats.linregress(t, v_y)

aceleracao_g = resultado.slope
incerteza_g = resultado.stderr
velocidade_inicial_v0 = resultado.intercept

# Exibindo os resultados
print("--- Resultados da Análise ---")
print(f"Equação da reta: v_y = ({aceleracao_g:.4f}) * t + ({velocidade_inicial_v0:.4f})")
print("")
print(f"Aceleração da Gravidade (g) encontrada (a): {aceleracao_g:.4f} m/s²")
print(f"Incerteza da Aceleração (delta_a): {incerteza_g:.4f} m/s²")
print("")
print("Resultado final no formato do Apêndice D:")
print(f"g = {abs(aceleracao_g):.4f} ± {incerteza_g:.4f} m/s²")

# Gráfico para visualização
t_linha = np.linspace(min(t), max(t), 100)
v_linha = aceleracao_g * t_linha + velocidade_inicial_v0

plt.figure(figsize=(10, 6))
plt.scatter(t, v_y, label='Seus Dados (Pontos Experimentais)')
plt.plot(t_linha, v_linha, color='red', label=f'Melhor Reta (Regressão Linear)\ny = {aceleracao_g:.3f}x + {velocidade_inicial_v0:.3f}')

plt.title('Análise da Queda Livre: Velocidade (v_y) vs. Tempo (t)')
plt.xlabel('Tempo (t) em segundos')
plt.ylabel('Velocidade Vertical (v_y) em m/s')
plt.legend()
plt.grid(True)
plt.show()

