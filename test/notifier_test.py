from app.notifier import upcoming_birthdays, send_email, send_sms

def test_upcoming_birthdays():
    assert upcoming_birthdays() == []

#
# leaving these commented out for now because they make real requests
# we'd normally prefer to "mock" or "fake" the requests,
# but these concepts are perhaps a little too advanced for an intro class
# the other option would be to un-comment it and let it execute on the CI server, in which case the CI server would need to be configured with environment variables
# hmmm...
#
#def test_send_email():
#    response = send_email()
#    #assert isinstance(response, python_http_client.client.Response)
#    assert response.__class__.__name__ == "Response"
#    assert response.status_code == 202
#
#def test_send_sms():
#    response = send_sms()
#    #assert isinstance(response, twilio.rest.api.v2010.account.message.MessageInstance)
#    assert response.__class__.__name__ == "MessageInstance"
#    assert "Callie Cousin's birthday is coming up on June 5th" in response.body
#
