from google.colab import files
import qrcode

def generar_qr(datos, nombre_archivo):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(datos)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(nombre_archivo)
    files.download(nombre_archivo)

if __name__ == "__main__":
    # Datos que quieres codificar en el QR
    datos_para_qr = "https://www.instagram.com/mc.trending?igsh=MTJqNHFxNnludGlqdA%3D%3D&utm_source=qr"

    # Nombre del archivo de salida
    nombre_archivo_qr = "codigo_qr.png"

    # Llamada a la función para generar el código QR y descargarlo
    generar_qr(datos_para_qr, nombre_archivo_qr)
