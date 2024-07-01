import {usuariosServices} from '../../servicios/usuarios-servicios.js'
import {ventasServices} from '../../servicios/ventas-servicios.js'
import {productosServices} from '../../servicios/productos-servicios.js'
const htmlHome = ` <div class="row" >
    <div class="col-lg-3 col-6">
        <!-- small box -->
        <div class="small-box bg-custom-success">
            <div class="inner">
            <h3 id="indVentas">150</h3>

            <p>Libros disponibles</p>
            </div>
            <div class="icon">
                <i class="ion ion-bag"></i>
            </div>
            <a href="#/ventas" class="small-box-footer">Más información <i class="fas fa-arrow-circle-right"></i></a>
        </div>
    </div>
    <!-- ./col -->
    <div class="col-lg-3 col-6">
        <!-- small box -->
        <div class="small-box bg-custom-success">
            <div class="inner">
            <h3 id="indSindespachar">53</h3>

            <p>Prestamos</p>
            </div>
            <div class="icon">
            <i class="ion ion-stats-bars"></i>
            </div>
            <a href="#/ventas" class="small-box-footer">Más información <i class="fas fa-arrow-circle-right"></i></a>
        </div>
    </div>
    <!-- ./col -->
    <div class="col-lg-3 col-6">
        <!-- small box -->
        <div class="small-box bg-custom-success">
            <div class="inner">
            <h3 id="indUsuarios">44</h3>

            <p>Usuarios Registrados</p>
            </div>
            <div class="icon">
            <i class="ion ion-person-add"></i>
            </div>
            <a href="#/usuarios" class="small-box-footer">Más información <i class="fas fa-arrow-circle-right"></i></a>
        </div>
    </div>
    <!-- ./col -->
    <div class="col-lg-3 col-6">
        <!-- small box -->
        <div class="small-box bg-custom-success">
            <div class="inner">
            <h3 id="indProductos">65</h3>

            <p>Cantidad de libros</p>
            </div>
            <div class="icon">
            <i class="ion ion-pie-graph"></i>
            </div>
            <a href="#/productos" class="small-box-footer">Más información <i class="fas fa-arrow-circle-right"></i></a>
        </div>
    </div>
    <!-- ./col -->
</div>
<style>
    .bg-custom-info {
        background-color: #ECF39E; /* Amarillo muy claro */
    }
    .bg-custom-success {
        background-color: #90A955; /* Verde oliva claro */
    }
    .bg-custom-warning {
        background-color: #FFD700; /* Amarillo dorado */
    }
    .bg-custom-danger {
        background-color: #DC143C; /* Rojo carmesí */
    }
    .small-box .inner h3, .small-box .inner p {
        color: #132A13; /* Verde oscuro */
    }
    .small-box a.small-box-footer {
        color: #132A13; /* Verde oscuro */
    }
    .small-box a.small-box-footer:hover {
        color: #ECF39E; /* Verde claro en hover */
        background-color: #31572C; /* Verde oscuro intermedio */
    }
</style>`

export async function Home() {
    let d = document
    let res = ''
    d.querySelector('.contenidoTitulo').innerHTML =
        'Sistema de gestion de libros📚'
    d.querySelector('.contenidoTituloSec').innerHTML = ''
    d.querySelector('.rutaMenu').innerHTML = 'Home'
    d.querySelector('.rutaMenu').setAttribute('href', '#/home')
    let cP = d.getElementById('contenidoPrincipal')

    cP.innerHTML = htmlHome

    let indVentas = d.getElementById('indVentas')
    let indSinDespachar = d.getElementById('indSindespachar')
    let indUsuarios = d.getElementById('indUsuarios')
    let indProductos = d.getElementById('indProductos')

    res = await usuariosServices.listar()
    //CANTIDAD DE USUARIOS
    indUsuarios.innerHTML = res.length

    //CANTIDAD DE VENTAS
    res = await ventasServices.listar()
    indVentas.innerHTML = res.length

    //CANTIDAD DE VENTAS SIN DESPACHAR (los valores que espera para el campo despachado son true y false)
    res = await ventasServices.listarVentasDespachadas(false)
    indSinDespachar.innerHTML = res.length

    //CANTIDAD DE PRODUCTOS
    res = await productosServices.listar()
    indProductos.innerHTML = res.length
}
