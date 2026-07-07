import usb.core
import usb.util

# Encuentra todos los dispositivos USB conectados
devices = usb.core.find(find_all=True)

if not devices:
    print("No se encontraron dispositivos USB.")
else:
    print("Dispositivos USB conectados:")
    for dev in devices:
        # Obtener información del dispositivo
        # Intenta obtener el descriptor del dispositivo
        try:
            manufacturer = usb.util.get_string(dev, dev.iManufacturer)
        except (ValueError, IndexError):
            manufacturer = "Desconocido"

        try:
            product = usb.util.get_string(dev, dev.iProduct)
        except (ValueError, IndexError):
            product = "Desconocido"

        print(f"  ID de Vendedor (Vendor ID): 0x{dev.idVendor:04x}")
        print(f"  ID de Producto (Product ID): 0x{dev.idProduct:04x}")
        print(f"  Fabricante: {manufacturer}")
        print(f"  Producto: {product}")
        print(f"  Número de serie: {dev.serial_number}")
        print(f"  Clase de dispositivo: {dev.bDeviceClass}")
        print("-" * 30)

        # Puedes añadir lógica aquí para filtrar por idVendor y idProduct
        # if dev.idVendor == 0xXXXX and dev.idProduct == 0xYYYY:
        #     print("¡Este es mi dispositivo!")