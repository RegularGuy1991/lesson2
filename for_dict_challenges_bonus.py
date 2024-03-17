"""
Пожалуйста, приступайте к этой задаче после того, как вы сделали и получили ревью ко всем остальным задачам
в этом репозитории. Она значительно сложнее.


Есть набор сообщений из чата в следующем формате:

```
messages = [
    {
        "id": "efadb781-9b04-4aad-9afe-e79faef8cffb",
        "sent_at": datetime.datetime(2022, 10, 11, 23, 11, 11, 721),
        "sent_by": 46,  # id пользователя-отправителя
        "reply_for": "7b22ae19-6c58-443e-b138-e22784878581",  # id сообщение, на которое это сообщение является ответом (может быть None)
        "seen_by": [26, 91, 71], # идентификаторы пользователей, которые видели это сообщение
        "text": "А когда ревью будет?",
    }
]
```

Так же есть функция `generate_chat_history`, которая вернёт список из большого количества таких сообщений.
Установите библиотеку lorem, чтобы она работала.

Нужно:
1. Вывести айди пользователя, который написал больше всех сообщений.
2. Вывести айди пользователя, на сообщения которого больше всего отвечали.
3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.
4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).
5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

Весь код стоит разбить на логические части с помощью функций.
"""
import random
import uuid
import datetime, time 

import lorem

from collections import Counter


def generate_chat_history():
    messages_amount = random.randint(200, 1000)
    users_ids = list(
        {random.randint(1, 10000) for _ in range(random.randint(5, 20))}
    )
    sent_at = datetime.datetime.now() - datetime.timedelta(days=100)
    messages = []
    for _ in range(messages_amount):
        sent_at += datetime.timedelta(minutes=random.randint(0, 240))
        messages.append({
            "id": uuid.uuid4(),
            "sent_at": sent_at,
            "sent_by": random.choice(users_ids),
            "reply_for": random.choice(
                [
                    None,
                    (
                        random.choice([m["id"] for m in messages])
                        if messages else None
                    ),
                ],
            ),
            "seen_by": random.sample(users_ids,
                                     random.randint(1, len(users_ids))),
            "text": lorem.sentence(),
        })
    return messages


if __name__ == "__main__":
   array = generate_chat_history()

users_id = []
reply_for = []
all_messages = []
seen_by = []

# 1. Вывести айди пользователя, который написал больше всех сообщений.



for i in array:
        users_id.append(i["sent_by"])
        reply_for.append(i['reply_for'])
        all_messages.append(i['id'])
        seen_by.append(i['seen_by'])

def most_messages_id(lst):
    value_counts = Counter(users_id)
    max_value = max(value_counts, key = value_counts.get)
    all_equal = all(value == list(value_counts.values())[0] for value in value_counts.values())
    if all_equal:
         return print(f'Все пользователи написали одинаковое количество сообщений, сообщений: {list(value_counts.values())[0]}')
    else:
         return print(f'Больше всех сообщений написал: {max_value}, сообщений: {max(value_counts.values())}')

most_messages_id(users_id)


# 2. Вывести айди пользователя, на сообщения которого больше всего отвечали.

def most_replied_message(lst):
    value_counts = Counter(x for x in reply_for if x is not None)
    message_id = max(value_counts, key = value_counts.get)
    return message_id


def find_user_from_id(messages):
     for one_message in messages:
          if one_message['id'] == most_replied_message(reply_for):
               return one_message['sent_by']
          

print(f'Чаще всего отвечали на сообщения пользователя: {find_user_from_id(array)} id сообщения: {most_replied_message(reply_for)}')

# 3. Вывести айди пользователей, сообщения которых видело больше всего уникальных пользователей.


# {'id': UUID('6387f5ba-628a-4037-b266-9511afe18ace'), 'sent_at': datetime.datetime(2024, 2, 24, 0, 28, 13, 807941),
#   'sent_by': 4185, 'reply_for': None, 'seen_by': [8171, 4739, 7203, 9101, 5676, 7247, 7547, 4185, 793, 434, 7969, 1676], 
#   'text': 'Dolorem est amet dolor neque non.'}



def most_seen_messgae(arr):
     seen_by_list = {}
     for message in arr:
          seen_by_list[message['sent_by']] = len(message['seen_by'])
          return print(f'Сообщение пользователя {max(seen_by_list)} увидели больше всего уникальных пользователей')
        
most_seen_messgae(array)

# 4. Определить, когда в чате больше всего сообщений: утром (до 12 часов), днём (12-18 часов) или вечером (после 18 часов).

def most_message_time(arr):
    morning_messages = 0
    day_massages = 0
    evening_messages = 0
    count = 0
    for i in array:
        count += 1
        time_only = i['sent_at'].time()
    if time_only < datetime.time(12):
        morning_messages += 1
    if time_only >= datetime.time(12) and time_only < datetime.time(18):
        day_massages += 1
    else:
        evening_messages += 1
        return morning_messages, day_massages, evening_messages, count

print(most_message_time(array))

# 5. Вывести идентификаторы сообщений, который стали началом для самых длинных тредов (цепочек ответов).

def most_replied_message(lst):
    value_counts = Counter(x for x in reply_for if x is not None)
    message_id = max(value_counts, key = value_counts.get)
    return message_id

print(f'сообщение с самым длинным тредом: {most_replied_message(reply_for)}')