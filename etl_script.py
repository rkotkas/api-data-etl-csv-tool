import requests
import json
import pandas as pd 
import re

#fetch information
def get_data(input_url):
    response = requests.get(input_url)
    
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("unsuccessful")

#transforms info into a pandas dataframe
def transform_data_into_df(data):
    df = pd.DataFrame(data)
    return df


#count the number of characters
def count_chars(text):
    char_count = len(re.sub("[^a-zA-Z0-9]", "", text.strip()))
    return char_count


#find field value from df
def find_field_from_df(data, field, index):
    df = pd.DataFrame(data)
    field_value = str(df[field].values[index])
    return field_value


def main():
    input_url = "https://jsonplaceholder.typicode.com/posts"
    field = "body"
    body_length_list = []

    data = get_data(input_url)
    dataframe = transform_data_into_df(data)
    for index, row in dataframe.iterrows():
        field_value = find_field_from_df(dataframe, field, index)
        body_length = count_chars(field_value)
        body_length_list.append(body_length)
    dataframe['body_length'] = body_length_list
    dataframe.to_csv('final_data.csv', index=False)

    print("success")

main()


def test_find_field_from_df():
    input = [
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  }]
    field = "body"
    output = find_field_from_df(input, field, 0)
    expected = "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    assert  output == expected

test_find_field_from_df()


def test_count_chars():
    field_value = "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    output = count_chars(field_value)
    expected = 136
    assert output == expected

test_count_chars()


def test_transform_data_into_df():
    input = [
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
  }]
    output = transform_data_into_df(input)
    expected = pd.DataFrame(input)
    assert output.equals(expected)

test_transform_data_into_df()