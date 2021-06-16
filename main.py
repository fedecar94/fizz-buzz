def fizz_buzz(max_number: int) -> None:
    fizz = 0
    buzz = 0

    for number in range(max_number + 1):
        message = ''

        if fizz == 3:
            message += 'Fizz'
            fizz = 0

        if buzz == 5:
            message += 'Buzz'
            buzz = 0

        if len(message) == 0:
            message = str(number)

        print(message)
        fizz += 1
        buzz += 1


if __name__ == '__main__':
    fizz_buzz(99)
