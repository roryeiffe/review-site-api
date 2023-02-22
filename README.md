## Review API

## Set Up
1. install [python](https://www.python.org/downloads/) 
   1. Choose the default options and to install pip
2. clone this repository
3. in the directory with the main.py run `pip install -r requirements.txt`
4. run `pip install "uvicorn[standard]"`
5. in the directory with the main.py run the application with `uvicorn main:app`
   1. *all data is persisted in memory*
   2. *restarting/stopping the application will erase data*
6. The applicaiton will run on port `http://localhost:8000`
   1. ***You can access interactable documentation of endpoints at `http://localhost:8000/docs`***

#### 