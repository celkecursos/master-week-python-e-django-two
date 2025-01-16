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

class ContactMessage(models.Model):
    """Modelo para armazenar mensagens de contato"""
    name = models.CharField(max_length=255, verbose_name="Nome")
    email = models.EmailField(verbose_name="E-mail")
    subject = models.CharField(max_length=255, verbose_name="Assunto")
    message = models.TextField(verbose_name="Mensagem")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Edição")

    def __str__(self):
        """Retorna: str: O assunto da mensagem."""
        return self.subject
    
    class Meta:
        verbose_name = "mensagem de contato"
        verbose_name_plural = "mensagens de contato"

class Contact(models.Model):
    """Model para armazenar informações de contato."""
    address = models.TextField(
        verbose_name="Endereço",
        help_text="Informe o endereço completo."
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última atualização")

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

class About(models.Model):
    title_topics = models.CharField(max_length=255, verbose_name="Título")
    subtitle_topics = models.TextField(verbose_name="Subtítulo")

    title_topic_one = models.CharField(max_length=255, verbose_name="Título do Tópico 1")
    description_topic_one = models.TextField(verbose_name="Subtítulo do Tópico 1")

    title_topic_two = models.CharField(max_length=255, verbose_name="Título do Tópico 2")
    description_topic_two = models.TextField(verbose_name="Subtítulo do Tópico2")

    title_topic_three = models.CharField(max_length=255, verbose_name="Título do Tópico 3")
    description_topic_three = models.TextField(verbose_name="Subtítulo do Tópico 3")

    def __str__(self):
        return self.title_topics

    class Meta:
        verbose_name = "Sobre"
        verbose_name_plural = "Sobre"