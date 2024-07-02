const url = 'http://127.0.0.1:8000/libros'

async function listar(id) {
    let cadUrl
    if (isNaN(id)) cadUrl = url
    else cadUrl = url + '/' + id
    return await fetch(cadUrl, {
        headers: {
            accept: 'application/json',
            'Content-type': 'application/json',
            Authorization: 'Bearer ' + localStorage.getItem('token'),
        },
    }).then(respuesta => respuesta.json())
}

async function crear(titulo, autor, isbn, editorial, disponible, categoria_id) {
    return await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            Authorization: 'Bearer ' + localStorage.getItem('token'),
        },
        body: JSON.stringify({
            titulo: titulo,
            autor: autor,
            isbn: isbn,
            editorial: editorial,
            disponible: disponible,
            categoria_id: categoria_id,
        }),
    }).then(respuesta => respuesta.json())
}

async function editar(
    id,
    titulo,
    autor,
    isbn,
    editorial,
    disponible,
    categoria_id
) {
    let urlPut = url + '/' + id
    return await fetch(urlPut, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            Authorization: 'Bearer ' + localStorage.getItem('token'),
        },
        body: JSON.stringify({
            titulo: titulo,
            autor: autor,
            isbn: isbn,
            editorial: editorial,
            disponible: disponible,
            categoria_id: categoria_id,
        }),
    }).then(respuesta => respuesta.json())
}

async function borrar(id) {
    let urlDelete = url + '/' + id
    return await fetch(urlDelete, {
        method: 'DELETE',
        headers: {
            Authorization: 'Bearer ' + localStorage.getItem('token'),
        },
    }).then(respuesta => respuesta.json())
}

export const librosServices = {
    listar,
    crear,
    editar,
    borrar,
}
