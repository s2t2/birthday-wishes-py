from app.notifier import upcoming_birthdays, send_email

def test_upcoming_birthdays():
    assert upcoming_birthdays() == []

## right now this test actually makes a request, so consider mocking/faking the results of that request
## ... but mocking is a little too advanced for the examples I'm trying to provide students
## ... so leaving this commented-out for now ...
#def test_send_email():
#    response = send_email()
#    #assert isinstance(response, python_http_client.client.Response)
#    #> NameError: name 'python_http_client' is not defined
#    # ... consider installing python_http_client (https://github.com/sendgrid/python-http-client)
#    # ... for now use these tests:
#    assert response.__class__.__name__ == "Response"
#    assert response.status_code == 202
