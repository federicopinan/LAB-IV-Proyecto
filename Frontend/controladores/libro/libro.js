import {librosServices} from '../../servicios/libros-servicios.js'
import {newLibro} from './new.js'
import {editLibro} from './new.js'
var dtable

const htmllibros = `
<div class="card">
   <div class="card-header">
   
   <h3 class="card-title"> 
       <a class="btn bg-dark btn-sm btnAgregarlibro" href="#/newlibros">Agregar Vehículo</a>
   </h3>

   </div>

   <!-- /.card-header -->
   <div class="card-body">            
   <table id="librosTable" class="table table-bordered table-striped tablelibros" width="100%">
       <thead>
           <tr>
           <th># </th>
           <th>Titulo</th>
           <th>Autor</th>
           <th>Editorial</th>
           <th>Disponible</th>
           <th>Categoría ID</th>
           </tr>
       </thead>
   
   </table>
   </div>
   <!-- /.card-body -->
</div> `

export async function libros() {
    let d = document
    let res = ''
    d.querySelector('.contenidoTitulo').innerHTML = 'Libros'
    d.querySelector('.contenidoTituloSec').innerHTML = ''
    d.querySelector('.rutaMenu').innerHTML = 'Libros'
    d.querySelector('.rutaMenu').setAttribute('href', '#/libros')
    let cP = d.getElementById('contenidoPrincipal')

    res = await librosServices.listar()
    res.forEach(element => {
        element.action =
            "<div class='btn-group'><a class='btn btn-warning btn-sm mr-1 rounded-circle btnEditarlibros'  href='#/editlibros' data-id_libros='" +
            element.id +
            "'> <i class='fas fa-pencil-alt'></i></a><a class='btn btn-danger btn-sm rounded-circle removeItem btnBorrarlibros'href='#/dellibros' data-id_libros='" +
            element.id +
            "'><i class='fas fa-trash'></i></a></div>"
    })

    cP.innerHTML = htmllibros

    llenarTabla(res)

    let btnAgregar = d.querySelector('.btnAgregarlibro')

    btnAgregar.addEventListener('click', agregar)
}

function enlazarEventos(oSettings) {
    let d = document
    let btnEditar = d.querySelectorAll('.btnEditarlibros')
    let btnBorrar = d.querySelectorAll('.btnBorrarlibros')
    for (let i = 0; i < btnEditar.length; i++) {
        btnEditar[i].addEventListener('click', editar)
        btnBorrar[i].addEventListener('click', borrar)
    }
}

function agregar() {
    newLibro()
}

function editar() {
    let id = parseInt(this.getAttribute('data-id_libros'), 10)
    editLibro(id)
}

async function borrar() {
    let id = parseInt(this.getAttribute('data-id_libros'), 10)
    let borrar = 0
    await Swal.fire({
        title: 'Está seguro que desea eliminar el libro?',
        showDenyButton: true,
        confirmButtonText: 'Si',
        denyButtonText: `Cancelar`,
        focusDeny: true,
    }).then(result => {
        if (result.isConfirmed) {
            borrar = 1
        } else if (result.isDenied) {
            borrar = 0
            Swal.fire('Se canceló la eliminación', '', 'info')
        }
    })
    if (borrar === 1) await librosServices.borrar(id)
    window.location.href = '#/libros'
}

function llenarTabla(res) {
    dtable = new DataTable('#librosTable', {
        responsive: true,
        data: res,
        columns: [
            {data: 'id'},
            {data: 'titulo'},
            {data: 'autor'},
            {data: 'isbn'},
            {data: 'editorial'},
            {data: 'disponible'},
            {data: 'categoria_id'},
            {data: 'action', orderable: false},
        ],
        fnDrawCallback: function (oSettings) {
            enlazarEventos(oSettings)
        },
        deferRender: true,
        retrieve: true,
        processing: true,
        language: {
            sProcessing: 'Procesando...',
            sLengthMenu: 'Mostrar _MENU_ registros',
            sZeroRecords: 'No se encontraron resultados',
            sEmptyTable: 'Ningún dato disponible en esta tabla',
            sInfo: 'Mostrando registros del _START_ al _END_ de un total de _TOTAL_',
            sInfoEmpty: 'Mostrando registros del 0 al 0 de un total de 0',
            sInfoFiltered: '(filtrado de un total de _MAX_ registros)',
            sInfoPostFix: '',
            sSearch: 'Buscar:',
            sUrl: '',
            sInfoThousands: ',',
            sLoadingRecords: 'Cargando...',
            oPaginate: {
                sFirst: 'Primero',
                sLast: 'Último',
                sNext: 'Siguiente',
                sPrevious: 'Anterior',
            },
            oAria: {
                sSortAscending:
                    ': Activar para ordenar la columna de manera ascendente',
                sSortDescending:
                    ': Activar para ordenar la columna de manera descendente',
            },
        },
    })
}
