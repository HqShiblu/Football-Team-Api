from rest_framework.test import APITestCase, RequestsClient

from ..models.player import Player
from ..models.player_skill import PlayerSkill

class ProcessTeamTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.client = RequestsClient()

    def setUp(self):
        Player.objects.all().delete()
        PlayerSkill.objects.all().delete()

    def test_sample(self):
        data = [
            {
                'position': 'goalkeeper',
                'mainSkill': 'speed',
                'numberOfPlayers': 1
            },
            {
                "position": "defender",
                "mainSkill": "strength",
                "numberOfPlayers": 1
            }
        ]

        response = self.client.post('http://127.0.0.1:8000/api/team/process', data=data, format='json')
        self.assertIsNotNone(response)
