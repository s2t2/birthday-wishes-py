
# TODO: prefer a more direct test which invokes application code
def test_row_data_conversion():
    birthday = {"name": "Person X", "month": "July", "day": 4}
    spreadsheet_row_data = list(birthday.values())
    assert spreadsheet_row_data == ["Person X", "July", 4]
