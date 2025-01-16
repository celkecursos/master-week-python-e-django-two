# BaseCommand: Classe base para criar comandos personalizados no Django. Ao herdar dessa classe, pode ser criado comandos que são executados pelo manage.py no terminal.
from django.core.management.base import BaseCommand
# Contact: Importar o modelo Contact da aplicação Contact. O modelo representa a tabela no banco de dados onde os dados serão manipulados.
from courses.models import Contact

class Command(BaseCommand):
    # Mensagem de ajuda que descreve o propósito do comando
    help = 'Seed para cadastrar registro na tabela Contact'

    # O self permite que o método acesse os atributos e outros métodos definidos na classe.
    # *args: tupla de argumentos posicionais.
    # **kwargs: dicionário de argumentos nomeados. 
    def handle(self, *args, **kwargs):
        # Criar a lista de planos com os dados a serem cadastrados
        contact = {
            'address': '<h3 class="mb-3">Nosso Endereço</h3><p><strong>Nome da Empresa</strong><br>Rua Exemplo, 123<br>Bairro, Cidade, Estado<br>Telefone: (00) 9 1234-5678<br>E-mail: cesar@celke.com.br<br></p><p><strong>Horário de Funcionamento:</strong><br>Segunda a Sexta: 9h às 18h<br>Sábado: 9h às 13h<br>Domingo: Fechado</p>',
        }

        # Atualiza o registro existente ou cria um novo com base no título
        Contact.objects.update_or_create(
            address=contact['address'], # Critério de busca: título
            defaults=contact # Valores padrão para criar ou atualizar
        )

        # Exibir uma mensagem no terminal indicando o sucesso da operação
        self.stdout.write(self.style.SUCCESS('Conteúdo da página contato adicionado com sucesso!'))