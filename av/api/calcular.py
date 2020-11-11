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

            painelgeral.pontuacao = painelgeral.realizado * Decimal(100) / painelgeral.orcadometa

            painelgeral.pontuacao = painelgeral.pontuacao * painelgeral.peso / Decimal(100)

            painelgeral.save()
            del painelgeral

        elif indicador.modo == 'CAL':

            detalheindicador = DetalheIndicador.objects.filter(periodo=periodo, idempresa=empresa, idfilial=filial,
                                                               idindicador=indicador, incluso=True)
            painelgeral = PainelGeral()
            painelgeral.idempresa = empresa
            painelgeral.idfilial = filial
            painelgeral.criadopor = user
            painelgeral.periodo = periodo
            painelgeral.idindicador = indicador
            painelgeral.peso = indicador.peso
            """
            Zerando realizado e orcado para nao ocorrer erro de tipos de variveis diferentes.
            """
            painelgeral.realizado = 0
            painelgeral.orcadometa = 0

            for detalhe in detalheindicador:
                painelgeral.realizado = calculo_indicador(painelgeral.realizado,
                                                          detalhe.resultado, detalhe.modoindicador)
                painelgeral.orcadometa = calculo_indicador(painelgeral.orcadometa, detalhe.meta, detalhe.modoindicador)
                
            if indicador.Inverso:
                if painelgeral.realizado <= painelgeral.orcadometa:
                    painelgeral.pontuacao = painelgeral.peso
                else:
                    painelgeral.pontuacao = 0
            else:
                if painelgeral.realizado >= painelgeral.orcadometa:
                    painelgeral.pontuacao = painelgeral.peso
                else:
                    painelgeral.pontuacao = 0
            
            painelgeral.save()
            del painelgeral
                
                
def calculo_indicador(inicio, depois, tipo):
    if tipo == "CSM":
        return Decimal(inicio) + Decimal(depois)
    elif tipo == "CSB":
        return Decimal(inicio) - Decimal(depois)
    elif tipo == "CMU":
        return Decimal(inicio) * Decimal(depois)
    elif tipo == "CDI":
        return Decimal(inicio) / Decimal(depois)
    else:
        return Decimal(inicio) + Decimal(depois)