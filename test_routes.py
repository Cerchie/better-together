
# run these tests like:
#
#    FLASK_ENV=production python -m unittest test_routes.py


from app import app
import os
from unittest import TestCase
from scenarios import create_scenario

# Don't have WTForms use CSRF at all, since it's a pain to test

app.config['WTF_CSRF_ENABLED'] = False

class RoutesTestCase(TestCase):
    """Testing routes."""

    def test_homepage_show(self):
        """to see if homepage appears with the correct html resp"""
        with app.test_client() as client: 
            resp = client.get("/")
            self.assertEqual(resp.status_code, 200)

            html = resp.get_data(as_text=True)
            self.assertIn('<p class="card-title">', html)

    def test_scenario_show(self):
        """to see if page returns scenario"""
        with app.test_client() as client: 
            resp = client.get("/scenario")
            self.assertEqual(resp.status_code, 200)

            html = resp.get_data(as_text=True)
            self.assertIn('Work Scenario', html)

    def test_specific_scenario_show(self):
        """to see if scenario one show ups"""
        with app.test_client() as client: 
            resp = client.get("/scenario/1")
            self.assertEqual(resp.status_code, 200)

            html = resp.get_data(as_text=True)
            self.assertIn('<p>Compare your response with the following:</p>', html)

    def test_general_scenario_show(self):
        """to see if scenarios show up"""
        with app.test_client() as client: 
            scenario = create_scenario(3434,'ice cream','so yummy', 'see the ice cream')

            resp = client.get(f"/scenario")
            self.assertEqual(resp.status_code, 200)

            html = resp.get_data(as_text=True)
            self.assertIn('ice cream', html)

####THIS TEST IS RETURNING THE JINJA TEMPLATE, SO THE HTML IS NOT FOUND

        

