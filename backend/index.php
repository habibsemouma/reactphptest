<?php

header('Access-Control-Allow-Origin: *'); 
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

// Check if the request method is GET
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    $data = array(
        array('id' => 1, 'name' => 'mo7', 'age' => 25),
        array('id' => 2, 'name' => 'kouider', 'age' => 30),
        array('id' => 3, 'name' => '3aljia', 'age' => 22)
    );

    header('Content-Type: application/json');

    echo json_encode($data);
} else {
    http_response_code(405);
    echo 'Method Not Allowed';
}
