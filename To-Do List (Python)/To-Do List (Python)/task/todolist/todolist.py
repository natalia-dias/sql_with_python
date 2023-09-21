from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


class Table(Base):
    __tablename__ = 'task'

    id = Column(Integer, default='default_value')
    task = Column(String)
    deadline = Column(DateTime)

    def __repr__(self):
        return self.task


engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()
Base.metadata.create_all(engine)


def menu():
    global todo_list
    while True:
        print("1) Today's tasks\n2) Add a task\n0) Exit")
        answer = int(input())
        print('')
        if answer == 1:
            print('Today:')
            if len(todo_list) == 0:
                print('Nothing to do!\n')
            else:
                print(todo_list.join(' '))
        elif answer == 2:
            new_task = input('Enter a task\n')
            todo_list.append(new_task)
            print('The task has been added!\n')
        elif answer == 0:
            print('Bye!')
            break


todo_list = []
menu()


print('Today:')
for index, task in enumerate(my_list):
    print(f'{index + 1}) {task}')

