from app.notifier import upcoming_birthdays

def test_upcoming_birthdays():
    assert upcoming_birthdays() == []
