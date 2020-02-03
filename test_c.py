from my_libraries.cache_handler import cache_method

# Using only the annotations, is possible to create simples caches data
@cache_method
def teste_cache(param1, param2):
    return param1 + " " + param2


result = teste_cache("Alex", "Maramaldo")
print(result)
result = teste_cache("Alex", "Maramaldo2")
print(result)
