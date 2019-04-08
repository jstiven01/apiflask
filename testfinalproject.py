from finalproject import app
import unittest

class FlaskTestCase(unittest.TestCase):
    
    #Ensuring Flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response =  tester.get('/restaurant/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    #Ensuring Main Tiltle of index
    def test_restaurant_page(self):
        tester = app.test_client(self)
        response =  tester.get('/restaurant/', content_type='html/text')
        self.assertTrue('Restaurants'.encode('UTF-8') in response.data)
    
        #Ensuring create a new restaurant
    def test_newrestaurant(self):
        tester = app.test_client(self)
        response =  tester.post('/restaurant/new/', 
                data=dict(name='Unitest Restaurant'),follow_redirects = True)
        self.assertTrue('Pollito'.encode('UTF-8') in response.data)

    def test_getallproviders(self):
        tester = app.test_client(self)
        response = tester.get('/restaurant/providers', content_type='application/json')
        print(response.data)
        self.assertTrue('Pimenton'.encode('UTF-8') in response.data)


if __name__ == '__main__':
    unittest.main()