from linkedin_api import Linkedin

import os
import json

api = Linkedin(os.environ['LINKEDIN_USERNAME'], os.environ['LINKEDIN_PASSWORD'])

print('API Connection Made')

params = {
    'keywords': 'software engineer',
    'limit': 1,
    'location_name': 'Seattle, Washington'
}

jobs = api.search_jobs(**params)

job = api.get_job(jobs[0]['dashEntityUrn'].split(':')[3])

print(job['description']['text'])