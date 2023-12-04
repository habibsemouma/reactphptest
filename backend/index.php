<?php

header('Access-Control-Allow-Origin: *');  // Replace * with your allowed domains
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

// Check if the request method is GET
if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    // Your logic to fetch or generate data
    $data = array(
        array('id' => 1, 'name' => 'mo7', 'age' => 25),
        array('id' => 2, 'name' => 'kouider', 'age' => 30),
        array('id' => 3, 'name' => '3aljia', 'age' => 22)
    );

    // Set the response header to indicate JSON content
    header('Content-Type: application/json');

    // Return the JSON-encoded data
    echo json_encode($data);
} else {
    // If the request method is not GET, return a 405 Method Not Allowed status
    http_response_code(405);
    echo 'Method Not Allowed';
}
