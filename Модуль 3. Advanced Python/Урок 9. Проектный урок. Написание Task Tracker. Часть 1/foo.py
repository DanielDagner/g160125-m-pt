import json


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, task):
        if task.strip():
            self.tasks.append(task.strip())
            self.save_tasks()
            return "Задача добавлена."
        return "Задача не может быть пустой."

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            self.save_tasks()
            return f"Задача \"{removed_task}\" удалена."
        return "Некорректный номер задачи."

    def get_tasks(self):
        return self.tasks


class TaskTracker:
    def __init__(self):
        self.manager = TaskManager()

    def show_tasks(self):
        tasks = self.manager.get_tasks()
        if not tasks:
            print("Список задач пуст.")
        else:
            print("\nСписок задач:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    def add_task(self):
        task = input("Введите задачу: ")
        print(self.manager.add_task(task))

    def delete_task(self):
        self.show_tasks()
        if not self.manager.get_tasks():
            return

        try:
            index = int(input("Введите номер задачи для удаления: ")) - 1
            print(self.manager.delete_task(index))
        except ValueError:
            print("Введите число.")

    def main(self):
        while True:
            print("\nМеню:")
            print("1. Показать задачи")
            print("2. Добавить задачу")
            print("3. Удалить задачу")
            print("4. Выйти")

            choice = input("Выберите действие: ").strip()
            match choice:
                case "1":
                    self.show_tasks()
                case "2":
                    self.add_task()
                case "3":
                    self.delete_task()
                case "4":
                    print("Выход из программы.")
                    break
                case _:
                    print("Некорректный выбор, попробуйте снова.")


if __name__ == "__main__":
    tracker = TaskTracker()
    tracker.main()
