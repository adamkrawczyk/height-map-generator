from PIL import Image
import numpy as np
import random

from generate_mountain import diamond_square


def generate_terrain(width, height, terrain_type):
    # Placeholder for terrain generation. For now, generate random heights
    if terrain_type == "random":
        # Generate random values between 0 and 65535 for 16-bit image
        return np.random.randint(0, 65536, size=(height, width)).astype(np.uint16)
    elif terrain_type == "mountain":
        return diamond_square(width, height, 0.2)
    # TODO: Add more terrain types with specific generation logic
    return None


def generate_height_map(width, height, terrain_type):
    # Generate terrain data
    terrain_data = generate_terrain(width, height, terrain_type)

    if terrain_data is None:
        print(f"Unknown terrain type: {terrain_type}")
        return

    # Convert to PIL Image
    # Convert the terrain data into 16-bit values and then shift to 8-bit for visualization
    terrain_data_16bit = np.clip(terrain_data * 65535, 0, 65535).astype(np.uint16)  # Convert to 16-bit

    # Save the 16-bit image
    img_16 = Image.fromarray(terrain_data_16bit, mode='I;16')
    img_16.save(f"{terrain_type}TerrainHeight_16bit_gsi.png")

    # Convert to 8-bit for visualization
    #img = Image.fromarray((terrain_data >> 8).astype(np.uint8), mode='L')
    #img.save(f"{terrain_type}TerrainHeight_gsi.png")


if __name__ == "__main__":
    width = int(input("Enter the width of the height map: "))
    height = int(input("Enter the height of the height map: "))
    terrain_type = input("Enter the type of terrain (e.g., 'random'): ")

    generate_height_map(width, height, terrain_type)
