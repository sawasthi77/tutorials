import pprint
message = 'It was a bright cold day in april and clocs were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] += 1

pprint.pformat(count)