from av.avcadastro.models import NotaFilial, PainelGeral, DetalheIndicador, Nota


def carrega_modulo(modulo, usuario):
    retorno = {}
    empresa_logada = usuario.idempresa
    filial_logada = usuario.idfilial
    
    notafilial = NotaFilial.objects.filter(idempresa=empresa_logada, idfilial=filial_logada)
    painelgeral = PainelGeral.objects.filter(idempresa=empresa_logada, idfilial=filial_logada)
    indicadores = DetalheIndicador.objects.filter(idempresa=empresa_logada, idfilial=filial_logada)
    notas = Nota.objects.all()
    retorno = {'notafilial': notafilial, 'painelgeral': painelgeral, 'indicadores': indicadores, 'notas': notas}
    
    return retorno
