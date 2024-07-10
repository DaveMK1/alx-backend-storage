-- creates a trigger that decreases the quantity of an item after adding a new order
SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan
    FROM metal_bands
    WHERE style LIKE '%Glam rock%'
    ORDER BY lifespan DESC;
