from cryptosleepwatcher.watcher import CryptoSleepWatcher

# Укажите нужные токены (CoinGecko IDs)
coins = ['bitcoin', 'ethereum', 'dogecoin']

# Интервал проверки в секундах
interval = 60  # 1 минута

# Сколько одинаковых показателей считается "сном"
sleep_threshold = 5  # 5 интервалов = 5 минут

watcher = CryptoSleepWatcher(coins, interval, sleep_threshold)
watcher.monitor()
