import tkinter as tk
import math
import re


class ScientificCalculator:
    def __init__(self, root):
        self.root = root

        # =========================
        # WINDOW
        # =========================
        self.root.title("Calculator")
        self.root.geometry("450x720")
        self.root.resizable(False, False)
        self.root.configure(bg="#121212")

        self.expression = ""
        self.degree_mode = True

        # =========================
        # COLORS
        # =========================
        self.bg = "#121212"
        self.display_bg = "#1E1E1E"
        self.number_bg = "#292929"
        self.function_bg = "#333333"
        self.operator_bg = "#FF9500"
        self.special_bg = "#A5A5A5"
        self.text_white = "#FFFFFF"
        self.text_dark = "#121212"
        self.border = "#3A3A3A"

        # =========================
        # HEADER
        # =========================
        header = tk.Frame(
            root,
            bg=self.bg
        )
        header.pack(
            fill="x",
            padx=18,
            pady=(15, 5)
        )

        title = tk.Label(
            header,
            text="CALCULATOR",
            font=("Arial", 16, "bold"),
            bg=self.bg,
            fg=self.text_white
        )
        title.pack(side="left")

        self.mode_button = tk.Button(
            header,
            text="DEG",
            font=("Arial", 10, "bold"),
            bg="#252525",
            fg="#FF9500",
            activebackground="#333333",
            activeforeground="#FF9500",
            relief="flat",
            bd=0,
            width=5,
            height=1,
            cursor="hand2",
            command=self.change_mode
        )
        self.mode_button.pack(side="right")

        # =========================
        # DISPLAY
        # =========================
        display_frame = tk.Frame(
            root,
            bg=self.display_bg,
            highlightbackground=self.border,
            highlightthickness=1
        )
        display_frame.pack(
            fill="x",
            padx=18,
            pady=12
        )

        self.display = tk.Entry(
            display_frame,
            font=("Arial", 30),
            justify="right",
            bg=self.display_bg,
            fg=self.text_white,
            insertbackground=self.text_white,
            relief="flat",
            bd=0
        )

        self.display.pack(
            fill="x",
            padx=15,
            pady=22
        )

        # =========================
        # BUTTON AREA
        # =========================
        button_frame = tk.Frame(
            root,
            bg=self.bg
        )
        button_frame.pack(
            padx=14,
            pady=5
        )

        buttons = [
            [
                ("sin", "function"),
                ("cos", "function"),
                ("tan", "function"),
                ("log", "function"),
                ("ln", "function")
            ],
            [
                ("(", "function"),
                (")", "function"),
                ("√", "function"),
                ("x²", "function"),
                ("xʸ", "function")
            ],
            [
                ("π", "function"),
                ("e", "function"),
                ("1/x", "function"),
                ("%", "function"),
                ("DEL", "delete")
            ],
            [
                ("7", "number"),
                ("8", "number"),
                ("9", "number"),
                ("÷", "operator"),
                ("AC", "clear")
            ],
            [
                ("4", "number"),
                ("5", "number"),
                ("6", "number"),
                ("×", "operator"),
                ("−", "operator")
            ],
            [
                ("1", "number"),
                ("2", "number"),
                ("3", "number"),
                ("+", "operator"),
                ("=", "equals")
            ],
            [
                ("0", "number"),
                (".", "number"),
                ("", "empty"),
                ("", "empty"),
                ("", "empty")
            ]
        ]

        for row_index, row in enumerate(buttons):

            for col_index, (text, button_type) in enumerate(row):

                if button_type == "empty":
                    continue

                bg_color = self.get_button_color(button_type)
                fg_color = self.get_text_color(button_type)

                button = tk.Button(
                    button_frame,
                    text=text,
                    font=("Arial", 14, "bold"),
                    width=5,
                    height=2,
                    bg=bg_color,
                    fg=fg_color,
                    activebackground=self.get_active_color(
                        button_type
                    ),
                    activeforeground=fg_color,
                    relief="flat",
                    bd=0,
                    cursor="hand2",
                    command=lambda value=text: self.press(value)
                )

                button.grid(
                    row=row_index,
                    column=col_index,
                    padx=4,
                    pady=4
                )

                # Efek hover
                button.bind(
                    "<Enter>",
                    lambda event,
                    b=button,
                    t=button_type:
                    self.hover_on(b, t)
                )

                button.bind(
                    "<Leave>",
                    lambda event,
                    b=button,
                    t=button_type:
                    self.hover_off(b, t)
                )

        # =========================
        # FOOTER
        # =========================
        footer = tk.Label(
            root,
            text="Python • Tkinter • Scientific Calculator",
            font=("Arial", 9),
            bg=self.bg,
            fg="#777777"
        )

        footer.pack(
            pady=12
        )

    # =====================================================
    # BUTTON COLORS
    # =====================================================

    def get_button_color(self, button_type):

        colors = {
            "number": self.number_bg,
            "function": self.function_bg,
            "operator": self.operator_bg,
            "equals": "#FF9500",
            "clear": "#D32F2F",
            "delete": "#555555"
        }

        return colors.get(
            button_type,
            self.number_bg
        )

    def get_text_color(self, button_type):

        if button_type == "clear":
            return self.text_white

        if button_type in [
            "operator",
            "equals"
        ]:
            return self.text_dark

        return self.text_white

    def get_active_color(self, button_type):

        colors = {
            "number": "#404040",
            "function": "#484848",
            "operator": "#FFB13B",
            "equals": "#FFB13B",
            "clear": "#E04A4A",
            "delete": "#666666"
        }

        return colors.get(
            button_type,
            "#404040"
        )

    # =====================================================
    # HOVER EFFECT
    # =====================================================

    def hover_on(self, button, button_type):

        button.configure(
            bg=self.get_active_color(button_type)
        )

    def hover_off(self, button, button_type):

        button.configure(
            bg=self.get_button_color(button_type)
        )

    # =====================================================
    # DEG / RAD
    # =====================================================

    def change_mode(self):

        self.degree_mode = not self.degree_mode

        if self.degree_mode:

            self.mode_button.config(
                text="DEG"
            )

        else:

            self.mode_button.config(
                text="RAD"
            )

    # =====================================================
    # BUTTON PRESS
    # =====================================================

    def press(self, value):

        if value == "":
            return

        # CLEAR
        if value == "AC":

            self.expression = ""
            self.update_display()
            return

        # DELETE
        if value == "DEL":

            self.expression = self.expression[:-1]
            self.update_display()
            return

        # EQUAL
        if value == "=":

            self.calculate()
            return

        # SQUARE ROOT
        if value == "√":

            self.expression += "sqrt("
            self.update_display()
            return

        # SQUARE
        if value == "x²":

            self.expression += "**2"
            self.update_display()
            return

        # POWER
        if value == "xʸ":

            self.expression += "**"
            self.update_display()
            return

        # PI
        if value == "π":

            self.expression += "pi"
            self.update_display()
            return

        # EULER
        if value == "e":

            self.expression += "e"
            self.update_display()
            return

        # RECIPROCAL
        if value == "1/x":

            self.expression += "1/("
            self.update_display()
            return

        # SIN
        if value == "sin":

            self.expression += "sin("
            self.update_display()
            return

        # COS
        if value == "cos":

            self.expression += "cos("
            self.update_display()
            return

        # TAN
        if value == "tan":

            self.expression += "tan("
            self.update_display()
            return

        # LOG
        if value == "log":

            self.expression += "log("
            self.update_display()
            return

        # LN
        if value == "ln":

            self.expression += "ln("
            self.update_display()
            return

        # MULTIPLICATION
        if value == "×":

            self.expression += "*"
            self.update_display()
            return

        # DIVISION
        if value == "÷":

            self.expression += "/"
            self.update_display()
            return

        # MINUS
        if value == "−":

            self.expression += "-"
            self.update_display()
            return

        # PERCENT
        if value == "%":

            self.expression += "/100"
            self.update_display()
            return

        # NORMAL BUTTON
        self.expression += value
        self.update_display()

    # =====================================================
    # FORMAT NUMBER
    # =====================================================

    def format_number(self, number):

        try:

            number = float(number)

            # Bilangan bulat
            if number.is_integer():

                return f"{int(number):,}".replace(
                    ",",
                    "."
                )

            # Bilangan desimal
            formatted = f"{number:.10f}".rstrip("0")

            integer_part, decimal_part = formatted.split(".")

            integer_part = f"{int(integer_part):,}".replace(
                ",",
                "."
            )

            return integer_part + "," + decimal_part

        except:

            return str(number)

    # =====================================================
    # FORMAT DISPLAY
    # =====================================================

    def format_display(self, expression):

        # Jika kosong
        if not expression:
            return ""

        # Jangan mengubah fungsi matematika
        if any(
            function in expression
            for function in [
                "sin",
                "cos",
                "tan",
                "log",
                "ln",
                "sqrt",
                "pi"
            ]
        ):
            return expression

        def replace_number(match):

            number = match.group()

            try:

                # Jangan mengubah angka desimal
                if "." in number:
                    return number

                return f"{int(number):,}".replace(
                    ",",
                    "."
                )

            except:

                return number

        return re.sub(
            r"\d+",
            replace_number,
            expression
        )

    # =====================================================
    # UPDATE DISPLAY
    # =====================================================

    def update_display(self):

        self.display.delete(
            0,
            tk.END
        )

        formatted = self.format_display(
            self.expression
        )

        self.display.insert(
            0,
            formatted
        )

    # =====================================================
    # CALCULATE
    # =====================================================

    def calculate(self):

        try:

            expression = self.expression

            # -------------------------
            # SIN
            # -------------------------

            def sin(x):

                if self.degree_mode:

                    x = math.radians(x)

                return math.sin(x)

            # -------------------------
            # COS
            # -------------------------

            def cos(x):

                if self.degree_mode:

                    x = math.radians(x)

                return math.cos(x)

            # -------------------------
            # TAN
            # -------------------------

            def tan(x):

                if self.degree_mode:

                    x = math.radians(x)

                return math.tan(x)

            # -------------------------
            # LOG
            # -------------------------

            def log(x):

                return math.log10(x)

            # -------------------------
            # LN
            # -------------------------

            def ln(x):

                return math.log(x)

            # -------------------------
            # SQRT
            # -------------------------

            def sqrt(x):

                return math.sqrt(x)

            # -------------------------
            # CALCULATION
            # -------------------------

            result = eval(
                expression,
                {
                    "__builtins__": {},

                    "sin": sin,
                    "cos": cos,
                    "tan": tan,

                    "log": log,
                    "ln": ln,
                    "sqrt": sqrt,

                    "pi": math.pi,
                    "e": math.e
                }
            )

            # -------------------------
            # FORMAT RESULT
            # -------------------------

            if isinstance(
                result,
                float
            ):

                if result.is_integer():

                    result = int(result)

            formatted_result = self.format_number(
                result
            )

            # Simpan nilai asli
            self.expression = str(result)

            # Tampilkan hasil
            self.display.delete(
                0,
                tk.END
            )

            self.display.insert(
                0,
                formatted_result
            )

        except ZeroDivisionError:

            self.show_error(
                "Tidak bisa dibagi 0"
            )

        except ValueError:

            self.show_error(
                "Nilai tidak valid"
            )

        except SyntaxError:

            self.show_error(
                "Ekspresi tidak lengkap"
            )

        except Exception:

            self.show_error(
                "Error"
            )

    # =====================================================
    # ERROR
    # =====================================================

    def show_error(self, message):

        self.expression = ""

        self.display.delete(
            0,
            tk.END
        )

        self.display.insert(
            0,
            message
        )


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":

    root = tk.Tk()

    calculator = ScientificCalculator(
        root
    )

    root.mainloop()