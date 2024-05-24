let I = document.getElementById('ICheck');
let II = document.getElementById('IICheck');
let III = document.getElementById('IIICheck');
let IV = document.getElementById('IVCheck');
let V = document.getElementById('VCheck');
let order = [];
let boxes = [I, II,III,IV,V]
document.addEventListener('DOMContentLoaded', (event) => {
  

    const checkboxes = [ 'ICheck', 'IICheck', 'IIICheck', 'IVCheck', 'VCheck'];
    checkboxes.forEach(id => {
        document.getElementById(id).addEventListener('click', function () {
            if (!order.includes(id)) {
                order.push(id);
                console.log(order);
            }
        });
    });
});


function Test() {
    fetch('/GetEnigma', {
        method: 'GET',
    })
        .then(response => response.json())
        .then(data => {
            console.log(data)
        })
        .catch(error => {
            console.error('Error', error)
        })
}

function ChangeEnigma() {
    let newEnigma = {
        Keyboard: {},
        Plugboard: { left: "", right: "ABCDEFGHIJKLMNOPQRSTUVWXYZ" },
        Left: { left: "ABCDEFGHIJKLMNOPQRSTUVWXYZ", notch: "", right: "" },
        Middle: { left: "ABCDEFGHIJKLMNOPQRSTUVWXYZ", notch: "", right: "" },
        Right: { left: "ABCDEFGHIJKLMNOPQRSTUVWXYZ", notch: "", right: "" },
        Reflector: { left: "ABCDEFGHIJKLMNOPQRSTUVWXYZ", right: "" }
    }

    order.forEach(rotor => {
        for (let i = 0; i < boxes.length; i++) {
            if (rotor == boxes[i].id) {
                // Fullfør rotorene i newenigma
            }
        }
})
}