import pandas as pd

"""
REMOVER ESTES CAMPOS
"Transmissora_SIGET","Num_Patrimonio","Concessao_SIGET","Codigo_Modulo_SIGET","Data_Fabricacao","Entrada_Operacao_Comercial",
"Cod_Ident_Ativo_Conces","Ident_Equip_Def_ONS","TX_NUM_EQUIPAMENTO","Tipo_Corrente","Valor_crista_corrente_suportavel_nominal",
"Tensao_suport_nominal_impulso_atmos_para_terra_entre_polos","Tensao_suport_nominal_impulso_atmos_entre_os_contatos_abertos",
"Tensao_suport_nominal_impulso_manobra","Tensao_suport_nominal_impulso_manobra_para_terra_entre_polos",
"Tensao_suport_nominal_impulso_manobra_entre_os_contatos_abertos","Limite_Eletromagnetico_corrente_induzida",
"Limite_Eletromagnetico_tensao_induzida","Limite_Eletrostatico_corrente_induzida","Limite_Eletrostatico_tensao_induzida",
"Norma_especificacao","FREQUENCIA_HZ","RELACAO_ASSIMETRIA","XR","CLASSE_DURABILIDADE_MECANICA","POSSUI_TRANSF_BARRAS",
"CORRENTE_NOMINAL_TRANSF_BARRAS","TENSAO_NOMINAL_TRANSF_BARRAS","TENSAO_FASE_TERRA","NIVEL_MAXIMO_RI",
"LAMINA_ATERRAMENTO","LAMINA_ATERRAMENTO_CLASSE_ACOPLAMENTO","LAMINA_ATERRAMENTO_CLASSE_DURABILIDADE",
"ID_AGENTE_PROPRIETARIO","DESCRICAO","TENSAO_NOMINAL_MANOBRAS_DISTANCIA_ISOLAMENTO_IMPULSO",
"TENSAO_NOMINAL_MANOBRAS_DISTANCIA_ISOLAMENTO_IMPULSO_60HZ","TENSAO_NOMINAL_SUPORTAVEL_INDUSTRIAL_ENTRE_POLOS",
"TENSAO_NOMINAL_SUPORTAVEL_INDUSTRIAL_CONTATOS_ABERTOS","TENSAO_NOMINAL_SUPORTAVEL_INDUSTRIAL_AUXILIAR_SUPORTAVEL",
"MRID","DATA_DESATIVACAO","CONECTIVIDADE_ATIVO_3","STATUS_ENVIO","CONTROLE_FISCAL_TEZ","ONDA","TIPO_OPERACAO",
"DATA_ATUALIZACAO","CampoEletromagneticoFaseTerra","idBDITEmpreendimento","idBDITFuncaoTransmissao","Status_Sistema","Status_Usuario"

"Tensao_Nominal":"tensao_nominal",
"Tensao_nominal_equip":"tensao_nominal_equipamento",
"Tensao_max_suport_cond_emerg_1h":"tensao_maxima_suporte_1h",
"Fabricante_Tipo":"fabricante_tipo",
"Norma_espec_Norma_aplic_ano_fabric":"norma_especificacao_ano_fabricacao",
"Corrente_nominal_eficaz":"corrente_nominal_eficaz",
"Corrente_suportavel_nominal_curta_duracao":"corrente_suportavel_nominal_curta_duracao",
"TIPO_EQUIPAMENTO":"tipo_equipamento",
"""

def clear_data(data):
    # eliminando colunas que nao serao trabalhadas
    # axis = 1 --> remove colunas
    return data.drop(["Transmissora_SIGET",
                      "Num_Patrimonio",
                      "Concessao_SIGET",
                      "Codigo_Modulo_SIGET",
                      "Data_Fabricacao",
                      "Entrada_Operacao_Comercial",
                      "Cod_Ident_Ativo_Conces",
                      "Ident_Equip_Def_ONS",
                      "TX_NUM_EQUIPAMENTO",
                      "Tipo_Corrente",
                      "Valor_crista_corrente_suportavel_nominal",
                      "Tensao_suport_nominal_impulso_atmos_para_terra_entre_polos",
                      "Tensao_suport_nominal_impulso_atmos_entre_os_contatos_abertos",
                      "Tensao_suport_nominal_impulso_manobra",
                      "Tensao_suport_nominal_impulso_manobra_para_terra_entre_polos",
                      "Tensao_suport_nominal_impulso_manobra_entre_os_contatos_abertos",
                      "Limite_Eletromagnetico_corrente_induzida",
                      "Limite_Eletromagnetico_tensao_induzida",
                      "Limite_Eletrostatico_corrente_induzida",
                      "Limite_Eletrostatico_tensao_induzida",
                      "Norma_especificacao",
                      "FREQUENCIA_HZ",
                      "RELACAO_ASSIMETRIA",
                      "XR",
                      "CLASSE_DURABILIDADE_MECANICA",
                      "POSSUI_TRANSF_BARRAS",
                      "CORRENTE_NOMINAL_TRANSF_BARRAS",
                      "TENSAO_NOMINAL_TRANSF_BARRAS",
                      "TENSAO_FASE_TERRA",
                      "NIVEL_MAXIMO_RI",
                      "LAMINA_ATERRAMENTO",
                      "LAMINA_ATERRAMENTO_CLASSE_ACOPLAMENTO",
                      "LAMINA_ATERRAMENTO_CLASSE_DURABILIDADE",
                      "ID_AGENTE_PROPRIETARIO",
                      "DESCRICAO",
                      "TENSAO_NOMINAL_MANOBRAS_DISTANCIA_ISOLAMENTO_IMPULSO",
                      "TENSAO_NOMINAL_MANOBRAS_DISTANCIA_ISOLAMENTO_IMPULSO_60HZ",
                      "TENSAO_NOMINAL_SUPORTAVEL_INDUSTRIAL_ENTRE_POLOS",
                      "TENSAO_NOMINAL_SUPORTAVEL_INDUSTRIAL_CONTATOS_ABERTOS",
                      "TENSAO_NOMINAL_SUPORTAVEL_INDUSTRIAL_AUXILIAR_SUPORTAVEL",
                      "MRID",
                      "DATA_DESATIVACAO",
                      "CONECTIVIDADE_ATIVO_3",
                      "STATUS_ENVIO",
                      "CONTROLE_FISCAL_TEZ",
                      "ONDA",
                      "TIPO_OPERACAO",
                      "DATA_ATUALIZACAO",
                      "CampoEletromagneticoFaseTerra",
                      "idBDITEmpreendimento",
                      "idBDITFuncaoTransmissao",
                      "Status_Sistema",
                      "Status_Usuario",
                      "Fabricante_Tipo"
                      ], axis=1)


