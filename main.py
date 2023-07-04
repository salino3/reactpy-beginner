# python -m venv venv
# pip install "reactpy[starlette]"
# pip install fastapi uvicorn # run ya lo no importo

#*> uvicorn main:app --reload

from fastapi import FastAPI
from reactpy import component, html 
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

 
@component
def App():
    return html.header(
        html.h1("My Task List!"),
        html.ul(
          html.li("Learn ReactPy"),
          html.li("Learn FastAPI"),
          html.li("Build something awesome"),
          html.img({
              "src": "https://picsum.photos/id/237/200",
              "style": {
                  "border": "solid blue 5px"
              },
              "alt": "random image"  

            })
        ),
       
    ) 

configure(app, App) 
  
# run(App)










