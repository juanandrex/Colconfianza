<?php
// Configuración de cabeceras para permitir peticiones JSON
header("Content-Type: application/json; charset=UTF-8");

// Leer el cuerpo de la petición
$input = file_get_contents("php://input");
$data = json_decode($input, true);

if (!$data) {
    echo json_encode(["status" => "error", "message" => "No se recibieron datos"]);
    exit;
}

try {
    // Asegúrate de que los datos no estén vacíos
    if (empty($data['nombre']) || empty($data['email'])) {
        throw new Exception("Los campos obligatorios están vacíos");
    }

    // Conexión a la base de datos
    $conn = new PDO("mysql:host=localhost;dbname=colconfianza_db", "root", "");
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Preparar el INSERT
    $stmt = $conn->prepare("INSERT INTO contactos (nombre, email, telefono, mensaje) VALUES (?, ?, ?, ?)");
    $stmt->execute([$data['nombre'], $data['email'], $data['telefono'], $data['mensaje']]);

    echo json_encode(["status" => "success", "message" => "Datos guardados exitosamente"]);
} catch (PDOException $e) {
    echo json_encode(["status" => "error", "message" => "Error de base de datos: " . $e->getMessage()]);
} catch (Exception $e) {
    echo json_encode(["status" => "error", "message" => $e->getMessage()]);
}
?>