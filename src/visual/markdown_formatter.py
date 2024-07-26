from rich.console import Console
from rich.markdown import Markdown


class MarkdownFormatter:
    def __init__(self):
        self.console = Console()

    def format_markdown(self, markdown_text):
        """
        Formatea y muestra el texto Markdown en la terminal.

        Args:
            markdown_text (str): El texto Markdown a formatear y mostrar.
        """
        md = Markdown(markdown_text)
        self.console.print(md)


if __name__ == "__main__":
    formatter = MarkdownFormatter()
    markdown_text = """
        # Título Principal

        Este es un párrafo con **negrita** y *cursiva*.

        ## Subtítulo

        - Elemento de lista 1
        - Elemento de lista 2
        - Elemento de lista 3

        ```python
        # Código de ejemplo en Python
        print("Hola, mundo!")
    """
    formatter.format_markdown(markdown_text)

