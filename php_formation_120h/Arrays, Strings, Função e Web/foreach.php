<?php

$contasCorrentes = [
    12345678910 => [
        'titular' => 'Vinicius',
        'saldo' => 1000
    ],
    12345678911 => [
        'titular' => 'Maria',
        'saldo' => 10000
    ],
    12325678912 => [
        'titular' => 'Alberto',
        'saldo' => 300
    ]
];

function mensagem (int $text){
    echo $text . PHP_EOL;
}
foreach ($contasCorrentes as $cpf => $conta) {
    mensagem($conta['titular']);
}
