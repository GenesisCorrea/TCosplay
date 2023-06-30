const content = document.querySelector('content');

try {
    fetch('https://cosplay-96d31-default-rtdb.firebaseio.com/otakumascotas.json')
    .then(respuesta =>{
        return respuesta.json()
    })
    .then(datos => {
        let contador =0;
        while (datos.length < contador) {

            let productos = document.createElement('div')
            let imgcont = document.createElement('div')
            let img = document.createElement('img')

            let contenido = document.createElement('div')
            let titulo = document.createElement('h2')
            let precio = document.createElement('p')

            let addcarr = document.createElement('button')

            productos.setAttribute('class', 'productos')

            imgcont.setAttribute('class', 'imgcont')
            img.setAttribute('src', datos[contador].img)
            img.setAttribute('alt', 'imagen de representacion')

            contenido.setAttribute('class', 'contenido')

            titulo.setAttribute('class', 'titulo')
            precio.setAttribute('class','precio')


            titulo.innerHTML = datos[contador].nombre;
            precio.innerHTML = datos[contador].precio +"$";

            addcarr.setAttribute('class','btnAddcarr')

            productos.appendChild(imgcont)
            imgcont.appendChild(img)
            productos.appendChild(contenido)
            contenido.appendChild(titulo)
            contenido.appendChild(precio)
            contenido.appendChild(addcarr)

            content.appendChild(productos)

            contador++;
        }

    })
} catch (error) {
    console.log(error)
}
