

from reactpy import component, html 


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
