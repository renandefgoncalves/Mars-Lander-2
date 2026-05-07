# CÓDIGO BASE FORNECIDO PELO CODINGAME
'''
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.
    print("-20 3")
'''

---

# CÓDIGO FINAL COMENTADO
'''
Onde a nave tem que pousar? Num plano de 1000m.
Como é a movimentação da nave? A nave se movimenta por inclinação, variando de -90° a 90°, mas, tem influência da propulsão dos motores e da gravidade. A velocidade horizontal e vertical podem ser negativas.
Controlar combustível.
O terreno é estático, havendo movimentação somente da nave. Como o próprio jogo me fornece a área de pouso com coordenadas prévias de todo o mapa, posso ter salvo na memória a zona segura de pouso.
Mapear barreiras (montanhas e declives)

import sys
import math

# FASE 1: MAPEAR TERRENO E ENCONTRAR A PISTA DE POUSO

surface_n = int(input())
surface_points = []

target_x1 = -1
target_x2 = -1
target_y = -1

for i in range(surface_n):
    x, y = [int(j) for j in input().split()]
    
    if i > 0:
        prev_x, prev_y = surface_points[-1]
        # Encontrou o terreno plano (mesma altura)
        if y == prev_y:
            target_x1 = prev_x
            target_x2 = x
            target_y = y
            
    surface_points.append((x, y))

# Vamos mirar no "olho do boi" (o centro exato da pista)
target_x = (target_x1 + target_x2) // 2

# ====================================================================
# FASE 2: PILOTO AUTOMÁTICO DE ALTA PRECISÃO (LOOP DO JOGO)
# ====================================================================
while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    is_over_target = target_x1 <= x <= target_x2

    # --- 1. RADAR DE MONTANHAS (SOBREVIVÊNCIA) ---
    highest_y = target_y
    if not is_over_target:
        # Pega a montanha mais alta EXATAMENTE entre a nave e o alvo
        for p_x, p_y in surface_points:
            if (x <= p_x <= target_x) or (target_x <= p_x <= x):
                if p_y > highest_y:
                    highest_y = p_y

    # --- 2. CONTROLADOR PROPORCIONAL DE VELOCIDADE HORIZONTAL ---
    # A mágica acontece aqui: A velocidade cai naturalmente conforme chega perto do centro
    dist_to_center = target_x - x
    target_h_speed = dist_to_center // 15
    
    # Trava a velocidade máxima em cruzeiro para 40 m/s (para não perder o controle)
    target_h_speed = max(-40, min(40, target_h_speed))

    # --- 3. CONTROLADOR DE ÂNGULO (FREIO E ACELERADOR) ---
    speed_diff = h_speed - target_h_speed
    
    # Fator de reação: 2.5. Quanto mais fora da velocidade, mais agressivo ele inclina
    desired_angle = int(speed_diff * 2.5) 
    
    # Limita inclinação máxima em 45 graus para garantir que o motor continue empurrando pra cima
    desired_angle = max(-45, min(45, desired_angle))

    # --- 4. CONTROLE DE POTÊNCIA E GRAVIDADE ---
    desired_power = 3 # Potência base (queda controlada e suave)

    if not is_over_target and y < highest_y + 400:
        # === EMERGÊNCIA DE MONTANHA ===
        # Risco de colisão! Trava a inclinação em no máximo 18 graus 
        # e joga a potência no 4 para a nave escalar o obstáculo
        desired_angle = max(-18, min(18, desired_angle))
        desired_power = 4
    else:
        if is_over_target:
            # === FASE DE POUSO FINAL ===
            if y < target_y + 150:
                # Chegou nos últimos 150 metros de altura!
                
                # Se a velocidade pros lados já está baixinha, zera a inclinação
                if abs(h_speed) <= 15:
                    desired_angle = 0
                else:
                    # Se não, inclina de leve só para frear as sobras do movimento
                    desired_angle = max(-25, min(25, desired_angle))
                    
                # Controle de precisão vertical milimétrico
                if v_speed <= -35:
                    desired_power = 4 # Freio final de paraquedas
                elif v_speed >= -15:
                    desired_power = 2 # Relaxa o motor para a nave encostar suavemente
                else:
                    desired_power = 3
            else:
                # Sobre a pista, mas lá no alto. 
                # Freia forte a queda se estiver caindo rápido ou inclinando muito
                if v_speed <= -30 or abs(desired_angle) > 15:
                    desired_power = 4
        else:
            # === VOO CRUZEIRO COMUM ===
            # Se a nave estiver caindo rápido demais, ou se deitou muito para frear, liga o turbo
            if v_speed <= -25 or abs(desired_angle) > 20:
                desired_power = 4

    # Envia o comando para a NASA
    print(f"{desired_angle} {desired_power}")

'''
