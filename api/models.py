from django.db import models

class Base(models.Model):
    criacao=models.DateTimeField(auto_now_add=True)
    actualizao=models.DateTimeField(auto_now=True)
    ativo=models.BooleanField(default=True)

    class Meta:
        abstract= True

class curso():
    titulo=models.CharField(max_length=255)
    url=models.URLField(unique=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return self.titulo

class Avaliacao(Base):
    curso=models.ForeignKey(Curso, related_name='avaliacoes' ,on_delete=models.CASCADE)
    nome=models.CharField(max_length=255)
    email=models.EmailField()
    comentario=models.TextField(blank=True, default='')
    Avaliacao=models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = "Avaliacao"
        verbose_name_plural =  "Avaliacaos"
        unique_together=['email', 'curso']
    
    def __str__(self):
        return f'{self.nome} avaliou o curso {self.curso} com nota {sefft.avaliacao}'  



