import json
import os
from datetime import datetime

TODO_FILE = "todo_list.json"

def load_tasks():
    """Загрузить задачи из файла JSON"""
    if not os.path.exists(TODO_FILE):
        #Если нет файла то возвращаем пустой массив
        return []
    
    try:
        with open(TODO_FILE, 'r', encoding='utf-8') as file:
            tasks = json.load(file)
            return tasks
    except(json.JSONDecodeError, FileNotFoundError):
        return [] 

def show_task(tasks):
    """Показать все задачи с номерами"""
    if not tasks:
        print("Список задач пуст!")
        return
    
    print("\n" + "="*40)
    print("Ваши задачи:")
    print("\n" + "="*40)

    for i, task in enumerate(tasks, 1):
        status = "✓" if task.get('complite', False) else " "
        if 'created_at' in task:
            print(f"   Добавлено: {task['created_at']}")
    print("="*40)

def add_task(tasks):
    """Добавить новую задачу"""
    text = input("Введите текст задачи: ").strip()

    if not text:
        print("Задача не может быть пустой")
        return tasks
    
    new_task = {
        'text' : text,
        'complite' : False,
        'create_at' : datetime.now().strftime("%Y-%m-%d %H:%M"),
        'id' : len(tasks) + 1
    }

    tasks.append(new_task)
    print(f"Задача добавлена, ID = {new_task['id']}")
    return tasks

def delete_task(tasks):
    pass

def save_task(tasks):
    with open(TODO_FILE, "w", encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)

def main():
    tasks = load_tasks()

