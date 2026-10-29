from create_data import create_data
import random
DATA = create_data("https://jsonplaceholder.typicode.com/posts")

def search_d_from_data(index:int, DATA:list[dict] = DATA) -> dict:
    return DATA[index - 1]

def titles_from_data(search_d_from_data):
    seled_d = search_d_from_data(random.randint(1,len(DATA)))
    value_title = seled_d["title"]
    return value_title

def main():
    print(f"Title from data(id - {search_d_from_data(random.randint(1,len(DATA)))["id"]}): {titles_from_data(search_d_from_data)}")

if __name__ == "__main__":
    main()