def rename_columns(data):
    mapa = {
        # CAMPOS PARA PREDIÇÃO
        "Tensao_Nominal": "tensao_nominal",
        "Tensao_nominal_equip": "tensao_nominal_equipamento",
        "Tensao_max_suport_cond_emerg_1h": "tensao_maxima_suporte_1h",
        "Fabricante_Tipo": "fabricante_tipo",
        "Norma_espec_Norma_aplic_ano_fabric": "norma_especificacao_ano_fabricacao",
        "Corrente_nominal_eficaz": "corrente_nominal_eficaz",
        "Corrente_suportavel_nominal_curta_duracao": "corrente_suportavel_nominal_curta_duracao",
        "TIPO_EQUIPAMENTO": "tipo_equipamento",
        # CARACTERISTICAS
        "Subestacao_SIGET": "subestacao_siget",
        "Num_Operacional": "numero_operacional",
        "Localizacao": "localizacao",
        "NOME_FABRICANTE": "nome_fabricante",
        "Conectividade_ativo": "conectividade_ativo",
        "ID_PATIO": "id_patio",
        "CONECTIVIDADE_ATIVO_2": "conectividade_ativo_2",
        "Sigla_Subestacao": "sigla_subestacao"
    }
    return data.rename(columns=mapa)


def clear_tensao_nominal(data):
    # eliminando colunas que nao serao trabalhadas
    # axis = 1 --> remove colunas
    to_return = data.drop(["tensao_nominal_equipamento",
                           "tensao_maxima_suporte_1h",
                           "norma_especificacao_ano_fabricacao",
                           "corrente_nominal_eficaz",
                           "corrente_suportavel_nominal_curta_duracao",
                           "tipo_equipamento",
                           "numero_operacional",
                           "subestacao_siget",
                           "conectividade_ativo",
                           "id_patio",
                           "conectividade_ativo_2"
                           ], axis=1)
    # eliminando missings - linhas em branco das colunas a serem classificaads
    to_return = to_return.dropna()
    to_return = replace_values_tensao_nominal(to_return)
    return to_return

def replace_values_tensao_nominal(data):
    data.loc[data['localizacao'] == 'Transformador', 'localizacao'] = 'transformador'
    data.loc[data['localizacao'] == 'Transformador#P', 'localizacao'] = 'transformador'
    data.loc[data['localizacao'] == 'Linha de transmissão', 'localizacao'] = 'linha_de_transmissao'
    data.loc[data['localizacao'] == 'Linha  de transmissão', 'localizacao'] = 'linha_de_transmissao'
    data.loc[data['localizacao'] == 'Linha de transmissão#P', 'localizacao'] = 'linha_de_transmissao'
    data.loc[data['localizacao'] == 'Capacitor', 'localizacao'] = 'capacitor'
    data.loc[data['localizacao'] == 'Outro', 'localizacao'] = 'outros'
    data.loc[data['localizacao'] == 'Outros', 'localizacao'] = 'outros'
    data.loc[data['localizacao'] == 'Outro#P', 'localizacao'] = 'outros'
    data.loc[data['localizacao'] == 'Reator', 'localizacao'] = 'reator'
    data.loc[data['localizacao'] == 'Desenergizados', 'localizacao'] = 'desenergizados'
    data.loc[data['localizacao'] == 'Barra', 'localizacao'] = 'barra'
    data.loc[data['localizacao'] == 'Compensador Estático', 'localizacao'] = 'compensador_estatico'
    return data

def apply_one_hot_encoding(data, fields):
    to_return = data
    for field in fields:
        # perform one hot encoding using get_dummies
        data_one_hot = pd.get_dummies(data[field])
        # add the one hot encoded columns to the original dataframe
        to_return = pd.concat([data, data_one_hot], axis=1)
    return to_return.drop(fields, axis=1)
