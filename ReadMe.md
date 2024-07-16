# Enable Debugging
Debuggers are essential tools in a developer's toolkit, enabling the swift identification and resolution of issues within a codebase.

Follow [this guide](https://code.visualstudio.com/docs/python/tutorial-flask#_run-the-app-in-the-debugger) to run the app in the debugger.

# Static Type Checking
Static type checkers are tools that analyze code to ensure type correctness before runtime, providing an added layer of validation in dynamically typed languages like Python. Similar to how TypeScript enhances JavaScript by introducing static types, static type checkers like Mypy bring the benefits of type safety to Python. These tools help developers catch potential errors early in the development process, leading to more reliable and maintainable code.

Follow [this guide](https://mypy.readthedocs.io/en/stable/getting_started.html) to add Mypy to your project.

Adding a .toml file to your project and setting `strict = true` will enforce strict typing. While strict may be too extreme, especially for existing code bases, you can mix typed and untyped code similar to Typescript.

# Global Error Handling and Logging
Every application should have some form of global error handling and logging.

For a Flask API, such as this one you can use `@app.errorhandler(Exception)` to manage all unhandled exceptions. Other frameworks may have their own methods of catching unhandled exceptions, but for a basic Python applications a `try: ... except: ...` block at the highest level will do.

# Adding Unit Tests and Mocks
In many applications unit tests can be help to quickly verify that code functionality has not changed unexpectedly. This can be helpful in production applications, even if it is only added as needed rather than aiming for exhaustive code coverage. I recommend using Pytest. This adds more than unittest, like better test feedback and the ability to run a single test with multiple inputs, and it is backwards compatible with unittest.