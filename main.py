from time import sleep
from crypto_proj import api_runner

update_interval = 2
no_itr = 5

if __name__ == "__main__":
    for i in range(no_itr):
        api_runner()
        sleep(update_interval)
    exit()