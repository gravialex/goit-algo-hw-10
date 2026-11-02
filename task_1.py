import time
from typing import Dict, List


def find_coins_greedy(amount: int, coins: List[int]) -> Dict[int, int]:
    result = {}
    for coin in coins:
        if amount <= 0:
            break
        count = amount // coin
        if count > 0:
            result[coin] = count
            amount -= coin * count
    return result


def find_min_coins(amount: int, coins: List[int]) -> Dict[int, int]:
    # мінімальна кількість монет для суми i
    min_coins = [float("inf")] * (amount + 1)
    min_coins[0] = 0

    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = coin_used[current_amount]
        result[coin] = result.get(coin, 0) + 1
        current_amount -= coin

    # Сортуємо результат за номіналом монет у зростаючому порядку
    sorted_result = {k: result[k] for k in sorted(result.keys(), reverse=False)}
    return sorted_result


if __name__ == "__main__":
    available_coins = [50, 25, 10, 5, 2, 1]
    test_amounts = [113, 1_123, 5_321, 12_345, 123_456]

    print(f"Доступні номінали: {available_coins}\n")

    for test_amount in test_amounts:
        print(f"--- Тестування для суми: {test_amount} ---")

        # Вимірювання часу жадібного алгоритму
        start_time = time.perf_counter()
        greedy_result = find_coins_greedy(test_amount, available_coins)
        greedy_time = time.perf_counter() - start_time

        # Вимірювання часу динамічного програмування
        start_time = time.perf_counter()
        dp_result = find_min_coins(test_amount, available_coins)
        dp_time = time.perf_counter() - start_time

        print(f"Жадібний алгоритм: {greedy_result} | Час: {greedy_time:.6f} сек")
        print(f"Динамічне програмування: {dp_result} | Час: {dp_time:.6f} сек")
        print()