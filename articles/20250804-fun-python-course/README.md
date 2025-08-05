These files are associated with my 4 August 2025 LinkedIn article titled "Free, Fun, AI-Focused Introduction to Python? - Yes; Taught by Google's 'cat-man'? - Yes and No"

The article tells about my experience with [DeepLearning.AI](https://deeplearning.ai)'s [AI Python for Beginners](https://learn.deeplearning.ai/courses/ai-python-for-beginners) course, taught by Andrew Ng.

The course was divided into 4 short sub-courses, each designed to be completed in one week:
- Week 1: Basics of AI Python Coding
- Week 2: Automating Tasks with Python
- Week 3: Working with Your Own Data and Documents in Python
- Week 4: Extending Python with Packages and APIs

As explained at [How to download slides for this course?](https://community.deeplearning.ai/t/how-to-download-slides-for-this-course/692935/5),
PDF lecture notes for the course can be downloaded from [AP4B: Lecture Notes](https://community.deeplearning.ai/t/ap4b-lecture-notes/731257).

# To try out the code for yourself, using Microsoft VS Code on Windows, do the following:

- If you haven't already done so, download/install Python and VS Code.
- In VS Code, install the Python and Jupyter extensions.
- Create a Python virtual environment for the project. One way to do so is
    - Within your project's main folder, in a VS Code terminal window:
            - python -m venv .venv
- Activate that virtual environment. One way to do so is to do the following in a VS Code terminal window:
    - Select your new virtual environment's Python interpreter as your project's Python interpreter.
    - Activate that virtual environment.
- Install project dependencies by executing the following:
    - pip install -r requirements.txt

# The code files

- build-fun-python-course-gif.py is a standalone Python script, which can be run within your virtual environment.
- Both cat-sonnet-project.ipynb and zen_of_python.ipynb are Jupyter Notebooks, which are run differently than standard Python scripts.
    - If you're not familiar with Jupyter Notebooks, you can find out more about them in the article [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
    - Because each of these two particular notebooks prompts an LLM, you'll need your own valid OpenAI API key before you can run either of them. If you don't already have one, you can get one by doing the following:<br>
        - Go to https://platform.openai.com/ and sign in or create an OpenAI account.<br>
        - When signed in, create an API key, which may require purchasing a credit for some small amount (such as $5 USD). Executing the code for this project should only use a small fraction of that.
    - To make the Jupyter Notebooks aware of your API key, copy example.env to .env, and substitute your API key (enclosed in double quotation marks) for "My-OpenAI-API-Key".
    - The first time you open either of the notebooks, you'll need to select your new virtual environment's Python interpreter as the interpreter for the notebook. 

# See [Tools Used](tools_used.md) for more information on the tools I used to create this article
