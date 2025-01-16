from django.core.management.base import BaseCommand
from courses.models import About

class Command(BaseCommand):
    help = 'Seed para cadastrar registros na tabela About'

    def handle(self, *args, **kwargs):
        about_data = {
            'title_topics': 'Sobre a Xxxxx',
            'subtitle_topics': 'Uma empresa comprometida em oferecer soluções inovadoras e acessíveis para transformar vidas e carreiras.',

            'title_topic_one': 'Nossa Missão',
            'description_topic_one': 'Proporcionar soluções que simplifiquem o aprendizado e promovam o crescimento pessoal e profissional de nossos clientes.',

            'title_topic_two': 'Nossa Visão',
            'description_topic_two': 'Ser referência em inovação e acessibilidade, transformando desafios em oportunidades por meio de conhecimento de qualidade.',

            'title_topic_three': 'Nossos Valores',
            'description_topic_three': 'Compromisso com a excelência, respeito pelas pessoas e paixão por ensinar e aprender.',
        }

        # Atualiza o registro existente ou cria um novo com base no título
        About.objects.update_or_create(
            title_topics=about_data['title_topics'],  # Critério de busca
            defaults=about_data  # Valores padrão para criar ou atualizar
        )

        self.stdout.write(self.style.SUCCESS('Registro na tabela About adicionado ou atualizado com sucesso!'))
