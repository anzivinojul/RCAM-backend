from django.test import TestCase

from recette.models import Recette

class RecetteTestCase(TestCase) :

    def setUp(self) :
        self.recetteBrownie = Recette()
        self.recetteBrownie.name = 'Brownie'
        self.recetteBrownie.time = '00:30'
        self.recetteBrownie.favorite = False
        self.recetteBrownie.difficulty = 'Facile'

    def test_create_recette(self) :
        nb_of_recette_before_add = Recette.objects.count()

        recetteCookie = Recette()
        recetteCookie.name = 'Cookie'
        recetteCookie.time = '00:30'
        recetteCookie.favorite = True
        recetteCookie.difficulty = 'Intermédiaire'

        recetteCookie.save()

        nb_of_recette_after_add = Recette.objects.count()

        self.assertTrue(nb_of_recette_after_add == nb_of_recette_before_add + 1)

    #def test_update_recette(self) : 
        #TODO
    
    #def test_delete_recette(self) :
        #TODO
