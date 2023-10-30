from app import process_query


def process_query(client):
    response = client.get('/query?q=What is 43 plus 45?')
    assert response.status_code == 200
    assert b'Result: 88.0' in response.data


# def test_knows_about_dinosaurs():
#     assert process_query("dinosaurs") == "Dinosaurs ruled the Earth 200 \
# million years ago"


# def test_does_not_know_about_asteroids():
#     assert process_query("asteroids") == "Unknown"


# def test_invalid_input():
#     assert process_query("abc") == "Invalid input"


# def test_team_name():
#     assert process_query("What is your name?") == "apex legend"


# def test_compare():
#     assert process_query("Which of the following numbers \
# is the largest:33,50,65?") == "65"


# def test_add1():
#     assert process_query('What is (\d+) plus (\d+)\?') == "77"
