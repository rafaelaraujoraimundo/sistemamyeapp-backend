from decimal import *

from av.avcadastro.models import DetalheIndicador, PainelGeral, Indicador
from core.models import Empresa, Filial


def calcular_indicador(empresaid, filialid, periodo, user):
    empresa = Empresa.objects.get(id=empresaid)
    filial = Filial.objects.get(id=filialid)
    indicadores = Indicador.objects.all()

    for indicador in indicadores:
        if indicador.modo == 'UNI':
            painelgeral = PainelGeral()
            detalheindicador = DetalheIndicador.objects.get(periodo=periodo, idempresa=empresa, idfilial=filial,
                                                            idindicador=indicador, incluso=True)
            painelgeral.idempresa = empresa
            painelgeral.idfilial = filial
            painelgeral.criadopor = user
            painelgeral.periodo = periodo
            painelgeral.idindicador = indicador
            painelgeral.peso = indicador.peso
            painelgeral.orcadometa = detalheindicador.meta
            painelgeral.realizado = detalheindicador.resultado
            painelgeral.peso = indicador.peso
            if detalheindicador.Inverso:
                if detalheindicador.resultado <= detalheindicador.meta:
                    painelgeral.pontuacao = painelgeral.peso
                else:
                    painelgeral.pontuacao = 0
            else:
                if detalheindicador.resultado >= detalheindicador.meta:
                    painelgeral.pontuacao = painelgeral.peso
                else:
                    painelgeral.pontuacao = 0

            painelgeral.save()
            del painelgeral

        elif indicador.modo == 'CAL':

            detalheindicador = DetalheIndicador.objects.filter(periodo=periodo, idempresa=empresa, idfilial=filial,
                                                               idindicador=indicador, incluso=True)
            print('TIPO CAL:' + str(detalheindicador.count()))

        elif indicador.modo == 'CON':
            painelgeral = PainelGeral()
            detalheindicador = DetalheIndicador.objects.filter(periodo=periodo, idempresa=empresa, idfilial=filial,
                                                               idindicador=indicador, incluso=True)
            painelgeral.idempresa = empresa
            painelgeral.idfilial = filial
            painelgeral.criadopor = user
            painelgeral.periodo = periodo
            painelgeral.idindicador = indicador
            painelgeral.peso = indicador.peso
            painelgeral.orcadometa = detalheindicador.count()
            """
            Zerando o Realizado para nao dar erro de Tipos diferentes.
            """
            painelgeral.realizado = 0
            
            for detalhe in detalheindicador:
                
                if detalhe.Inverso:
                    if detalhe.resultado <= detalhe.meta:
                        painelgeral.realizado = painelgeral.realizado + 1
                    else:
                        painelgeral.pontuacao = 0
                else:
                    if detalhe.resultado >= detalhe.meta:
                        painelgeral.realizado = painelgeral.realizado + 1
                    else:
                        painelgeral.pontuacao = 0
                        
            painelgeral.pontuacao = painelgeral.realizado * Decimal(100)/painelgeral.orcadometa

            painelgeral.pontuacao = painelgeral.pontuacao*painelgeral.peso/Decimal(100)        
           
            painelgeral.save()
            del painelgeral
                

