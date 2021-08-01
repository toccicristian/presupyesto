import repositorios.productos
import modelos.producto


def test_generar_db():
    producto = modelos.producto.Producto()
    producto.set_automatizado(False)
    producto.set_borrado(False)
    producto.set_producto_url('https://aikencomputacion.com.ar/ry33200-san-justo-cpu-amd-am4-ryzen-3-3200g-c-video.htm')
    producto.set_codigo('0001')
    producto.add_tag('PROCESADORES')
    producto.add_tag('AMD')
    producto.add_tag('COMPONENTES')
    producto.set_nombre('CPU AMD AM4 RYZEN 3 3200G C/VIDEO')
    producto.set_descripcion('ES UN MICRO DE AMD')
    producto.set_costo(39710.11)
    producto.set_tipo_de_cambio(1.00)
    producto.set_existencias('consultar')
    producto.set_urlextra('https://aikencomputacion.com.ar/bytedata/foto/RY33200.JPG')
    producto.set_urlextra2('url2')

    producto2 = modelos.producto.Producto()
    producto2.set_automatizado(False)
    producto2.set_borrado(False)
    producto2.set_producto_url('https://aikencomputacion.com.ar/msia320-san-justo-mother-am4-msi-a320m-pro-vh.htm')
    producto2.set_codigo('0002')
    producto2.add_tag('MOTHERBOARDS')
    producto2.add_tag('MSI')
    producto2.add_tag('COMPONENTES')
    producto2.set_nombre('MOTHER AM4 MSI A320M PRO-VH')
    producto2.set_descripcion('ES UN MOTHERBOARD DE MSI')
    producto2.set_costo(8236.81)
    producto2.set_tipo_de_cambio(1.00)
    producto2.set_existencias('consultar')
    producto2.set_urlextra('url1')
    producto2.set_urlextra2('url2')

    producto3 = modelos.producto.Producto()
    producto3.set_automatizado(False)
    producto3.set_borrado(False)
    producto3.set_producto_url(
        'https://aikencomputacion.com.ar/8g2400f-san-justo-memoria-ddr4-8gb-2400-kingston-hyperx-fury.htm')
    producto3.set_codigo('0003')
    producto3.add_tag('MEMORIAS')
    producto3.add_tag('KINGSTON')
    producto3.add_tag('COMPONENTES')
    producto3.set_nombre('MEMORIA DDR4 8GB 2400 KINGSTON HYPERX FURY')
    producto3.set_descripcion('ES UNA MEMORIA DE KINGSTON')
    producto3.set_costo(7206.19)
    producto3.set_tipo_de_cambio(1.00)
    producto3.set_existencias('consultar')
    producto3.set_urlextra('url1')
    producto3.set_urlextra2('url2')

    repositorios.productos.salva_producto(producto)
    repositorios.productos.salva_producto(producto2)
    repositorios.productos.salva_producto(producto3)


