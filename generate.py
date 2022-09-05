import random
import json


with open('random'+ str(random.randint(0,100)) +'.txt', 'w') as f:
    data = [random.randint(0, 100) for _ in range(100)]
    f.write(json.dumps(data))
