
# run these tests like:
#
#    FLASK_ENV=production python -m unittest test_routes.py


from app import app
import os
from unittest import TestCase

# Don't have WTForms use CSRF at all, since it's a pain to test

app.config['WTF_CSRF_ENABLED'] = False

class RoutesTestCase(TestCase):
    """Testing routes."""

    def test_homepage_show(self):
        """to see if honepage appears with the correct html resp"""
        with app.test_client() as client: 
            resp = client.get("/")
            self.assertEqual(resp.status_code, 200)

            html = resp.get_data(as_text=True)
            self.assertIn('<p class="card-title">', html)

    def test_scenario_show(self):
        """to see if honepage returns scenario"""
        with app.test_client() as client: 
            resp = client.get("/scenario")
            self.assertEqual(resp.status_code, 200)

            html = resp.get_data(as_text=True)
            self.assertIn('<button id="response" class="btn btn-info">', html)
        

