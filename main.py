import media_geometrica
import media_ponderada
import media_harmonica
import media_aritmetica

def main():
    while True:
        print("Escolha uma das opções de cálculo:")
        print("1. Média Geométrica")
        print("2. Média Ponderada")
        print("3. Média Harmônica")
        print("4. Média Aritmética")
        print("5. Sair")

        opcao = int(input("Digite o número da opção desejada: "))

        if opcao == 5:
            print("Encerrando o programa.")
            break

        x = int(input("Digite o valor de x (inteiro e positivo): "))
        y = int(input("Digite o valor de y (inteiro e positivo): "))
        z = int(input("Digite o valor de z (inteiro e positivo): "))

        if opcao == 1:
            resultado = media_geometrica.calcular_media_geometrica(x, y, z)
        elif opcao == 2:
            resultado = media_ponderada.calcular_media_ponderada(x, y, z)
        elif opcao == 3:
            resultado = media_harmonica.calcular_media_harmonica(x, y, z)
        elif opcao == 4:
            resultado = media_aritmetica.calcular_media_aritmetica(x, y, z)
        else:
            print("Opção inválida. Tente novamente.")
            continue

        print(f"O resultado é: {resultado}")

if __name__ == "__main__":
    main()
