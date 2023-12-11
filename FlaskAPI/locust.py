from locust import HttpUser, task
from faker import Faker
fake = Faker()



class LoggingUser(HttpUser):
    @task
    def test_index(self):
        self.client.get('/', params={'name': 'Kiko'})
        self.client.post('/', json={'name': fake.profile()})
