"""
Contains the string formatter for our test case request body.
"""


from getgauge.python import data_store

import uuid, string
from random import randint, SystemRandom


def string_format(data):
    if "<null>" in data:
        '''
        <null>          --->   None
        abc<null>def    --->   None
        '''
        return None
    elif "<empty>" in data :
        '''
        <empty>          --->   ''
        abc<empty>def    --->   ''
        '''
        return ""
    elif "<empty_array>" in data:
        '''
        <empty_array>          --->   []
        abc<empty_array>def    --->   []
        '''
        return []
    elif "<skip>" in data:
        return "SKIP"
    elif "<timestamp>" in data:
        '''
        <timestamp>              --->   '16712345678'
        abc<timestamp>def        --->   'abc16712345678def'
        <timestamp>@yahoo.com    --->   '16712345678@yahoo.com'
        '''
        return data.replace("<timestamp>", data_store.scenario.timestamp)
    elif "<bool_true>" in data:
        return True
    elif "<bool_false>" in data:
        return False
    elif "<uuid>" in data:
        '''
        <uuid>              --->   'abcd-1234-qwer-5678'
        <uuid>@yahoo.com    --->   'abcd-1234-qwer-5678@yahoo.com'
        '''
        uuid_data = str(uuid.uuid4())
        return data.replace("<uuid>", uuid_data)
    elif "<numbers_" in data:
        '''
        <numbers_5>          --->   '12345' (random)
        abc<numbers_5>def    --->   'abc12345def' (random)
        '''
        # Get index of "<" and ">" to replace only the <numbers_..> with generated number
        start_index = data.index("<")
        end_index = data.index(">")

        count = int(data[start_index:end_index].split("_")[1])
        # count[0] = numbers , count[1] = 8
        # count = int(count[1].replace(">",""))
        generated_number = ""

        for i in range(count):
            generated_number += str(randint(0,9))

        return data.replace(data[start_index:end_index + 1], generated_number)
    elif "<random_" in data:
        '''
        <random_5>          --->   'a1b2c' (random)
        abc<random_5>def    --->   'abcz1x2cdef' (random)
        '''
        # Get index of "<" and ">" to replace only the <random_..> with generated number
        start_index = data.index("<")
        end_index = data.index(">")
        # count[0] = random_ , count[1] = 5
        count = int(data[start_index:end_index].split("_")[1])

        generated_random_text = ''.join(SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(count))
        return data.replace(data[start_index:end_index + 1], generated_random_text)

    elif "<randomUpper_" in data:
        '''
        <random_5>          --->   'a1b2c' (random)
        abc<random_5>def    --->   'abcz1x2cdef' (random)
        '''
        # Get index of "<" and ">" to replace only the <random_..> with generated number
        start_index = data.index("<")
        end_index = data.index(">")
        # count[0] = random_ , count[1] = 5
        count = int(data[start_index:end_index].split("_")[1])

        generated_random_text = ''.join(SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(count))
        return data.replace(data[start_index:end_index + 1], generated_random_text)

    elif "<spaces_" in data:
        '''
        <spaces_5>          --->   '     '
        abc<spaces_5>123    --->   'abc     123'
        '''
        # Get index of "<" and ">" to replace only the <numbers_..> with generated number
        start_index = data.index("<")
        end_index = data.index(">")

        count = int(data[start_index:end_index].split("_")[1])
        # count[0] = numbers , count[1] = 8
        # count = int(count[1].replace(">",""))
        generated_spaces = ""

        for i in range(count):
            generated_spaces += " "

        return data.replace(data[start_index:end_index + 1], generated_spaces)
    elif "<empty_" in data :
        '''
        <empty_5>          --->   '     '
        abc<empty_5>123    --->   '     '
        '''
        # Get index of "<" and ">" to replace only the <empty_..> with generated number
        start_index = data.index("<")
        end_index = data.index(">")
        generated_spaces = ""

        count = int(data[start_index:end_index].split("_")[1])
        for i in range(count):
            generated_spaces += " "
        return generated_spaces

    elif "<phone>" in data:
        generated_phone_number = ""
        for _ in range(10):
            generated_phone_number += str(randint(0,9))
        return generated_phone_number
    elif "<tin>" in data:
        tin = ""
        for _ in range(0,12):
            random_number = randint(0,9)
            tin += str(random_number)
        return tin
    else:
        return data
