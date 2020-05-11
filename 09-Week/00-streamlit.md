
# Streamlit and Conda

## Learning objectives
By the end of this lesson students will be able to
1. Use a terminal from within VSCode
1. Create, activate and deactivate conda environments
1. Understand virtual environments 
1. Create a streamlit app to serve models and visualizations
1. Know when streamlit might be a good solution 
1. Understand how streamlit operates at a high level
1. Use plotly express to create interactive visualizations

## Create a new conda environment

1. Open VSCode (or if you insist, a different text editor you know well:) ) 
1. Make a new conda environment named `st` [Common conda commands] (https://gist.github.com/discdiver/0bb3bf96f02c182f96d45278f9564551)
    - it does not matter what folder you are in
    - install the packages `python pandas numpy plotly` at creation
    - 

1. Deactivate your current conda environment and any other virtual environments
1. Activate your `st` conda environment
    - you are now in a virtual environment
    - `conda list` to see what is in the environment
1. When it is active `pip install streamlit`
    - why does your conda virtual environment need to be active before installing?


## Create a streamlit app

1. Arrange your screen(s) so you can see a browser window and your text editor. 
1. Navigate to the folder where you want to create your app
1. Make a new python file named `my_app.py`
1. In the file, add `import streamlit as st` and save the file
1. In the terminal, in the same directory as your `my_app.py` file execute `streamlit run my_app.py`
    - You should see a browser window pop up


The rest of the lesson will be coding in our `my_app.py` file and a discussion of what streamlit is, how to use it, and when to use it.

If we get ambitious, we'll also discuss local imports, docker, kubernetes, code style, and black. 😀