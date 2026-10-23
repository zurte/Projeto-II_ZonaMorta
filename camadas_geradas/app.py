"""Interface de terminal. A App SÓ lê o que a pessoa digita e mostra mensagens: nenhum SQL aqui."""


class App:
    """Menu do terminal para player."""

    def __init__(self, repositorio):
        self.repositorio = repositorio

    def rodar(self):
        while True:
            print("\n=== PLAYER ===")
            print("1 - Cadastrar")
            print("2 - Listar")
            print("3 - Atualizar")
            print("4 - Excluir")
            print("0 - Sair")
            opcao = input("Escolha: ").strip()

            if opcao == "1":
                self.cadastrar()
            elif opcao == "2":
                self.listar()
            elif opcao == "3":
                self.atualizar()
            elif opcao == "4":
                self.excluir()
            elif opcao == "0":
                print("Até logo!")
                break
            else:
                print("Opção inválida.")

    # ---- telas
    def cadastrar(self):
        vida = self._ler_inteiro("Vida", False)
        velocidade = self._ler_inteiro("Velocidade", False)
        try:
            novo = self.repositorio.criar(Player(vida=vida, velocidade=velocidade))
            print(f"Cadastrado com sucesso: {novo}")
        except Exception as erro:  # o banco recusa dados inválidos (ex.: valor repetido em coluna única)
            print(f"Não foi possível cadastrar: {erro}")

    def listar(self):
        for player in self.repositorio.listar():
            print(player)
        print("(fim da lista)")

    def atualizar(self):
        id = self._ler_inteiro("Id para atualizar", True)
        player = self.repositorio.buscar_por_id(id)
        if player is None:
            print("Não encontrado.")
            return
        player.vida = self._ler_inteiro("Vida", False)
        player.velocidade = self._ler_inteiro("Velocidade", False)
        self.repositorio.atualizar(player)
        print("Atualizado.")

    def excluir(self):
        id = self._ler_inteiro("Id para excluir", True)
        self.repositorio.deletar(id)
        print("Excluído (se existia).")

    # ---- leitura segura da entrada (a interface valida; o banco é a segunda barreira)
    def _ler_texto(self, rotulo, obrigatorio):
        while True:
            valor = input(f"{rotulo}: ").strip()
            if valor or not obrigatorio:
                return valor or None
            print("Campo obrigatório.")

    def _ler_inteiro(self, rotulo, obrigatorio):
        while True:
            valor = input(f"{rotulo}: ").strip()
            if not valor and not obrigatorio:
                return None
            try:
                return int(valor)
            except ValueError:
                print("Digite um número inteiro.")

    def _ler_real(self, rotulo, obrigatorio):
        while True:
            valor = input(f"{rotulo}: ").strip().replace(",", ".")
            if not valor and not obrigatorio:
                return None
            try:
                return float(valor)
            except ValueError:
                print("Digite um número (ex.: 12.5).")
