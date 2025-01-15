from django.db import models

class Home(models.Model):
    """Modelo para gerenciar o conteúdo da página inicial"""
    title = models.CharField(max_length=255, verbose_name="Título")
    subtitle = models.CharField(max_length=255, verbose_name="Subtítulo")
    text_btn = models.CharField(max_length=50, verbose_name="Texto do Botão")
    link_btn = models.URLField(max_length=500, verbose_name="Link do Botão")
    title_topics = models.CharField(max_length=255, verbose_name="Título dos Tópicos")
    subtitle_topics = models.CharField(max_length=255, verbose_name="Subtítulo dos Tópicos")
    title_topic_one = models.CharField(max_length=255, verbose_name="Título do Tópico 1")
    description_topic_one = models.TextField(verbose_name="Descrição do Tópico 1")
    title_topic_two = models.CharField(max_length=255, verbose_name="Título do Tópico 2")
    description_topic_two = models.TextField(verbose_name="Descrição do Tópico 2")
    title_topic_three = models.CharField(max_length=255, verbose_name="Título do Tópico 3")
    description_topic_three = models.TextField(verbose_name="Descrição do Tópico 3")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Página Inicial"
        verbose_name_plural = "Páginas Iniciais"

