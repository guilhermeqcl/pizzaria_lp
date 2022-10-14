
 def cadastrar_ingrediente(ingrediente, preco, dic_ingredientes, tipo_ingrediente):
    '''
    cadastra ingredientes do tipo massa, molho, queijo e cobertura

    param dic_ingredientes: dicionário com as chaves massa, molho, queijo e cobertura. Os valores desse dicionário são um dicionário com os ingredientes.
    param ingrediente: ingrediente a ser adicionado
    param preco: preço do ingrediente
    param tipo_ingrediente: dicionários massa, molho, queijo ou cobertura com as chaves ingredientes e valor é o preço.
    return: inventario atualizado
    type dic_ingredientes: dic{tipo_ingrediente}
    type tipo_ingrediente: dic{ingrediente: preco}
    type ingrediente: str
    type preco: float
    rtype: dic{dic{ingrediente: valor}}
    type ingredientes: str    
    '''

    pass

def remover_ingredientes(ingrediente, dic_ingredientes, tipo_ingrediente):
    '''
    remove ingredientes do tipo massa, molho, queijo e cobertura

    param dic_ingredientes: dicionário com as chaves massa, molho, queijo e cobertura. Os valores desse dicionário são uma lista com os ingredientes.
    param ingrediente: ingrediente a ser removido
    param tipo_ingrediente: massa, molho, queijo ou cobertura
    return: inventario atualizado
    type dic_ingredientes: dic{tipo_ingrediente}
    type tipo_ingrediente: dic{ingrediente: preco}
    type ingrediente: str
    rtype: dic{dic{ingrediente: valor}}
    type ingredientes: str    
    '''
    
    pass

def listar_ingredientes(dic_ingredientes,  tipo_ingrediente):
    '''
    lista ingredientes de um tipo

    param dic_ingredientes: dicionário com as chaves massa, molho, queijo e cobertura. Os valores desse dicionário são uma lista com os ingredientes.
    param tipo_ingrediente: massa, molho, queijo ou cobertura
    return: lista de ingredientes do tipo selecionado
    type dic_ingredientes: dic{list[str]}
    type tipo_ingrediente: str
    rtype: list[str]
    '''
    pass

def montar_pizza():
    '''
    escolhe tipos de ingredientes para montar a pizza


    '''
