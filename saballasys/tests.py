# from django.test import TestCase
# from saballasys.views import MainPage
# from saballasys.models import Users
# from django.http import HttpRequest

# class HomePageTest(TestCase):
# 	def test_mainpage_temp(self):
# 		response=self.client.get('/')
# 		self.assertTemplateUsed(response,'mainpage.html')

# 	def test_responding_save(self):
# 		respo = self.client.post('/', data={'name':'newname',
# 			'proc':'newproc','mobo':'newmobo','gpu':'newgpu','desc':'newdesc'})
# 		self.assertEqual(Users.objects.count(),1)
# 		newinput = Users.objects.first()
# 		self.assertEqual(newinput.fname,'newname')


# 	def test_redirec(self):
# 		respo = self.client.post('/', data=
# 			{'name':'newname','proc':'newproc',
# 			'mobo':'newmobo','gpu':'newgpu',
# 			'desc':'newdesc'})
# 		self.assertEqual(respo.status_code, 302)
# 		self.assertEqual(respo['location'],'/')


# 	def test_save_item(self):
# 		self.client.get('/')
# 		self.assertEqual(Users.objects.count(),0)

# class ORMTest(TestCase):
# 	def test_saving_retrieving_list(self):
# 		item1 = Users()
# 		item1.fname = 'Jay-ar Saballa'
# 		item1.fproc = 'Ryzen 5 2600'
# 		item1.fmobo = 'B450 Mortar Max'
# 		item1.fgpu = 'GTX 1660 Super'
# 		item1.fdesc = 'Editting and Gaming'
# 		item1.save()
# 		item2 = Users()
# 		item2.fname = 'Jing'
# 		item2.fproc = 'Ryzen 3 3400G'
# 		item2.fmobo = 'B450 Tomahawk'
# 		item2.fgpu = 'GTX 1050 Ti'
# 		item2.fdesc = 'Web Browsing'
# 		item2.save()
# 		items = Users.objects.all()
# 		self.assertEqual(items.count(),2)
# 		items1 = items[0]
# 		items2 = items[1]
# 		self.assertEqual(items1.fname, 'Jay-ar Saballa')
# 		self.assertEqual(items2.fname, 'Jing')

# 	def test_temp(self):
# 		Users.objects.create(fname='Abcd')
# 		Users.objects.create(fname='Efgh')
# 		respo = self.client.get('/')
# 		self.assertIn('Abcd', respo.content.decode())
# 		self.assertIn('Efgh', respo.content.decode())



# 	"""
# 	def test_mainpage_responding_view(self):
# 		response=self.client.get('/')
# 		'''
# 		request = HttpRequest()
# 		response = MainPage(request)
# 		'''
# 		html = response.content.decode('utf8')
# 		'''
# 		self.assertTrue(html.startswith('<!DOCTYPE html>'))
# 		self.assertIn('<title>Tinkle Out Loud</title>',html)
# 		self.assertTrue(html.endswith(''))'''
# 		stringPage=render_to_string('mainpage.html')
# 		self.assertEqual(html,stringPage)
# 		self.assertTemplateUsed(response,'mainpage.html')
# 		"""
