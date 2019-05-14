from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.urls import reverse

from .models import *
from .views import *
# Create your tests here.


class Tester(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, post_list)

    def test_post_detail(self):
        found = resolve('/post/' + 1)
        self.assertEqual(found.func, post_detail)

    def test_new_post(self):
        found = resolve('/post/new/')
        self.assertEqual(found.func, post_new)

    def test_edit(self):
        found = resolve('/post/'+ str(1) + '/edit/')
        self.assertEqual(found.func, post_edit)

    def test_drafts(self):
        found = resolve('/drafts/')
        self.assertEqual(found.func, post_draft_list)

    def test_publish(self):
        found = resolve('/post/' + str(1) + '/publish/')
        self.assertEqual(found.func, post_publish)

    def test_comment(self):
        found = resolve('/post/' + str(1) + '/remove/')
        self.assertEqual(found.func, post_remove)


    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = post_list(request)
        html = response.content.decode('utf8')
        self.assertFalse(html.startswith('<html>'))
        self.assertTrue(html.endswith('</html>'))

    def test_post_detail_returns_correct_html(self):
        request = HttpRequest()
        response = post_list(request)
        html = response.content.decode('utf8')
        self.assertFalse(html.startswith('<html>'))

        self.assertTrue(html.endswith('</html>'))

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)


    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('post_list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_drafts_uses_correct_template(self):
        response = self.client.get(reverse('post_draft_list'))
        self.assertEquals(response.status_code, 302)
        #self.assertTemplateUsed(response, 'post_draft_list.html')

    def test_new_uses_correct_template(self):
        response = self.client.get(reverse('post_new'))
        self.assertEquals(response.status_code, 302)
        #self.assertTemplateUsed(response, 'blog/post_edit.html')
