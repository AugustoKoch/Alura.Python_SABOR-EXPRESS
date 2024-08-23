import os
from time import sleep


restaurantes = [{'nome':'Augustitos', 'categoria':'Brasileira', 'ativo':True},
                {'nome':'Supremos', 'categoria':'Pizza', 'ativo':False},
                {'nome':'Petitos', 'categoria':'Italiana', 'ativo':False}]

def exibir_nome_do_programa():
    print('𝓢𝓪𝓫𝓸𝓻 𝓔𝔁𝓹𝓻𝓮𝓼𝓼\n')

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar/Desativar Restaurante')
    print('4. Sair\n')

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    restaurantes.append({'nome': nome_do_restaurante, 'categoria':categoria, 'ativo':False})
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Restaurantes: ')
    
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativo' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alterar_estado_restaurante():
    exibir_subtitulo("Alterar estado do restaurante")
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante}, foi ativado com sucesso!' if restaurante['ativo'] else f'restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    
    if not restaurante_encontrado:
        print(f'O restaurante {nome_restaurante} não foi encontrado')

    voltar_ao_menu_principal()

def finalizar_app():
    exibir_subtitulo('Encerrando o programa')

def opcao_invalida():
    print('Opção inválida, tente novamente')
    sleep(3)
    os.system('cls')

    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
    sleep(5)
    print('\nVocê será direcionado de volta ao menu principal\n')
    sleep(3)
    main()

def exibir_subtitulo(subtitulo):
    os.system('cls')
    linha = '*' * len(subtitulo)
    print(linha)
    print(subtitulo)
    print(linha)
    print()

def ecolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        match opcao_escolhida:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alterar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    ecolher_opcao()

if __name__ == '__main__':
    main()