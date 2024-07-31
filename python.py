import heapq
import time

class Request:
    def __init__(self, user, priority, timestamp):
        self.user = user
        self.priority = priority
        self.timestamp = timestamp

    def __lt__(self, other):
        return self.priority < other.priority

class ServerQueue:
    def __init__(self):
        self.queue = []
        self.stats = []

    def add_request(self, user, priority):
        timestamp = time.time()
        request = Request(user, priority, timestamp)
        heapq.heappush(self.queue, request)
        self.stats.append((user, timestamp))
        print(f"Požadavek uživatele '{user}' s prioritou {priority} byl přidán do fronty.")

    def process_request(self):
        if self.is_empty():
            print("Fronta požadavků je prázdná.")
            return
        request = heapq.heappop(self.queue)
        print(f"Zpracovává se požadavek uživatele '{request.user}' s prioritou {request.priority}.")

    def display_queue(self):
        if self.is_empty():
            print("Fronta požadavků je prázdná.")
            return
        print("Obsah fronty požadavků:")
        for request in self.queue:
            print(f"Uživatel: {request.user}, Priorita: {request.priority}, Čas: {time.ctime(request.timestamp)}")

    def display_stats(self):
        if not self.stats:
            print("Žádné statistiky nejsou k dispozici.")
            return
        print("Statistiky požadavků:")
        for user, timestamp in self.stats:
            print(f"Uživatel: {user}, Čas: {time.ctime(timestamp)}")

    def is_empty(self):
        return len(self.queue) == 0

def menu():
    server_queue = ServerQueue()
    while True:
        print("\nMenu:")
        print("1. Přidat požadavek do fronty")
        print("2. Zpracovat požadavek")
        print("3. Zobrazit frontu požadavků")
        print("4. Zobrazit statistiky požadavků")
        print("5. Ukončit program")
        choice = input("Vyberte akci: ")

        if choice == '1':
            user = input("Zadejte jméno uživatele: ")
            priority = int(input("Zadejte prioritu (nižší číslo znamená vyšší prioritu): "))
            server_queue.add_request(user, priority)
        elif choice == '2':
            server_queue.process_request()
        elif choice == '3':
            server_queue.display_queue()
        elif choice == '4':
            server_queue.display_stats()
        elif choice == '5':
            break
        else:
            print("Neplatná volba, zkuste to znovu.")

if __name__ == "__main__":
    menu()
