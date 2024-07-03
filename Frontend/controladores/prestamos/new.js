// Cambios necesarios en Reservas-new.js

import {prestamoServices} from '../../servicios/prestamos-servicios.js'

const htmlPrestamos = `
<div class="card card-dark card-outline">
	
	<form class="needs-validation frmAmPrestamo" enctype="multipart/form-data">
	
		<div class="card-header">
               
			<div class="col-md-8 offset-md-2">	
               
				<!--=====================================
                Libro ID
                ======================================-->
				
				<div class="form-group mt-5">
					
					<label>Libro ID</label>

					<input 
					type="number" 
					class="form-control"
					name="libro_id"
                    id="prestamoLibroID"
					required>

					<div class="valid-feedback">Valid.</div>
            		<div class="invalid-feedback">Please fill out this field.</div>

				</div>

				<!--=====================================
                Usuario ID
                ======================================-->

				<div class="form-group mt-2">
					
					<label>Usuario ID</label>

					<input 
					type="number" 
					class="form-control"
					name="usuario_id"
                    id="prestamoUsuarioId"
					required>

					<div class="valid-feedback">Valid.</div>
            		<div class="invalid-feedback">Please fill out this field.</div>

				</div>

				<!--=====================================
                Fecha Prestamo
                ======================================-->

				<div class="form-group mt-2">
					
					<label>Fecha Prestamo</label>

					<input 
					type="date" 
					class="form-control"
					name="fecha_prpestamo"
                    id="prestamoFechaPrestamo"
					required>

					<div class="valid-feedback">Valid.</div>
            		<div class="invalid-feedback">Please fill out this field.</div>

				</div>

				<!--=====================================
                Fecha Devolución
                ======================================-->

				<div class="form-group mt-2">
					
					<label>Fecha Devolución</label>

					<input 
					type="date" 
					class="form-control"
					name="fecha_devolucion"
                    id="prestamoFechaDevolucion"
					required>

					<div class="valid-feedback">Valid.</div>
            		<div class="invalid-feedback">Please fill out this field.</div>

				</div>
			
			</div>
		
		</div>

		<div class="card-footer">
			
			<div class="col-md-8 offset-md-2">
	
				<div class="form-group mt-3">

					<a href="#/prestamos" class="btn btn-light border text-left">Cancelar</a>
					
					<button type="submit" class="btn bg-dark float-right">Guardar</button>

				</div>

			</div>

		</div>

	</form>

</div> `

var formulario = ''
var txtLibroId = ''
var txtUsuarioId = ''
var txtFechaPrestamo = ''
var txtFechaDevolucion = ''
let prestamoID = 0

export async function newPrestamo() {
    let d = document

    d.querySelector('.contenidoTitulo').innerHTML = 'Agregar Prestamo'
    d.querySelector('.contenidoTituloSec').innerHTML += 'Agregar'

    crearFormulario()

    formulario = d.querySelector('.frmAmPrestamo')
    formulario.addEventListener('submit', guardar)
}

export async function editPrestamo(id) {
    let d = document
    prestamoID = id
    d.querySelector('.contenidoTitulo').innerHTML = 'Editar Prestamo'
    d.querySelector('.contenidoTituloSec').innerHTML += 'Editar'
    crearFormulario()

    formulario = d.querySelector('.frmAmPrestamo')
    formulario.addEventListener('submit', modificar)
    let prestamo = await prestamoServices.listar(id)

    txtLibroId.value = prestamo.libro_id
    txtUsuarioId.value = prestamo.usuario_id
    txtFechaPrestamo.value = prestamo.fecha_prestamo
    txtFechaDevolucion.value = prestamo.fecha_devolucion
}

function crearFormulario() {
    let d = document
    d.querySelector('.rutaMenu').innerHTML = 'Prestamos'
    d.querySelector('.rutaMenu').setAttribute('href', '#/prestamos')

    let cP = d.getElementById('contenidoPrincipal')
    cP.innerHTML = htmlPrestamos

    var script = document.createElement('script')
    script.type = 'text/javascript'
    script.src = '../controladores/validaciones.js'
    cP.appendChild(script)

    txtLibroId = d.getElementById('prestamoLibroID')
    txtUsuarioId = d.getElementById('prestamoUsuarioId')
    txtFechaPrestamo = d.getElementById('prestamoFechaPrestamo')
    txtFechaDevolucion = d.getElementById('prestamoFechaDevolucion')
}

function guardar(e) {
    e.preventDefault()
    const formData = new FormData(e?.target)
    const values = Object.fromEntries(formData)

    prestamoServices
        .crear(
            values.libro_id,
            values.usuario_id,
            values.fecha_reserva,
            values.fecha_devolucion
        )
        .then(respuesta => {
            formulario.reset()
            window.location.href = '#/prestamos'
        })
        .catch(error => console.log(error))
}

function modificar(e) {
    e.preventDefault()
    const formData = new FormData(e?.target)
    const values = Object.fromEntries(formData)

    prestamoServices
        .editar(
            prestamoID,
            values.libro_id,
            values.usuario_id,
            values.fecha_reserva,
            values.fecha_devolucion
        )
        .then(respuesta => {
            formulario.reset()
            window.location.href = '#/prestamos'
        })
        .catch(error => console.log(error))
}
