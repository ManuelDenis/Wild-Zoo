from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: [Lion, Tiger, Cheetah], price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
        elif self.__animal_capacity > len(self.animals) and self.__budget < price:
            return "Not enough budget"
        elif self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"

    def hire_worker(self, worker: [Keeper, Caretaker, Vet]):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for w in self.workers:
            if w.name == worker_name:
                self.workers.remove(w)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salary = 0
        for w in self.workers:
            total_salary += w.salary
        if self.__budget >= total_salary:
            self.__budget -= total_salary
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_animals_care = 0
        for a in self.animals:
            total_animals_care += a.money_for_care
        if self.__budget >= total_animals_care:
            self.__budget -= total_animals_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = []
        tigers = []
        cheetah = []
        text = f"You have {len(self.animals)} animals\n"
        for a in self.animals:
            if a.__class__.__name__ == 'Lion':
                lions.append(a)
            elif a.__class__.__name__ == 'Tiger':
                tigers.append(a)
            elif a.__class__.__name__ == 'Cheetah':
                cheetah.append(a)
        text += f"----- {len(lions)} Lions:\n"
        for l in lions:
            text += f"{l}\n"
        text += f"----- {len(tigers)} Tigers:\n"
        for t in tigers:
            text += f"{t}\n"
        text += f"----- {len(cheetah)} Cheetah:\n"
        for c in cheetah:
            text += f"{c}\n"
        return text

    def workers_status(self):
        works = {'Keeper': [], 'Caretaker': [], 'Vet': []}
        for w in self.workers:
            if w.__class__.__name__ == 'Keeper':
                works['Keeper'].append(w)
            elif w.__class__.__name__ == 'Caretaker':
                works['Caretaker'].append(w)
            elif w.__class__.__name__ == 'Vet':
                works['Vet'].append(w)

        text = f"You have {len(self.workers)} workers\n"

        for k, v in works.items():
            text += f"----- {len(v)} {k}s:\n"
            for x in v:
                text += f"{x}\n"
        return text
