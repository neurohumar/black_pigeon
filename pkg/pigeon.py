#! /bin/python3

"""importing required modules"""
import zipfile
import os
from cryptography.fernet import Fernet

class Locker:
    """
    Class for encrypting and compressing content
    parameters : zipfile_name:str , encrypton_key:byte , copy_files_to_archive:bool, files_to_compress:list
    """

    def __init__(self,zipfilename="secret.zip",key=None,copy=True,*files):
        self.zipfile_name = zipfilename
        self.key = key
        self.files = files
        self.copy = copy
        self.encrypted_files = []
        self.lock()
        self.compress()

    def __generate_key(self):
        return Fernet.generate_key()

    def lock(self):
        if self.key is None:
            self.key = self.__generate_key()

        fernet = Fernet(self.key)

        for file in self.files:
            temp_path = f"{file}"
            print(file)

            if self.copy is True:
                temp_path = f"copy-{os.path.basename(file)}"

            with open(file,"rb") as f:
                encrypted_content = fernet.encrypt(f.read())

            with open(temp_path,"wb") as fc:
                fc.write(encrypted_content)

            self.encrypted_files.append(temp_path)



    def compress(self):
        with zipfile.ZipFile(self.zipfile_name,"w") as zf:
            for enc_file in self.encrypted_files:
                zf.write(filename=enc_file,arcname=os.path.basename(enc_file),compress_type=zipfile.ZIP_LZMA)
                os.remove(enc_file)

    def get_key(self):
        return self.key.decode()





class Unlocker:
    """
    Class for extracting zipfile and decrypting the content of the extracted files_to_compress

    parameters : zipfile_name , encrypton_key , default_output_path
    """
    def __init__(self,zipfile_name="secret.zip",key=None,default_output_path="secret_path/"):
        self.zipfile_name = zipfile_name
        self.key = key.encode()
        self.output_path = default_output_path
        self.decompress()
        self.unlock()
        os.remove(self.zipfile_name)

    def unlock(self):
        fernet = Fernet(self.key)

        for file in os.listdir(self.output_path):
            file_path = os.path.join(self.output_path,file)
            with open(file_path,"rb") as f:
                content = fernet.decrypt(f.read())

            with open(file_path,"wb") as fc:
                fc.write(content)


    def  decompress(self):
        try:
            with zipfile.ZipFile(self.zipfile_name) as zf:
                zf.extractall(self.output_path)
        except Exception as E:
            print(f"\033[1;31mSomething went wrong !\t{E}")


class Injector:
    """
    Class for injecting the content into the various types of image files
    
    parameters : container_image , payload_file

    """

    def __init__(self,container_image,payload_file):
        self.container = container_image
        self.payload = payload_file
        self.allowed_file_type = ["jpeg","png"]

        if self.check_extension() == "jpeg":
            self.inject_to_jpeg()
        elif self.check_extension() == "png":
            self.inject_to_png()
        os.remove(self.payload)


    def check_extension(self):
        if self.container:
            extension = self.container.split(".")[-1]
            if extension in self.allowed_file_type:
                return extension
            return False
        return None
        

    def inject_to_jpeg(self):
        EOI_marker = "ffd9"
        with open(self.container,"rb+") as cf , open(self.payload,"rb") as pf:
            index = cf.read().index(bytes.fromhex(EOI_marker))
            cf.seek(index + 4)
            cf.write(pf.read())


    def inject_to_png(self):
        EOI_marker = "0000000049454E44AE426082"
        with open(self.container,"rb+") as cf , open(self.payload,"rb") as pf:
            index = cf.read().index(bytes.fromhex(EOI_marker))
            cf.seek(index + 12)
            cf.write(pf.read())


class Extractor:
    """
    Class for extracting hidden media files from the container_image

    parameters : container_image , output_file_path
    """

    def __init__(self,container_image,output_file_path):
        self.container = container_image
        self.output_path = output_file_path
        if self.check_extension() == "png":
            self.extract_from_png()
        elif self.check_extension() == "jpeg":
            self.extract_from_jpeg()
        
    
    def check_extension(self):
        return self.container.split(".")[-1]

    def extract_from_png(self): 
        EOI_marker = "0000000049454E44AE426082"
        with open(self.container,"rb+") as f , open(self.output_path,"wb") as fc:
            index = f.read().index(bytes.fromhex(EOI_marker))
            f.seek(index + 12)
            fc.write(f.read())
            f.truncate()

    def extract_from_jpeg(self):
        EOI_marker = "ffd9"
        with open(self.container,"rb+") as f , open(self.output_path,"wb") as fc:
            index = f.read().index(bytes.fromhex(EOI_marker))
            f.seek(index + 4)
            fc.write(f.read())
            f.truncate()



