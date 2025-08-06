# Free, Fun, AI-Focused Introduction to Python? Yes! Taught by Google’s "cat man"? Yes and No.

With so many free introductory Python courses online, is there really a need for another? My answer is a definite "yes."

I recently completed [DeepLearning.AI](https://www.linkedin.com/company/deeplearningai/)’s free, four-week [AI Python for Beginners](https://www.deeplearning.ai/short-courses/ai-python-for-beginners/) course. Although I already knew the basics of Python, I hadn’t programmed extensively with it. And I saw the course as a good way to familiarize myself with DeepLearning.ai’s learning platform and to introduce me to some of the ways Python can interface with AI.

![.GIF showing 2 Jupyter notebooks, an 'Is this a cat?' slide show, and my course certificate](images/fun-python-course.gif)

The course is divided into four "weeks," each with a different focus.

## Week 1: Basics of AI Python Coding
For me, this was largely review, except for the AI focus of Lesson 9 ("Building LLM prompts with variables") and the "Using functions in AI programs" section of Lesson 10 ("Functions - Actions on Data"). Two of the more memorable, fun examples were programmatically prompting an LLM (large language model) to write a 300-word children’s story and to write a poem with a specified number of lines about a specified topic.

## Week 2: Automating Tasks with Python
We used Python to prompt an LLM to compose a brief email message, write a "Happy Birthday" poem for a friend, write a 300-word movie review, provide promotional descriptions of ice cream flavors, translate the flavors from English to Spanish, draft a thank-you note, create a presentation outline, get recipe recommendations, and create a shopping list. That was much more interesting than many of the examples and exercises typically used in an introductory Python course!

## Week 3: Working with Your Own Data and Documents in Python
In the week’s final lesson, we had an LLM create detailed travel itineraries for seven major world cities from information we were given. The first piece of information was a .csv file listing planned arrival and departure dates for each city and the country the city was in. The second was a .txt travel journal for each city, from which we prompted an LLM to extract .csv files listing restaurants mentioned, with a specialty dish for each. Then we prompted it to create a daily itinerary for each city, with detailed activities and meals at the mentioned restaurants.

## Week 4: Extending Python with Packages and APIs
We explored some of Python’s built-in packages like math, statistics, and random. And we also installed free, third-party packages from PyPI ([Python’s Package Index](https://pypi.org/)):
- pandas (described on PyPI as a "powerful Python data analysis toolkit"): Used to load and filter car sales data. 
- matplotlib ("a comprehensive library for creating static, animated, and interactive visualizations"): Used to create scatter plots of car pricing data and a pie chart of car sales data.
- requests ("Python HTTP for Humans") and Beautiful Soup (a "screen-scraping library"): Used to download the content from a webpage and extract information from it, with an LLM used to summarize the information.
- aisetup ("source code repository for deeplearning.ai courses"): Used to make course "helper functions" (like get_llm_response() and print_llm_response()) available outside the course.
- openai ("the official Python library for the OpenAI API package"): Used with OpenAI’s Chat Completions API (using our own API keys), including experimenting with changing the system role and the temperature (randomness).

I can’t share with you the actual code we used in the course. So, I’ve instead included two Jupyter notebooks that do things similar to what was done in the course:
- [zen_of_python.ipynb](zen_of_python.ipynb): A Jupyter notebook that asks an LLM about the "Zen of Python"
- [cat_sonnet_project.ipynb](cat_sonnet_project.ipynb): A Jupyter notebook that prompts an LLM with:
    - Write [a sonnet about the Google Brain Project](sonnet.md), mentioning the involvement of both [Andrew Ng](https://www.linkedin.com/in/andrewyng/) and [Jeff Dean](https://www.linkedin.com/in/jeff-dean-8b212555/), and why the latter has sometimes been called the "cat man".
    - The poem should be in Shakespearean style, with each line exactly 10 syllables long and a rhyme scheme of ABABCDCDEFEFGG.
    - Precede the poem with a title in bold, and ensure that the poem is formatted in Markdown.

And I’ve also included [build_fun_python_course_gif.py](build_fun_python_course_gif.py): A Python script that creates an animated .gif file showing:
    - The above 2 Jupyter notebooks
    - An "Is this a cat?" slide show, **very loosely** modeled after the "Google Brain Project"
    - My "AI Python for Beginners" course completion certificate

That's the .gif file displayed at the top of this article.

Who should take this course? Anyone relatively new to Python or interested in a fun, practical introduction to using Python with AI. There are no course prerequisites, and no specific prior knowledge or experience is needed. There's no need to install Python or anything else. For most lessons, the online course platform has a Jupyter notebook on the left and an accompanying video on the right. 

If you’re wondering what I meant by "Taught by Google’s 'cat man'? Yes and No.", let me explain. [Andrew Ng](https://www.linkedin.com/in/andrewyng/), the course instructor, founded and led Google’s famous "cat project," so someone **might** call **him** "Google’s 'cat man.'" However, I read that [Jeff Dean](https://www.linkedin.com/in/jeff-dean-8b212555/), a senior engineer on that project, was actually the one "favored" with that nickname. For more information on the project, see the article [Google brain simulator teaches itself to recognize cats](https://www.zdnet.com/article/google-brain-simulator-teaches-itself-to-recognize-cats/) on ZDNet. Or ask [😺 GPT](https://chatgpt.com/g/g-NDDXC050T-catgpt)! (Yes, there really is a ***[CAT gpt](https://chatgpt.com/g/g-NDDXC050T-catgpt)***! ). 



This write-up and accompanying code are my own work, inspired and assisted by AI tools where needed:
- I wrote the article myself, using several tools to check my spelling, grammar, and style. And I incorporated a number of improvements suggested by Perplexity AI.
- I wrote the Python code myself. As encouraged to do in the course, if I didn’t know how to do something, I asked AI for assistance.
- And I used AI to generate the individual image files for my "Is this a cat?" slide show.

I thoroughly enjoyed the course. I really like DeepLearning.ai’s learning platform. And the course instructor, Andrew Ng, seems to be one of those rare individuals who is an expert in his field yet knows how to instruct those with much less knowledge and experience in that field. I learned some ways Python can interface with AI, and even gained more Python knowledge than I expected.

If you’re interested in learning more about using Python with AI, I highly recommend this course. It's accessible, creative, fun, and practical.

Let me know in the comments if you have other AI-focused Python courses you'd recommend, or if there's anything you'd like to ask me about this one.
