import requests

class token():
        def get_token(self):
                url = "https://federate-qa.ipipeline.com/as/token.oauth2"
                body = {'grant_type': 'client_credentials',
                        'scope':'iGO.DTC',
                        'client_secret': 'dVSkWgVPgQN1owWVbSmk8l6rHKDzboGYDlA3RUArbm0BcWLUtknF2gLBtJXzX3UI',
                        'client_id':'igo-dtc-tester',
                        'subject':'testMattGuardian'}
                headers = {'Content-Type': 'application/x-www-form-urlencoded'}
                resp = requests.post(url, headers=headers, data=body)
                a = resp.json()
                return a["access_token"]

