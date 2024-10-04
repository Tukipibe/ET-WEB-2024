let items = [
    {
        "nombre":"Arsene Lupin: Caballero ladron.",
        "precio":10000,
        "imagen":"{% url 'arsene.jpg' %}"
    },
    {
        "nombre":"Solo leveling Vol 1.",
        "precio":20000,
        "imagen":"url('car1.jpeg')"
    },
    {
        "nombre":"Las aventuras de Sherlock Holmes",
        "precio":10000,
        "imagen":"{% url 'sherlock.jpg' %}"
    },
    {
        "nombre":"Animales Fantasticos y donde encontrarlos",
        "precio":15000,
        "imagen":"{% url 'animales.png' %}"
    },
    {
        "nombre":"Solo leveling Vol 2.",
        "precio":25000,
        "imagen":"{% url 'slv2.jpg' %}"
    }
    
]

function cargar(){
    fetch('https://mindicador.cl/api').then(function(response) {
    return response.json();
}).then(function(dailyIndicators) {
    let dolar = parseFloat(dailyIndicators.dolar.valor);
    let productos = document.querySelector("#productos");
    for(let item of items){
        let producto = document.createElement("div");
        producto.classList.add("producto");

        let imagen = document.createElement("div");
        imagen.classList.add("imagen");
        imagen.style.backgroundImage = "url("+ item.imagen +")";
        producto.appendChild(imagen);

        let nombre = document.createElement("div");
        nombre.classList.add("nombre");
        nombre.innerHTML = item.nombre;
        producto.appendChild(nombre);

        let precio = document.createElement("div");
        precio.classList.add("precio");
        precio.innerHTML = item.precio + " (USD $"+(item.precio/dolar).toFixed(1) + ")";
        producto.appendChild(precio);

        productos.appendChild(producto);
    }
}).catch(function(error) {
    console.log('Requestfailed', error);
});
}