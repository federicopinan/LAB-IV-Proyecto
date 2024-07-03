import {librosServices} from '../../servicios/libros-servicios.js'

const htmlAmLibros = `
<div class="card card-dark card-outline">
	
	<form  class="needs-validation frmAmLibro"  enctype="multipart/form-data">
	
		<div class="card-header">
               
			<div class="col-md-8 offset-md-2">	
               
				<!--=====================================
                Autor
                ======================================-->
				
				<div class="form-group mt-5">
					
					<label>Autor</label>

					<input 
					type="text" 
					class="form-control"
					pattern="[A-Za-zñÑáéíóúÁÉÍÓÚ0-9 ]{1,}"
					onchange="validateJS(event,'text')"
					name="Autor"
                    id="libroTitulo"
					required>

					<div class="valid-feedback">Valid.</div>
            		<div class="invalid-feedback">Please fill out this field.</div>

				</div>

				<!--=====================================
                Marca
                ======================================-->

				<div class="form-group mt-2">
					
					<label>Marca</label>

					<input 
					type="text" 
					class="form-control"
					onchange="validateJS(event,'text')"
					name="titulo"
                    id="libroTitulo"
					required>

					<div class="valid-feedback">Valid.</div>
            		<div class="invalid-feedback">Please fill out this field.</div>

				</div>

				<!--=====================================
                Año
                ======================================-->

				<div class="form-group mt-2">
					
					<label>Año</label>

					<input 
					type="number" 
					class="form-control"
					onchange="validateJS(event,'text')"
					name="isbn"
                    id="libroIsbn"
					required>

					<div class="valid-feedback">Valid.</div>
            		<div class="invalid-feedback">Please fill out this field.</div>

				</div>

				<!--=====================================
                Matrícula
                ======================================-->

				<div class="form-group mt-2">
					
					<label>Matrícula</label>

					<input 
					type="text" 
					class="form-control"
					onchange="validateJS(event,'text')"
					name="editorial"
                    id="libroEditorial"
					required>

					<div class="valid-feedback">Valid.</div>
            		<div class="invalid-feedback">Please fill out this field.</div>

				</div>

				<!--=====================================
                Categoría ID
                ======================================-->

				<div class="form-group mt-2">
					
					<label>Categoría ID</label>

					<input 
					type="number" 
					class="form-control"
					onchange="validateJS(event,'text')"
					name="disponible"
                    id="libroDisponible"
					required>

					<div class="valid-feedback">Valid.</div>
            		<div class="invalid-feedback">Please fill out this field.</div>

				</div>

				<!--=====================================
                Capacidad
                ======================================-->

				<div class="form-group mt-2">
					
					<label>Capacidad</label>

					<input 
					type="number" 
					class="form-control"
					onchange="validateJS(event,'text')"
					name="categoria_id"
                    id="liborCategoria_id"
					required>

					<div class="valid-feedback">Valid.</div>
            		<div class="invalid-feedback">Please fill out this field.</div>

				</div>
			
			</div>
		
		</div>

		<div class="card-footer">
			
			<div class="col-md-8 offset-md-2">
	
				<div class="form-group mt-3">

					<a href="#/libro" class="btn btn-light border text-left">Cancelar</a>
					
					<button type="submit" class="btn bg-dark float-right">Guardar</button>

				</div>

			</div>

		</div>

	</form>

</div> `

var formulario = ''
var txtTitulo = ''
var txtAutor = ''
var txtIsbn = ''
var txtEditorial = ''
var txtDisponble = ''
var txtCategoria_id = ''
let Id_libro = 0

export async function newLibro() {
    let d = document

    d.querySelector('.contenidoTitulo').innerHTML = 'Agregar Libro'
    d.querySelector('.contenidoTituloSec').innerHTML += 'Agregar'

    crearFormulario()

    formulario = d.querySelector('.frmAmLibro')
    formulario.addEventListener('submit', guardar)
}

export async function editLibro(id) {
    let d = document
    Id_libro = id
    d.querySelector('.contenidoTitulo').innerHTML = 'Editar Libro'
    d.querySelector('.contenidoTituloSec').innerHTML += 'Editar'
    crearFormulario()

    formulario = d.querySelector('.frmAmLibro')
    formulario.addEventListener('submit', modificar)
    let libro = await librosServices.listar(id)

    txtTitulo.value = libro.titulo
    txtAutor.value = libro.Autor
    txtIsbn.value = libro.isbn
    txtEditorial.value = libro.editorial
    txtDisponble.value = libro.disponible
    txtCategoria_id.value = libro.categoria_id
}

function crearFormulario() {
    let d = document
    d.querySelector('.rutaMenu').innerHTML = 'Libros'
    d.querySelector('.rutaMenu').setAttribute('href', '#/libro')

    let cP = d.getElementById('contenidoPrincipal')
    cP.innerHTML = htmlAmLibros

    var script = document.createElement('script')
    script.type = 'text/javascript'
    script.src = '../controladores/validaciones.js'
    cP.appendChild(script)

    txtTitulo = d.getElementById('libroTitulo')
    txtAutor = d.getElementById('libroTitulo')
    txtIsbn = d.getElementById('libroIsbn')
    txtEditorial = d.getElementById('libroEditorial')
    txtDisponble = d.getElementById('libroDisponible')
    txtCategoria_id = d.getElementById('liborCategoria_id')
}

function guardar(e) {
    e.preventDefault()
    const formData = new FormData(e?.target)
    const values = Object.fromEntries(formData)
    console.log(values)

    // No incluir 'id' en la solicitud de creación
    librosServices
        .crear(
            values.Autor,
            values.titulo,
            values.disponible,
            values.isbn,
            values.editorial,
            values.categoria_id
        )
        .then(respuesta => {
            formulario.reset()
            window.location.href = '#/libro'
        })
        .catch(error => console.log(error))
}

function modificar(e) {
    e.preventDefault()
    const formData = new FormData(e?.target)
    const values = Object.fromEntries(formData)

    librosServices
        .editar(
            Id_libro,
            values.Autor,
            values.titulo,
            values.disponible,
            values.isbn,
            values.editorial,
            values.categoria_id
        )
        .then(respuesta => {
            formulario.reset()
            window.location.href = '#/libro'
        })
        .catch(error => console.log(error))
}
