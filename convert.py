import os
import tifffile
from tqdm import tqdm
from utils import get_args

def convert_to_tif(
    svs_path: str, 
    tif_path: str
    ) -> None:
    
    """
    Converts an svs file to a tif file.

    Parameters
    ----------
    svs_path: str
        The path to the svs file.

    tif_path: str
        The path to the tif file.
    """

    with tifffile.TiffFile(svs_path) as svs:
        highest_resolution_image = svs.pages[0].asarray()
        
        tifffile.imwrite(tif_path, highest_resolution_image, ome=True, metadata={'axes': 'YXC'}, compression="deflate")
            
            
def main():
    args = get_args("config.yaml")
    source_dir = args["source_dir"]
    dest_dir = args["dest_dir"]

    os.makedirs(dest_dir, exist_ok=True)
    
    error_files = []
    svs_images = [f for f in os.listdir(source_dir) if "svs" in f]
    
    for image in tqdm(svs_images, desc="De-identifying svs files"):
        id = image.split(".")[0]
        
        svs_path = os.path.join(source_dir, image)
        tif_path = os.path.join(dest_dir, f"{id}.ome.tif")
        
        try:
            convert_to_tif(svs_path, tif_path)
            print(f"{image} de-identified\n")
            
        except Exception as e:
            print(f"An error occured when processing {image}.\n")
            error_files.append(image)
            
    print("Completed")
    print("Error files:")
    
    with open('error-files.txt', 'w') as file:
        for f in error_files:
            file.write(f + '\n')
            print(f)
        

if __name__ == "__main__":
    main()    