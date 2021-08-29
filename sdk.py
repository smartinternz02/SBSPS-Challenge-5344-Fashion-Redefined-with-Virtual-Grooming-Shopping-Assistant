# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 17:54:55 2021

@author: afrin
"""

import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('0DO7ewiZ_P2m-oP0eob6y_IVkWZTGUjGVFSj7n_GDUYy')
assistant = AssistantV2(
    version='2021-06-14',
    authenticator = authenticator
)

assistant.set_service_url('https://api.eu-gb.assistant.watson.cloud.ibm.com')
response = assistant.create_session(
    assistant_id='7f2c2119-ad5c-4679-8124-55b8162b6e12'
).get_result()
session_id = response
session_id = session_id["session_id"]
print(type(session_id))
print(session_id)

while True:
    input_text = input("enter the text")
    response = assistant.message(
        assistant_id='7f2c2119-ad5c-4679-8124-55b8162b6e12',
        session_id=session_id,
        input={
            'message_type': 'text',
            'text': input_text
        }
    ).get_result()
    print(response)
    print(response["output"]["generic"][0]["text"])