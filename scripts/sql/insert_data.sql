/*Insercion de datos*/

INSERT INTO components (name, description, quantity, mass, material) VALUES
('Optical Lens', 'High precision optical lens for observation', 10, 0.05, 'Glass'),
('Sensor', 'High sensitivity sensor for capturing images', 5, 0.1, 'Silicon');

INSERT INTO suppliers (name, contact_info) VALUES
('Thorlabs', 'contact@thorlabs.com'),
('Optics Company', 'contact@optics.com');

INSERT INTO orders (component_id, supplier_id, order_date, quantity, status) VALUES
(1, 1, '2024-07-15', 10, 'Pending'),
(2, 2, '2024-07-15', 5, 'Completed');