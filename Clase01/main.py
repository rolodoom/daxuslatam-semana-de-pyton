# --------------------------
# Librerías
# --------------------------
from fpdf import FPDF
from babel.numbers import format_currency
from typing import Union

# --------------------------
# Variables
# --------------------------
debug = False  # True o False para activar o desactivar el modo debug

# --------------------------
# Constantes
# --------------------------
# https://babel.pocoo.org/en/latest/api/numbers.html#module-babel.numbers
# Configuración de monedas necesarias para el proyecto
CURRENCY_LOCALE_MAP = {
    "COP": "es_CO",
    "USD": "en_US",
    "GBP": "en_GB",
    "EUR": "es_ES",
}


# --------------------------
# Funciones
# --------------------------
def format_money(value: Union[str, float, int], currency: str):
    """
    Funcion para formatear el valor

    Args:
        value (float): Valor a formatear
        currency (str): Moneda a formatear

    Returns:
        str: Valor formateado
    """
    currency = currency.upper()
    locale = CURRENCY_LOCALE_MAP[currency]
    formatted = format_currency(float(value), currency, locale=locale)
    return f"{currency} {formatted}"


# --------------------------
# Entrada de datos
# --------------------------

if debug:
    # Datos de prueba
    proyecto, horas_estimadas, moneda_seleccionada, valor_hora, plazo_estimado = (
        "Un proyecto de Python",
        "34",
        "COP",
        "50000",
        "3 meses",
    )
else:
    # Entrada de datos reales
    proyecto = input("Descricpión del Proyecto: ")
    horas_estimadas = input("Horas estimadas: ")
    moneda_seleccionada = input("Moneda de pago (COP, USD, GBP, EUR): ")
    valor_hora = input("Valor de hora trabajada: ")
    plazo_estimado = input("Tiempo de entrega (estimado): ")


# --------------------------
# calcular el valor total
# --------------------------
valor_total = float(horas_estimadas) * float(valor_hora)


# --------------------------
# Creando el PDF
# --------------------------
if __name__ == "__main__":

    # Definir el tamaño y orientación del pdf
    pdf = FPDF(orientation="P", unit="mm", format=(215.9, 279.4))

    # Agregar una página
    pdf.add_page()

    # Definir el tipo de letra
    pdf.set_font("Arial")

    # Agregar la imagen de fondo con el tamaño adecuado
    pdf.image("template.png", x=0, y=0, w=215.9, h=279.4)

    # Escribir el texto en el pdf
    pdf.text(118, 153, proyecto)
    pdf.text(118, 168, horas_estimadas)
    pdf.text(118, 184, f"{format_money(valor_hora, moneda_seleccionada)}")
    pdf.text(118, 198, plazo_estimado)

    # Escribir el texto final en otro color y tamaño
    pdf.set_text_color(255, 255, 255)
    pdf.set_font_size(20)
    pdf.text(118, 215, f"{format_money(valor_total, moneda_seleccionada)}")

    # Crear el archivo pdf
    pdf.output("presupuesto.pdf")

    print("Presupuesto creado con exito")