def test_generar_db_autocod():
    producto = modelos.producto.Producto()
    producto.set_automatizado(False)
    producto.set_borrado(False)
    producto.set_producto_url('https://aikencomputacion.com.ar/ry33200-san-justo-cpu-amd-am4-ryzen-3-3200g-c-video.htm')
    producto.add_tag('PROCESADORES')
    producto.add_tag('AMD')
    producto.add_tag('COMPONENTES')
    producto.set_nombre('CPU AMD AM4 RYZEN 3 3200G C/VIDEO')
    producto.set_descripcion('ES UN MICRO DE AMD')
    producto.set_costo(39710.11)
    producto.set_tipo_de_cambio(1.00)
    producto.set_existencias('consultar')
    producto.set_urlextra('https://aikencomputacion.com.ar/bytedata/foto/RY33200.JPG')
    producto.set_urlextra2('url2')

    producto2 = modelos.producto.Producto()
    producto2.set_automatizado(False)
    producto2.set_borrado(False)
    producto2.set_producto_url('https://aikencomputacion.com.ar/msia320-san-justo-mother-am4-msi-a320m-pro-vh.htm')
    producto2.add_tag('MOTHERBOARDS')
    producto2.add_tag('MSI')
    producto2.add_tag('COMPONENTES')
    producto2.set_nombre('MOTHER AM4 MSI A320M PRO-VH')
    producto2.set_descripcion('ES UN MOTHERBOARD DE MSI')
    producto2.set_costo(8236.81)
    producto2.set_tipo_de_cambio(1.00)
    producto2.set_existencias('consultar')
    producto2.set_urlextra('url1')
    producto2.set_urlextra2('url2')

    producto3 = modelos.producto.Producto()
    producto3.set_automatizado(False)
    producto3.set_borrado(False)
    producto3.set_producto_url(
        'https://aikencomputacion.com.ar/8g2400f-san-justo-memoria-ddr4-8gb-2400-kingston-hyperx-fury.htm')
    producto3.add_tag('MEMORIAS')
    producto3.add_tag('KINGSTON')
    producto3.add_tag('COMPONENTES')
    producto3.set_nombre('MEMORIA DDR4 8GB 2400 KINGSTON HYPERX FURY')
    producto3.set_descripcion('ES UNA MEMORIA DE KINGSTON')
    producto3.set_costo(7206.19)
    producto3.set_tipo_de_cambio(1.00)
    producto3.set_existencias('consultar')
    producto3.set_urlextra('url1')
    producto3.set_urlextra2('url2')

    repositorios.productos.crea_producto(producto)
    repositorios.productos.crea_producto(producto2)
    repositorios.productos.crea_producto(producto3)


def test_repositorios_productos_busca_por_nombre():
    print(
        'resultado :' + str(repositorios.productos.busca_por_nombre('CPU AMD AM4 RYZEN 3 3200G C/VIDEO').get_nombre()))
    print('resultado :' + str(repositorios.productos.busca_por_nombre('MOTHER AM4 MSI A320M PRO-VH').get_nombre()))
    print('resultado :' + str(
        repositorios.productos.busca_por_nombre('MEMORIA DDR4 8GB 2400 KINGSTON HYPERX FURY').get_nombre()))


def test_repositorios_productos_busca_por_codigo():
    print('resultado :' + str(repositorios.productos.busca_por_codigo('0001').get_nombre()))
    print('resultado :' + str(repositorios.productos.busca_por_codigo('0002').get_nombre()))
    print('resultado :' + str(repositorios.productos.busca_por_codigo('0003').get_nombre()))


def test_repositorios_productos_busca_por_tags():
    def busqueda_por_tags(tags=list()):
        print('Tag(s) : ', end='')
        for tag in tags:
            print(tag+';', end='')
        resultados = repositorios.productos.busca_por_tags(tags)
        if not resultados:
            print(' : SIN RESULTADOS')
            return 0
        print(" ")
        for producto in resultados:
            print(producto.get_nombre().ljust(50) + '\t' + str(producto.get_costo()).rjust(15))
    tags = list()
    tags.append('COMPONENTES')
    busqueda_por_tags(tags)
    tags.append('KINGSTON')
    busqueda_por_tags(tags)
    tags.clear()
    tags.append('COMPONENTOS')
    busqueda_por_tags(tags)
    tags.clear()
    tags.append('MSI')
    busqueda_por_tags(tags)
    tags.clear()


def test_repositorios_elimina_producto():
    producto_a_eliminar=modelos.producto.Producto()
    producto_a_eliminar=repositorios.productos.busca_por_nombre('CPU AMD AM4 RYZEN 3 3200G C/VIDEO')
    repositorios.productos.elimina_producto(producto_a_eliminar)
    tags = list()
    tags.append('COMPONENTES')
    lista_resultados=repositorios.productos.busca_por_tags(tags)
    for resultado in lista_resultados:
        print(resultado.get_nombre())


# test_generar_db()
# test_generar_db_autocod()
# test_repositorios_productos_busca_por_nombre()
# test_repositorios_productos_busca_por_codigo()
# test_repositorios_productos_busca_por_tags()
# test_repositorios_elimina_producto()
