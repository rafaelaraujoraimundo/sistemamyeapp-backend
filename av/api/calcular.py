from av.avcadastro.models import DetalheIndicador, PainelGeral, Indicador
from core.models import Empresa, Filial


def calcular_indicador(empresaid, filialid, periodo):
    empresa = Empresa.objects.get(id=empresaid)
    filial = Filial.objects.get(id=filialid)
    detalheindicador = DetalheIndicador.objects.filter(periodo=periodo, idempresa=empresa, idfilial=filial)
    painelgeral = PainelGeral()
    indicadores = Indicador.objects.all()
    
    for indicador in indicadores:
        if indicador.modo == 'UNI':
            
            
            detalheindicador = DetalheIndicador.objects.filter(periodo=periodo, idempresa=empresa, idfilial=filial, 
                                                               idindicador=indicador, incluso=True)
            print('TIPO UNI:' + str(detalheindicador.count()))
        
        elif indicador.modo == 'CAL':

            detalheindicador = DetalheIndicador.objects.filter(periodo=periodo, idempresa=empresa, idfilial=filial,
                                                               idindicador=indicador, incluso=True)
            print('TIPO CAL:' + str(detalheindicador.count()))
        
        elif indicador.modo == 'CON':

            detalheindicador = DetalheIndicador.objects.filter(periodo=periodo, idempresa=empresa, idfilial=filial,
                                                               idindicador=indicador, incluso=True)
            print('TIPO CON:' + str(detalheindicador.count()))


