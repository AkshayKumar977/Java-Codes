import flet as ft
from flet import Icons
import math
import sympy
from sympy import factorial,sin,cos,tan,pi
def main(page:ft.Page):
    page.title = "Scientific Calculator"
    expression = ""
    display = ft.TextField(value = "",read_only = True)
    def themeswitch(e):
        if e.control.value:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        button.label = ft.Text(f"{page.theme_mode.value} theme")
        page.update()
    def button_click(f):
        nonlocal expression
        button_value = f.control.text
        if button_value == "=":
            expr = expression
            expr = expr.replace('π','pi')
            expr = expr.replace('^2','**2')
            expr = expr.replace("^3","**3")
            expr = expr.replace("√","sqrt")
            expr = expr.replace("^-1","**-1")
            expr = expr.replace('fact','factorial')
            if 'sin⁻¹' in expr:
                expr = expr.replace('sin⁻¹','asin')
            elif 'cos⁻¹' in expr:
                expr = expr.replace('cos⁻¹','acos')
            elif 'tan⁻¹' in expr:
                expr = expr.replace('tan⁻¹','atan')
            result = sympy.sympify(expr,locals = {
                
              "pi": sympy.pi,
               "sin": sympy.sin,
              "cos": sympy.cos,
              "tan": sympy.tan,
              "asin": sympy.asin,
               "acos": sympy.acos,
              "atan": sympy.atan,
              "sqrt": sympy.sqrt,
               "log": sympy.log,
               "ln": sympy.ln,
              "factorial": sympy.factorial,
              "nPr": lambda n, r: math.perm(n, r),
              "nCr": lambda n, r: math.comb(n, r)
})

            
            result_eval = sympy.N(result)
            display.value = str(result_eval)
            expression = str(result_eval)
        elif button_value == "C":
            expression = ""
            display.value = ""
        elif button_value == "DEL":
            expression = expression[:-1]
            display.value = expression
        else:
            expression+=button_value
            display.value = expression
        
        page.update() 
    button = ft.Switch(label = "Theme",on_change=themeswitch)
   
    
    page.add(
        ft.Container(
            display,
            bgcolor = "blue",
            margin = 20,
            padding = 10
        ),
        ft.Row([
            ft.ElevatedButton("sin",on_click = button_click),
            ft.ElevatedButton("cos",on_click = button_click),
            ft.ElevatedButton("tan",on_click = button_click),
            ft.ElevatedButton('π',on_click = button_click),
            ft.ElevatedButton('sin⁻¹',on_click = button_click),
            ft.ElevatedButton('cos⁻¹',on_click = button_click),
            ft.ElevatedButton('tan⁻¹',on_click = button_click),
        ]),
        ft.Row([
        ft.ElevatedButton("7",on_click = button_click),
        ft.ElevatedButton("8",on_click = button_click),
        ft.ElevatedButton("9",on_click = button_click),
        ft.ElevatedButton("/",on_click = button_click),
        ft.ElevatedButton("^2",on_click = button_click),
        ft.ElevatedButton("^3",on_click = button_click),
        ft.ElevatedButton("√",on_click = button_click)

        ]),
        ft.Row([
            ft.ElevatedButton("4",on_click = button_click),
            ft.ElevatedButton("5",on_click = button_click),
            ft.ElevatedButton("6",on_click = button_click),
            ft.ElevatedButton("*",on_click = button_click),
            ft.ElevatedButton("log",on_click = button_click),
            ft.ElevatedButton("ln",on_click = button_click),
            ft.ElevatedButton("nPr",on_click = button_click), 
        ]),
        ft.Row([
            ft.ElevatedButton("1",on_click = button_click),
            ft.ElevatedButton("2",on_click = button_click),
            ft.ElevatedButton("3",on_click = button_click),
            ft.ElevatedButton("-",on_click = button_click),
            ft.ElevatedButton("nCr",on_click = button_click),
            ft.ElevatedButton("fact",on_click = button_click),
            ft.ElevatedButton("^-1",on_click = button_click)
        ]),
        ft.Row([
            ft.ElevatedButton("0",on_click = button_click),
            ft.ElevatedButton(".",on_click = button_click),
            ft.ElevatedButton("=",on_click = button_click),
            ft.ElevatedButton("+",on_click = button_click),
            ft.ElevatedButton(",",on_click = button_click)

        ]),
        ft.Row([
            ft.ElevatedButton("(",on_click = button_click),
            ft.ElevatedButton(")",on_click = button_click),
            ft.ElevatedButton("C",on_click = button_click),
            ft.ElevatedButton("DEL",on_click = button_click)

        ]),
        ft.Row(
        controls=[button],
        alignment=ft.MainAxisAlignment.END,
        
    ),
        
    )
ft.app(target = main)