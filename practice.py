from collections import deque


def person_is_seller(person):
    return person[-1] == 'm'


graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuje', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['tom', 'jonny']
graph['anuje'] = []
graph['peggy'] = []
graph['tom'] = []
graph['jonny'] = []


def search(name):
    search_deque = deque()
    search_deque += graph[name]
    searched = []
    while search_deque:
        person = search_deque.popleft()
        if person_is_seller(person):
            print(person + ' is a mango seller')
            return True
        else:
            searched.append(person)
            search_deque += graph[person]
    return False


print(search('you'))