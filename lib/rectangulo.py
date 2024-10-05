def get_area(largo: int, ancho: int) -> int:
    """Calcula el área de un rectángulo dado su largo y ancho."""
    return largo * ancho

def get_identificador() -> str:
    """Devuelve el identificador del tipo de figura."""
    return "rectángulo"

def get_perimetro(largo: int, ancho: int) -> int:
    """Calcula el perímetro de un rectángulo dado su largo y ancho."""
    return 2 * (largo + ancho)
