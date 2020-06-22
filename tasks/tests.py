from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Task

class TaskModelTests(TestCase):

  @classmethod
  def setUpTestData(cls):
      test_user = get_user_model().objects.create_user(username='tester',password='pass')
      test_user.save()

      test_post = Task.objects.create(
          owner = test_user,
          title = 'Plan meals',
          message = 'For week june 29 to july 4th'
      )
      test_post.save()

  def test_blog_content(self):
      task = Task.objects.get(id=1)

      self.assertEqual(str(task.owner), 'tester')
      self.assertEqual(task.title, 'Plan meals')
      self.assertEqual(task.message, 'For week june 29 to july 4th')