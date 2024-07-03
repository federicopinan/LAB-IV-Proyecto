import {librosServices} from '../../servicios/libros-servicios.js'

const htmlAmLibros = `
<div class="card card-dark card-outline">
	
	<form  class="needs-validation frmAmLibro"  enctype="multipart/form-data">
	
		<div class="card-header">
               
			<div class="col-md-8 offset-md-2">	
               
				<!--=====================================
                a
                ======================================-->
				
				<div class="form-group mt-5">
					
					<label>Titulo</label>

					<input 
					type="text" 
					class="form-control"
					pattern="[A-Za-zñÑáéíóúÁÉÍÓÚ0-9 ]{1,}"
					onchange="validateJS(event,'text')"
					name="titulo"
                    id="libroTitulo"
					required>

					<div class="valid-feedback">Valid.</div>
            		<div class="invalid-feedback">Please fill out this field.</div>

				</div>

				<!--=====================================
                a
                ======================================-->

				<div class="form-group mt-2">
					
					<label>a</label>

					<input 
					type="text" 
					class="form-control"
					onchange="validateJS(event,'text')"
					name="autor"
                    id="libroAutor"
					required>

					<div class="valid-feedback">Valid.</div>
            		<div class="invalid-feedback">Please fill out this field.</div>

				</div>

				<!--=====================================
                Isbn
                ======================================-->

				<div class="form-group mt-2">
					
					<label>Isbn</label>

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
                Editorial
                ======================================-->

				<div class="form-group mt-2">
					
					<label>Editorial</label>

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
                Disponible
                ======================================-->

				<div class="form-group mt-2">
					
					<label>Disponible</label>

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
                Categoria ID
                ======================================-->

				<div class="form-group mt-2">
					
					<label>Categoria ID</label>

					<input 
					type="number" 
					class="form-control"
					onchange="validateJS(event,'text')"
					name="categoria_id"
                    id="libroCategoria_id"
					required>

					<div class="valid-feedback">Valid.</div>
            		<div class="invalid-feedback">Please fill out this field.</div>

				</div>
			
			</div>
		
		</div>

		<div class="card-footer">
			
			<div class="col-md-8 offset-md-2">
	
				<div class="form-group mt-3">

					<a href="#/libros" class="btn btn-light border text-left">Cancelar</a>
					
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
    txtAutor.value = libro.autor
    txtIsbn.value = libro.isbn
    txtEditorial.value = libro.editorial
    txtDisponble.value = libro.disponible
    txtCategoria_id.value = libro.categoria_id
}

function crearFormulario() {
    let d = document
    d.querySelector('.rutaMenu').innerHTML = 'Libros'
    d.querySelector('.rutaMenu').setAttribute('href', '#/libros')

    let cP = d.getElementById('contenidoPrincipal')
    cP.innerHTML = htmlAmLibros

    var script = document.createElement('script')
    script.type = 'text/javascript'
    script.src = '/Frontend/controladores/validaciones.js'
    cP.appendChild(script)

    txtTitulo = d.getElementById('libroTitulo')
    txtAutor = d.getElementById('libroAutor')
    txtIsbn = d.getElementById('libroIsbn')
    txtEditorial = d.getElementById('libroEditorial')
    txtDisponble = d.getElementById('libroDisponible')
    txtCategoria_id = d.getElementById('libroCategoria_id')
}

function guardar(e) {
    e.preventDefault()
    const formData = new FormData(e?.target)
    const values = Object.fromEntries(formData)
    console.log(values)

    // No incluir 'id' en la solicitud de creación
    librosServices
        .crear(
            values.titulo,
            values.autor,
            values.disponible,
            values.isbn,
            values.editorial,
            values.categoria_id
        )
        .then(respuesta => {
            formulario.reset()
            window.location.href = '#/libros'
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
            values.titulo,
            values.autor,
            values.disponible,
            values.isbn,
            values.editorial,
            values.categoria_id
        )
        .then(respuesta => {
            formulario.reset()
            window.location.href = '#/libros'
        })
        .catch(error => console.log(error))
}
