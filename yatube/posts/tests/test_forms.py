from django.test import TestCase, Client
from django.urls import reverse

from posts.forms import PostForm
from posts.models import Post, Group, User


class PostFormTests(TestCase):
    """Форма для создания и редактирования поста."""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.group = Group.objects.create(
            title='Тестовая группа',
            slug='test-slug',
        )
        cls.author = User.objects.create(username='TestUser')
        cls.authorized_client = Client()
        cls.authorized_client.force_login(cls.author)
        cls.post = Post.objects.create(
            text='Текст тестового поста',
            author=cls.author,
            group=cls.group,
        )
        cls.form = PostForm()

    def test_postform_creates_post(self):
        """Валидная форма PostForm создаёт запись в БД."""
        posts_count = Post.objects.count()
        form_data = {
            'text': 'Текст из формы',
            'group': PostFormTests.group.pk,
        }
        response = PostFormTests.authorized_client.post(
            reverse('posts:post_create'),
            data=form_data,
            follow=True
        )
        self.assertRedirects(
            response,
            reverse(
                'posts:profile',
                kwargs={'username': 'TestUser'}
            )
        )
        self.assertEqual(Post.objects.count(), posts_count + 1)
        self.assertTrue(
            Post.objects.filter(
                text='Текст из формы',
                group=PostFormTests.group,
                author=PostFormTests.author
            ).exists(),
            'Создаваемый пост не обнаружен в БД.'
        )

    def test_postform_edits_post(self):
        """Валидная форма PostForm редактирует запись в БД."""
        form_data = {
            'text': 'Отредактировано',
            'group': PostFormTests.group.pk,
        }
        response = PostFormTests.authorized_client.post(
            reverse(
                'posts:post_edit',
                kwargs={'post_id': PostFormTests.post.id},
            ),
            data=form_data,
            follow=True
        )
        self.assertRedirects(
            response,
            reverse(
                'posts:post_detail',
                kwargs={'post_id': PostFormTests.post.id}
            ),
        )
        self.assertTrue(
            Post.objects.filter(
                text='Отредактировано',
                group=PostFormTests.group,
                author=PostFormTests.author
            ).exists(),
            ('Отредактированный пост не был записан в БД.')
        )
