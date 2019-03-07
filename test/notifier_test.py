from app.notifier import upcoming_birthdays

def test_upcoming_birthdays():
    assert upcoming_birthdays() == []

# def test_send_email():
#     response = send_email()
#     assert isinstance(response, "python_http_client.client.Response")
