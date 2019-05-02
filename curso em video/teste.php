<?php
include './autoload.php'; //script para carregar a biblioteca de Machine Learning

$tokenizer = new HybridLogic\Classifier\Basic;
$classifier = new HybridLogic\Classifier($tokenizer);

$classifier->train('Positivo', 'Eu estou de bem com a vida e acredito que tudo é bom');
$classifier->train('Positivo', 'O sucesso é um prazer quando tudo está certo');
$classifier->train('Neutra', 'o sol está brilhando');
$classifier->train('Neutra', 'A terra é plana');

$classifier->train('Negativa', 'não gostei de sua atitude');
$classifier->train('Negativa', 'Você mentiu para que eu pudesse perder');
$classifier->train('Negativa', 'Tudo está errado com você');
$classifier->train('Positivo', 'você venceu na vida');

echo "Classificação de sentimento \n";
$texto = "estou com vontade de comer chocolate";

$groups = $classifier->classify($texto);


echo " Positivo  = ".number_format($groups['Positivo']*100,2)."% | Neutro  = ".number_format($groups['Neutra']*100,2). "|Negativa = ".number_format($groups['Negativa']*100,2). "% \n" ;
//var_dump($groups);
?>
