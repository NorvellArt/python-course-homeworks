import json
from random import choice
from typing import List, TypedDict


class IPerson(TypedDict):
    name: str
    tel: str


class IPersonObj(TypedDict):
    key: IPerson


def gen_person() -> IPerson:
    name: str = ''
    tel: str = ''

    letters: List[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    num: List[str] = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(num)

    person: IPerson = {
        'name': name,
        'tel': tel
    }
    return person


def gen_person_obj() -> IPersonObj:
    person_obj = gen_person()
    return {person_obj['tel']: {'name': person_obj['name'], 'tel': person_obj['tel']}}


def write_json(person_dict: IPersonObj) -> None:
    try:
        data: IPersonObj = json.load(open('persons.json'))
    except FileNotFoundError:
        data = person_dict

    data.update(person_dict)
    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person_obj())
