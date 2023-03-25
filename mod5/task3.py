class BlockErrors:
    def __init__(self, error_types: set):
        self.error_types = error_types

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return any(isinstance(exc_val, err_type) for err_type in self.error_types)


if __name__ == '__main__':
    err_types = {Exception}
    with BlockErrors(err_types):
        a = 1 / '0'
    print('Выполнено без ошибок')