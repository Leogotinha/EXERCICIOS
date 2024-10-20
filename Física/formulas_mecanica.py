def vel_esc_media(posicao_final,posicao_inicial,tempo_inicial,tempo_final):
    vel_media = (posicao_final-posicao_inicial)/(tempo_final-tempo_inicial)
    return vel_media
def mu(posicao_inicial=0,velocidade=0,tempo=0):
    posicao_final = posicao_inicial+(velocidade*tempo)
    return posicao_final

def acel_esc_media(vel_final,vel_inicial,tempo_inicial,tempo_final):
    acel_media = (vel_final-vel_inicial)/(tempo_final-tempo_inicial)
    return acel_media    
