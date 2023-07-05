# python -m venv venv
# pip install "reactpy[starlette]"
# pip install fastapi uvicorn # run ya lo no importo

#*> uvicorn main:app --reload

from fastapi import FastAPI
from reactpy import component, html, hooks 
from reactpy.backend.fastapi import configure

app = FastAPI()

# @component
# def GoodComponent():
#   return html.p("This is a good component")

# @component
# def BadComponent():
#     try:
#         msg = "This is an error component"
#         raise RuntimeError(msg)
#     except RuntimeError as e:
#         return html.p("Error occurred: " + str(e))

# minuto 20.35  -  https://www.youtube.com/watch?v=EE3wnE0nb4U&list=PLR6Dij52PfvM68Kn7zQcoPLv_1YFH_Kp0&index=2&ab_channel=FaztCode

@component
def Task(task):
    counter, set_counter = hooks.use_state(0)
    
    def handle_click(event):
        set_counter(counter + 1)
        print("Clicked!")

    if task['priority'] > 1:
        return html.li({"key": task['id'],
                   "style": {
                       "background": "#FFFF3F",
                       "padding": "1rem",
                       "border": "1px solid black",
                       "margin": "1rem"
                       }
                   }, f" ⚠️ { task['text']} - { task['priority']}")
    else:
        return html.li({"key": task['id'],
                   "style": {
                       "background": "lightblue",
                       "padding": "1rem",
                       "border": "1px solid black",
                       "margin": "1rem"
                       }
                   }, html.div( {
                       "style": {
                           "display": "flex",
                           "justify-content": "space-between",
                       }
                   },
            f"{ task['text']} - { task['priority']} - {counter}",
            html.button({
                "on_click": handle_click
            },"Delete")
                   ))       
    


@component
def TaskList():
    tasks = [
        {"id": 0, "text": "make breackfast", "priority": 1},
        {"id": 0, "text": "do something", "priority": 1},
        {"id": 1, "text": "make lunch", "priority": 2},
        {"id": 2, "text": "make dinner", "priority": 2},
        {"id": 3, "text": "make dessert", "priority": 4},
    ]
    data = [Task(task) for task in tasks]

    return html.ul(
       data
    )


@component
def App():
    return html.main(
        html.h1("My Tasks"),
        html.div(
      TaskList()
        )
    )  

configure(app, App) 
  
# run(App)










