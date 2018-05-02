import json
import yaml
import requests
from string import Template

# Beispiel von http://docs.dev.comsulting.net/top-api-usage/apicalculations/ ohne Tarife

API_TOKEN = "API_EXPLAIN"
API_URL = "https://main.top-api.io"

# Die Studie, z.B. digital facts
ANALYSE_ID = '0810233601' 

MEDIUM_CODE = "AGOF_dga11fre"

# Count-Route zur Berechung der Leistungswerte
# siehe Doku https://main.top-api.io/doc/api/analyses.api.html#id4
# und Live-API https://main.top-api.io/swagger-ui/#!/analyses/countAnalysis

countPath = Template("$url/analyses/$analysisID/count?access_token=$token").substitute(
	{'url': API_URL, 'analysisID': ANALYSE_ID, 'token': API_TOKEN})

body = """

   items:
   - type: MO
     key: $code
   period: DM
   info: true

"""

body = Template(body).substitute({'code': MEDIUM_CODE})

response = requests.post(countPath, json=yaml.load(body), headers={'Content-Type': 'application/json'})

print(json.dumps(json.loads(response.text), indent=2))
