from time import sleep
import api_runner_func

update_interval = 2
no_itr = 5

def main():
    crypto_data = get_crypto_data(API_URL, PARAMS, API_KEY)
    if crypto_data:
        for i in range(no_itr):
            update_csv(crypto_data, 'api_project.csv')
            sleep(update_interval)

if __name__ == "__main__":
    main()
