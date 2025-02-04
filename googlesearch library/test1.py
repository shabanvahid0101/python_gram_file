from googlesearch import search
query = input("Enter your query: ")
for url in search(query):
    print(url)