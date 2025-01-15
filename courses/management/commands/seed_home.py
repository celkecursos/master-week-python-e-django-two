# BaseCommand: Classe base para criar comandos personalizados no Django. Ao herdar dessa classe, pode ser criado comandos que são executados pelo manage.py no terminal.
from django.core.management.base import BaseCommand
# Home: Importar o modelo Home da aplicação home. O modelo representa a tabela no banco de dados onde os dados serão manipulados.
from courses.models import Home

class Command(BaseCommand):
    # Mensagem de ajuda que descreve o propósito do comando
    help = 'Seed para cadastrar registro na tabela Home'

    # O self permite que o método acesse os atributos e outros métodos definidos na classe.
    # *args: tupla de argumentos posicionais.
    # **kwargs: dicionário de argumentos nomeados. 
    def handle(self, *args, **kwargs):
        # Criar a lista de planos com os dados a serem cadastrados
        home = {
            'title': 'Bem-vindo à Academia Xxxxx!',
            'subtitle': 'Transforme seu corpo e sua mente com treinos personalizados e alcance seus objetivos de forma eficiente.',
            'text_btn': 'Explore Nossos Planos',
            'link_btn': 'https://celke.com.br',
            'title_topics': 'Por Que Treinar Conosco?',
            'subtitle_topics': 'Cuidar da saúde e bem-estar é essencial para uma vida equilibrada e feliz. Treinar na nossa academia ajuda você a:',
            'title_topic_one': 'Manter-se Saudável',
            'description_topic_one': 'Melhore sua saúde física e mental com treinos que se adaptam ao seu estilo de vida.',
            'title_topic_two': 'Alcançar Resultados',
            'description_topic_two': 'Conte com profissionais qualificados para ajudar você a atingir suas metas de forma eficiente.',
            'title_topic_three': 'Ganhar Confiança',
            'description_topic_three': 'Melhore sua autoestima e bem-estar geral com um corpo saudável e ativo.',
        }

        # Atualiza o registro existente ou cria um novo com base no título
        Home.objects.update_or_create(
            title=home['title'], # Critério de busca: título
            defaults=home # Valores padrão para criar ou atualizar
        )

        # Exibir uma mensagem no terminal indicando o sucesso da operação
        self.stdout.write(self.style.SUCCESS('Conteúdo da página inicial adicionado com sucesso!'))