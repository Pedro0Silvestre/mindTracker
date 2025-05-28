const botao = document.getElementById('botao');

botao.addEventListener('click', function(event) {
    event.preventDefault();

    let respostas = [];

    const resposta1 = document.getElementById('questao1').value;
    respostas.push(resposta1);
    
    const resposta2 = document.getElementById('questao2').value;
    respostas.push(resposta2);

    const resposta3 = document.getElementById('questao3').value;
    respostas.push(resposta3);

    const resposta4 = document.getElementById('questao4').value;
    respostas.push(resposta4);

    const resposta5 = document.getElementById('questao5').value;
    respostas.push(resposta5);

    localStorage.setItem('respostas', JSON.stringify(respostas));
    const respostasArmazenadas = JSON.parse(localStorage.getItem('respostas'));
});