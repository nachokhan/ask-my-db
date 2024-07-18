-- Create tables
CREATE TABLE people (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    last_name VARCHAR(100),
    birthday DATE
);

CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(255),
    category VARCHAR(50)
);

CREATE TABLE person_company (
    person_id INT,
    company_id INT,
    PRIMARY KEY (person_id, company_id),
    FOREIGN KEY (person_id) REFERENCES people (id),
    FOREIGN KEY (company_id) REFERENCES companies (id)
);

-- Insert initial data into people
INSERT INTO people (name, last_name, birthday) VALUES
('Joaquín', 'Pérez', '1980-01-01'),
('María', 'González', '1985-02-02'),
('Lucía', 'Rodríguez', '1990-03-03'),
('Martín', 'Fernández', '1995-04-04'),
('Ana', 'López', '2000-05-05'),
('Diego', 'Martínez', '1970-06-06'),
('Sofía', 'Gómez', '1965-07-07'),
('Pablo', 'Díaz', '1955-08-08'),
('Camila', 'Álvarez', '1945-09-09'),
('Facundo', 'Romero', '1935-10-10');

-- Insert initial data into companies
INSERT INTO companies (name, address, category) VALUES
('TechAr', 'Calle Falsa 123', 'Tecnología'),
('SaludArgentina', 'Avenida Siempreviva 456', 'Salud'),
('EduArg', 'Boulevard Educativo 789', 'Educación'),
('SaboresDelSur', 'Pasaje Gourmet 101', 'Alimentos y Bebidas');

-- Insert relationships between people and companies
INSERT INTO person_company (person_id, company_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 1),
(5, 4),
(6, 2),
(7, 3),
(8, 4),
(9, 1),
(10, 2);
