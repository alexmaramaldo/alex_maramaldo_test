# Alex Maramaldo Test
The project has 3 main files, `test_a.py`, `test_b.py` and `test_c.py`, with the answer about exercise.
To run a specific file, you need to run `python test_a.py` and can see the result on stout from the console.

# Configuration
You need to run `pip install -r requirements.txt` to install the base to the project.

# Question A
Run `python test_a.py`
Have a simple execute file importing the Overlap Class, this files is inside `my_libraries` folder, and have the name `overlap.py`

# Question B
Run `python test_b.py` to check the simple example
Run `pytest` if you need to check the tests, you need to install the requirements before
In this question, I created the StringCompare Class on `my_libraries` folder, and the tests on the `tests` folder.

# Question C
Run `python test_c.py` to check the examples
I created a class Cache Handler, using the library DiskCache, so the Disk Cache have a simple structure to save all the cache on SQLite, and you can use the time to expiration it, my main idea was using is with a custom configuration and ANNOTATIONS,
after it, it is most easy to use the main method, is just put @cache_method on top from methods, and, dynamically, the cache will be saved with a custom name using the params to create the unique name.
