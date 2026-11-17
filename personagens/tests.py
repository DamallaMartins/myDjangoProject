from django.test import TestCase
from django.urls import reverse
from django.utils.formats import date_format
from .models import Personagem


class PersonagemViewTests(TestCase):
    def setUp(self):
        self.personagem = Personagem.objects.create(
            nome='Gandalf',
            classe='Mago',
        )

    def test_create_page_uses_form_template(self):
        response = self.client.get(reverse('personagem_criar'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'personagens/personagem_form.html')

    def test_edit_page_renders_and_invalid_post_keeps_instance(self):
        url = reverse('personagem_editar', args=[self.personagem.pk])

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'personagens/personagem_form.html')

        response = self.client.post(url, {'nome': '', 'classe': 'Mago'})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())
        self.personagem.refresh_from_db()
        self.assertEqual(self.personagem.nome, 'Gandalf')

    def test_detail_page_links_to_delete_view(self):
        response = self.client.get(
            reverse('personagem_detalhe', args=[self.personagem.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            reverse('personagem_deletar', args=[self.personagem.pk]),
        )
        self.assertContains(
            response,
            date_format(self.personagem.data_de_criacao, 'DATE_FORMAT'),
        )
