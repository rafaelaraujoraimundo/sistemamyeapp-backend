

def valida_perfil(usuario, modulo):
    
    if usuario.idmodulos.filter(id=modulo).count() == 1:
        valida = True
    else:
        valida = False
    
    return valida
