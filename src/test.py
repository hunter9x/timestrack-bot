import pytest
from bot import *

input = [{'type': 'message', 'user': 'U4YVBHXQ9', 'text': '<@UB1E70YQN> talk2bot', 'client_msg_id': '10f13fc8-a2b6-4a61-ad4f-2a7a2bf6ad22', 'team': 'T4Y3K9MRR', 'channel': 'G5BEJEQCS', 'event_ts': '1530453903.000074', 'ts': '1530453903.000074'}]

attachments = [{"pretext": "pre-hello", "text": "text-world"}]

@pytest.mark.skip(reason='basic test: passed everytime')
def test_SlackConnection():
    assert slack_connnect() == True

@pytest.mark.skip(reason='pytestskip')
def test_readRTM():
    print(f'{readRTM()}')

def test_parseSlackInput():
    assert parseSlackInput(input, "UB1E70YQN") == ["U4YVBHXQ9", "talk2bot", "G5BEJEQCS"] 

def test_getBotId():
    assert getBotId('timekeeper') == "UB1E70YQN"

def test_postMessage_text():
    assert postMessage("G5BEJEQCS", "test message")["ok"] == True

def test_postMessage_attachments():
    assert postMessage("G5BEJEQCS", "", attachments)["ok"] == True
    