from locust import HttpUser, task, between
import json

class SeedClassifier(HttpUser):
    wait_time = between(1,2)

    @task
    def get_prediction(self):
        payload = {
            "area": 15.26,
            "perimeter": 14.84,
            "compactness": 0.871,
            "length": 5.763,
            "width": 3.312,
            "asymmetry": 2.221, 
            "kernel length": 5.22
                }
        header = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        self.client.post('/function-1', data=json.dumps(payload), headers=header, catch_response=False)

