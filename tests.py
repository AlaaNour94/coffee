import unittest
import xmlrunner
from mock import patch
from mongoengine import connect, disconnect
from database.models import CoffeeMachine, CoffeePod
from main import app


class TestCoffee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        disconnect()
        connect('mongoenginetest', host='mongomock://localhost')
        machines = [
            CoffeeMachine(name='m1', type="ES", model="ss", water_line=True),
            CoffeeMachine(name='m2', type="SMALL", model="ss", water_line=False),
            CoffeeMachine(name='m3', type="LARGE", model="ss", water_line=True),
            CoffeeMachine(name='m4', type="LARGE", model="ss", water_line=False),
        ]

        pods = [
            CoffeePod(name='p1', type="ES", flavor="VANILLA", size=2),
            CoffeePod(name='p2', type="SMALL", flavor="MOCHA", size=5),
            CoffeePod(name='p3', type="LARGE", flavor="PSL", size=7),
            CoffeePod(name='p4', type="LARGE", flavor="VANILLA", size=5),
        ]

        CoffeeMachine.objects.insert(machines)
        CoffeePod.objects.insert(pods)

    @classmethod
    def tearDownClass(cls):
        disconnect()

    def test_coffee_machine_return_all(self):
        self.client = app.test_client()
        response = self.client.get('/coffee-machines').json
        self.assertEqual(4, len(response))

    def test_filter_coffee_machine(self):
        self.client = app.test_client()
        response = self.client.get('/coffee-machines?type=large').json
        self.assertEqual(2, len(response))
        self.assertCountEqual(['m3', 'm4'], [x['name'] for x in response])

        response = self.client.get('/coffee-machines?type=large&water_line=false').json
        self.assertEqual(1, len(response))

        response = self.client.get('/coffee-machines?type=large&water_line=true').json
        self.assertEqual(1, len(response))

    def test_filter_coffee_pod(self):
        self.client = app.test_client()
        response = self.client.get('/coffee-pods?type=large').json
        self.assertEqual(2, len(response))
        self.assertCountEqual(['p3', 'p4'], [x['name'] for x in response])

        response = self.client.get('/coffee-pods?type=large&size=2').json
        self.assertEqual(0, len(response))

        response = self.client.get('/coffee-pods?type=large&size=5').json
        self.assertEqual(1, len(response))
    
    @patch("main.CoffeeMachine.objects", side_effect=Exception("test"))
    def test_error_happend(self, coffee_machine_mock):
        self.client = app.test_client()
        response = self.client.get('/coffee-machines?type=large').json
        coffee_machine_mock.assert_called_with(type='LARGE')
        self.assertEqual(response, {'error': 'Something bad happend please try later'})


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
