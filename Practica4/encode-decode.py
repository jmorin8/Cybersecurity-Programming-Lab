import base64
import sys
from os.path import exists


# Decoding b64 txt to images
def decode(var):
    dot=var.find('.') # finding dot to remove original extension

    decoded_image=f'{var[:dot]}.jpg' # decoded imaged will saved with jpg extension 

    print(f'[*] Decoding {var}')

    open(decoded_image, 'wb').write(base64.b64decode(open(var, "rb").read()))

    print(f'[*] Image {decoded_image} saved')




# Encoding files to b64
def encode(var):
    dot=var.find('.') # finding dot to remove original extension

    encoded_file=f'{var[:dot]}.txt' # encoded file will saved with txt extension

    print(f'[*] Encoding {var}') 

    open(encoded_file, 'wb').write(base64.b64encode(open(var, "rb").read()))

    print(f'[*] File {encoded_file} saved')
  



if __name__=="__main__":
    print('-'*5,'Welcome','-'*5)

    option=input("[*] Choose an option (decode/encode): ")

    if option in ("decode", "de"):
        fl_name=input("[*] Filename to decode: ")         
        
        # Check if provided file exists or not
        if exists(fl_name): # Filename has to be in the same path the program is
            decode(fl_name)
        else:
            print('[ERROR] Incorrect filename or file does not exist')
            sys.exit()
    
    elif option in ("encode", "en"):
        fl_name=input("[*] Filename to encode: ")
        
        # Check if provided file exists or not
        if exists(fl_name): # Filename has to be in the same path the program is
            encode(fl_name)
        else:
            print('[ERROR] Incorrect filename or file does not exist')
            sys.exit()
    
    else:
        print('[ERROR] Not a valid option...')
        sys.exit()