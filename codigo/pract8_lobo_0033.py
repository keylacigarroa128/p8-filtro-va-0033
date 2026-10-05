
import cv2

# Cargar la imagen
imagen = cv2.imread("lobo.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro Gaussiano
imagen_suavizada = cv2.GaussianBlur(
    imagen,
    (7, 7),
    0
)

# Mostrar imágenes
cv2.imshow("Imagen original de lobo 0033", imagen)
cv2.imshow("Imagen suavizada - Filtro Gaussiano - de el lobo 0033", imagen_suavizada)

# Guardar resultado
cv2.imwrite(
    "../resultados/paisaje_gaussiano.jpg",
    imagen_suavizada
)

print("Filtro Gaussiano aplicado correctamente.")
print("Resultado guardado en:")
print("../resultados/paisaje_gaussiano.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()

print(" Keyla Paola NC = 0033")