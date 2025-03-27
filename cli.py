class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, _id, function):
        self.commands[(_id)] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class BookCLI(SimpleCLI):
    def __init__(self, book_model):
        super().__init__()
        self.book_model = book_model
        self.add_command("create", self.create_book)
        self.add_command("read", self.read_book)
        self.add_command("update", self.update_book)
        self.add_command("delete", self.delete_book)

    def create_book(self):
        _id = int(input("Enter the id: "))
        titulo = str(input("Enter the title: "))
        autor = str(input("Enter the autor: "))
        ano = int(input("Enter the ano: "))
        preco = float(input("Enter the price: "))

        self.book_model.create_book(_id, titulo, autor, ano, preco)

    def read_book(self):
        autor = str(input("Enter the autor: "))
        book = self.book_model.read_book_by_autor(autor)
        if book:
            print(book['_id'])
            print(f"titulo: {book['titulo']}")
            print(f"autor: {book['autor']}")
            print(f"ano: {book['ano']}")
            print(f"preco: {book['preco']}")

    def update_book(self):
        _id = int(input("Enter the id: "))
        titulo = str(input("Enter the new titulo: "))
        autor = str(input("Enter the new autor: "))
        ano = int(input("Enter the ano: "))
        preco = float(input("Enter the price: "))
        self.book_model.update_book(_id, titulo, autor, ano, preco)

    def delete_book(self):
        _id = input("Enter the id: ")
        self.book_model.delete_book(_id)
        
    def run(self):
        print("Welcome to the book CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
        