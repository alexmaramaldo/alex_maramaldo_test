from my_libraries.cache_handler import cache_method


@cache_method
def teste_cache(param1, param2):
    return 1


result = teste_cache("Alex", "Maramaldo")
print(result)
result = teste_cache("Alex", "Maramaldo")
