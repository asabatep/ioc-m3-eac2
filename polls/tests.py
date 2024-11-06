from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Create your tests here.

from django.contrib.auth.models import User
class MySeleniumTests(StaticLiveServerTestCase):

    admin_user = 'isard'
    admin_pass = 'pirineus'
    staff_user = 'user'
    staff_pass = 'ContraSenya123?'

    # no crearem una BD de test en aquesta ocasió (comentem la línia)
    #fixtures = ['testdb.json',]
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        opts = Options()
        cls.selenium = WebDriver(options=opts)
        cls.selenium.implicitly_wait(5)
        # creem superusuari
        user = User.objects.create_user("isard", "isard@isardvdi.com", "pirineus")
        user.is_superuser = True
        user.is_staff = True
        user.save()

    @classmethod
    def tearDownClass(cls):
        # tanquem browser
        # comentar la propera línia si volem veure el resultat de l'execució al navegador
        #cls.selenium.quit()
        super().tearDownClass()
 
#    def test_login(self):
#        # anem directament a la pàgina d'accés a l'admin panel
#        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))
# 
#        # comprovem que el títol de la pàgina és el què esperem
#        self.assertEqual( self.selenium.title , "Log in | Django site admin" )
# 
#        # introduïm dades de login i cliquem el botó "Log in" per entrar
#        username_input = self.selenium.find_element(By.NAME,"username")
#        username_input.send_keys('isard')
#        password_input = self.selenium.find_element(By.NAME,"password")
#        password_input.send_keys('pirineus')
#        self.selenium.find_element(By.XPATH,'//input[@value="Log in"]').click()
# 
#        # comprovem si hem aconseguit entrar a l'admin panel pel títol de la pàgina
#        self.assertEqual( self.selenium.title , "Site administration | Django site admin" )
#

    def test_create_user(self):
        # anem directament a la pàgina d'accés a l'admin panel
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))
 
        # comprovem que el títol de la pàgina és el què esperem
        self.assertEqual( self.selenium.title , "Log in | Django site admin" )
 
        # introduïm dades de login i cliquem el botó "Log in" per entrar
        username_input = self.selenium.find_element(By.NAME,"username")
        username_input.send_keys('isard')
        password_input = self.selenium.find_element(By.NAME,"password")
        password_input.send_keys('pirineus')
        self.selenium.find_element(By.XPATH,'//input[@value="Log in"]').click()
 
        # comprovem si hem aconseguit entrar a l'admin panel pel títol de la pàgina
        self.assertEqual( self.selenium.title , "Site administration | Django site admin" )


        self.selenium.get('%s%s' % (self.live_server_url, '/admin/auth/user/add/'))
        self.assertEqual( self.selenium.title , "Add user | Django site admin" )
        username_input = self.selenium.find_element(By.NAME,"username")
        username_input.send_keys('user')
        password_input = self.selenium.find_element(By.NAME,"password1")
        password_input.send_keys('ContraSenya123?')
        password_input = self.selenium.find_element(By.NAME,"password2")
        password_input.send_keys('ContraSenya123?')
        self.selenium.find_element(By.NAME,'_continue').click()

        self.selenium.find_element(By.NAME,'is_staff').click()
        self.selenium.find_element(By.NAME,'_save').click()

        self.selenium.find_element(By.XPATH, "//button[@type='submit' and text()='Log out']").click()
    #def test_staff_user(self):
        # anem directament a la pàgina d'accés a l'admin panel
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))
 
        # comprovem que el títol de la pàgina és el què esperem
        self.assertEqual( self.selenium.title , "Log in | Django site admin" )
 
        # introduïm dades de login i cliquem el botó "Log in" per entrar
        username_input = self.selenium.find_element(By.NAME,"username")
        username_input.send_keys('user')
        password_input = self.selenium.find_element(By.NAME,"password")
        password_input.send_keys('ContraSenya123?')
        self.selenium.find_element(By.XPATH,'//input[@value="Log in"]').click()
 
        # comprovem si hem aconseguit entrar a l'admin panel pel títol de la pàgina
        self.assertEqual( self.selenium.title , "Site administration | Django site admin" )
        
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/auth/user/add/'))
        self.assertEqual( self.selenium.title , "403 Forbidden" )

        self.selenium.get('%s%s' % (self.live_server_url, '/admin/polls/question/add/'))
        self.assertEqual( self.selenium.title , "403 Forbidden" )

