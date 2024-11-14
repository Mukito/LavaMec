from django.db.models import TextChoices

# aqui escreve todos os servicos segindo a regra 3 digitos segido de descrição
class ChoicesCategoriaManutencao(TextChoices):
    TROCAR_VALVULA_MOTOR = "TVM", "Trocar valvula do motor"
    TROCAR_OLEO = "TO", "Troca de Oleo"
    BALANCEAMENTO = "B", "Banlanceamento"
    LAVAGEM = "LS", "Lavagem Simples"
    LAVAGEM_COMPLETA = "LC", "Lavagem Completa"