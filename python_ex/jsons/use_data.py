from create_data import create_data

# in dict: userId; id; title; body

DATA = create_data("https://jsonplaceholder.typicode.com/posts")

def request_payload():
    # ...
    return "userId" # for example

def use_data(request_payload,DATA:list[dict]) -> str:
    req = request_payload()
    if  req == "userId":
        count_users_posts = {}
        for d in DATA:
            count_users_posts[f"User{d["userId"]}"] += 1 # TODO: fix the program and complete

    return count_users_posts





def main():
    print(use_data(request_payload,DATA))
if __name__ == "__main__":
    main()
